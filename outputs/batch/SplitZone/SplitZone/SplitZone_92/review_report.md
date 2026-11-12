# Play-Annotation-Generator Annotation Review — SplitZone_92

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_92`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | DT1 | defense | `2` | `2` |
| ✅ EXACT | `Action_Handoff` | DT1 | defense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 7 | START | 8 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 7 | START | 8 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 7 | START | 8 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 7 | START | 8 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 7 | START | 8 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 7 | START | 8 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 7 | START | 8 | 183 |
| ✅ EXACT | `Action_BallSnap` | C | `3` | `3` | 181 | START | 181 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `0` | `0` | 184 | START | 184 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `1` | 184 | START | 184 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `10` | 184 | START | 184 | 204 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | `14` | `14` | 184 | START | 216 | 245 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `3` | `3` | 184 | START | 193 | 217 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 184 | START | 184 | 256 |
| ✅ EXACT | `Action_SnapReceive` | DT1 | `2` | `2` | 192 | END | 181 | 192 |
| ✅ EXACT | `Action_Handoff` | DT1 | `2` | `2` | 204 | START | 204 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `5` | 211 | START | 211 | 219 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 256 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 210 | 203 | inferred_complete_timeline |
| `Action_BallCarry` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 221 | 329 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 8–327
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 183 | 176 | inferred_complete_timeline |
| `Action_SplitBlock` | 184 | 206 | 23 | inferred_complete_timeline |
| `Action_SplitBlock` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 225 | 228 | 4 | inferred_complete_timeline |
| `Action_SplitBlock` | 233 | 256 | 24 | inferred_complete_timeline |
| `Action_None` | 257 | 327 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 8–296
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 183 | 176 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 192 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 256 | 54 | inferred_complete_timeline |
| `Action_None` | 257 | 296 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 8–245
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 10 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 14 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 157 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 245 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 8–217
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 143 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 180 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 181 | 192 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 217 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 8–228
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 183 | 176 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 204 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 228 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 8–326
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 183 | 176 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 256 | 73 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 268 | 8 | inferred_complete_timeline |
| `Action_None` | 271 | 276 | 6 | inferred_complete_timeline |
| `Action_None` | 278 | 326 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 8–298
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 19 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 180 | 145 | inferred_complete_timeline |
| `Action_None` | 181 | 185 | 5 | inferred_complete_timeline |
| `Action_None` | 191 | 232 | 42 | inferred_complete_timeline |
| `Action_None` | 234 | 298 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 180 | 173 | inferred_complete_timeline |
| `Action_None` | 181 | 187 | 7 | inferred_complete_timeline |
| `Action_None` | 190 | 217 | 28 | inferred_complete_timeline |
| `Action_None` | 219 | 226 | 8 | inferred_complete_timeline |
| `Action_None` | 296 | 329 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 8–258
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 180 | 173 | inferred_complete_timeline |
| `Action_SnapReceive` | 181 | 192 | 12 | inferred_complete_timeline |
| `Action_None` | 193 | 203 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_None` | 211 | 258 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 17 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 149 | 129 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 167 | 14 | inferred_complete_timeline |
| `Action_None` | 190 | 216 | 27 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 180 | 173 | inferred_complete_timeline |
| `Action_None` | 181 | 329 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 8–252
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 180 | 173 | inferred_complete_timeline |
| `Action_None` | 181 | 237 | 57 | inferred_complete_timeline |
| `Action_None` | 241 | 252 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 8–62
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 62 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 8–308
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 180 | 173 | inferred_complete_timeline |
| `Action_None` | 186 | 308 | 123 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 8–35 | 26 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 156–329 | 166 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 159–310 | 142 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 173–241 | 59 | 6 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 220–329 | 102 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 225–329 | 105 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 237–328 | 92 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 252–259 | 8 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 253–271 | 19 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 261–266 | 6 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 270–299 | 29 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 276–291 | 16 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 277–329 | 52 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 297–329 | 33 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 300–329 | 30 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 303–325 | 23 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 314–329 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `0` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (LG): Annotated start 184 != Inferred start 216
- ⚠️ `Action_ZoneBlock` for actor_track_id `3` (C): Annotated start 184 != Inferred start 193
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 186: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '3' (C): higher_priority='Action_BallSnap' [181–192], lower_priority='Action_ZoneBlock' annotated_start=184, effective_Action_ZoneBlock_start=193.
- ⚠️ Action 'Action_SplitBlock' range [184-206] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [212-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [225-228] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-327] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-256] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-296] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-258] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-217] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-252] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [211-219] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-256] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-268] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-276] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-326] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-217] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-62] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-204] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [206-228] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-19] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-232] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-298] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-16] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-35] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-17] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-167] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-216] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-10] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-157] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-181] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [216-245] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-308] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-201] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-287] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-192] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-201] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-310] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-196] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-231] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-241] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-329] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-328] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-271] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-266] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-291] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-304] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-325] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>