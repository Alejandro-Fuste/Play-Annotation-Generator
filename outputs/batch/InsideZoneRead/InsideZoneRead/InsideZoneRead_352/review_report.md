# Play-Annotation-Generator Annotation Review — InsideZoneRead_352

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_352`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 157
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_Keep` | QB | offense | `3` | `2` |
| ⚠️ START CHANGED | `Action_BallCarry` | QB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 22 | START | 22 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `11` | 25 | START | 25 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `12` | 25 | START | 25 | 100 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 25 | START | 100 | 102 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `5` | 25 | START | 25 | 103 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `7` | 25 | START | 25 | 103 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 36 | END | 22 | 36 |
| ✅ EXACT | `Action_ReadDefender` | QB | `3` | `2` | 42 | START | 42 | 51 |
| ✅ EXACT | `Action_Keep` | QB | `3` | `2` | 52 | START | 52 | 77 |
| ⚠️ START CHANGED | `Action_BallCarry` | QB | `3` | `2` | 78 | START | 79 | 82 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 103 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 36 | 15 | inferred_complete_timeline |
| `Action_None` | 37 | 41 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 42 | 51 | 10 | inferred_complete_timeline |
| `Action_Keep` | 52 | 77 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 79 | 82 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 79 | 58 | inferred_complete_timeline |
| `Action_None` | 82 | 162 | 81 | inferred_complete_timeline |
| `Action_None` | 171 | 329 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 65 | 44 | inferred_complete_timeline |
| `Action_None` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_None` | 85 | 102 | 18 | inferred_complete_timeline |
| `Action_None` | 104 | 177 | 74 | inferred_complete_timeline |
| `Action_None` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_None` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_None` | 201 | 284 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 49 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 103 | 14 | inferred_complete_timeline |
| `Action_None` | 104 | 233 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 103 | 79 | inferred_complete_timeline |
| `Action_None` | 104 | 270 | 167 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 34 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 108 | 5 | inferred_complete_timeline |
| `Action_None` | 110 | 258 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 103 | 79 | inferred_complete_timeline |
| `Action_None` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 282 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 100 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_None` | 104 | 123 | 20 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 156 | 28 | inferred_complete_timeline |
| `Action_None` | 159 | 169 | 11 | inferred_complete_timeline |
| `Action_None` | 172 | 192 | 21 | inferred_complete_timeline |
| `Action_None` | 197 | 241 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 74 | 53 | inferred_complete_timeline |
| `Action_None` | 79 | 149 | 71 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 185 | 28 | inferred_complete_timeline |
| `Action_None` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_None` | 194 | 214 | 21 | inferred_complete_timeline |
| `Action_None` | 220 | 302 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–307
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 307 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 98 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 91 | 70 | inferred_complete_timeline |
| `Action_None` | 104 | 142 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 317 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 329 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 89 | 68 | inferred_complete_timeline |
| `Action_None` | 93 | 317 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 110 | 89 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 54–56 | 3 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 69–83 | 15 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 80–230 | 151 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 98–278 | 178 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 116–168 | 49 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 123–125 | 3 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 135–136 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 139–289 | 150 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 142–143 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 150–282 | 133 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 151–272 | 121 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 156–157 | 2 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 158–230 | 73 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 158–172 | 9 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 162–230 | 69 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 166–275 | 110 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 186–240 | 55 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 193–202 | 6 | 2 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 231–314 | 77 | 2 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 231–320 | 88 | 2 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 231–282 | 51 | 2 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 231–238 | 8 | 1 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 250–262 | 6 | 2 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 268–285 | 18 | 1 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 273–283 | 8 | 2 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 283–329 | 47 | 1 | Undefined position; Undefined team |
| `43` | `49` | Position_Unknown | Team_Unknown | 283–329 | 47 | 1 | Undefined position; Undefined team |
| `44` | `50` | Position_Unknown | Team_Unknown | 283–284 | 2 | 1 | Undefined position; Undefined team |
| `45` | `53` | Position_Unknown | Team_Unknown | 287–288 | 2 | 1 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 291–293 | 3 | 1 | Undefined position; Undefined team |
| `47` | `57` | Position_Unknown | Team_Unknown | 300–329 | 30 | 1 | Undefined position; Undefined team |
| `48` | `59` | Position_Unknown | Team_Unknown | 319–320 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 25 != Inferred start 100
- ⚠️ `Action_BallCarry` for actor_track_id `3` (QB): Annotated start 78 != Inferred start 79

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [22–36], lower_priority='Action_ZoneBlock' annotated_start=25, effective_Action_ZoneBlock_start=37.
- ⚠️ Action 'Action_None' range [22-317] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-91] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [52-77] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [79-82] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-89] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-317] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-282] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-270] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-149] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-185] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-214] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-98] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-307] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-49] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-86] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-156] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-241] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [22-34] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-258] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-102] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-284] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-110] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-83] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-230] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-191] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-278] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-199] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-289] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-282] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-185] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-272] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-230] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-230] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-275] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-240] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-299] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-314] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-314] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-320] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-241] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-282] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-238] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-285] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-278] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '48' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.

</details>