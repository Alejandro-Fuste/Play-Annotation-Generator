# Play-Annotation-Generator Annotation Review — SplitZone_283

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_283`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_PressEdge` | LB2 | defense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | TE | offense | `12` | `12` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 72 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `15` | `15` | 73 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 73 | START | 73 | 119 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `5` | 73 | START | 73 | 119 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `7` | `7` | 73 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `9` | 73 | START | 73 | 119 |
| ✅ EXACT | `Action_PressEdge` | LB2 | `10` | `10` | 75 | START | 75 | 191 |
| ✅ EXACT | `Action_Handoff` | TE | `12` | `12` | 80 | START | 80 | 100 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `7` | 157 | START | 157 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `12` | `12` | 170 | START | 170 | 173 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 173 | END | 157 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `8` | `8` | 204 | START | 204 | 362 |

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
- **Visible Frames:** 0–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_SnapReceive` | 157 | 173 | 17 | inferred_complete_timeline |
| `Action_None` | 174 | 196 | 23 | inferred_complete_timeline |
| `Action_None` | 198 | 203 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 204 | 362 | 159 | inferred_complete_timeline |
| `Action_BallCarry` | 364 | 419 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 198 | 42 | inferred_complete_timeline |
| `Action_None` | 200 | 247 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_Handoff` | 80 | 100 | 21 | inferred_complete_timeline |
| `Action_None` | 101 | 169 | 69 | inferred_complete_timeline |
| `Action_SplitBlock` | 170 | 173 | 4 | inferred_complete_timeline |
| `Action_SplitBlock` | 175 | 199 | 25 | inferred_complete_timeline |
| `Action_SplitBlock` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 419 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 119 | 47 | inferred_complete_timeline |
| `Action_None` | 120 | 241 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 119 | 47 | inferred_complete_timeline |
| `Action_None` | 120 | 181 | 62 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 156 | 84 | inferred_complete_timeline |
| `Action_BallSnap` | 157 | 173 | 17 | inferred_complete_timeline |
| `Action_None` | 174 | 255 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–10
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 119 | 47 | inferred_complete_timeline |
| `Action_None` | 120 | 323 | 204 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 248 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 419 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 156 | 10 | inferred_complete_timeline |
| `Action_None` | 157 | 240 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 233 | 77 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 419 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PressEdge` | 75 | 191 | 117 | inferred_complete_timeline |
| `Action_None` | 192 | 259 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 419 | 263 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–262 | 250 | 5 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 56–244 | 189 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 209–250 | 40 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 222–237 | 16 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 223–228 | 6 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 231–273 | 43 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 240–241 | 2 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 267–330 | 64 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 318–320 | 3 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 339–342 | 4 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 372–385 | 10 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 392–419 | 28 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 396–419 | 24 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 409–411 | 3 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 410–411 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `15` (RG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `7` (C)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [157–173], lower_priority='Action_ZoneBlock' annotated_start=73, effective_Action_ZoneBlock_start=174.
- ⚠️ Segment 'Action_ZoneBlock' for track '15' has invalid range: start=73, end=10. Clamping end to start.
- ⚠️ Action 'Action_None' range [157-419] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-248] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-323] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-419] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-241] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-198] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-247] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-255] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [204-362] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-181] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-259] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [170-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [175-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-110] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-262] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-244] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-233] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-250] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-237] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-273] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-330] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-385] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-411] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>