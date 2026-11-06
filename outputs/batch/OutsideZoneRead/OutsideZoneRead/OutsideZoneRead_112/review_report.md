# Play-Annotation-Generator Annotation Review — OutsideZoneRead_112

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_112`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 128
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Keep` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 6 | START | 6 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 6 | START | 6 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 6 | START | 6 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 6 | START | 6 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 6 | START | 6 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 6 | START | 6 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 6 | START | 6 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 24 | START | 24 | 37 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `10` | 27 | START | 27 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `12` | 27 | START | 27 | 95 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 27 | START | 38 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `2` | 27 | START | 27 | 66 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `3` | 27 | START | 27 | 95 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 37 | END | 24 | 37 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `6` | `5` | 44 | START | 44 | 52 |
| ✅ EXACT | `Action_Keep` | QB | `6` | `5` | 53 | START | 53 | 75 |
| ✅ EXACT | `Action_BallCarry` | QB | `6` | `5` | 76 | START | 76 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 95 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 6–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 23 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 37 | 14 | inferred_complete_timeline |
| `Action_None` | 38 | 43 | 6 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 44 | 52 | 9 | inferred_complete_timeline |
| `Action_Keep` | 53 | 75 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 76 | 359 | 284 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 6–341
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 23 | 18 | inferred_complete_timeline |
| `Action_None` | 24 | 329 | 306 | inferred_complete_timeline |
| `Action_None` | 334 | 337 | 4 | inferred_complete_timeline |
| `Action_None` | 340 | 341 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 6–161
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 26 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 95 | 69 | inferred_complete_timeline |
| `Action_None` | 96 | 161 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 6–215
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 26 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 95 | 69 | inferred_complete_timeline |
| `Action_None` | 96 | 211 | 116 | inferred_complete_timeline |
| `Action_None` | 213 | 215 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 6–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 23 | 18 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 37 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 95 | 58 | inferred_complete_timeline |
| `Action_None` | 96 | 104 | 9 | inferred_complete_timeline |
| `Action_None` | 107 | 359 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 6–66
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 26 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 66 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 6–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 26 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 95 | 69 | inferred_complete_timeline |
| `Action_None` | 96 | 170 | 75 | inferred_complete_timeline |
| `Action_None` | 172 | 359 | 188 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 6–219
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 23 | 18 | inferred_complete_timeline |
| `Action_None` | 24 | 219 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 6–200
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 23 | 18 | inferred_complete_timeline |
| `Action_None` | 24 | 200 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 6–180
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 23 | 18 | inferred_complete_timeline |
| `Action_None` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 115 | 121 | 7 | inferred_complete_timeline |
| `Action_None` | 133 | 180 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 6–283
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 23 | 18 | inferred_complete_timeline |
| `Action_None` | 24 | 283 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 6–285
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 23 | 18 | inferred_complete_timeline |
| `Action_None` | 24 | 285 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 6–253
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 23 | 18 | inferred_complete_timeline |
| `Action_None` | 24 | 253 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 23 | 18 | inferred_complete_timeline |
| `Action_None` | 24 | 359 | 336 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `18` | Position_Unknown | Team_Unknown | 77–358 | 282 | 1 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 82–87 | 6 | 1 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 91–359 | 269 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 99–359 | 261 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 110–359 | 250 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 126–359 | 234 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 126–130 | 5 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 129–358 | 226 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 132–359 | 226 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 135–359 | 225 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 135–359 | 225 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 165–198 | 8 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 168–171 | 4 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 242–258 | 16 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 245–247 | 3 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 254–309 | 50 | 4 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 261–309 | 43 | 4 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 263–292 | 25 | 3 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 270–280 | 6 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 274–291 | 13 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 274–275 | 2 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 276–295 | 20 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 276–280 | 5 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 286–287 | 2 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 289–293 | 5 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 294–296 | 3 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 333–334 | 2 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 350–359 | 10 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 353–354 | 2 | 1 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 354–355 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 27 != Inferred start 38
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [24–37], lower_priority='Action_ZoneBlock' annotated_start=27, effective_Action_ZoneBlock_start=38.
- ⚠️ Action 'Action_None' range [24-253] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-329] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [27-66] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-283] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [76-359] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-285] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-219] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-180] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-161] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [27-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-211] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-95] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-358] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-359] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-325] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-352] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-358] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-162] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-253] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-273] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-281] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-309] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-283] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-299] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-280] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-283] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-295] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-293] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '45' has 1 frames without a visible bounding box.
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