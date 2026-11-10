# Play-Annotation-Generator Annotation Review — RPO_48

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_48`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `17` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_RunBlock` | RG | `10` | `10` | 22 | START | 22 | 82 |
| ✅ EXACT | `Action_RunBlock` | LG | `11` | `11` | 22 | START | 22 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `12` | `12` | 22 | START | 24 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `4` | `4` | 22 | START | 22 | 76 |
| ✅ EXACT | `Action_RunBlock` | LT | `9` | `9` | 22 | START | 22 | 82 |
| ✅ EXACT | `Action_ReadDefender` | QB | `7` | `7` | 27 | START | 27 | 50 |
| ✅ EXACT | `Action_PullBall` | QB | `7` | `7` | 51 | START | 51 | 64 |
| ✅ EXACT | `Action_ThrowPass` | RB | `6` | `6` | 75 | START | 75 | 82 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 26 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 27 | 50 | 24 | inferred_complete_timeline |
| `Action_PullBall` | 51 | 64 | 14 | inferred_complete_timeline |
| `Action_None` | 65 | 77 | 13 | inferred_complete_timeline |
| `Action_None` | 82 | 179 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 74 | 54 | inferred_complete_timeline |
| `Action_ThrowPass` | 75 | 82 | 8 | inferred_complete_timeline |
| `Action_None` | 83 | 285 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 22 | 82 | 61 | inferred_complete_timeline |
| `Action_None` | 83 | 281 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 22 | 82 | 61 | inferred_complete_timeline |
| `Action_None` | 83 | 275 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 27 | 82 | 56 | inferred_complete_timeline |
| `Action_None` | 83 | 231 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 22 | 82 | 61 | inferred_complete_timeline |
| `Action_None` | 83 | 189 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 22 | 76 | 55 | inferred_complete_timeline |
| `Action_RunBlock` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_None` | 83 | 175 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 77 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 77 | 57 | inferred_complete_timeline |
| `Action_None` | 82 | 286 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 121 | 101 | inferred_complete_timeline |
| `Action_None` | 125 | 240 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–288
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 153 | 133 | inferred_complete_timeline |
| `Action_None` | 155 | 288 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 85 | 65 | inferred_complete_timeline |
| `Action_None` | 91 | 104 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 121 | 101 | inferred_complete_timeline |
| `Action_None` | 126 | 329 | 204 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 32–329 | 298 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 52–329 | 274 | 4 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 77–329 | 247 | 3 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 80–275 | 196 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 85–329 | 244 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 108–170 | 63 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 119–329 | 211 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 136–320 | 185 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 141–329 | 188 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 165–329 | 165 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 172–329 | 158 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 182–199 | 15 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 183–311 | 129 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 222–223 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 289–290 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 301–329 | 28 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 302–329 | 9 | 4 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 302–307 | 6 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 309–329 | 21 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 314–329 | 16 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 316–329 | 12 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 318–319 | 2 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 318–329 | 7 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 320–329 | 5 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 320–329 | 5 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 325–329 | 5 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 55 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [21-85] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-104] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-288] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-77] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-286] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-77] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [22-76] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-285] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-77] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-179] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-240] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-281] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-275] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 21, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [21-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [24-25] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-231] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-249] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-272] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-275] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-170] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-320] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-173] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-311] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-304] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-307] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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