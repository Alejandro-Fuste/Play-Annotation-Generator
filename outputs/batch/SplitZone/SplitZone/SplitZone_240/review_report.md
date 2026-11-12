# Play-Annotation-Generator Annotation Review — SplitZone_240

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_240`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 35
- **Ball Tracks:** 2
- **Action Segments:** 114
- **Validation Warnings:** 122
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
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 116 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 114 | START | 114 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `11` | 117 | START | 117 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 117 | START | 128 | 147 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `3` | 117 | START | 117 | 187 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `4` | 117 | START | 117 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `9` | 117 | START | 117 | 161 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `7` | `7` | 122 | START | 122 | 147 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 127 | END | 114 | 127 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 132 | START | 132 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `5` | 147 | START | 147 | 229 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 187 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–338
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_SnapReceive` | 114 | 127 | 14 | inferred_complete_timeline |
| `Action_None` | 128 | 131 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 132 | 146 | 15 | inferred_complete_timeline |
| `Action_None` | 147 | 338 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_BallCarry` | 147 | 229 | 83 | inferred_complete_timeline |
| `Action_BallCarry` | 233 | 242 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 246 | 247 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_SplitBlock` | 122 | 147 | 26 | inferred_complete_timeline |
| `Action_SplitBlock` | 155 | 161 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 161 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 173 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–412
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 187 | 71 | inferred_complete_timeline |
| `Action_None` | 188 | 193 | 6 | inferred_complete_timeline |
| `Action_None` | 196 | 352 | 157 | inferred_complete_timeline |
| `Action_None` | 354 | 412 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_BallSnap` | 114 | 127 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 147 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 159 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 187 | 23 | inferred_complete_timeline |
| `Action_None` | 188 | 193 | 6 | inferred_complete_timeline |
| `Action_None` | 195 | 258 | 64 | inferred_complete_timeline |
| `Action_None` | 265 | 268 | 4 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–401
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 187 | 71 | inferred_complete_timeline |
| `Action_None` | 188 | 256 | 69 | inferred_complete_timeline |
| `Action_None` | 260 | 391 | 132 | inferred_complete_timeline |
| `Action_None` | 400 | 401 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–403
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 187 | 71 | inferred_complete_timeline |
| `Action_None` | 188 | 403 | 216 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_None` | 114 | 265 | 152 | inferred_complete_timeline |
| `Action_None` | 267 | 335 | 69 | inferred_complete_timeline |
| `Action_None` | 341 | 344 | 4 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_None` | 363 | 407 | 45 | inferred_complete_timeline |
| `Action_None` | 418 | 419 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_None` | 114 | 203 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_None` | 114 | 176 | 63 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |
| `Action_None` | 270 | 276 | 7 | inferred_complete_timeline |
| `Action_None` | 309 | 316 | 8 | inferred_complete_timeline |
| `Action_None` | 319 | 332 | 14 | inferred_complete_timeline |
| `Action_None` | 335 | 340 | 6 | inferred_complete_timeline |
| `Action_None` | 342 | 343 | 2 | inferred_complete_timeline |
| `Action_None` | 355 | 358 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_None` | 114 | 196 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_None` | 114 | 365 | 252 | inferred_complete_timeline |
| `Action_None` | 372 | 419 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 48–122
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 48 | 113 | 66 | inferred_complete_timeline |
| `Action_None` | 114 | 122 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_None` | 114 | 252 | 139 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 70–126 | 57 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 167–358 | 114 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 172–291 | 120 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 172–347 | 167 | 6 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 179–419 | 211 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 188–419 | 215 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 191–196 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 200–419 | 192 | 6 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 216–391 | 117 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 243–327 | 85 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 259–419 | 133 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 288–315 | 21 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 289–419 | 131 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 290–419 | 130 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 331–419 | 89 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 348–392 | 28 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 350–419 | 70 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 352–419 | 47 | 5 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 388–419 | 32 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 411–416 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | 143 | 143 | 1 | 100.0% | None |
| `24` | `25` | 200 | 200 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [114–127], lower_priority='Action_ZoneBlock' annotated_start=117, effective_Action_ZoneBlock_start=128.
- ⚠️ Action 'Action_None' range [114-252] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-365] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-256] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-391] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-403] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [147-229] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [233-242] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [246-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-335] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-344] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-407] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [122-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [155-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-203] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-173] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-338] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-352] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-412] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-276] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-316] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-332] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-340] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-358] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-147] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [149-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-258] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-273] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-358] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-291] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-223] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-283] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-344] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-318] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-339] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-310] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-327] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-347] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-322] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-391] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-327] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-363] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-306] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-419] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-360] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-380] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-392] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-372] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-406] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-416] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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