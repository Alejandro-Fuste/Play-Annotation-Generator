# Play-Annotation-Generator Annotation Review — Counter_146

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_146`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 146
- **Validation Warnings:** 161
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 110
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | DT1 | defense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | defense | `7` | `6` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `22` | `19` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 132 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | DT1 | `7` | `6` | 169 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `15` | `14` | 174 | START | 174 | 202 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | `7` | `6` | 174 | START | 193 | 194 |
| ✅ EXACT | `Action_DownBlock` | RG | `8` | `7` | 174 | START | 174 | 257 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `13` | `12` | 174 | START | 174 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `22` | `19` | 174 | START | 174 | 176 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `9` | `8` | 174 | END | N/A | N/A |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 200 | START | 200 | 213 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `9` | 214 | START | 214 | 262 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 257 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 159 | 25 | inferred_complete_timeline |
| `Action_None` | 183 | 195 | 13 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 200 | 213 | 14 | inferred_complete_timeline |
| `Action_None` | 214 | 289 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–334
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_BallCarry` | 214 | 262 | 49 | inferred_complete_timeline |
| `Action_BallCarry` | 264 | 265 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 274 | 280 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 293 | 294 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 299 | 303 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 327 | 334 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PullBlock` | 174 | 178 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 180 | 187 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 200 | 202 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 173 | 127 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 257 | 84 | inferred_complete_timeline |
| `Action_None` | 258 | 264 | 7 | inferred_complete_timeline |
| `Action_None` | 274 | 359 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 173 | 156 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 202 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 209 | 257 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 45 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 58 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 90 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 256 | 88 | inferred_complete_timeline |
| `Action_None` | 260 | 309 | 50 | inferred_complete_timeline |
| `Action_None` | 312 | 318 | 7 | inferred_complete_timeline |
| `Action_None` | 340 | 353 | 14 | inferred_complete_timeline |
| `Action_None` | 357 | 359 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 94 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 133 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 157 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 204 | 212 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 219 | 257 | 39 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 215 | 47 | inferred_complete_timeline |
| `Action_None` | 218 | 220 | 3 | inferred_complete_timeline |
| `Action_None` | 228 | 272 | 45 | inferred_complete_timeline |
| `Action_None` | 277 | 309 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 63 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 13 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 33 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 45 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 74 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 85 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 107 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 318 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 29 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 99 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 152 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 168 | 1 | inferred_complete_timeline |
| `Action_None` | 169 | 176 | 8 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 206 | 16 | inferred_complete_timeline |
| `Action_None` | 214 | 216 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 5–359 | 269 | 10 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 18–217 | 155 | 6 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 42–224 | 141 | 9 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 115–359 | 232 | 7 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 123–359 | 176 | 8 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 173–359 | 134 | 5 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 183–359 | 153 | 5 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 199–240 | 38 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 200–359 | 147 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 223–359 | 137 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 228–359 | 125 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 228–359 | 126 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 240–359 | 120 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 247–359 | 107 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 250–359 | 110 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 285–359 | 75 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 310–359 | 50 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 348–359 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `7` (DT1)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `22` (4 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `9` (QB)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 123 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 294: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-63] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-318] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-256] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-309] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-318] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-353] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-29] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-152] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-164] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-206] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-94] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-194] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [204-212] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [216-217] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [219-257] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-257] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-264] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-159] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-289] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [214-262] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [264-265] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [274-280] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [293-294] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [299-303] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [327-334] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-45] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-58] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-215] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-272] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-309] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [174-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [180-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [200-202] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-13] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-33] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-85] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '14' starts at frame 174, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [174-202] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [209-257] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-82] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-168] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-176] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-266] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-301] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-359] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-113] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-168] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-176] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-217] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 169, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [169-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-204] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-224] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-267] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' for track '19' starts at frame 174, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PullLeadBlock' range [174-176] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [182-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [211-220] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-193] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-268] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-282] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-220] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-264] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-308] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-211] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-240] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-345] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-344] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-290] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-325] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-286] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-312] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-359] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>