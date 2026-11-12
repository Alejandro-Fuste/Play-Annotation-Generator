# Play-Annotation-Generator Annotation Review — SplitZone_234

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_234`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 6 | START | 7 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 6 | START | 7 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 6 | START | 7 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 6 | START | 7 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `15` | `Group` | 6 | START | 7 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 6 | START | 7 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 6 | START | 7 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 6 | START | 7 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 6 | START | 7 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 6 | START | 7 | 196 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `5` | 169 | START | 169 | 181 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `11` | `11` | 172 | START | 172 | 272 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `13` | `13` | 172 | START | 172 | 248 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `3` | 172 | START | 172 | 275 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `5` | `5` | 172 | START | 182 | 234 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 172 | START | 172 | 269 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `6` | `6` | 179 | START | 179 | 221 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 181 | END | 169 | 181 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 189 | START | 189 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `9` | 197 | START | 197 | 204 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 275 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 7–324
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_SnapReceive` | 169 | 181 | 13 | inferred_complete_timeline |
| `Action_None` | 182 | 188 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 189 | 196 | 8 | inferred_complete_timeline |
| `Action_None` | 197 | 324 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 196 | 190 | inferred_complete_timeline |
| `Action_BallCarry` | 197 | 204 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 209 | 359 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 7–219
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_None` | 169 | 219 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 7–267
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_None` | 169 | 267 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 7–353
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 178 | 172 | inferred_complete_timeline |
| `Action_SplitBlock` | 179 | 221 | 43 | inferred_complete_timeline |
| `Action_SplitBlock` | 224 | 275 | 52 | inferred_complete_timeline |
| `Action_None` | 276 | 353 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 7–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 171 | 165 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 269 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 7–248
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 171 | 165 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 248 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 7–313
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_BallSnap` | 169 | 181 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 234 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 245 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 248 | 275 | 28 | inferred_complete_timeline |
| `Action_None` | 276 | 313 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 7–272
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 171 | 165 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 272 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 171 | 165 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 275 | 104 | inferred_complete_timeline |
| `Action_None` | 276 | 359 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 7–245
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_None` | 169 | 245 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 7–187
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_None` | 169 | 187 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 7–275
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_None` | 169 | 240 | 72 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 250 | 3 | inferred_complete_timeline |
| `Action_None` | 253 | 260 | 8 | inferred_complete_timeline |
| `Action_None` | 272 | 275 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 7–227
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_None` | 169 | 210 | 42 | inferred_complete_timeline |
| `Action_None` | 218 | 221 | 4 | inferred_complete_timeline |
| `Action_None` | 225 | 227 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 7–270
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_None` | 169 | 224 | 56 | inferred_complete_timeline |
| `Action_None` | 260 | 270 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 7–265
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_None` | 169 | 265 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_None` | 169 | 267 | 99 | inferred_complete_timeline |
| `Action_None` | 271 | 359 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_None` | 169 | 359 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_None` | 169 | 359 | 191 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 201–204 | 4 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 212–284 | 62 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 215–323 | 106 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 242–359 | 118 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 245–298 | 48 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 250–359 | 110 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 265–288 | 23 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 268–270 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 288–289 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 314–318 | 5 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 338–343 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 104 frames exceeds threshold 90 frames [start=172, end=275].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (C) duration 104 frames exceeds threshold 90 frames [start=172, end=275].
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [169–181], lower_priority='Action_ZoneBlock' annotated_start=172, effective_Action_ZoneBlock_start=182.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 98 frames exceeds threshold 90 frames [start=172, end=269].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (RG) duration 101 frames exceeds threshold 90 frames [start=172, end=272].
- ⚠️ Action 'Action_None' range [169-267] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-187] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-240] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-260] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [182-234] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-245] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-313] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [179-221] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-353] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-245] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [197-204] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [206-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [209-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-272] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-248] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-168] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-324] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-265] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-270] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-254] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-284] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-258] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-323] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-298] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-273] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-288] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-318] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-343] for track '29' has 1 frames without a visible bounding box.
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

</details>