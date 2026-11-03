# Play-Annotation-Generator Annotation Review — OutAndUp_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_61`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 299
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 126
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB1 | offense | `16` | `16` |
| ✅ EXACT | `Action_SellOut` | WR2 | offense | `2` | `2` |
| ✅ EXACT | `Action_RunGoRoute` | WR2 | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | QB1 | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | `15` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `16` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 22 | START | 22 | 36 |
| ✅ EXACT | `Action_PassBlock` | RT | `14` | `14` | 28 | START | 28 | 174 |
| ✅ EXACT | `Action_PassBlock` | LG | `18` | `18` | 28 | START | 28 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 28 | START | 37 | 40 |
| ✅ EXACT | `Action_PassBlock` | LT | `20` | `20` | 28 | START | 28 | 172 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 28 | START | 28 | 36 |
| ✅ EXACT | `Action_SnapReceive` | QB1 | `16` | `16` | 36 | END | 22 | 36 |
| ✅ EXACT | `Action_SellOut` | WR2 | `2` | `2` | 87 | START | 87 | 115 |
| ✅ EXACT | `Action_RunGoRoute` | WR2 | `2` | `2` | 116 | START | 116 | 234 |
| ✅ EXACT | `Action_ThrowPass` | QB1 | `16` | `16` | 128 | START | 128 | 137 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 36 | 15 | inferred_complete_timeline |
| `Action_None` | 37 | 127 | 91 | inferred_complete_timeline |
| `Action_ThrowPass` | 128 | 137 | 10 | inferred_complete_timeline |
| `Action_None` | 138 | 163 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>QB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 181 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 128 | 107 | inferred_complete_timeline |
| `Action_None` | 131 | 222 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_SellOut` | 87 | 115 | 29 | inferred_complete_timeline |
| `Action_RunGoRoute` | 116 | 234 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 192 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 166 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 172 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 170 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 36 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 40 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 185 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 36 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 174 | 147 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 94 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 51 | 30 | inferred_complete_timeline |
| `Action_None` | 54 | 177 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 73 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 175 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 145 | 124 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 183 | 4 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 120 | 99 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 223 | 202 | inferred_complete_timeline |
| `Action_None` | 225 | 252 | 28 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 131 | 110 | inferred_complete_timeline |
| `Action_None` | 136 | 299 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 210 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 299 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 297 | 276 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–206 | 180 | 7 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 0–221 | 220 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 0–189 | 103 | 15 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 0–217 | 204 | 7 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 11–131 | 87 | 9 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 39–79 | 9 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 69–70 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 70–181 | 111 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 89–91 | 3 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 100–198 | 96 | 3 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 100–123 | 24 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 114–174 | 61 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 118–159 | 25 | 5 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 137–139 | 3 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 150–262 | 113 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 208–250 | 5 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 283–290 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 94 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [22–36], lower_priority='Action_PassBlock' annotated_start=28, effective_Action_PassBlock_start=37.
- ⚠️ Action 'Action_None' range [22-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-222] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [116-234] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-223] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-252] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-297] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-174] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-181] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-170] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-40] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-124] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-202] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-136] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-221] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-48] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-78] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-21] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-47] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-130] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-194] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-17] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-55] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-82] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-101] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-42] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-71] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-128] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-181] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-198] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-123] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-174] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-154] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-262] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-290] for track '40' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>