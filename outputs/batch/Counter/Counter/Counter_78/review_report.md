# Play-Annotation-Generator Annotation Review — Counter_78

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_78`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 41
- **Ball Tracks:** 1
- **Action Segments:** 111
- **Validation Warnings:** 138
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `12` | `11` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `30` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `16` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 153 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 154 | START | 154 | 168 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `11` | `10` | 158 | START | 169 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `12` | `11` | 158 | START | 158 | 230 |
| ✅ EXACT | `Action_DownBlock` | LG | `7` | `6` | 158 | START | 158 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `13` | `12` | 158 | START | 158 | 175 |
| ⚠️ START CHANGED | `Action_PullLeadBlock` | Position_Unknown | `30` | `21` | 158 | START | 182 | 185 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 168 | END | 154 | 168 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `16` | `15` | 172 | START | 173 | 359 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 179 | START | 179 | 190 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 251 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_SnapReceive` | 154 | 168 | 15 | inferred_complete_timeline |
| `Action_None` | 169 | 178 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 179 | 190 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 45 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 66 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 105 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 126 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 136 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 164 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 173 | 359 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 206 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 230 | 73 | inferred_complete_timeline |
| `Action_DownBlock` | 235 | 238 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 241 | 251 | 11 | inferred_complete_timeline |
| `Action_None` | 252 | 263 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 157 | 39 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 191 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_BallSnap` | 154 | 168 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 169 | 184 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 208 | 215 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 246 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 157 | 149 | inferred_complete_timeline |
| `Action_PullBlock` | 158 | 175 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 196 | 223 | 28 | inferred_complete_timeline |
| `Action_PullBlock` | 229 | 241 | 13 | inferred_complete_timeline |
| `Action_None` | 255 | 289 | 35 | inferred_complete_timeline |
| `Action_None` | 304 | 312 | 9 | inferred_complete_timeline |
| `Action_None` | 320 | 359 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 189 | 36 | inferred_complete_timeline |
| `Action_None` | 201 | 211 | 11 | inferred_complete_timeline |
| `Action_None` | 217 | 224 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 153 | 144 | inferred_complete_timeline |
| `Action_None` | 154 | 215 | 62 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |
| `Action_None` | 229 | 251 | 23 | inferred_complete_timeline |
| `Action_None` | 254 | 272 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 157 | 269 | 113 | inferred_complete_timeline |
| `Action_None` | 271 | 291 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 146 | 71 | inferred_complete_timeline |
| `Action_None` | 156 | 191 | 36 | inferred_complete_timeline |
| `Action_None` | 196 | 259 | 64 | inferred_complete_timeline |
| `Action_None` | 262 | 269 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 214 | 61 | inferred_complete_timeline |
| `Action_None` | 222 | 253 | 32 | inferred_complete_timeline |
| `Action_None` | 271 | 274 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 267 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 223 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 189 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 301 | 148 | inferred_complete_timeline |
| `Action_None` | 303 | 359 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `25` | Position_Unknown | Team_Unknown | 103–205 | 31 | 2 | Undefined position; Undefined team |
| `18` | `26` | Position_Unknown | Team_Unknown | 123–359 | 237 | 2 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 130–176 | 45 | 3 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 179–181 | 3 | 1 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 182–185 | 4 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 186–330 | 135 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 208–272 | 23 | 2 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 233–270 | 19 | 3 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 236–320 | 80 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 246–359 | 112 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 247–274 | 25 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 250–285 | 15 | 3 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 253–303 | 49 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 267–314 | 45 | 2 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 280–317 | 38 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 282–291 | 10 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 285–321 | 37 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 293–359 | 56 | 2 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 319–327 | 9 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 329–359 | 31 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 333–359 | 27 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 337–359 | 13 | 3 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 341–359 | 19 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 352–359 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `20` | 86 | 87 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `13` (3 segments found)
- ⚠️ `Action_PullLeadBlock` for actor_track_id `30` (Position_Unknown): Annotated start 158 != Inferred start 182
- ⚠️ `Action_BallCarry` for actor_track_id `16` (RB): Annotated start 172 != Inferred start 173

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [154–168], lower_priority='Action_DownBlock' annotated_start=158, effective_Action_DownBlock_start=169.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (LT) duration 94 frames exceeds threshold 90 frames [start=158, end=251].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '12' (RG) duration 94 frames exceeds threshold 90 frames [start=158, end=251].
- ⚠️ Action 'Action_PreSnap' range [0-144] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-269] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-291] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-223] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-189] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-214] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-253] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-267] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-301] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [158-191] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-191] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-259] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-189] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-224] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [179-190] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [169-184] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [208-215] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-246] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [158-230] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [235-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [158-175] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [196-223] for track '12' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [229-241] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-289] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-312] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-215] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-251] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-272] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-45] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-105] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-126] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-136] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-164] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [173-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-205] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-172] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [182-185] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-206] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-289] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-330] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-217] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-272] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-313] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-283] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-261] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-274] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-285] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-290] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-303] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-309] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-317] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-291] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-321] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-318] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-327] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-345] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '39' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.

</details>