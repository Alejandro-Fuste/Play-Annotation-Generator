# Play-Annotation-Generator Annotation Review — InsideZoneRead_132

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_132`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 132
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 100
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `7` |
| ⚠️ START CHANGED | `Action_Handoff` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `6` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 101 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 151 | START | 151 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `9` | 154 | START | 154 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 154 | START | 165 | 194 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `11` | 154 | START | 154 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `1` | 154 | START | 154 | 163 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 154 | START | 154 | 199 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 164 | END | 151 | 164 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `7` | 168 | START | 168 | 180 |
| ⚠️ START CHANGED | `Action_Handoff` | QB | `8` | `7` | 182 | START | 183 | 189 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `11` | `10` | 195 | START | 195 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `2` | 196 | START | 196 | 208 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 233 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 150 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 151 | 164 | 14 | inferred_complete_timeline |
| `Action_None` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 168 | 180 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 183 | 189 | 7 | inferred_complete_timeline |
| `Action_None` | 251 | 259 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 195 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 208 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 261 | 286 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 288 | 289 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 292 | 305 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 310 | 359 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 25 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 75 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 199 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 163 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 196 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_BallSnap` | 151 | 164 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 194 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 195 | 233 | 39 | inferred_complete_timeline |
| `Action_None` | 234 | 262 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–330
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 171 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 197 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 210 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 231 | 17 | inferred_complete_timeline |
| `Action_None` | 236 | 267 | 32 | inferred_complete_timeline |
| `Action_None` | 278 | 312 | 35 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 330 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 233 | 80 | inferred_complete_timeline |
| `Action_None` | 234 | 310 | 77 | inferred_complete_timeline |
| `Action_None` | 319 | 359 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 16 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 25 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 59 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 150 | 85 | inferred_complete_timeline |
| `Action_None` | 151 | 166 | 16 | inferred_complete_timeline |
| `Action_None` | 235 | 244 | 10 | inferred_complete_timeline |
| `Action_None` | 246 | 285 | 40 | inferred_complete_timeline |
| `Action_None` | 287 | 359 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 57 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 150 | 90 | inferred_complete_timeline |
| `Action_None` | 151 | 226 | 76 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 302 | 10 | inferred_complete_timeline |
| `Action_None` | 307 | 359 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–18
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 18 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 150 | 98 | inferred_complete_timeline |
| `Action_None` | 151 | 201 | 51 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 211 | 226 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_None` | 151 | 215 | 65 | inferred_complete_timeline |
| `Action_None` | 219 | 234 | 16 | inferred_complete_timeline |
| `Action_None` | 238 | 271 | 34 | inferred_complete_timeline |
| `Action_None` | 276 | 279 | 4 | inferred_complete_timeline |
| `Action_None` | 282 | 309 | 28 | inferred_complete_timeline |
| `Action_None` | 324 | 359 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 14–32 | 19 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 38–269 | 154 | 6 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 74–359 | 250 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 155–359 | 147 | 12 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 193–355 | 131 | 9 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 197–341 | 131 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 216–314 | 98 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 231–246 | 16 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 238–311 | 74 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 246–359 | 101 | 5 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 255–285 | 30 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 260–359 | 97 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 288–355 | 60 | 4 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 290–359 | 70 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 306–359 | 54 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 336–359 | 24 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 336–359 | 24 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 339–359 | 21 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 355–359 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `8` (QB): Annotated start 182 != Inferred start 183
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 106 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [151–164], lower_priority='Action_ZoneBlock' annotated_start=154, effective_Action_ZoneBlock_start=165.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-185] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-181] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-208] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [261-286] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [288-289] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [292-305] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-199] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-25] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-75] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-201] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-226] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [168-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [183-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-259] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-234] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-271] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-309] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-171] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-197] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [215-231] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-267] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-312] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-330] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [195-233] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-262] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-310] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-16] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-25] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-59] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-166] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-244] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-285] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-226] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-302] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-18] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-93] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-284] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-204] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-248] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-286] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-304] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-233] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-241] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-289] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-310] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-318] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-355] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-273] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-330] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-341] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-245] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-314] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-246] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-311] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-283] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-339] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-277] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-285] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-270] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-359] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-327] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-335] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-350] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '33' has 1 frames without a visible bounding box.
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

</details>