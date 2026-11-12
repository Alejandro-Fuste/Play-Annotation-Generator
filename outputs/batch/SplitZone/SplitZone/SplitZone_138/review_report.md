# Play-Annotation-Generator Annotation Review — SplitZone_138

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_138`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 153
- **Validation Warnings:** 183
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 135
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `0` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `0` | `Group` | 25 | START | 26 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 25 | START | 26 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 25 | START | 42 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 25 | START | 43 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 25 | START | 46 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 25 | START | 26 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `5` | `Group` | 25 | START | 26 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 25 | START | 26 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `9` | `Group` | 25 | START | 26 | 97 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `17` | 98 | START | 98 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `13` | 101 | START | 101 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `16` | 101 | START | 101 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `17` | 101 | START | 112 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `4` | 101 | START | 101 | 134 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 101 | START | 101 | 144 |
| ✅ EXACT | `Action_SnapReceive` | QB | `0` | `0` | 111 | END | 98 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `0` | `0` | 132 | START | 221 | 223 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 264 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 26–387
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 97 | 72 | inferred_complete_timeline |
| `Action_SnapReceive` | 98 | 111 | 14 | inferred_complete_timeline |
| `Action_None` | 112 | 131 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 221 | 223 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 225 | 326 | 102 | inferred_complete_timeline |
| `Action_BallCarry` | 331 | 387 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 26–389
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 97 | 72 | inferred_complete_timeline |
| `Action_None` | 98 | 133 | 36 | inferred_complete_timeline |
| `Action_None` | 135 | 138 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 167 | 19 | inferred_complete_timeline |
| `Action_None` | 170 | 185 | 16 | inferred_complete_timeline |
| `Action_None` | 192 | 250 | 59 | inferred_complete_timeline |
| `Action_None` | 295 | 303 | 9 | inferred_complete_timeline |
| `Action_None` | 315 | 333 | 19 | inferred_complete_timeline |
| `Action_None` | 335 | 342 | 8 | inferred_complete_timeline |
| `Action_None` | 345 | 357 | 13 | inferred_complete_timeline |
| `Action_None` | 359 | 366 | 8 | inferred_complete_timeline |
| `Action_None` | 386 | 387 | 2 | inferred_complete_timeline |
| `Action_None` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 26–144
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 97 | 72 | inferred_complete_timeline |
| `Action_None` | 98 | 137 | 40 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 42–191
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 42 | 58 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 97 | 21 | inferred_complete_timeline |
| `Action_None` | 98 | 191 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 26–144
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 100 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 144 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 26–389
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 100 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 134 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 224 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 230 | 232 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 248 | 264 | 17 | inferred_complete_timeline |
| `Action_None` | 265 | 273 | 9 | inferred_complete_timeline |
| `Action_None` | 275 | 389 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 46–180
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 46 | 97 | 52 | inferred_complete_timeline |
| `Action_BallSnap` | 98 | 111 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 165 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 180 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 43–151
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 43 | 100 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 112 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 26–320
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 100 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 206 | 106 | inferred_complete_timeline |
| `Action_ZoneBlock` | 221 | 264 | 44 | inferred_complete_timeline |
| `Action_None` | 265 | 320 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 26–253
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 97 | 72 | inferred_complete_timeline |
| `Action_None` | 98 | 143 | 46 | inferred_complete_timeline |
| `Action_None` | 146 | 228 | 83 | inferred_complete_timeline |
| `Action_None` | 231 | 233 | 3 | inferred_complete_timeline |
| `Action_None` | 244 | 253 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 26–389
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 52 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 97 | 40 | inferred_complete_timeline |
| `Action_None` | 98 | 322 | 225 | inferred_complete_timeline |
| `Action_None` | 349 | 389 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 26–387
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 97 | 72 | inferred_complete_timeline |
| `Action_None` | 98 | 283 | 186 | inferred_complete_timeline |
| `Action_None` | 287 | 321 | 35 | inferred_complete_timeline |
| `Action_None` | 326 | 364 | 39 | inferred_complete_timeline |
| `Action_None` | 369 | 370 | 2 | inferred_complete_timeline |
| `Action_None` | 372 | 387 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 26–389
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 43 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 74 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 97 | 21 | inferred_complete_timeline |
| `Action_None` | 98 | 180 | 83 | inferred_complete_timeline |
| `Action_None` | 182 | 244 | 63 | inferred_complete_timeline |
| `Action_None` | 257 | 281 | 25 | inferred_complete_timeline |
| `Action_None` | 290 | 293 | 4 | inferred_complete_timeline |
| `Action_None` | 338 | 370 | 33 | inferred_complete_timeline |
| `Action_None` | 372 | 389 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 26–245
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 97 | 72 | inferred_complete_timeline |
| `Action_None` | 98 | 185 | 88 | inferred_complete_timeline |
| `Action_None` | 193 | 201 | 9 | inferred_complete_timeline |
| `Action_None` | 208 | 245 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 26–239
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 97 | 72 | inferred_complete_timeline |
| `Action_None` | 98 | 180 | 83 | inferred_complete_timeline |
| `Action_None` | 182 | 239 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 26–168
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 97 | 72 | inferred_complete_timeline |
| `Action_None` | 98 | 168 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 26–119
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 97 | 72 | inferred_complete_timeline |
| `Action_None` | 98 | 119 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 26–59 | 34 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 137–233 | 88 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 137–289 | 153 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 154–243 | 51 | 7 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 158–349 | 186 | 4 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 174–389 | 178 | 6 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 185–205 | 21 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 187–389 | 195 | 4 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 190–389 | 178 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 193–208 | 16 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 197–389 | 193 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 202–215 | 14 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 228–385 | 148 | 4 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 234–283 | 46 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 242–246 | 5 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 249–389 | 105 | 3 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 256–259 | 4 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 261–389 | 123 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 267–389 | 115 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 294–389 | 95 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 297–389 | 91 | 2 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 298–309 | 12 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 300–369 | 70 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 301–389 | 80 | 4 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 306–389 | 62 | 4 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 317–389 | 68 | 3 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 327–338 | 12 | 1 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 336–373 | 36 | 2 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 338–389 | 25 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 121 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (LG) duration 164 frames exceeds threshold 90 frames [start=101, end=264].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RT) duration 164 frames exceeds threshold 90 frames [start=101, end=264].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [98–111], lower_priority='Action_ZoneBlock' annotated_start=101, effective_Action_ZoneBlock_start=112.
- ⚠️ Action 'Action_None' range [112-131] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [221-223] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [225-326] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [331-387] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-52] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-322] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-389] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-228] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-253] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-224] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [230-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-273] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-389] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-133] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-167] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-185] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-303] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-333] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-342] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-357] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-366] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-59] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-168] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-245] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-244] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-281] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-370] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-320] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-283] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-321] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-364] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-387] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-180] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-233] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-289] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-184] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-243] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-253] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-349] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-232] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-285] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-253] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-280] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-231] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-389] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-208] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-271] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-280] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-367] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-385] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-254] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-278] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-293] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-266] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-389] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-294] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-389] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-374] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-309] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-369] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-307] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-339] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-320] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-348] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-344] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-370] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-338] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-366] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-373] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-350] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-376] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.

</details>