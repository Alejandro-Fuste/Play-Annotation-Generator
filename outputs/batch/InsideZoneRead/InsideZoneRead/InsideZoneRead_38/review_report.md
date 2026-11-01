# Play-Annotation-Generator Annotation Review — InsideZoneRead_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_38`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 62 | START | 62 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 64 | START | 64 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 64 | START | 75 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `3` | 64 | START | 64 | 107 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 64 | START | 64 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `8` | 64 | START | 64 | 85 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 74 | END | 62 | 74 |
| ✅ EXACT | `Action_ReadDefender` | QB | `2` | `1` | 77 | START | 77 | 91 |
| ✅ EXACT | `Action_Handoff` | QB | `2` | `1` | 92 | START | 92 | 101 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `4` | 102 | START | 102 | 111 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 152 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_SnapReceive` | 62 | 74 | 13 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 77 | 91 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 92 | 101 | 10 | inferred_complete_timeline |
| `Action_None` | 102 | 121 | 20 | inferred_complete_timeline |
| `Action_None` | 127 | 359 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_BallCarry` | 102 | 111 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 107 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 152 | 38 | inferred_complete_timeline |
| `Action_None` | 153 | 163 | 11 | inferred_complete_timeline |
| `Action_None` | 167 | 220 | 54 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 152 | 89 | inferred_complete_timeline |
| `Action_None` | 153 | 273 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_BallSnap` | 62 | 74 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 78 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 152 | 48 | inferred_complete_timeline |
| `Action_None` | 153 | 221 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 152 | 89 | inferred_complete_timeline |
| `Action_None` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_None` | 167 | 359 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 85 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 95 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 145 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 152 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 260 | 108 | inferred_complete_timeline |
| `Action_None` | 270 | 282 | 13 | inferred_complete_timeline |
| `Action_None` | 287 | 292 | 6 | inferred_complete_timeline |
| `Action_None` | 296 | 305 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 254 | 193 | inferred_complete_timeline |
| `Action_None` | 256 | 260 | 5 | inferred_complete_timeline |
| `Action_None` | 266 | 327 | 62 | inferred_complete_timeline |
| `Action_None` | 330 | 359 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 244 | 183 | inferred_complete_timeline |
| `Action_None` | 304 | 336 | 33 | inferred_complete_timeline |
| `Action_None` | 346 | 353 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 129 | 68 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 280 | 219 | inferred_complete_timeline |
| `Action_None` | 289 | 296 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 212 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 61 | 28 | inferred_complete_timeline |
| `Action_None` | 62 | 73 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 213 | 152 | inferred_complete_timeline |
| `Action_None` | 215 | 218 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 75–77 | 3 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 90–305 | 207 | 3 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 98–359 | 262 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 126–175 | 50 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 134–215 | 82 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 158–287 | 126 | 4 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 165–292 | 85 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 198–359 | 119 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 201–209 | 7 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 204–249 | 46 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 213–230 | 18 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 227–342 | 115 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 278–359 | 66 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 280–310 | 24 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 280–342 | 59 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 290–310 | 20 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 293–359 | 61 | 4 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 294–359 | 66 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 303–348 | 14 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 323–359 | 30 | 3 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 332–359 | 24 | 4 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 349–359 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [62–74], lower_priority='Action_ZoneBlock' annotated_start=64, effective_Action_ZoneBlock_start=75.
- ⚠️ Action 'Action_None' range [62-254] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-327] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-280] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-296] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-107] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-220] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-273] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-244] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-336] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-353] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-212] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-95] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-145] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-260] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-282] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-305] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-213] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-152] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-221] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-305] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-284] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-292] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-311] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-230] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-320] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-342] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-301] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-317] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-359] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-286] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-310] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-342] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-310] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-302] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-335] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-349] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-307] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-344] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-335] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-343] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-334] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-342] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-355] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '35' has 1 frames without a visible bounding box.
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

</details>