# Play-Annotation-Generator Annotation Review — SplitZone_149

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_149`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RB | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `10` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `16` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 10 | START | 11 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 10 | START | 11 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 10 | START | 11 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 10 | START | 11 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 10 | START | 11 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 10 | START | 11 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 10 | START | 11 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `4` | `Group` | 10 | START | 11 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 10 | START | 11 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 10 | START | 11 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 10 | START | 11 | 137 |
| ✅ EXACT | `Action_BallSnap` | RB | `10` | `10` | 135 | START | 135 | 149 |
| ✅ EXACT | `Action_ZoneBlock` | C | `16` | `16` | 138 | START | 138 | 176 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `18` | `18` | 138 | START | 138 | 268 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 138 | START | 138 | 238 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `21` | 138 | START | 138 | 268 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 138 | START | 138 | 268 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `4` | `4` | 145 | START | 145 | 184 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 149 | END | 135 | 149 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `17` | 152 | START | 152 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `10` | 167 | START | 167 | 169 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `16` | `16` | 177 | START | 177 | 268 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 268 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_SnapReceive` | 135 | 149 | 15 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 152 | 166 | 15 | inferred_complete_timeline |
| `Action_None` | 167 | 334 | 168 | inferred_complete_timeline |
| `Action_None` | 337 | 359 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 11–342
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_BallSnap` | 135 | 149 | 15 | inferred_complete_timeline |
| `Action_None` | 150 | 166 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 171 | 342 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 144 | 134 | inferred_complete_timeline |
| `Action_SplitBlock` | 145 | 184 | 40 | inferred_complete_timeline |
| `Action_SplitBlock` | 186 | 268 | 83 | inferred_complete_timeline |
| `Action_None` | 269 | 359 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 135 | 359 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 135 | 359 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 11–355
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 135 | 355 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 137 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 268 | 131 | inferred_complete_timeline |
| `Action_None` | 269 | 359 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 137 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 238 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 241 | 243 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 248 | 268 | 21 | inferred_complete_timeline |
| `Action_None` | 269 | 359 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 137 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 176 | 39 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 177 | 268 | 92 | inferred_complete_timeline |
| `Action_None` | 269 | 359 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 137 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 268 | 131 | inferred_complete_timeline |
| `Action_None` | 269 | 273 | 5 | inferred_complete_timeline |
| `Action_None` | 276 | 359 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 137 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 268 | 131 | inferred_complete_timeline |
| `Action_None` | 269 | 359 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 11–358
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 135 | 203 | 69 | inferred_complete_timeline |
| `Action_None` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_None` | 235 | 358 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 135 | 359 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 135 | 265 | 131 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_None` | 273 | 303 | 31 | inferred_complete_timeline |
| `Action_None` | 313 | 359 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 135 | 269 | 135 | inferred_complete_timeline |
| `Action_None` | 271 | 359 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 135 | 355 | 221 | inferred_complete_timeline |
| `Action_None` | 358 | 359 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 11–186
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 135 | 179 | 45 | inferred_complete_timeline |
| `Action_None` | 183 | 186 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 135 | 359 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 135 | 204 | 70 | inferred_complete_timeline |
| `Action_None` | 206 | 262 | 57 | inferred_complete_timeline |
| `Action_None` | 266 | 294 | 29 | inferred_complete_timeline |
| `Action_None` | 296 | 359 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 135 | 359 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 135 | 321 | 187 | inferred_complete_timeline |
| `Action_None` | 329 | 335 | 7 | inferred_complete_timeline |
| `Action_None` | 340 | 359 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 11–359 | 339 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 185–192 | 7 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 188–315 | 127 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 215–227 | 13 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 243–247 | 5 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 268–357 | 65 | 8 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 311–312 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 334–349 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 131 frames exceeds threshold 90 frames [start=138, end=268].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '16' (C) duration 92 frames exceeds threshold 90 frames [start=177, end=268].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 131 frames exceeds threshold 90 frames [start=138, end=268].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 131 frames exceeds threshold 90 frames [start=138, end=268].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 131 frames exceeds threshold 90 frames [start=138, end=268].
- ⚠️ Action 'Action_None' range [135-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-358] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-306] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-315] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-265] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-303] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-359] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [145-184] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [186-268] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [167-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-342] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-321] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-335] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-355] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-204] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-262] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-294] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [177-268] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-334] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-355] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-238] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [241-243] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-244] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-315] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-227] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-276] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-291] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-304] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-312] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-336] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-348] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-357] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-349] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>