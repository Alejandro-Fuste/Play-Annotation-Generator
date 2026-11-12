# Play-Annotation-Generator Annotation Review — SplitZone_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_8`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 28
- **Ball Tracks:** 1
- **Action Segments:** 76
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 174 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 172 | START | 172 | 188 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | `14` | `14` | 175 | START | 175 | 179 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `11` | 175 | START | 175 | 262 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `12` | 175 | START | 189 | 207 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 175 | START | 175 | 262 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `8` | 175 | START | 175 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `9` | 175 | START | 175 | 191 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `2` | 188 | END | 172 | 188 |
| ✅ EXACT | `Action_Handoff` | QB | `2` | `2` | 196 | START | 196 | 216 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `7` | 217 | START | 217 | 245 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 262 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_SnapReceive` | 172 | 188 | 17 | inferred_complete_timeline |
| `Action_None` | 189 | 195 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 196 | 216 | 21 | inferred_complete_timeline |
| `Action_None` | 217 | 245 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_BallCarry` | 217 | 245 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 247 | 338 | 92 | inferred_complete_timeline |
| `Action_BallCarry` | 343 | 359 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 262 | 88 | inferred_complete_timeline |
| `Action_None` | 263 | 296 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 190 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 222 | 240 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 248 | 262 | 15 | inferred_complete_timeline |
| `Action_None` | 263 | 321 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 171 | 102 | inferred_complete_timeline |
| `Action_BallSnap` | 172 | 188 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 207 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 221 | 228 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 262 | 16 | inferred_complete_timeline |
| `Action_None` | 263 | 276 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 191 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 246 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 262 | 88 | inferred_complete_timeline |
| `Action_None` | 263 | 290 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 275 | 104 | inferred_complete_timeline |
| `Action_None` | 284 | 287 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 171 | 130 | inferred_complete_timeline |
| `Action_None` | 172 | 264 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 219 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 171 | 95 | inferred_complete_timeline |
| `Action_None` | 172 | 222 | 51 | inferred_complete_timeline |
| `Action_None` | 228 | 235 | 8 | inferred_complete_timeline |
| `Action_None` | 243 | 324 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 270 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 171 | 89 | inferred_complete_timeline |
| `Action_None` | 172 | 236 | 65 | inferred_complete_timeline |
| `Action_None` | 238 | 243 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 359 | 188 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 16–318 | 250 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 65–201 | 137 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 186–263 | 78 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 225–320 | 85 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 241–243 | 3 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 249–359 | 110 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 270–327 | 58 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 274–331 | 58 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 293–344 | 52 | 1 | Undefined position; Undefined team |
| `24` | `37` | Position_Unknown | Team_Unknown | 320–323 | 4 | 1 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 333–340 | 8 | 1 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 334–359 | 14 | 2 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 351–352 | 2 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 354–359 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `20` | 199 | 204 | 5 | 83.3% | 200 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [172–188], lower_priority='Action_ZoneBlock' annotated_start=175, effective_Action_ZoneBlock_start=189.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-243] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [196-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '2' starts at frame 217, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [217-245] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-270] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-219] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-290] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-222] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-324] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-216] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [217-245] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [247-338] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [343-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [208-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [222-240] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-321] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-191] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [206-246] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-275] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-296] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-207] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [221-228] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [247-262] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-276] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-174] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [175-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [233-262] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-318] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-263] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-240] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-248] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-320] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-344] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-327] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-331] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-344] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-340] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>