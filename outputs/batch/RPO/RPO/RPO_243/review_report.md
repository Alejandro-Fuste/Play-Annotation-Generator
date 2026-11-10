# Play-Annotation-Generator Annotation Review — RPO_243

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_243`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `0` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `10` | `10` | 74 | START | 74 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `18` | `18` | 74 | START | 74 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `19` | `19` | 74 | START | 74 | 76 |
| ✅ EXACT | `Action_RunBlock` | LT | `5` | `5` | 74 | START | 74 | 133 |
| ✅ EXACT | `Action_RunBlock` | RT | `8` | `8` | 74 | START | 74 | 133 |
| ✅ EXACT | `Action_ReadDefender` | QB | `20` | `20` | 83 | START | 83 | 91 |
| ✅ EXACT | `Action_PullBall` | QB | `20` | `20` | 92 | START | 92 | 98 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 124 | START | 124 | 133 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 82 | 10 | inferred_complete_timeline |
| `Action_ReadDefender` | 83 | 91 | 9 | inferred_complete_timeline |
| `Action_PullBall` | 92 | 98 | 7 | inferred_complete_timeline |
| `Action_None` | 99 | 123 | 25 | inferred_complete_timeline |
| `Action_ThrowPass` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_None` | 134 | 210 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 83 | 11 | inferred_complete_timeline |
| `Action_None` | 85 | 190 | 106 | inferred_complete_timeline |
| `Action_None` | 194 | 210 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 210 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 210 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 205 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 74 | 133 | 60 | inferred_complete_timeline |
| `Action_None` | 134 | 168 | 35 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 210 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 74 | 104 | 31 | inferred_complete_timeline |
| `Action_RunBlock` | 109 | 127 | 19 | inferred_complete_timeline |
| `Action_None` | 134 | 210 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 74 | 97 | 24 | inferred_complete_timeline |
| `Action_RunBlock` | 109 | 133 | 25 | inferred_complete_timeline |
| `Action_None` | 134 | 200 | 67 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 78 | 133 | 56 | inferred_complete_timeline |
| `Action_None` | 134 | 189 | 56 | inferred_complete_timeline |
| `Action_None` | 196 | 202 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 74 | 133 | 60 | inferred_complete_timeline |
| `Action_None` | 134 | 201 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 100 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 210 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 78 | 6 | inferred_complete_timeline |
| `Action_None` | 94 | 133 | 40 | inferred_complete_timeline |
| `Action_None` | 137 | 151 | 15 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 90 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 86 | 14 | inferred_complete_timeline |
| `Action_None` | 89 | 106 | 18 | inferred_complete_timeline |
| `Action_None` | 110 | 121 | 12 | inferred_complete_timeline |
| `Action_None` | 126 | 133 | 8 | inferred_complete_timeline |
| `Action_None` | 135 | 142 | 8 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 123 | 51 | inferred_complete_timeline |
| `Action_None` | 143 | 210 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 210 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 210 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 176 | 104 | inferred_complete_timeline |
| `Action_None` | 189 | 210 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 183 | 111 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 191 | 200 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 167 | 95 | inferred_complete_timeline |
| `Action_None` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_None` | 193 | 206 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 61–210 | 148 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 93–210 | 90 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 122–210 | 69 | 6 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 151–190 | 31 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 169–210 | 42 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 66 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [73-205] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-176] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-206] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-106] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-183] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-200] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-201] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [74-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [109-127] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-210] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-133] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-190] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [74-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-200] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [74-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [78-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-189] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-206] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-154] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-139] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-172] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-179] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '25' has 1 frames without a visible bounding box.
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

</details>