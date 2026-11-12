# Play-Annotation-Generator Annotation Review — SplitZone_178

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_178`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 132
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 4
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `0` | `0` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `3` | `3` |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | Team_Unknown | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `0` | `Group` | 16 | START | 17 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 16 | START | 17 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 16 | START | 17 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 16 | START | 24 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 16 | START | 17 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 16 | START | 17 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 16 | START | 17 | 225 |
| ✅ EXACT | `Action_BallSnap` | QB | `14` | `14` | 193 | START | 193 | 204 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `1` | 196 | START | 196 | 227 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `10` | `10` | 196 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `2` | 196 | START | 196 | 267 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `4` | `4` | 196 | START | N/A | N/A |
| ✅ EXACT | `Action_SplitBlock` | HB | `0` | `0` | 198 | START | 198 | 239 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `3` | `3` | 204 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | `3` | `3` | 212 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `6` | 226 | START | 226 | 238 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 320 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 24–337
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 75 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 141 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 146 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 153 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 192 | 37 | inferred_complete_timeline |
| `Action_BallSnap` | 193 | 204 | 12 | inferred_complete_timeline |
| `Action_None` | 205 | 221 | 17 | inferred_complete_timeline |
| `Action_None` | 226 | 337 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 17–289
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 225 | 209 | inferred_complete_timeline |
| `Action_BallCarry` | 226 | 238 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 243 | 289 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 17–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 197 | 181 | inferred_complete_timeline |
| `Action_SplitBlock` | 198 | 239 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 17–419
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 195 | 179 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 267 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 270 | 298 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 300 | 308 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 317 | 3 | inferred_complete_timeline |
| `Action_None` | 322 | 419 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 17–174
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 174 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 17–169
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 136 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 155 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 169 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 17–351
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 195 | 179 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 227 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 230 | 320 | 91 | inferred_complete_timeline |
| `Action_None` | 321 | 351 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 17–252
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 21 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 192 | 159 | inferred_complete_timeline |
| `Action_None` | 193 | 252 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 17–419
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 192 | 176 | inferred_complete_timeline |
| `Action_None` | 193 | 210 | 18 | inferred_complete_timeline |
| `Action_None` | 275 | 364 | 90 | inferred_complete_timeline |
| `Action_None` | 366 | 367 | 2 | inferred_complete_timeline |
| `Action_None` | 372 | 373 | 2 | inferred_complete_timeline |
| `Action_None` | 398 | 403 | 6 | inferred_complete_timeline |
| `Action_None` | 405 | 419 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 17–419
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 180 | 164 | inferred_complete_timeline |
| `Action_None` | 198 | 419 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 67–103
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 67 | 74 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 97 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 103 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 17–267
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 192 | 176 | inferred_complete_timeline |
| `Action_None` | 193 | 267 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 17–238
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 192 | 176 | inferred_complete_timeline |
| `Action_None` | 193 | 238 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 17–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 192 | 176 | inferred_complete_timeline |
| `Action_None` | 193 | 419 | 227 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 17–133 | 39 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 17–419 | 381 | 8 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 181–300 | 81 | 4 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 195–243 | 49 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 205–349 | 142 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 223–259 | 37 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 242–274 | 28 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 246–419 | 126 | 6 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 248–419 | 166 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 274–419 | 115 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 274–291 | 18 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 282–345 | 59 | 4 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 283–324 | 42 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 287–419 | 133 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 296–419 | 124 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 314–419 | 98 | 4 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 337–419 | 71 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 339–419 | 59 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 368–370 | 3 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 369–378 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `10` (RG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (4 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `4` (LG)
- ❌ Missing segment for action `Action_SnapReceive` on target `3` (Position_Unknown)
- ❌ Missing segment for action `Action_Handoff` on target `3` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RT) duration 125 frames exceeds threshold 90 frames [start=196, end=320].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 125 frames exceeds threshold 90 frames [start=196, end=320].
- ⚠️ Segment 'Action_SnapReceive' for track '3' has invalid range: start=193, end=133. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '3' has invalid range: start=212, end=133. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '4' has invalid range: start=196, end=174. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '10' has invalid range: start=196, end=169. Clamping end to start.
- ⚠️ Action 'Action_SplitBlock' range [198-239] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-227] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-351] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-267] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [270-298] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [300-308] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [315-317] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-419] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-53] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-238] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [226-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [243-289] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-364] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-403] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-267] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-419] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-155] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-161] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-21] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-252] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-419] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-216] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-375] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-385] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-398] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-410] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-419] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-153] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-192] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-221] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-337] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-74] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-249] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-300] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-243] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-341] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-349] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-259] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-274] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-270] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-385] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-399] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-280] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-326] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-291] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-302] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-345] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-324] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-338] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-342] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-370] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>