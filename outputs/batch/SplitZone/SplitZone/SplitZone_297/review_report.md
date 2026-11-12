# Play-Annotation-Generator Annotation Review — SplitZone_297

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_297`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 115
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 9
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_SplitBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `3` | `3` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_BallSnap` | RB | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `3` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `0` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `16` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 167 |
| ✅ EXACT | `Action_SplitBlock` | RT | `9` | `9` | 168 | START | 168 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `0` | `0` | 170 | START | 170 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `12` | 170 | START | 170 | 191 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 170 | START | 170 | 204 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `6` | 170 | START | 170 | 204 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `9` | 170 | START | 170 | 204 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `4` | `4` | 171 | END | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `3` | `3` | 174 | START | 174 | 194 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `4` | `4` | 183 | START | 183 | 189 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `4` | 190 | START | 190 | 199 |
| ✅ EXACT | `Action_BallSnap` | RB | `3` | `3` | 199 | START | 199 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `3` | 200 | START | 200 | 317 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `0` | `0` | 204 | START | 204 | 237 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 183 | 189 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 190 | 199 | 10 | inferred_complete_timeline |
| `Action_None` | 200 | 248 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PressEdge` | 174 | 194 | 21 | inferred_complete_timeline |
| `Action_PressEdge` | 197 | 198 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 199 | 199 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 200 | 317 | 118 | inferred_complete_timeline |
| `Action_BallCarry` | 324 | 325 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 328 | 329 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 334 | 341 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 344 | 347 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 350 | 352 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 355 | 359 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 213 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–338
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 250 | 52 | inferred_complete_timeline |
| `Action_None` | 256 | 338 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 198 | 138 | inferred_complete_timeline |
| `Action_None` | 199 | 359 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 204 | 35 | inferred_complete_timeline |
| `Action_None` | 205 | 284 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 203 | 34 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 204 | 237 | 34 | inferred_complete_timeline |
| `Action_None` | 238 | 241 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 191 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 204 | 6 | inferred_complete_timeline |
| `Action_None` | 205 | 359 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 204 | 35 | inferred_complete_timeline |
| `Action_None` | 205 | 354 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_SplitBlock` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 204 | 35 | inferred_complete_timeline |
| `Action_None` | 205 | 359 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 359 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_None` | 202 | 213 | 12 | inferred_complete_timeline |
| `Action_None` | 217 | 220 | 4 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 184 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 198 | 12 | inferred_complete_timeline |
| `Action_None` | 199 | 199 | 1 | inferred_complete_timeline |
| `Action_None` | 210 | 222 | 13 | inferred_complete_timeline |
| `Action_None` | 229 | 304 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 196 | 12 | inferred_complete_timeline |
| `Action_None` | 207 | 220 | 14 | inferred_complete_timeline |
| `Action_None` | 222 | 359 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 238 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 247 | 49 | inferred_complete_timeline |
| `Action_None` | 250 | 344 | 95 | inferred_complete_timeline |
| `Action_None` | 346 | 359 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 178 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 198 | 9 | inferred_complete_timeline |
| `Action_None` | 199 | 224 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 274 | 76 | inferred_complete_timeline |
| `Action_None` | 276 | 359 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `24` | Position_Unknown | Team_Unknown | 94–165 | 7 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 101–161 | 58 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 146–167 | 16 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 214–217 | 4 | 1 | Undefined position; Undefined team |
| `24` | `38` | Position_Unknown | Team_Unknown | 222–357 | 136 | 1 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 228–250 | 23 | 1 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 229–359 | 131 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 232–235 | 4 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 251–359 | 103 | 5 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 251–252 | 2 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 257–359 | 103 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 260–359 | 100 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 262–359 | 98 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 274–285 | 11 | 2 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 304–359 | 45 | 5 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 304–357 | 51 | 2 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 321–359 | 39 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 327–359 | 33 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 341–342 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `4` (QB)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (7 segments found)

### Track Identity Issues

- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '3' has invalid range: start=199, end=171. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '4' has invalid range: start=199, end=171. Clamping end to start.
- ⚠️ Action 'Action_None' range [238-241] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-198] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-284] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [174-194] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [200-317] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [324-325] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [328-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [334-341] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [344-347] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [350-352] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-338] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-354] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-213] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-247] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-344] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-359] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [170-191] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-274] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-196] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-220] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-359] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-213] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-178] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-198] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 199, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [199-224] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-184] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 199, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [199-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-304] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-165] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-163] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-357] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-298] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-327] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-279] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-309] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-319] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-333] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-359] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-352] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '38' has 1 frames without a visible bounding box.
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

</details>