# Play-Annotation-Generator Annotation Review — SplitZone_84

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_84`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 39
- **Ball Tracks:** 2
- **Action Segments:** 91
- **Validation Warnings:** 117
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 25 | START | 26 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 25 | START | 26 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 25 | START | 26 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 25 | START | 26 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 25 | START | 26 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 25 | START | 26 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 25 | START | 26 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 25 | START | 26 | 150 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 148 | START | 148 | 160 |
| ✅ EXACT | `Action_SplitBlock` | TE | `10` | `10` | 151 | START | 151 | 186 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `12` | 151 | START | 151 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 151 | START | 161 | 201 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `2` | 151 | START | 151 | 242 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 151 | START | 151 | 242 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `9` | 151 | START | 151 | 208 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 160 | END | 148 | 160 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 163 | START | 163 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `5` | 173 | START | 173 | 190 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 242 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 26–274
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 147 | 122 | inferred_complete_timeline |
| `Action_SnapReceive` | 148 | 160 | 13 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 163 | 172 | 10 | inferred_complete_timeline |
| `Action_None` | 173 | 274 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 26–287
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 172 | 147 | inferred_complete_timeline |
| `Action_BallCarry` | 173 | 190 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 213 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 215 | 287 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 26–186
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 150 | 125 | inferred_complete_timeline |
| `Action_SplitBlock` | 151 | 186 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 26–328
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 150 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 242 | 92 | inferred_complete_timeline |
| `Action_None` | 243 | 325 | 83 | inferred_complete_timeline |
| `Action_None` | 327 | 328 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 26–298
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 150 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 242 | 92 | inferred_complete_timeline |
| `Action_None` | 243 | 298 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 26–303
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 147 | 122 | inferred_complete_timeline |
| `Action_BallSnap` | 148 | 160 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 201 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 228 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 231 | 242 | 12 | inferred_complete_timeline |
| `Action_None` | 243 | 303 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 26–226
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 150 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 173 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 207 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 226 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 26–274
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 150 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 208 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 242 | 33 | inferred_complete_timeline |
| `Action_None` | 243 | 274 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 26–324
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 147 | 122 | inferred_complete_timeline |
| `Action_None` | 148 | 226 | 79 | inferred_complete_timeline |
| `Action_None` | 238 | 310 | 73 | inferred_complete_timeline |
| `Action_None` | 312 | 318 | 7 | inferred_complete_timeline |
| `Action_None` | 321 | 324 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 26–200
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 81 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 147 | 64 | inferred_complete_timeline |
| `Action_None` | 148 | 178 | 31 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 26–294
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 147 | 122 | inferred_complete_timeline |
| `Action_None` | 148 | 231 | 84 | inferred_complete_timeline |
| `Action_None` | 233 | 294 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 26–256
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 147 | 122 | inferred_complete_timeline |
| `Action_None` | 148 | 249 | 102 | inferred_complete_timeline |
| `Action_None` | 254 | 256 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 26–218
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 64 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 147 | 82 | inferred_complete_timeline |
| `Action_None` | 148 | 218 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 26–311
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 147 | 122 | inferred_complete_timeline |
| `Action_None` | 148 | 311 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 26–359
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 147 | 122 | inferred_complete_timeline |
| `Action_None` | 148 | 359 | 212 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 47–178 | 132 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 63–77 | 9 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 152–359 | 175 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 155–269 | 55 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 176–178 | 3 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 223–359 | 135 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 224–232 | 9 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 225–301 | 76 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 237–359 | 123 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 243–280 | 29 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 255–359 | 105 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 255–256 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 277–308 | 32 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 297–298 | 2 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 312–333 | 9 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 319–321 | 3 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 330–358 | 29 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 336–359 | 21 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 338–341 | 4 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 340–341 | 2 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 344–359 | 16 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 349–359 | 11 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `35` | `48` | 340 | 344 | 5 | 100.0% | None |
| `39` | `54` | 355 | 355 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LG) duration 92 frames exceeds threshold 90 frames [start=151, end=242].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 92 frames exceeds threshold 90 frames [start=151, end=242].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 92 frames exceeds threshold 90 frames [start=151, end=242].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 92 frames exceeds threshold 90 frames [start=151, end=242].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [148–160], lower_priority='Action_ZoneBlock' annotated_start=151, effective_Action_ZoneBlock_start=161.
- ⚠️ Action 'Action_None' range [148-311] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-294] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-298] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-310] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-318] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-81] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-178] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [173-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-213] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [215-287] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-325] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-274] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-208] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-274] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [151-186] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-173] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [212-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [161-201] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [205-228] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-303] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-249] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-232] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-301] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-253] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-270] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-280] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-308] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-333] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-358] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-341] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-359] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '40' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>