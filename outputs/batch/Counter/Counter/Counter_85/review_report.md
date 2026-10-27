# Play-Annotation-Generator Annotation Review — Counter_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_85`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 76
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `19` | `18` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 4 | START | 4 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 4 | START | 4 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `15` | `Group` | 4 | START | 4 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 4 | START | 4 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 4 | START | 4 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 4 | START | 4 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 4 | START | 4 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 4 | START | 4 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 4 | START | 4 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 4 | START | 4 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 4 | START | 4 | 153 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 154 | START | 154 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `19` | `18` | 157 | START | 157 | 172 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `8` | `7` | 157 | START | 171 | 175 |
| ✅ EXACT | `Action_PullBlock` | RG | `22` | `21` | 157 | START | 157 | 172 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `20` | `19` | 157 | START | 157 | 174 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `20` | 170 | END | 154 | 170 |
| ✅ EXACT | `Action_Handoff` | QB | `21` | `20` | 178 | START | 178 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `15` | 198 | START | 198 | 221 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 229 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_SnapReceive` | 154 | 170 | 17 | inferred_complete_timeline |
| `Action_None` | 171 | 177 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 178 | 197 | 20 | inferred_complete_timeline |
| `Action_None` | 198 | 329 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 4–312
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 197 | 194 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 221 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 224 | 299 | 76 | inferred_complete_timeline |
| `Action_BallCarry` | 311 | 312 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 329 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 4–213
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 213 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 4–327
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 327 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 174 | 21 | inferred_complete_timeline |
| `Action_None` | 247 | 249 | 3 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 291 | 32 | inferred_complete_timeline |
| `Action_None` | 294 | 302 | 9 | inferred_complete_timeline |
| `Action_None` | 320 | 323 | 4 | inferred_complete_timeline |
| `Action_None` | 326 | 329 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 174 | 21 | inferred_complete_timeline |
| `Action_None` | 242 | 329 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 4–211
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 156 | 153 | inferred_complete_timeline |
| `Action_DownBlock` | 157 | 172 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 204 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 210 | 211 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_BallSnap` | 154 | 170 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 171 | 175 | 5 | inferred_complete_timeline |
| `Action_None` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 329 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 4–172
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 156 | 153 | inferred_complete_timeline |
| `Action_PullBlock` | 157 | 172 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 4–174
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 156 | 153 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 157 | 174 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 4–329
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 180 | 27 | inferred_complete_timeline |
| `Action_None` | 182 | 185 | 4 | inferred_complete_timeline |
| `Action_None` | 188 | 202 | 15 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 301 | 58 | inferred_complete_timeline |
| `Action_None` | 303 | 329 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 4–236
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 177 | 24 | inferred_complete_timeline |
| `Action_None` | 191 | 236 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 4–174
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 174 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 4–173
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 173 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–202
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 202 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–329
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 183 | 30 | inferred_complete_timeline |
| `Action_None` | 218 | 231 | 14 | inferred_complete_timeline |
| `Action_None` | 233 | 237 | 5 | inferred_complete_timeline |
| `Action_None` | 239 | 243 | 5 | inferred_complete_timeline |
| `Action_None` | 249 | 329 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 4–300
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 243 | 90 | inferred_complete_timeline |
| `Action_None` | 245 | 253 | 9 | inferred_complete_timeline |
| `Action_None` | 257 | 279 | 23 | inferred_complete_timeline |
| `Action_None` | 281 | 283 | 3 | inferred_complete_timeline |
| `Action_None` | 286 | 300 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 4–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 329 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 278 | 125 | inferred_complete_timeline |
| `Action_None` | 283 | 314 | 32 | inferred_complete_timeline |
| `Action_None` | 320 | 329 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 4–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 329 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 4–301
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 153 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 301 | 148 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 214–329 | 99 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 251–329 | 79 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 260–318 | 44 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 264–329 | 61 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 264–329 | 66 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 266–329 | 58 | 4 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 270–312 | 42 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 274–329 | 56 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (4 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `8` (C): Annotated start 157 != Inferred start 171
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [154–170], lower_priority='Action_DownBlock' annotated_start=157, effective_Action_DownBlock_start=171.
- ⚠️ Action 'Action_None' range [154-243] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-253] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-279] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-300] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-202] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-301] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-327] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-301] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [171-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-202] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-231] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-278] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-314] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-291] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-302] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-221] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [224-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [311-312] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-177] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [206-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [210-211] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [157-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [157-172] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-221] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-252] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-318] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-274] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-291] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-318] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-313] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-274] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-291] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-309] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '29' has 1 frames without a visible bounding box.
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

</details>