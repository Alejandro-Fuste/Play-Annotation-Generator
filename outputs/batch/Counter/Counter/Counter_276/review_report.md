# Play-Annotation-Generator Annotation Review — Counter_276

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_276`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 123
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB2 | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `6` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `8` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 61 | START | 61 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `10` | `9` | 64 | START | 64 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `9` | `8` | 64 | START | 64 | 94 |
| ✅ EXACT | `Action_PullBlock` | RT | `12` | `11` | 64 | START | 64 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | C | `16` | `15` | 64 | START | 78 | 109 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 77 | END | 64 | 77 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `16` | 84 | START | 84 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB2 | `8` | `7` | 103 | START | 106 | 130 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 171 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 43 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 64 | 77 | 14 | inferred_complete_timeline |
| `Action_None` | 78 | 83 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 84 | 102 | 19 | inferred_complete_timeline |
| `Action_None` | 103 | 147 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 150 | 90 | inferred_complete_timeline |
| `Action_None` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_None` | 176 | 245 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 130 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 193 | 202 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 212 | 241 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 253 | 269 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 121 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 97 | 37 | inferred_complete_timeline |
| `Action_None` | 99 | 115 | 17 | inferred_complete_timeline |
| `Action_None` | 118 | 175 | 58 | inferred_complete_timeline |
| `Action_None` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 250 | 31 | inferred_complete_timeline |
| `Action_None` | 263 | 265 | 3 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_DownBlock` | 64 | 87 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 91 | 137 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 26 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 57 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 61 | 77 | 17 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 78 | 109 | 32 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 113 | 164 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_DownBlock` | 64 | 94 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 102 | 170 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PullBlock` | 64 | 123 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 48 | 18 | inferred_complete_timeline |
| `Action_None` | 62 | 67 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 77 | 17 | inferred_complete_timeline |
| `Action_None` | 85 | 94 | 10 | inferred_complete_timeline |
| `Action_None` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 269 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 74 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 99 | 39 | inferred_complete_timeline |
| `Action_None` | 142 | 148 | 7 | inferred_complete_timeline |
| `Action_None` | 154 | 159 | 6 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 101 | 41 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 119 | 13 | inferred_complete_timeline |
| `Action_None` | 122 | 269 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 90 | 30 | inferred_complete_timeline |
| `Action_None` | 107 | 125 | 19 | inferred_complete_timeline |
| `Action_None` | 164 | 269 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 212 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 73 | 13 | inferred_complete_timeline |
| `Action_None` | 90 | 135 | 46 | inferred_complete_timeline |
| `Action_None` | 137 | 191 | 55 | inferred_complete_timeline |
| `Action_None` | 209 | 215 | 7 | inferred_complete_timeline |
| `Action_None` | 223 | 254 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 89–171 | 82 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 107–269 | 118 | 7 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 124–269 | 118 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 146–262 | 87 | 4 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 160–163 | 4 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 170–210 | 27 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 170–207 | 22 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 195–269 | 72 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 196–269 | 62 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 203–230 | 28 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 222–269 | 35 | 4 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 226–269 | 44 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 236–269 | 34 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 242–269 | 26 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 251–269 | 19 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 257–269 | 13 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 264–269 | 6 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 554: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (RG) duration 107 frames exceeds threshold 90 frames [start=64, end=170].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [61–77], lower_priority='Action_PullLeadBlock' annotated_start=64, effective_Action_PullLeadBlock_start=78.
- ⚠️ Action 'Action_None' range [61-90] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-212] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-73] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-135] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-215] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-254] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-48] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-67] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-245] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-175] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-250] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [64-94] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [102-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [64-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [91-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [64-123] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-101] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-119] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [78-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [113-164] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-43] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-171] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-181] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-213] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-262] for track '20' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-246] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-230] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-269] for track '30' has 1 frames without a visible bounding box.
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

</details>