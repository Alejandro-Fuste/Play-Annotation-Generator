# Play-Annotation-Generator Annotation Review — JetSweep_172

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_172`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 40
- **Ball Tracks:** 1
- **Action Segments:** 94
- **Validation Warnings:** 121
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
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `18` |
| ✅ EXACT | `Action_LeadBlock` | TE1 | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 0 | START | 0 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 177 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `20` | `18` | 177 | START | 178 | 188 |
| ✅ EXACT | `Action_LeadBlock` | TE1 | `8` | `7` | 178 | START | 178 | 179 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `1` | 178 | START | 178 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `3` | 178 | START | 178 | 199 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `4` | 178 | START | 178 | 199 |
| ✅ EXACT | `Action_ZoneBlock` | C | `7` | `6` | 178 | START | 178 | 199 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `8` | 178 | START | 178 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | LG | `2` | `1` | 182 | START | 182 | 194 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 188 | END | 177 | 188 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 199 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 200 | START | 200 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `21` | `19` | 204 | START | 204 | 206 |

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
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_SnapReceive` | 177 | 188 | 12 | inferred_complete_timeline |
| `Action_None` | 189 | 199 | 11 | inferred_complete_timeline |
| `Action_Toss` | 200 | 203 | 4 | inferred_complete_timeline |
| `Action_None` | 204 | 260 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_LeadBlock` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 205 | 29 | inferred_complete_timeline |
| `Action_None` | 253 | 352 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 199 | 22 | inferred_complete_timeline |
| `Action_None` | 200 | 231 | 32 | inferred_complete_timeline |
| `Action_None` | 236 | 249 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_JetMotion` | 182 | 194 | 13 | inferred_complete_timeline |
| `Action_JetMotion` | 198 | 201 | 4 | inferred_complete_timeline |
| `Action_JetMotion` | 215 | 256 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 199 | 22 | inferred_complete_timeline |
| `Action_None` | 200 | 222 | 23 | inferred_complete_timeline |
| `Action_None` | 227 | 232 | 6 | inferred_complete_timeline |
| `Action_None` | 238 | 254 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 199 | 22 | inferred_complete_timeline |
| `Action_None` | 200 | 200 | 1 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 199 | 22 | inferred_complete_timeline |
| `Action_None` | 200 | 210 | 11 | inferred_complete_timeline |
| `Action_None` | 218 | 245 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 184 | 8 | inferred_complete_timeline |
| `Action_None` | 188 | 204 | 17 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |
| `Action_None` | 215 | 218 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 189 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–14
- **Visible Samples:** 15

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 39 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 46 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 193 | 17 | inferred_complete_timeline |
| `Action_None` | 206 | 218 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 220 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 4–276 | 261 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 13–81 | 59 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 57–59 | 3 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 178–259 | 80 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 182–257 | 63 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 187–252 | 66 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 188–236 | 49 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 188–346 | 98 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 196–237 | 6 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 198–283 | 86 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 200–246 | 47 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 204–222 | 17 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 213–267 | 55 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 247–251 | 5 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 262–292 | 29 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 266–359 | 88 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 268–303 | 36 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 291–359 | 69 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 298–352 | 54 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 313–351 | 39 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 313–315 | 3 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 326–359 | 34 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 342–359 | 18 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 352–353 | 2 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 354–359 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `26` | `30` | 202 | 202 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (Position_Unknown): Annotated start 177 != Inferred start 178
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_JetMotion` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 345: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [177-189] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [182-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [198-201] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [215-256] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-205] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-352] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-245] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [178-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '4' starts at frame 200, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [200-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-222] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-254] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [178-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-231] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-249] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-260] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-39] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-220] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-218] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-214] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-236] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-276] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-81] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-59] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [178-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [204-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [214-248] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [255-257] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-252] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-343] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-283] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-246] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-218] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-267] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-287] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-279] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-303] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-352] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-351] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '39' has 1 frames without a visible bounding box.
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