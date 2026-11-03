# Play-Annotation-Generator Annotation Review — OutAndUp_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_31`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_SellOut` | WR1 | offense | `4` | `4` |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 15 | START | 15 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 18 | START | 29 | 157 |
| ✅ EXACT | `Action_PassBlock` | RG | `16` | `16` | 18 | START | 18 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 18 | START | 18 | 71 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 18 | START | 18 | 87 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 28 | END | 15 | 28 |
| ✅ EXACT | `Action_SellOut` | WR1 | `4` | `4` | 86 | START | 86 | 103 |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | `4` | `4` | 104 | START | 104 | 201 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 123 | START | 123 | 133 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 28 | 14 | inferred_complete_timeline |
| `Action_None` | 29 | 122 | 94 | inferred_complete_timeline |
| `Action_ThrowPass` | 123 | 133 | 11 | inferred_complete_timeline |
| `Action_None` | 134 | 169 | 36 | inferred_complete_timeline |
| `Action_None` | 171 | 182 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 202 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_SellOut` | 86 | 103 | 18 | inferred_complete_timeline |
| `Action_RunGoRoute` | 104 | 201 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 173 | 159 | inferred_complete_timeline |
| `Action_None` | 177 | 269 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 83 | 69 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_None` | 113 | 188 | 76 | inferred_complete_timeline |
| `Action_None` | 195 | 269 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 115 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 87 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 15 | 28 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 157 | 129 | inferred_complete_timeline |
| `Action_PassBlock` | 159 | 236 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 157 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 71 | 54 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 234 | 158 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 110 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 111 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 161 | 147 | inferred_complete_timeline |
| `Action_None` | 210 | 217 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 168 | 154 | inferred_complete_timeline |
| `Action_None` | 170 | 218 | 49 | inferred_complete_timeline |
| `Action_None` | 220 | 232 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 161 | 147 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 209 | 34 | inferred_complete_timeline |
| `Action_None` | 214 | 269 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 269 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 128 | 114 | inferred_complete_timeline |
| `Action_None` | 134 | 194 | 61 | inferred_complete_timeline |
| `Action_None` | 196 | 199 | 4 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 269 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 130 | 116 | inferred_complete_timeline |
| `Action_None` | 132 | 184 | 53 | inferred_complete_timeline |
| `Action_None` | 186 | 190 | 5 | inferred_complete_timeline |
| `Action_None` | 194 | 269 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 269 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 180 | 166 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–123 | 116 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 99–103 | 5 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 130–228 | 85 | 7 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 154–236 | 82 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 156–216 | 59 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 160–232 | 64 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 164–238 | 55 | 7 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 178–232 | 39 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 191–193 | 3 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 208–232 | 21 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 216–218 | 3 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 228–230 | 3 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 237–269 | 33 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 240–244 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 34: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [15–28], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=29.
- ⚠️ Action 'Action_None' range [15-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-184] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [104-201] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-161] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-209] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-217] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-83] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-188] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-194] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-218] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-232] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-169] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-182] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [159-236] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-71] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-234] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-142] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-185] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-204] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-223] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-223] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-176] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-238] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-232] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-218] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-269] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '34' has 1 frames without a visible bounding box.
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