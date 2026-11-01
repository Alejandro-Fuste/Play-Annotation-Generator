# Play-Annotation-Generator Annotation Review — InsideZoneRead_127

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_127`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 85 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 83 | START | 83 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 86 | START | 98 | 162 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `22` | `21` | 86 | START | 86 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `8` | `7` | 86 | START | 86 | 162 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `8` | 86 | START | 86 | 162 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 97 | END | 83 | 97 |
| ✅ EXACT | `Action_ReadDefender` | QB | `18` | `17` | 102 | START | 102 | 111 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 112 | START | 112 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `14` | `13` | 122 | START | 122 | 186 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 162 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_SnapReceive` | 83 | 97 | 15 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 102 | 111 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 112 | 121 | 10 | inferred_complete_timeline |
| `Action_None` | 122 | 359 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_BallCarry` | 122 | 186 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 192 | 218 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 133 | 51 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 282 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 237 | 155 | inferred_complete_timeline |
| `Action_None` | 240 | 359 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 359 | 277 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 307 | 225 | inferred_complete_timeline |
| `Action_None` | 319 | 322 | 4 | inferred_complete_timeline |
| `Action_None` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_None` | 330 | 332 | 3 | inferred_complete_timeline |
| `Action_None` | 342 | 343 | 2 | inferred_complete_timeline |
| `Action_None` | 346 | 351 | 6 | inferred_complete_timeline |
| `Action_None` | 353 | 359 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 162 | 77 | inferred_complete_timeline |
| `Action_None` | 163 | 287 | 125 | inferred_complete_timeline |
| `Action_None` | 304 | 307 | 4 | inferred_complete_timeline |
| `Action_None` | 314 | 318 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 143 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_BallSnap` | 83 | 97 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 162 | 65 | inferred_complete_timeline |
| `Action_None` | 163 | 193 | 31 | inferred_complete_timeline |
| `Action_None` | 195 | 206 | 12 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 240 | 28 | inferred_complete_timeline |
| `Action_None` | 242 | 251 | 10 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 342 | 86 | inferred_complete_timeline |
| `Action_None` | 344 | 348 | 5 | inferred_complete_timeline |
| `Action_None` | 350 | 359 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 162 | 77 | inferred_complete_timeline |
| `Action_None` | 163 | 359 | 197 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 268 | 186 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 307 | 16 | inferred_complete_timeline |
| `Action_None` | 315 | 318 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 359 | 277 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 178 | 96 | inferred_complete_timeline |
| `Action_None` | 180 | 252 | 73 | inferred_complete_timeline |
| `Action_None` | 254 | 284 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 126 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–335
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 253 | 171 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_None` | 281 | 302 | 22 | inferred_complete_timeline |
| `Action_None` | 305 | 323 | 19 | inferred_complete_timeline |
| `Action_None` | 334 | 335 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 180 | 98 | inferred_complete_timeline |
| `Action_None` | 183 | 207 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–351
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 344 | 262 | inferred_complete_timeline |
| `Action_None` | 350 | 351 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 210 | 128 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 228 | 14 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 214 | 132 | inferred_complete_timeline |
| `Action_None` | 216 | 230 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 359 | 277 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 229 | 147 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–359 | 360 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 151–195 | 43 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 155–232 | 66 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 209–229 | 21 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 214–359 | 146 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 237–359 | 123 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 238–359 | 75 | 8 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 264–359 | 69 | 6 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 276–309 | 30 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 293–359 | 67 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 295–296 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 312–359 | 41 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 316–318 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 256: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [83–97], lower_priority='Action_ZoneBlock' annotated_start=86, effective_Action_ZoneBlock_start=98.
- ⚠️ Action 'Action_None' range [83-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-133] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-282] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-344] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-307] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-351] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-253] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-302] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-323] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-287] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-307] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-318] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-307] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [122-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [192-218] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-252] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-284] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-210] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-228] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-214] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-230] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-229] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-240] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-251] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-342] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-348] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-174] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-212] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-243] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-292] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-305] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-342] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-356] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-315] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-342] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-356] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-290] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-303] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-336] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-342] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>