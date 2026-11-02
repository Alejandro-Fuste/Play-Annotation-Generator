# Play-Annotation-Generator Annotation Review — JetSweep_189

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_189`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 135
- **Validation Warnings:** 130
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
- **Inferred Coverage Segments (Action_None):** 110
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR1 | offense | `1` | `0` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Toss` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR1 | `1` | `0` | 1 | START | 1 | 82 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 58 | START | 58 | 71 |
| ✅ EXACT | `Action_LeadBlock` | TE | `17` | `16` | 60 | START | 60 | 143 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `17` | 60 | START | 60 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 60 | START | 72 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 60 | START | 60 | 78 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 71 | END | 58 | 71 |
| ✅ EXACT | `Action_Toss` | QB | `6` | `5` | 82 | START | 82 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `1` | `0` | 85 | START | 85 | 265 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 143 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 71 | 14 | inferred_complete_timeline |
| `Action_None` | 72 | 81 | 10 | inferred_complete_timeline |
| `Action_Toss` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_None` | 85 | 205 | 121 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 216 | 5 | inferred_complete_timeline |
| `Action_None` | 218 | 268 | 51 | inferred_complete_timeline |
| `Action_None` | 271 | 286 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 329 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_JetMotion` | 1 | 82 | 82 | inferred_complete_timeline |
| `Action_JetMotion` | 84 | 84 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 265 | 181 | inferred_complete_timeline |
| `Action_BallCarry` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 329 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 187 | 130 | inferred_complete_timeline |
| `Action_None` | 192 | 197 | 6 | inferred_complete_timeline |
| `Action_None` | 200 | 212 | 13 | inferred_complete_timeline |
| `Action_None` | 216 | 221 | 6 | inferred_complete_timeline |
| `Action_None` | 275 | 280 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_LeadBlock` | 60 | 143 | 84 | inferred_complete_timeline |
| `Action_None` | 144 | 252 | 109 | inferred_complete_timeline |
| `Action_None` | 254 | 329 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 143 | 84 | inferred_complete_timeline |
| `Action_None` | 144 | 329 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_BallSnap` | 58 | 71 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 143 | 72 | inferred_complete_timeline |
| `Action_None` | 144 | 231 | 88 | inferred_complete_timeline |
| `Action_None` | 234 | 236 | 3 | inferred_complete_timeline |
| `Action_None` | 239 | 325 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 78 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 143 | 21 | inferred_complete_timeline |
| `Action_None` | 144 | 329 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 329 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 329 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 329 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 118 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 296 | 239 | inferred_complete_timeline |
| `Action_None` | 299 | 312 | 14 | inferred_complete_timeline |
| `Action_None` | 314 | 316 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 158 | 101 | inferred_complete_timeline |
| `Action_None` | 160 | 329 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 270 | 213 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_None` | 281 | 282 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 296 | 9 | inferred_complete_timeline |
| `Action_None` | 298 | 303 | 6 | inferred_complete_timeline |
| `Action_None` | 308 | 310 | 3 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 181 | 124 | inferred_complete_timeline |
| `Action_None` | 183 | 188 | 6 | inferred_complete_timeline |
| `Action_None` | 201 | 219 | 19 | inferred_complete_timeline |
| `Action_None` | 226 | 229 | 4 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 329 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 195 | 138 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 216 | 5 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 235 | 7 | inferred_complete_timeline |
| `Action_None` | 237 | 264 | 28 | inferred_complete_timeline |
| `Action_None` | 267 | 283 | 17 | inferred_complete_timeline |
| `Action_None` | 286 | 290 | 5 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |
| `Action_None` | 297 | 312 | 16 | inferred_complete_timeline |
| `Action_None` | 315 | 325 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 329 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 268 | 211 | inferred_complete_timeline |
| `Action_None` | 271 | 275 | 5 | inferred_complete_timeline |
| `Action_None` | 280 | 329 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–329 | 329 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 13–66 | 38 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 75–82 | 8 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 83–98 | 16 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 117–329 | 198 | 4 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 154–329 | 172 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 158–162 | 5 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 179–207 | 18 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 198–301 | 78 | 5 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 213–274 | 40 | 5 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 236–242 | 5 | 2 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 274–275 | 2 | 1 | Undefined position; Undefined team |
| `33` | `53` | Position_Unknown | Team_Unknown | 285–315 | 16 | 4 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 287–316 | 16 | 5 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 301–329 | 26 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 95 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [58–71], lower_priority='Action_ZoneBlock' annotated_start=60, effective_Action_ZoneBlock_start=72.
- ⚠️ Action 'Action_JetMotion' range [1-82] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-265] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [268-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-187] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-212] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-280] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-205] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-268] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-286] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-181] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-329] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-87] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-158] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-195] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-264] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-283] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-312] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-325] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-296] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-312] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-316] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-270] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-296] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-303] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-329] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-252] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-329] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-275] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-231] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-325] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-27] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-98] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-226] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-267] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-276] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-285] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-237] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-312] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-306] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-311] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>