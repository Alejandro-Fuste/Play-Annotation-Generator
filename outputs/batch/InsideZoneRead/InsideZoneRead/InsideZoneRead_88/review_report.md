# Play-Annotation-Generator Annotation Review — InsideZoneRead_88

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_88`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 148
- **Validation Warnings:** 166
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 122
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 23 | START | 23 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 23 | START | 23 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 23 | START | 23 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 23 | START | 23 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 23 | START | 23 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 23 | START | 23 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 23 | START | 23 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 23 | START | 23 | 62 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 63 | START | 63 | 76 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `0` | 65 | START | 65 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `9` | 65 | START | 65 | 113 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `3` | 65 | START | 65 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `6` | 65 | START | 65 | 146 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `8` | `7` | 65 | START | 77 | 101 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 76 | END | 63 | 76 |
| ✅ EXACT | `Action_ReadDefender` | QB | `5` | `4` | 82 | START | 82 | 93 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 94 | START | 94 | 106 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `8` | `7` | 102 | START | 102 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `14` | `13` | 107 | START | 109 | 303 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 146 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 23–389
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 62 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 63 | 76 | 14 | inferred_complete_timeline |
| `Action_None` | 77 | 81 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 82 | 93 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 94 | 106 | 13 | inferred_complete_timeline |
| `Action_None` | 107 | 244 | 138 | inferred_complete_timeline |
| `Action_None` | 246 | 253 | 8 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 258 | 268 | 11 | inferred_complete_timeline |
| `Action_None` | 270 | 389 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 23–389
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 103 | 81 | inferred_complete_timeline |
| `Action_BallCarry` | 109 | 303 | 195 | inferred_complete_timeline |
| `Action_BallCarry` | 315 | 389 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 23–65
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 62 | 40 | inferred_complete_timeline |
| `Action_None` | 63 | 65 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 23–253
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 33 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 64 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 146 | 82 | inferred_complete_timeline |
| `Action_None` | 147 | 162 | 16 | inferred_complete_timeline |
| `Action_None` | 165 | 253 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 23–214
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 64 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 113 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 146 | 26 | inferred_complete_timeline |
| `Action_None` | 147 | 187 | 41 | inferred_complete_timeline |
| `Action_None` | 202 | 207 | 6 | inferred_complete_timeline |
| `Action_None` | 211 | 214 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 23–140
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 62 | 40 | inferred_complete_timeline |
| `Action_BallSnap` | 63 | 76 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 101 | 25 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 102 | 140 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 23–389
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 64 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 146 | 82 | inferred_complete_timeline |
| `Action_None` | 147 | 171 | 25 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 207 | 11 | inferred_complete_timeline |
| `Action_None` | 215 | 233 | 19 | inferred_complete_timeline |
| `Action_None` | 235 | 243 | 9 | inferred_complete_timeline |
| `Action_None` | 245 | 268 | 24 | inferred_complete_timeline |
| `Action_None` | 272 | 282 | 11 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_None` | 287 | 389 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 23–262
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 64 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 146 | 82 | inferred_complete_timeline |
| `Action_None` | 147 | 255 | 109 | inferred_complete_timeline |
| `Action_None` | 260 | 262 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 23–389
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 62 | 40 | inferred_complete_timeline |
| `Action_None` | 63 | 389 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 23–139
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 62 | 40 | inferred_complete_timeline |
| `Action_None` | 63 | 139 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 29–182
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 43 | 15 | inferred_complete_timeline |
| `Action_None` | 69 | 120 | 52 | inferred_complete_timeline |
| `Action_None` | 122 | 161 | 40 | inferred_complete_timeline |
| `Action_None` | 168 | 172 | 5 | inferred_complete_timeline |
| `Action_None` | 174 | 182 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 23–253
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 62 | 40 | inferred_complete_timeline |
| `Action_None` | 63 | 75 | 13 | inferred_complete_timeline |
| `Action_None` | 123 | 138 | 16 | inferred_complete_timeline |
| `Action_None` | 143 | 151 | 9 | inferred_complete_timeline |
| `Action_None` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 251 | 253 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 23–263
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 62 | 40 | inferred_complete_timeline |
| `Action_None` | 63 | 228 | 166 | inferred_complete_timeline |
| `Action_None` | 231 | 233 | 3 | inferred_complete_timeline |
| `Action_None` | 235 | 242 | 8 | inferred_complete_timeline |
| `Action_None` | 250 | 263 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 23–205
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 62 | 40 | inferred_complete_timeline |
| `Action_None` | 63 | 177 | 115 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 205 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 23–60
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 60 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 23–143
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 62 | 40 | inferred_complete_timeline |
| `Action_None` | 63 | 143 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `19` | Position_Unknown | Team_Unknown | 99–389 | 268 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 126–389 | 258 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 149–253 | 105 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 151–389 | 228 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 157–205 | 16 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 157–389 | 225 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 189–328 | 81 | 8 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 220–253 | 10 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 221–389 | 169 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 273–278 | 4 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 294–382 | 81 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 300–389 | 87 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 306–389 | 79 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 310–383 | 74 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 310–389 | 68 | 5 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 318–354 | 5 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 318–389 | 72 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 318–387 | 65 | 4 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 321–389 | 49 | 4 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 321–389 | 69 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 324–389 | 60 | 4 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 325–389 | 55 | 5 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 350–375 | 24 | 3 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 359–361 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `8` (C): Annotated start 65 != Inferred start 77
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 116 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [63–76], lower_priority='Action_ZoneBlock' annotated_start=65, effective_Action_ZoneBlock_start=77.
- ⚠️ Action 'Action_None' range [147-255] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-228] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-171] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-207] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-233] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-243] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-268] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-282] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-389] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-244] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-268] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-205] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-33] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-162] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-253] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [102-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-45] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-138] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [109-303] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-120] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-161] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-136] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-320] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-389] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-135] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-383] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-253] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-167] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-205] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-389] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-208] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-301] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-256] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-270] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-382] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-383] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-389] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-383] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-338] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-356] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-389] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-333] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-380] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-334] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-358] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-383] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-389] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-389] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-343] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-384] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-340] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-354] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-374] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-367] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-375] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '39' has 1 frames without a visible bounding box.
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