# Play-Annotation-Generator Annotation Review — OutRoutes_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_35`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `3` | `3` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 359 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `16` | `16` | 30 | START | 30 | 340 |
| ✅ EXACT | `Action_PassBlock` | LG | `18` | `18` | 30 | START | 30 | 359 |
| ✅ EXACT | `Action_PassBlock` | RG | `19` | `19` | 30 | START | 30 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 30 | START | 30 | 85 |
| ✅ EXACT | `Action_PassBlock` | LT | `21` | `21` | 30 | START | 30 | 359 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `1` | `1` | 36 | START | 36 | 359 |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | `3` | `3` | 36 | START | 36 | 106 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 36 | END | 36 | 36 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 81 | START | 81 | 91 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `3` | `3` | 107 | START | 107 | 117 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `3` | `3` | 118 | START | 118 | 191 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 36 | 36 | 1 | inferred_complete_timeline |
| `Action_None` | 37 | 80 | 44 | inferred_complete_timeline |
| `Action_ThrowPass` | 81 | 91 | 11 | inferred_complete_timeline |
| `Action_None` | 92 | 359 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_RunOutRoute` | 36 | 106 | 71 | inferred_complete_timeline |
| `Action_SecureCatch` | 107 | 117 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 118 | 191 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_RunOutRoute` | 36 | 359 | 324 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 359 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 359 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 85 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 113 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 325 | 208 | inferred_complete_timeline |
| `Action_PassBlock` | 329 | 359 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 124 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 340 | 311 | inferred_complete_timeline |
| `Action_PassBlock` | 349 | 359 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 307 | 308 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 315 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 359 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 287 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 359 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 297 | 298 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 303 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 311 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 359 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 286 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 146 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 315 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 359 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 88–202 | 55 | 11 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 92–143 | 32 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 108–109 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 128–320 | 187 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 188–190 | 3 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 197–216 | 10 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 211–309 | 60 | 8 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 234–259 | 25 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 235–341 | 40 | 8 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 272–273 | 2 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 274–359 | 44 | 4 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 305–357 | 35 | 7 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 306–359 | 53 | 2 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 338–359 | 22 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 341–352 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 79 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_RunOutRoute' range [36-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-307] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-315] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [118-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-287] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-220] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-146] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-315] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-286] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-340] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-297] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-303] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-311] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-113] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-325] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [329-359] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-110] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-121] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-148] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-163] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-113] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-136] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-305] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-310] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-320] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-216] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-236] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-247] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-278] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-295] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-309] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-244] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-259] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-251] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-260] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-272] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-284] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-289] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-300] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-341] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-279] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-320] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-344] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-359] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-309] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-320] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-324] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-340] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-350] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-357] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-359] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-352] for track '36' has 1 frames without a visible bounding box.
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

</details>