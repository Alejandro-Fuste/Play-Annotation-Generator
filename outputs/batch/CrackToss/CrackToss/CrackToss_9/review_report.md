# Play-Annotation-Generator Annotation Review — CrackToss_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_9`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 186
- **Validation Warnings:** 222
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 158
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `20` | `19` |
| ❌ MISSING SEGMENT | `Action_CrackBlock` | WR2 | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `24` | `22` |
| ✅ EXACT | `Action_Toss` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 199 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `15` | `14` | 200 | START | 200 | 202 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `20` | `19` | 202 | END | 200 | 202 |
| ❌ MISSING SEGMENT | `Action_CrackBlock` | WR2 | `13` | `12` | 204 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE | `12` | `11` | 204 | START | 206 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `24` | `22` | 204 | START | 224 | 229 |
| ✅ EXACT | `Action_Toss` | Position_Unknown | `20` | `19` | 210 | START | 210 | 234 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `1` | `0` | 235 | START | 235 | 301 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 310 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–316
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_BallCarry` | 235 | 301 | 67 | inferred_complete_timeline |
| `Action_BallCarry` | 315 | 316 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 218 | 19 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 278 | 281 | 4 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 347 | 359 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 50 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 159 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 175 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 178 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–332
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 332 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 109 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 148 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 159 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 202 | 39 | inferred_complete_timeline |
| `Action_PullBlock` | 206 | 210 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 212 | 232 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 241 | 265 | 25 | inferred_complete_timeline |
| `Action_PullBlock` | 269 | 271 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 274 | 275 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 302 | 305 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 313 | 315 | 3 | inferred_complete_timeline |
| `Action_None` | 317 | 359 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 61 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 141 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 199 | 53 | inferred_complete_timeline |
| `Action_None` | 200 | 204 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–335
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 34 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 67 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 108 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 186 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 199 | 5 | inferred_complete_timeline |
| `Action_None` | 200 | 200 | 1 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_None` | 309 | 335 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–340
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 232 | 33 | inferred_complete_timeline |
| `Action_None` | 308 | 314 | 7 | inferred_complete_timeline |
| `Action_None` | 318 | 324 | 7 | inferred_complete_timeline |
| `Action_None` | 328 | 340 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 243 | 44 | inferred_complete_timeline |
| `Action_None` | 246 | 248 | 3 | inferred_complete_timeline |
| `Action_None` | 251 | 291 | 41 | inferred_complete_timeline |
| `Action_None` | 311 | 359 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–303
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 244 | 45 | inferred_complete_timeline |
| `Action_None` | 302 | 303 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 248 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–342
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 342 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 269 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 359 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 7–207 | 176 | 7 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 10–357 | 271 | 10 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 12–200 | 129 | 11 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 12–291 | 219 | 13 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 12–56 | 18 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 12–293 | 212 | 8 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 12–49 | 12 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 42–200 | 56 | 10 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 153–233 | 22 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 263–283 | 13 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 269–279 | 11 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 274–286 | 10 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 280–318 | 39 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 292–359 | 64 | 3 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 292–359 | 17 | 6 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 310–312 | 3 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 313–314 | 2 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 317–324 | 7 | 2 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 319–359 | 41 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 320–359 | 33 | 5 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 324–332 | 9 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 327–359 | 32 | 2 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 329–334 | 6 | 1 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 334–335 | 2 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 341–359 | 19 | 1 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 343–345 | 3 | 1 | Undefined position; Undefined team |
| `40` | `62` | Position_Unknown | Team_Unknown | 357–359 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CrackBlock` on target `13` (WR2)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (9 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `24` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 165 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '11' (TE) duration 107 frames exceeds threshold 90 frames [start=204, end=310].
- ⚠️ Segment 'Action_CrackBlock' for track '12' has invalid range: start=204, end=178. Clamping end to start.
- ⚠️ Action 'Action_BallCarry' range [235-301] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [315-316] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-332] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-248] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-342] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-269] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-291] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-359] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-34] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-67] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-186] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '8' starts at frame 200, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [200-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-335] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-232] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-314] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-324] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-340] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-218] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-109] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-148] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-202] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [206-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [212-232] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [235-236] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [238-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [241-265] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [269-271] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [274-275] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [302-305] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [309-310] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-50] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-61] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-141] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 200, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [200-204] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-67] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-199] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-199] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-271] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-306] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-353] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-67] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-111] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-188] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 200, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [200-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-22] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-51] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-57] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-252] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-285] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-49] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-25] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-43] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-293] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-45] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-181] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-199] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 200, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [200-200] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-159] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-170] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [224-229] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [231-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-274] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-279] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-286] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-318] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-298] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-337] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-352] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-334] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-354] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-332] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-353] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-334] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>