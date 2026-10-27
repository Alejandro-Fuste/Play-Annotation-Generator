# Play-Annotation-Generator Annotation Review — Counter_184

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_184`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT1 | defense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | CB3 | defense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | CB3 | defense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB1 | defense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 65 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 74 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `23` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 90 |
| ✅ EXACT | `Action_BallSnap` | QB | `15` | `14` | 165 | START | 165 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB2 | `11` | `10` | 168 | START | 168 | 186 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | QB | `15` | `14` | 168 | START | 168 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `7` | `6` | 168 | START | 168 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `16` | `15` | 168 | START | 168 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT1 | `13` | `12` | 168 | START | 168 | 198 |
| ✅ EXACT | `Action_SnapReceive` | CB3 | `10` | `9` | 177 | END | 165 | 177 |
| ✅ EXACT | `Action_Handoff` | CB3 | `10` | `9` | 188 | START | 188 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB1 | `8` | `7` | 204 | START | 205 | 236 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 260 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 113 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 138 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 164 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 168 | 178 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 232 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 206–329
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 206 | 235 | 30 | inferred_complete_timeline |
| `Action_None` | 239 | 323 | 85 | inferred_complete_timeline |
| `Action_None` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_None` | 165 | 308 | 144 | inferred_complete_timeline |
| `Action_None` | 311 | 329 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_None` | 165 | 273 | 109 | inferred_complete_timeline |
| `Action_None` | 279 | 282 | 4 | inferred_complete_timeline |
| `Action_None` | 285 | 288 | 4 | inferred_complete_timeline |
| `Action_None` | 297 | 329 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_None` | 165 | 216 | 52 | inferred_complete_timeline |
| `Action_None` | 220 | 259 | 40 | inferred_complete_timeline |
| `Action_None` | 265 | 320 | 56 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_None` | 165 | 197 | 33 | inferred_complete_timeline |
| `Action_None` | 201 | 215 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 219–329
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 219 | 227 | 9 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |
| `Action_None` | 244 | 313 | 70 | inferred_complete_timeline |
| `Action_None` | 322 | 329 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 74–329
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 74 | 164 | 91 | inferred_complete_timeline |
| `Action_None` | 165 | 278 | 114 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 287 | 295 | 9 | inferred_complete_timeline |
| `Action_None` | 311 | 329 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 65–191
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 65 | 167 | 103 | inferred_complete_timeline |
| `Action_PullBlock` | 168 | 187 | 20 | inferred_complete_timeline |
| `Action_PullBlock` | 189 | 191 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 268–329
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_None` | 271 | 274 | 4 | inferred_complete_timeline |
| `Action_None` | 278 | 329 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 167 | 71 | inferred_complete_timeline |
| `Action_DownBlock` | 168 | 214 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 232 | 242 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 246 | 247 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 167 | 116 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 168 | 198 | 31 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 218 | 260 | 43 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 271 | 329 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 194–322
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 194 | 222 | 29 | inferred_complete_timeline |
| `Action_None` | 229 | 322 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 167 | 86 | inferred_complete_timeline |
| `Action_DownBlock` | 168 | 186 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 190 | 209 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 216 | 234 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 239 | 260 | 22 | inferred_complete_timeline |
| `Action_None` | 261 | 329 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 164 | 75 | inferred_complete_timeline |
| `Action_None` | 165 | 172 | 8 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 254 | 37 | inferred_complete_timeline |
| `Action_None` | 256 | 329 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_BallCarry` | 205 | 236 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 238 | 329 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_None` | 165 | 177 | 13 | inferred_complete_timeline |
| `Action_None` | 179 | 329 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_SnapReceive` | 165 | 177 | 13 | inferred_complete_timeline |
| `Action_None` | 178 | 187 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 188 | 203 | 16 | inferred_complete_timeline |
| `Action_None` | 204 | 329 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `22` | Position_Unknown | Team_Unknown | 254–280 | 23 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 271–329 | 59 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 274–329 | 28 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 290–329 | 40 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 296–329 | 33 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 300–310 | 11 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '10' (LB2) duration 93 frames exceeds threshold 90 frames [start=168, end=260].
- ⚠️ Action 'Action_None' range [165-216] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-259] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-320] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-273] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-308] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [168-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [232-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [246-247] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [205-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [238-329] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [168-186] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-209] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [216-234] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-254] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [168-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [212-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-138] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [168-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [185-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [201-232] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [168-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [189-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-278] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-295] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-222] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-322] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-323] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-313] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-276] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-310] for track '26' has 1 frames without a visible bounding box.
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

</details>