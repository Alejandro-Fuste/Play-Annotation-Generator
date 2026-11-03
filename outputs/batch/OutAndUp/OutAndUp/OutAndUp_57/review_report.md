# Play-Annotation-Generator Annotation Review — OutAndUp_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_57`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 123
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_SellOut` | WR2 | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR2 | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 0 | START | 0 | 8 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 9 | START | 9 | 13 |
| ✅ EXACT | `Action_PassBlock` | LG | `14` | `14` | 12 | START | 12 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 12 | START | 14 | 109 |
| ✅ EXACT | `Action_PassBlock` | RG | `18` | `18` | 12 | START | 12 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `19` | `19` | 12 | START | 12 | 67 |
| ✅ EXACT | `Action_PassBlock` | RT | `20` | `20` | 12 | START | 12 | 191 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `21` | 13 | END | 9 | 13 |
| ✅ EXACT | `Action_SellOut` | WR2 | `10` | `10` | 66 | START | 66 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR2 | `10` | `10` | 82 | START | 82 | 295 |
| ✅ EXACT | `Action_ThrowPass` | QB | `21` | `21` | 86 | START | 86 | 97 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 9 | 13 | 5 | inferred_complete_timeline |
| `Action_None` | 14 | 85 | 72 | inferred_complete_timeline |
| `Action_ThrowPass` | 86 | 97 | 12 | inferred_complete_timeline |
| `Action_None` | 98 | 104 | 7 | inferred_complete_timeline |
| `Action_None` | 121 | 124 | 4 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 180 | 41 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 129 | 121 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 286 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_SellOut` | 66 | 81 | 16 | inferred_complete_timeline |
| `Action_RunGoRoute` | 82 | 295 | 214 | inferred_complete_timeline |
| `Action_RunGoRoute` | 297 | 329 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 257 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 245 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 67 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 170 | 102 | inferred_complete_timeline |
| `Action_PassBlock` | 174 | 186 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 180 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 9 | 13 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 109 | 96 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 204 | 86 | inferred_complete_timeline |
| `Action_PassBlock` | 209 | 251 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 253 | 255 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 67 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 191 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 108 | 100 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 190 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 106 | 98 | inferred_complete_timeline |
| `Action_None` | 108 | 203 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 236 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 313 | 305 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 327 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 221 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 245 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 293 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 329 | 321 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 229 | 221 | inferred_complete_timeline |
| `Action_None` | 231 | 329 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 133 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 78–141 | 64 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 86–87 | 2 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 96–104 | 5 | 2 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 99–101 | 3 | 1 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 123–125 | 3 | 1 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 129–180 | 52 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 138–139 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 139–215 | 55 | 9 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 146–329 | 160 | 12 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 149–151 | 3 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 150–194 | 11 | 3 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 151–217 | 65 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 153–313 | 134 | 11 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 162–166 | 5 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 175–180 | 5 | 2 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 204–207 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 87 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [9–13], lower_priority='Action_PassBlock' annotated_start=12, effective_Action_PassBlock_start=14.
- ⚠️ Action 'Action_None' range [9-108] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-190] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-229] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-236] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-286] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-327] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-129] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-257] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-106] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [82-295] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-133] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-313] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-180] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-293] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-204] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [209-251] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [253-255] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-245] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-67] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-170] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [174-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-191] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-180] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-143] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-199] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-215] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-173] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-209] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-225] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-250] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-260] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-217] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-159] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-180] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-286] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-313] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '38' has 1 frames without a visible bounding box.
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