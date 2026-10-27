# Play-Annotation-Generator Annotation Review — Counter_342

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_342`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 103 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 104 | START | 104 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `16` | `15` | 107 | START | 107 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `7` | `6` | 107 | START | 107 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `9` | `8` | 107 | START | 118 | 141 |
| ✅ EXACT | `Action_PullBlock` | LG | `13` | `12` | 107 | START | 107 | 122 |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | `5` | `4` | 107 | START | 107 | 122 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 117 | END | 104 | 117 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 129 | START | 129 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `17` | `16` | 141 | START | 141 | 159 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 194 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_SnapReceive` | 104 | 117 | 14 | inferred_complete_timeline |
| `Action_None` | 118 | 128 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 129 | 138 | 10 | inferred_complete_timeline |
| `Action_None` | 183 | 299 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 140 | 102 | inferred_complete_timeline |
| `Action_BallCarry` | 141 | 159 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 167 | 229 | 63 | inferred_complete_timeline |
| `Action_BallCarry` | 235 | 260 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 263 | 299 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 107 | 122 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 97 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_None` | 104 | 121 | 18 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 127 | 149 | 23 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 26 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 35 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_None` | 104 | 115 | 12 | inferred_complete_timeline |
| `Action_None` | 121 | 125 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PullBlock` | 107 | 122 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_BallSnap` | 104 | 117 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 118 | 141 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 194 | 51 | inferred_complete_timeline |
| `Action_None` | 195 | 299 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 117 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 126 | 194 | 69 | inferred_complete_timeline |
| `Action_None` | 195 | 299 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 111 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 118 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 123 | 135 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 153 | 155 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 184 | 27 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 197 | 94 | inferred_complete_timeline |
| `Action_None` | 201 | 250 | 50 | inferred_complete_timeline |
| `Action_None` | 257 | 289 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 154 | 44 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 299 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 182 | 79 | inferred_complete_timeline |
| `Action_None` | 184 | 213 | 30 | inferred_complete_timeline |
| `Action_None` | 215 | 299 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 122 | 19 | inferred_complete_timeline |
| `Action_None` | 124 | 138 | 15 | inferred_complete_timeline |
| `Action_None` | 140 | 151 | 12 | inferred_complete_timeline |
| `Action_None` | 155 | 299 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 214 | 111 | inferred_complete_timeline |
| `Action_None` | 239 | 299 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 237 | 134 | inferred_complete_timeline |
| `Action_None` | 239 | 299 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 111 | 8 | inferred_complete_timeline |
| `Action_None` | 114 | 157 | 44 | inferred_complete_timeline |
| `Action_None` | 159 | 295 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 242 | 139 | inferred_complete_timeline |
| `Action_None` | 271 | 280 | 10 | inferred_complete_timeline |
| `Action_None` | 285 | 299 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–99 | 100 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 18–196 | 158 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 123–130 | 8 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 128–299 | 138 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 132–299 | 141 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 134–170 | 37 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 147–269 | 122 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 163–299 | 133 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 169–299 | 112 | 7 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 176–299 | 119 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 181–233 | 49 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 203–229 | 21 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 207–298 | 63 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 236–299 | 52 | 3 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 278–299 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 87 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 686: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [104–117], lower_priority='Action_DownBlock' annotated_start=107, effective_Action_DownBlock_start=118.
- ⚠️ Action 'Action_None' range [104-237] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-157] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-295] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-197] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-250] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-289] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-242] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-280] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [107-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-213] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-154] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-299] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [118-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-138] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-149] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-214] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [107-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [129-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [123-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [150-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [158-184] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-140] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [141-159] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [167-229] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-260] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [263-299] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-26] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-35] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-22] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-196] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-130] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-141] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-213] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-299] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-206] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-214] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-265] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-224] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-257] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-208] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-229] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-233] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-270] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-298] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-242] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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