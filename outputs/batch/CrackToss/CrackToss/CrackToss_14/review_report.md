# Play-Annotation-Generator Annotation Review — CrackToss_14

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_14`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `29` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | LB4 | defense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | DT2 | defense | `23` | `22` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `18` | `17` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 2 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 2 | START | 2 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 2 | START | 2 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 2 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 2 | START | 2 | 203 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 2 | START | 2 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `25` | `Group` | 2 | START | 2 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `29` | `Group` | 2 | START | 2 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | LB4 | `16` | `15` | 169 | START | 169 | 169 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 171 | END | 169 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | DT2 | `23` | `22` | 172 | START | 172 | 204 |
| ✅ EXACT | `Action_PullBlock` | LT | `18` | `17` | 172 | START | 172 | 278 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 177 | START | 177 | 203 |
| ✅ EXACT | `Action_BallCarry` | RB | `20` | `19` | 204 | START | 204 | 316 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 278 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_SnapReceive` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_None` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_Toss` | 177 | 203 | 27 | inferred_complete_timeline |
| `Action_None` | 204 | 223 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 2–316
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 203 | 202 | inferred_complete_timeline |
| `Action_BallCarry` | 204 | 316 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `29`</summary>

- **xml_track_id:** `28`
- **actor_track_id:** `29`
- **team_side:** `offense`
- **Visible Frames:** 2–312
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 117 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 142 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 152 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 168 | 11 | inferred_complete_timeline |
| `Action_None` | 169 | 203 | 35 | inferred_complete_timeline |
| `Action_None` | 206 | 258 | 53 | inferred_complete_timeline |
| `Action_None` | 261 | 263 | 3 | inferred_complete_timeline |
| `Action_None` | 266 | 312 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 2–214
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 168 | 167 | inferred_complete_timeline |
| `Action_None` | 169 | 214 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 2–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 171 | 170 | inferred_complete_timeline |
| `Action_PullBlock` | 172 | 278 | 107 | inferred_complete_timeline |
| `Action_None` | 279 | 329 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `25`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 2–313
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 168 | 167 | inferred_complete_timeline |
| `Action_None` | 169 | 254 | 86 | inferred_complete_timeline |
| `Action_None` | 257 | 313 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 245 | 77 | inferred_complete_timeline |
| `Action_None` | 247 | 253 | 7 | inferred_complete_timeline |
| `Action_None` | 256 | 270 | 15 | inferred_complete_timeline |
| `Action_None` | 272 | 329 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 2–321
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 168 | 167 | inferred_complete_timeline |
| `Action_None` | 169 | 258 | 90 | inferred_complete_timeline |
| `Action_None` | 269 | 321 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 183 | 15 | inferred_complete_timeline |
| `Action_None` | 186 | 329 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 281 | 113 | inferred_complete_timeline |
| `Action_None` | 283 | 316 | 34 | inferred_complete_timeline |
| `Action_None` | 319 | 329 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 2–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 171 | 170 | inferred_complete_timeline |
| `Action_CrackBlock` | 172 | 204 | 33 | inferred_complete_timeline |
| `Action_CrackBlock` | 209 | 239 | 31 | inferred_complete_timeline |
| `Action_CrackBlock` | 242 | 249 | 8 | inferred_complete_timeline |
| `Action_CrackBlock` | 254 | 278 | 25 | inferred_complete_timeline |
| `Action_None` | 279 | 329 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 2–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 30 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 168 | 137 | inferred_complete_timeline |
| `Action_None` | 169 | 255 | 87 | inferred_complete_timeline |
| `Action_None` | 260 | 329 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 241 | 73 | inferred_complete_timeline |
| `Action_None` | 243 | 249 | 7 | inferred_complete_timeline |
| `Action_None` | 251 | 313 | 63 | inferred_complete_timeline |
| `Action_None` | 320 | 322 | 3 | inferred_complete_timeline |
| `Action_None` | 325 | 329 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 2–73
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 73 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 97 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 113 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 168 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 169 | 169 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 171 | 171 | 1 | inferred_complete_timeline |
| `Action_None` | 172 | 304 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 2–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 168 | 167 | inferred_complete_timeline |
| `Action_None` | 169 | 215 | 47 | inferred_complete_timeline |
| `Action_None` | 219 | 224 | 6 | inferred_complete_timeline |
| `Action_None` | 228 | 329 | 102 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–208 | 209 | 2 | Undefined position; Undefined team |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 2–211 | 210 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 2–72 | 71 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 2–275 | 273 | 3 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 56–329 | 274 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 79–329 | 250 | 3 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 174–176 | 3 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 179–329 | 148 | 2 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 185–243 | 55 | 5 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 223–226 | 4 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 273–329 | 57 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 288–329 | 42 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 294–322 | 12 | 2 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 311–329 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `23` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 30: Duplicate assignment for track ID '23' in grid. Overwriting previous assignment.
- ⚠️ Row 30: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '17' (LT) duration 107 frames exceeds threshold 90 frames [start=172, end=278].
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-245] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-253] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-270] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-208] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-281] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-316] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-223] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-241] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-249] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-313] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' for track '15' starts at frame 169, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallSnap' range [169-169] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-304] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-255] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-214] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [204-316] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-215] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-321] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [172-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [209-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [242-249] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-254] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-313] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-72] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-168] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-275] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-117] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-142] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-152] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-168] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-258] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-312] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-222] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-192] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-200] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-243] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-303] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
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