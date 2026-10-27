# Play-Annotation-Generator Annotation Review — Counter_186

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_186`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB3 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB3 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB2 | defense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | RG | offense | `22` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | SAF | defense | `14` | `13` |
| ✅ EXACT | `Action_PlaySideFakeStep` | LB1 | defense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `22` | `16` |
| ⚠️ START CHANGED | `Action_Handoff` | RG | offense | `22` | `16` |
| ⚠️ START CHANGED | `Action_BallCarry` | LB1 | defense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 91 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 113 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 51 |
| ✅ EXACT | `Action_BallSnap` | CB3 | `11` | `10` | 190 | START | 190 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB3 | `11` | `10` | 193 | START | 193 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB2 | `5` | `4` | 193 | START | 193 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | `9` | `8` | 193 | START | 193 | 245 |
| ❌ MISSING SEGMENT | `Action_PullBlock` | RG | `22` | `16` | 193 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | SAF | `14` | `13` | 193 | START | 193 | 206 |
| ✅ EXACT | `Action_PlaySideFakeStep` | LB1 | `7` | `6` | 196 | START | 196 | 219 |
| ✅ EXACT | `Action_SnapReceive` | RG | `22` | `16` | 202 | END | 190 | 202 |
| ⚠️ START CHANGED | `Action_Handoff` | RG | `22` | `16` | 211 | START | 214 | 229 |
| ⚠️ START CHANGED | `Action_BallCarry` | LB1 | `7` | `6` | 235 | START | 236 | 331 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 278 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 91–359
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 91 | 155 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 219 | 222 | 4 | inferred_complete_timeline |
| `Action_None` | 229 | 248 | 20 | inferred_complete_timeline |
| `Action_None` | 270 | 359 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 234 | 45 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 264 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 189 | 95 | inferred_complete_timeline |
| `Action_None` | 190 | 359 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 192 | 137 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 245 | 53 | inferred_complete_timeline |
| `Action_DownBlock` | 248 | 257 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 273 | 278 | 6 | inferred_complete_timeline |
| `Action_None` | 279 | 359 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 113–229
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 113 | 189 | 77 | inferred_complete_timeline |
| `Action_SnapReceive` | 190 | 202 | 13 | inferred_complete_timeline |
| `Action_None` | 203 | 207 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 214 | 229 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 293 | 104 | inferred_complete_timeline |
| `Action_None` | 295 | 330 | 36 | inferred_complete_timeline |
| `Action_None` | 336 | 357 | 22 | inferred_complete_timeline |
| `Action_None` | 359 | 359 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 359 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 189 | 79 | inferred_complete_timeline |
| `Action_None` | 190 | 203 | 14 | inferred_complete_timeline |
| `Action_None` | 208 | 211 | 4 | inferred_complete_timeline |
| `Action_None` | 217 | 220 | 4 | inferred_complete_timeline |
| `Action_None` | 222 | 227 | 6 | inferred_complete_timeline |
| `Action_None` | 235 | 238 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 16 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 189 | 171 | inferred_complete_timeline |
| `Action_None` | 190 | 221 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–331
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 196 | 219 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 331 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 93 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 125 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 130 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 136 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 166 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 197 | 6 | inferred_complete_timeline |
| `Action_None` | 209 | 213 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 20 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 78 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 189 | 100 | inferred_complete_timeline |
| `Action_None` | 190 | 359 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 192 | 123 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 219 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 222 | 278 | 57 | inferred_complete_timeline |
| `Action_None` | 279 | 296 | 18 | inferred_complete_timeline |
| `Action_None` | 302 | 359 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 189 | 105 | inferred_complete_timeline |
| `Action_BallSnap` | 190 | 192 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 203 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 207 | 217 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 224 | 227 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 246 | 250 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 258 | 267 | 10 | inferred_complete_timeline |
| `Action_None` | 286 | 319 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 193 | 206 | 14 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 213 | 272 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `24` | Position_Unknown | Team_Unknown | 223–271 | 47 | 2 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 224–359 | 133 | 3 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 227–359 | 123 | 3 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 230–359 | 130 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 235–336 | 102 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 251–348 | 97 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 279–297 | 19 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 280–359 | 76 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 281–359 | 79 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 292–359 | 68 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 292–359 | 68 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 314–359 | 46 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 316–359 | 44 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 343–359 | 17 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 347–359 | 13 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 353–359 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (3 segments found)
- ❌ Missing segment for action `Action_PullBlock` on target `22` (RG)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `14` (2 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `22` (RG): Annotated start 211 != Inferred start 214
- ⚠️ `Action_BallCarry` for actor_track_id `7` (LB1): Annotated start 235 != Inferred start 236

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_PullBlock' for track '16' has invalid range: start=193, end=189. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-234] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-293] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-330] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-357] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-219] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-296] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [196-219] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [236-331] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-245] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [248-257] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [273-278] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-203] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [207-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [224-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [246-250] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [258-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-319] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-16] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-189] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-221] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-166] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-182] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [193-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [213-272] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-20] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-155] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-248] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [214-229] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-259] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-271] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-266] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-286] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-359] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-336] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-264] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-348] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-297] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-322] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-359] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-359] for track '27' has 1 frames without a visible bounding box.
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