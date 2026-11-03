# Play-Annotation-Generator Annotation Review — StopAndGo_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_21`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_VerticalStem` | TE | offense | `10` | `10` |
| ✅ EXACT | `Action_SellStop` | TE | offense | `10` | `10` |
| ✅ EXACT | `Action_RunGoRoute` | TE | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 2 | START | 2 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 5 | START | 23 | 143 |
| ✅ EXACT | `Action_PassBlock` | RT | `19` | `19` | 5 | START | 5 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 5 | START | 5 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 5 | START | 5 | 73 |
| ✅ EXACT | `Action_PassBlock` | LT | `3` | `3` | 5 | START | 5 | 54 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 22 | END | 2 | 22 |
| ✅ EXACT | `Action_VerticalStem` | TE | `10` | `10` | 22 | START | 22 | 68 |
| ✅ EXACT | `Action_SellStop` | TE | `10` | `10` | 69 | START | 69 | 77 |
| ✅ EXACT | `Action_RunGoRoute` | TE | `10` | `10` | 78 | START | 78 | 288 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 137 | START | 137 | 141 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 22 | 21 | inferred_complete_timeline |
| `Action_None` | 23 | 131 | 109 | inferred_complete_timeline |
| `Action_None` | 136 | 136 | 1 | inferred_complete_timeline |
| `Action_ThrowPass` | 137 | 141 | 5 | inferred_complete_timeline |
| `Action_None` | 156 | 161 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 91 | 90 | inferred_complete_timeline |
| `Action_None` | 94 | 172 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 229 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 260 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 189 | 188 | inferred_complete_timeline |
| `Action_None` | 191 | 235 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_VerticalStem` | 22 | 68 | 47 | inferred_complete_timeline |
| `Action_SellStop` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_RunGoRoute` | 78 | 288 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 54 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 73 | 69 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 125 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 161 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 22 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 143 | 121 | inferred_complete_timeline |
| `Action_PassBlock` | 166 | 179 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 31 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 58 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 156 | 70 | inferred_complete_timeline |
| `Action_PassBlock` | 159 | 175 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 189 | 201 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 203 | 212 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 137 | 133 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 94 | 93 | inferred_complete_timeline |
| `Action_None` | 102 | 146 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 46 | 45 | inferred_complete_timeline |
| `Action_None` | 48 | 191 | 144 | inferred_complete_timeline |
| `Action_None` | 193 | 226 | 34 | inferred_complete_timeline |
| `Action_None` | 228 | 329 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 58 | 57 | inferred_complete_timeline |
| `Action_None` | 70 | 126 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 48 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 329 | 328 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 329 | 328 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 235 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 329 | 328 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 176 | 175 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 191 | 3 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 329 | 328 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 140 | 139 | inferred_complete_timeline |
| `Action_None` | 143 | 145 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 196 | 40 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 280 | 80 | inferred_complete_timeline |
| `Action_None` | 290 | 329 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 47–180 | 114 | 7 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 54–76 | 10 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 65–223 | 159 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 154–201 | 43 | 5 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 173–179 | 7 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 215–329 | 114 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 269–294 | 26 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 298–329 | 29 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 304–329 | 26 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [2–22], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=23.
- ⚠️ Action 'Action_None' range [2-229] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-260] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-54] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-94] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-146] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-189] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-235] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-235] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-191] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-226] for track '9' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [78-288] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-126] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-280] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-176] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-172] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-143] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [166-179] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-48] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-131] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [137-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-137] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-31] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-58] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [159-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [179-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [189-201] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [203-212] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-125] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-161] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-71] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-144] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-56] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-223] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-166] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-293] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-294] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-323] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>