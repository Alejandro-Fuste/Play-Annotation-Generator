# Play-Annotation-Generator Annotation Review — SlantAndGo_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_41`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 119
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | SAF1 | defense | `10` | `10` |
| ✅ EXACT | `Action_SellRoute` | CB1 | defense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | CB1 | defense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | SAF1 | defense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 31 | START | 31 | 46 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `12` | `12` | 34 | START | 47 | 220 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `14` | `14` | 34 | START | 34 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 34 | START | 34 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 34 | START | 34 | 105 |
| ✅ EXACT | `Action_SnapReceive` | SAF1 | `10` | `10` | 46 | END | 31 | 46 |
| ✅ EXACT | `Action_SellRoute` | CB1 | `19` | `19` | 72 | START | 72 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | CB1 | `19` | `19` | 99 | START | 99 | 271 |
| ✅ EXACT | `Action_ThrowPass` | SAF1 | `10` | `10` | 118 | START | 118 | 126 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–303
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 303 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 112 | 82 | inferred_complete_timeline |
| `Action_None` | 116 | 216 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 238 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 287 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 105 | 75 | inferred_complete_timeline |
| `Action_None` | 109 | 202 | 94 | inferred_complete_timeline |
| `Action_None` | 205 | 220 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 71 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 98 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 144 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 223 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 134 | 101 | inferred_complete_timeline |
| `Action_PassBlock` | 136 | 140 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 142 | 143 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 46 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 220 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 105 | 72 | inferred_complete_timeline |
| `Action_PassBlock` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 184 | 154 | inferred_complete_timeline |
| `Action_None` | 186 | 220 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 110 | 80 | inferred_complete_timeline |
| `Action_None` | 132 | 150 | 19 | inferred_complete_timeline |
| `Action_None` | 152 | 168 | 17 | inferred_complete_timeline |
| `Action_None` | 173 | 186 | 14 | inferred_complete_timeline |
| `Action_None` | 190 | 202 | 13 | inferred_complete_timeline |
| `Action_None` | 204 | 212 | 9 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 85 | 55 | inferred_complete_timeline |
| `Action_None` | 97 | 101 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 101 | 71 | inferred_complete_timeline |
| `Action_None` | 106 | 276 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 186 | 156 | inferred_complete_timeline |
| `Action_None` | 191 | 250 | 60 | inferred_complete_timeline |
| `Action_None` | 252 | 259 | 8 | inferred_complete_timeline |
| `Action_None` | 262 | 268 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_SellRoute` | 72 | 98 | 27 | inferred_complete_timeline |
| `Action_VerticalStem` | 99 | 271 | 173 | inferred_complete_timeline |
| `Action_VerticalStem` | 273 | 329 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 199 | 169 | inferred_complete_timeline |
| `Action_None` | 201 | 208 | 8 | inferred_complete_timeline |
| `Action_None` | 210 | 219 | 10 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 196 | 166 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 46 | 16 | inferred_complete_timeline |
| `Action_None` | 47 | 117 | 71 | inferred_complete_timeline |
| `Action_ThrowPass` | 118 | 126 | 9 | inferred_complete_timeline |
| `Action_None` | 127 | 199 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 236 | 206 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–329 | 328 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–208 | 208 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–327 | 320 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 71–96 | 24 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 78–104 | 10 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 104–216 | 113 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 117–118 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 123–131 | 9 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 127–156 | 20 | 4 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 152–154 | 3 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 157–222 | 64 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 165–221 | 54 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 181–229 | 45 | 3 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 193–255 | 56 | 7 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 201–219 | 13 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `12` (C): Annotated start 34 != Inferred start 47
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 55: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ Row 56: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ Row 56: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [31–46], lower_priority='Action_PassBlock' annotated_start=34, effective_Action_PassBlock_start=47.
- ⚠️ Action 'Action_None' range [31-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-168] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-186] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-202] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-212] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-184] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-220] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-208] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-219] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-236] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-85] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-287] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-216] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-276] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-196] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-199] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-220] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-250] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-98] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-302] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-329] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-303] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-204] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [136-140] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [142-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [99-271] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [273-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-235] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-327] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-105] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [152-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-77] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-96] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-216] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-136] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-211] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-205] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-221] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-217] for track '32' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-235] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-219] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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