# Play-Annotation-Generator Annotation Review — JetSweep_96

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_96`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 3 | START | 3 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 3 | START | 3 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 3 | START | 3 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 3 | START | 3 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 3 | START | 3 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 3 | START | 3 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 3 | START | 3 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 3 | START | 3 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `22` | `Group` | 3 | START | 3 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 3 | START | 3 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 3 | START | 3 | 93 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `2` | `1` | 70 | START | 70 | 122 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 94 | START | 94 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 98 | START | 109 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `16` | 98 | START | 98 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `17` | 98 | START | 98 | 126 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `19` | `18` | 98 | START | 98 | 157 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `6` | 98 | START | 98 | 157 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 108 | END | 94 | 108 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 115 | START | 115 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `2` | `1` | 123 | START | 123 | 272 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 157 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 3–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_SnapReceive` | 94 | 108 | 15 | inferred_complete_timeline |
| `Action_None` | 109 | 114 | 6 | inferred_complete_timeline |
| `Action_Toss` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_None` | 123 | 343 | 221 | inferred_complete_timeline |
| `Action_None` | 347 | 350 | 4 | inferred_complete_timeline |
| `Action_None` | 353 | 359 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 3–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 328 | 235 | inferred_complete_timeline |
| `Action_None` | 331 | 359 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 69 | 67 | inferred_complete_timeline |
| `Action_JetMotion` | 70 | 122 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 123 | 272 | 150 | inferred_complete_timeline |
| `Action_BallCarry` | 278 | 294 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 297 | 359 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–281
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 242 | 149 | inferred_complete_timeline |
| `Action_None` | 245 | 255 | 11 | inferred_complete_timeline |
| `Action_None` | 260 | 264 | 5 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |
| `Action_None` | 274 | 281 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 3–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 308 | 215 | inferred_complete_timeline |
| `Action_None` | 313 | 351 | 39 | inferred_complete_timeline |
| `Action_None` | 355 | 359 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 3–327
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 327 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 3–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 97 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 143 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 157 | 13 | inferred_complete_timeline |
| `Action_None` | 158 | 359 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 3–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 97 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 126 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 157 | 26 | inferred_complete_timeline |
| `Action_None` | 158 | 320 | 163 | inferred_complete_timeline |
| `Action_None` | 323 | 324 | 2 | inferred_complete_timeline |
| `Action_None` | 328 | 359 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 3–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_BallSnap` | 94 | 108 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 141 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 157 | 14 | inferred_complete_timeline |
| `Action_None` | 158 | 264 | 107 | inferred_complete_timeline |
| `Action_None` | 266 | 359 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 3–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 97 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 157 | 60 | inferred_complete_timeline |
| `Action_None` | 158 | 338 | 181 | inferred_complete_timeline |
| `Action_None` | 342 | 350 | 9 | inferred_complete_timeline |
| `Action_None` | 352 | 359 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 3–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 97 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 157 | 60 | inferred_complete_timeline |
| `Action_None` | 158 | 359 | 202 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 3–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 359 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 138 | 45 | inferred_complete_timeline |
| `Action_None` | 144 | 151 | 8 | inferred_complete_timeline |
| `Action_None` | 154 | 359 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 154 | 61 | inferred_complete_timeline |
| `Action_None` | 159 | 298 | 140 | inferred_complete_timeline |
| `Action_None` | 300 | 359 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 3–342
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 342 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 359 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–309
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 260 | 167 | inferred_complete_timeline |
| `Action_None` | 262 | 309 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 333 | 240 | inferred_complete_timeline |
| `Action_None` | 336 | 359 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 3–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 359 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–281
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 245 | 152 | inferred_complete_timeline |
| `Action_None` | 248 | 273 | 26 | inferred_complete_timeline |
| `Action_None` | 276 | 281 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 3–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 359 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–281
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 94 | 281 | 188 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 197–218 | 19 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 202–207 | 6 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 217–276 | 60 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 229–311 | 52 | 6 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 308–359 | 52 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 308–325 | 13 | 4 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 324–326 | 3 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 325–359 | 35 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 337–359 | 23 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [94–108], lower_priority='Action_ZoneBlock' annotated_start=98, effective_Action_ZoneBlock_start=109.
- ⚠️ Action 'Action_None' range [94-242] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-255] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-281] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-272] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [278-294] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-260] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-309] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-333] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-154] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-298] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-328] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-245] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-273] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-281] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-327] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-281] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-264] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-343] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-350] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-320] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-338] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-350] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-342] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-308] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-351] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-205] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-276] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-250] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-266] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-311] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '28' has 1 frames without a visible bounding box.
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