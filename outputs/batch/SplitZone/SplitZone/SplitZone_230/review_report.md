# Play-Annotation-Generator Annotation Review — SplitZone_230

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_230`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 1
- **Action Segments:** 95
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_SplitBlock` | LB2 | defense | `3` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 10 | START | 11 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 10 | START | 11 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 10 | START | 11 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 10 | START | 11 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 10 | START | 26 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 10 | START | 27 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 10 | START | 11 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 10 | START | 11 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 10 | START | 11 | 181 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 179 | START | 179 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 182 | START | 184 | 187 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `15` | 182 | START | 182 | 297 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `16` | `16` | 182 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RT | `17` | `17` | 182 | START | 182 | 297 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `8` | 182 | START | 182 | 232 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `12` | `12` | 183 | END | 179 | 179 |
| ✅ EXACT | `Action_SplitBlock` | LB2 | `3` | `3` | 193 | START | 193 | 297 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 210 | START | 210 | 231 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `5` | 232 | START | 232 | 241 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 297 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 103 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 122 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 179 | 179 | 1 | inferred_complete_timeline |
| `Action_None` | 187 | 209 | 23 | inferred_complete_timeline |
| `Action_Handoff` | 210 | 231 | 22 | inferred_complete_timeline |
| `Action_None` | 232 | 359 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 11–345
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 231 | 221 | inferred_complete_timeline |
| `Action_BallCarry` | 232 | 241 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 248 | 250 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 252 | 345 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 11–200
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 178 | 168 | inferred_complete_timeline |
| `Action_None` | 179 | 200 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 11–264
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 51 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 178 | 126 | inferred_complete_timeline |
| `Action_None` | 179 | 264 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 181 | 171 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 297 | 116 | inferred_complete_timeline |
| `Action_None` | 298 | 359 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 11–232
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 181 | 171 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 232 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 11–278
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 178 | 168 | inferred_complete_timeline |
| `Action_BallSnap` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 187 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 239 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 278 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 26–52
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 33 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 52 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 181 | 155 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 297 | 116 | inferred_complete_timeline |
| `Action_None` | 298 | 359 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 11–264
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 178 | 168 | inferred_complete_timeline |
| `Action_None` | 179 | 264 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 178 | 168 | inferred_complete_timeline |
| `Action_None` | 179 | 359 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 178 | 168 | inferred_complete_timeline |
| `Action_None` | 179 | 286 | 108 | inferred_complete_timeline |
| `Action_None` | 288 | 350 | 63 | inferred_complete_timeline |
| `Action_None` | 352 | 359 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 178 | 168 | inferred_complete_timeline |
| `Action_None` | 179 | 263 | 85 | inferred_complete_timeline |
| `Action_None` | 283 | 329 | 47 | inferred_complete_timeline |
| `Action_None` | 336 | 359 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 178 | 168 | inferred_complete_timeline |
| `Action_None` | 179 | 251 | 73 | inferred_complete_timeline |
| `Action_None` | 255 | 359 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 192 | 182 | inferred_complete_timeline |
| `Action_SplitBlock` | 193 | 297 | 105 | inferred_complete_timeline |
| `Action_None` | 298 | 359 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 11–278
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 178 | 168 | inferred_complete_timeline |
| `Action_None` | 179 | 275 | 97 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 178 | 168 | inferred_complete_timeline |
| `Action_None` | 179 | 296 | 118 | inferred_complete_timeline |
| `Action_None` | 299 | 307 | 9 | inferred_complete_timeline |
| `Action_None` | 312 | 359 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 11–359 | 336 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 152–161 | 8 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 208–211 | 4 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 215–218 | 4 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 221–359 | 138 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 268–359 | 92 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 274–359 | 78 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 289–359 | 71 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 291–359 | 69 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 295–359 | 65 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 296–359 | 62 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 299–359 | 61 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 300–359 | 57 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 303–339 | 37 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 318–359 | 39 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 325–328 | 4 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 349–350 | 2 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 352–358 | 6 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 352–353 | 2 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 353–359 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `20` | `23` | 213 | 213 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `16` (RG)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 97 frames exceeds threshold 90 frames [start=182, end=278].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [179–183], lower_priority='Action_ZoneBlock' annotated_start=182, effective_Action_ZoneBlock_start=184.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LT) duration 116 frames exceeds threshold 90 frames [start=182, end=297].
- ⚠️ Segment 'Action_ZoneBlock' for track '16' has invalid range: start=182, end=52. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RT) duration 116 frames exceeds threshold 90 frames [start=182, end=297].
- ⚠️ Action 'Action_None' range [179-275] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-51] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [193-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-296] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-307] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [232-241] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [252-345] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-205] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-273] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [182-232] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-251] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-286] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-350] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-329] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-359] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' for track '12' starts at frame 179, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_SnapReceive' range [179-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-239] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [247-278] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-200] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-230] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-285] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-322] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-317] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-359] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-353] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-339] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-335] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-355] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>