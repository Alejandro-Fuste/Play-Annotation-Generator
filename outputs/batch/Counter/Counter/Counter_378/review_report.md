# Play-Annotation-Generator Annotation Review — Counter_378

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_378`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 173
- **Validation Warnings:** 211
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 144
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | offense | `15` | `13` |
| ✅ EXACT | `Action_DownBlock` | DT1 | defense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `20` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `24` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 2 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 7 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 64 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 98 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 168 | 173 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `9` | `8` | 184 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | `15` | `13` | 187 | START | 187 | 191 |
| ✅ EXACT | `Action_DownBlock` | DT1 | `4` | `3` | 187 | START | 187 | 253 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `9` | `8` | 187 | START | 209 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `20` | `15` | 187 | START | 187 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `1` | `0` | 187 | START | 187 | 206 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 202 | END | 184 | 202 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 214 | START | 214 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `24` | `18` | 238 | START | 238 | 238 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 268 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 2–233
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 18 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 25 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 46 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 84 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 183 | 98 | inferred_complete_timeline |
| `Action_SnapReceive` | 184 | 202 | 19 | inferred_complete_timeline |
| `Action_None` | 203 | 207 | 5 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 214 | 233 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 98–246
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 98 | 186 | 89 | inferred_complete_timeline |
| `Action_DownBlock` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 197 | 246 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 64–382
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 64 | 69 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 108 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 119 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 148 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 183 | 18 | inferred_complete_timeline |
| `Action_None` | 184 | 209 | 26 | inferred_complete_timeline |
| `Action_None` | 214 | 217 | 4 | inferred_complete_timeline |
| `Action_None` | 225 | 277 | 53 | inferred_complete_timeline |
| `Action_None` | 299 | 328 | 30 | inferred_complete_timeline |
| `Action_None` | 331 | 332 | 2 | inferred_complete_timeline |
| `Action_None` | 337 | 382 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 168–225
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 168 | 173 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 186 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 187 | 189 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 194 | 225 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 7–39
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 35 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 39 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 199 | 16 | inferred_complete_timeline |
| `Action_None` | 259 | 266 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 389 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_DownBlock` | 187 | 253 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 145–227
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 145 | 183 | 39 | inferred_complete_timeline |
| `Action_None` | 184 | 227 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 260 | 77 | inferred_complete_timeline |
| `Action_None` | 264 | 267 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 24 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 183 | 154 | inferred_complete_timeline |
| `Action_None` | 184 | 226 | 43 | inferred_complete_timeline |
| `Action_None` | 241 | 302 | 62 | inferred_complete_timeline |
| `Action_None` | 309 | 311 | 3 | inferred_complete_timeline |
| `Action_None` | 314 | 317 | 4 | inferred_complete_timeline |
| `Action_None` | 326 | 327 | 2 | inferred_complete_timeline |
| `Action_None` | 334 | 347 | 14 | inferred_complete_timeline |
| `Action_None` | 351 | 352 | 2 | inferred_complete_timeline |
| `Action_None` | 358 | 364 | 7 | inferred_complete_timeline |
| `Action_None` | 369 | 370 | 2 | inferred_complete_timeline |
| `Action_None` | 377 | 389 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 27 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 183 | 142 | inferred_complete_timeline |
| `Action_None` | 184 | 233 | 50 | inferred_complete_timeline |
| `Action_None` | 244 | 248 | 5 | inferred_complete_timeline |
| `Action_None` | 252 | 284 | 33 | inferred_complete_timeline |
| `Action_None` | 287 | 288 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 341 | 50 | inferred_complete_timeline |
| `Action_None` | 363 | 365 | 3 | inferred_complete_timeline |
| `Action_None` | 367 | 368 | 2 | inferred_complete_timeline |
| `Action_None` | 373 | 381 | 9 | inferred_complete_timeline |
| `Action_None` | 384 | 389 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–347 | 329 | 4 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–46 | 41 | 3 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–366 | 214 | 10 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 47–62 | 6 | 2 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 203–367 | 108 | 6 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 207–236 | 30 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 212–302 | 55 | 6 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 216–230 | 13 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 232–312 | 9 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 242–319 | 62 | 4 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 247–386 | 119 | 6 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 250–318 | 41 | 5 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 257–389 | 129 | 4 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 268–315 | 27 | 4 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 276–308 | 33 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 276–389 | 97 | 7 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 284–389 | 96 | 2 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 296–389 | 93 | 2 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 306–336 | 10 | 3 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 317–389 | 33 | 5 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 322–389 | 64 | 3 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 326–389 | 58 | 2 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 332–389 | 52 | 3 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 332–378 | 37 | 4 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 335–389 | 54 | 2 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 336–388 | 37 | 6 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 343–389 | 46 | 2 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 362–367 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `9` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `24` (5 segments found)

### Track Identity Issues

- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 154 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PullLeadBlock' range [187-206] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [226-268] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-347] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [187-253] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-260] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-27] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-233] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-248] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-284] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-341] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-365] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-381] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-389] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-46] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-24] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-183] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-226] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-347] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-364] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-19] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-51] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-158] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [209-212] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [223-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-311] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-366] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-18] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-25] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-84] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [214-233] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-35] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-62] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-69] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-108] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-119] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-148] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-183] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-277] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-328] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-382] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [187-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [197-246] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-227] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [187-189] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [194-225] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-243] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-302] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-367] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-236] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '18' starts at frame 238, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [238-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [272-273] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [275-294] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [296-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [300-302] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-312] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-263] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-307] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-273] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-330] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-386] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-272] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-300] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-275] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-288] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-389] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-284] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-305] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-308] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-290] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-303] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-317] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-307] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-305] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-361] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-384] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-389] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-350] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-347] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-366] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-340] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-389] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-352] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-372] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-381] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-388] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-380] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>