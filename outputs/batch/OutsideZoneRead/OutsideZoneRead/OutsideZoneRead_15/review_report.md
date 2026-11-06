# Play-Annotation-Generator Annotation Review — OutsideZoneRead_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_15`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `1` | `1` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 403 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 166 |
| ✅ EXACT | `Action_ZoneBlock` | C | `11` | `11` | 167 | START | 167 | 180 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `14` | 167 | START | 167 | 185 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `19` | `19` | 167 | START | 167 | 206 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 167 | START | 167 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `9` | 167 | START | 167 | 189 |
| ✅ EXACT | `Action_PressEdge` | RB | `1` | `1` | 172 | START | 172 | 204 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `12` | `12` | 173 | START | 173 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `12` | `12` | 206 | START | 206 | 389 |

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
- **Visible Frames:** 0–413
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 173 | 205 | 33 | inferred_complete_timeline |
| `Action_Keep` | 206 | 389 | 184 | inferred_complete_timeline |
| `Action_Keep` | 392 | 413 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_PressEdge` | 172 | 204 | 33 | inferred_complete_timeline |
| `Action_None` | 205 | 318 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–403
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 403 | 404 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–342
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 206 | 40 | inferred_complete_timeline |
| `Action_None` | 207 | 232 | 26 | inferred_complete_timeline |
| `Action_None` | 235 | 240 | 6 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 342 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–384
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 206 | 40 | inferred_complete_timeline |
| `Action_None` | 207 | 239 | 33 | inferred_complete_timeline |
| `Action_None` | 244 | 281 | 38 | inferred_complete_timeline |
| `Action_None` | 283 | 358 | 76 | inferred_complete_timeline |
| `Action_None` | 362 | 384 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 180 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 185 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–361
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 189 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 206 | 15 | inferred_complete_timeline |
| `Action_None` | 207 | 361 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 419 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–411
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 411 | 412 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 259 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 267 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 248 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–411
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 364 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 366 | 411 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 336 | 337 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 355 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 194–318 | 122 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 201–362 | 162 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 207–210 | 4 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 215–419 | 203 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 218–234 | 17 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 229–230 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 233–288 | 16 | 5 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 235–306 | 59 | 5 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 251–364 | 94 | 3 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 268–359 | 91 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 272–273 | 2 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 286–287 | 2 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 287–338 | 26 | 3 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 296–349 | 54 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 301–349 | 39 | 3 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 302–358 | 40 | 3 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 350–352 | 3 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 369–419 | 51 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 415–419 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 73 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_None' range [205-318] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-403] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-298] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-233] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-336] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-355] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [192-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-361] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-252] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [206-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [392-413] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-358] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-364] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-411] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-232] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-240] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-342] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-411] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-281] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-358] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-384] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-203] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-213] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-318] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-362] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-234] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-234] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-266] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-285] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-240] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-257] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-302] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-254] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-283] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-364] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-313] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-359] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-310] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-338] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-349] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-304] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-349] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-307] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-330] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-358] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-352] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-419] for track '41' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>