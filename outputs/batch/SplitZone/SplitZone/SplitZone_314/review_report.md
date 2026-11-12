# Play-Annotation-Generator Annotation Review — SplitZone_314

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_314`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 158
- **Validation Warnings:** 176
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 10
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 138
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `18` | `18` |
| ✅ EXACT | `Action_SplitBlock` | LB2 | defense | `2` | `2` |
| ✅ EXACT | `Action_PressEdge` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 56 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `15` | `15` | 24 | START | 24 | 25 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `18` | `18` | 25 | END | 24 | 25 |
| ✅ EXACT | `Action_SplitBlock` | LB2 | `2` | `2` | 33 | START | 33 | 97 |
| ✅ EXACT | `Action_PressEdge` | QB | `13` | `13` | 41 | START | 41 | 60 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `14` | 57 | START | 57 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `4` | 57 | START | 57 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `6` | 57 | START | 57 | 60 |
| ✅ EXACT | `Action_ZoneBlock` | C | `7` | `7` | 57 | START | 57 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 57 | START | 57 | 75 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `13` | 61 | START | 61 | 71 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `15` | `15` | 64 | START | 64 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `13` | `13` | 73 | START | 73 | 196 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–300
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PressEdge` | 41 | 60 | 20 | inferred_complete_timeline |
| `Action_Handoff` | 61 | 71 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 73 | 196 | 124 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 300 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 197 | 174 | inferred_complete_timeline |
| `Action_None` | 199 | 205 | 7 | inferred_complete_timeline |
| `Action_None` | 207 | 230 | 24 | inferred_complete_timeline |
| `Action_None` | 234 | 242 | 9 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 359 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 165 | 142 | inferred_complete_timeline |
| `Action_None` | 169 | 289 | 121 | inferred_complete_timeline |
| `Action_None` | 292 | 294 | 3 | inferred_complete_timeline |
| `Action_None` | 296 | 304 | 9 | inferred_complete_timeline |
| `Action_None` | 307 | 359 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 75 | 19 | inferred_complete_timeline |
| `Action_None` | 76 | 79 | 4 | inferred_complete_timeline |
| `Action_None` | 81 | 93 | 13 | inferred_complete_timeline |
| `Action_None` | 96 | 204 | 109 | inferred_complete_timeline |
| `Action_None` | 208 | 359 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 75 | 19 | inferred_complete_timeline |
| `Action_None` | 76 | 87 | 12 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 108 | 9 | inferred_complete_timeline |
| `Action_None` | 110 | 178 | 69 | inferred_complete_timeline |
| `Action_None` | 192 | 209 | 18 | inferred_complete_timeline |
| `Action_None` | 212 | 261 | 50 | inferred_complete_timeline |
| `Action_None` | 263 | 318 | 56 | inferred_complete_timeline |
| `Action_None` | 321 | 359 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 75 | 19 | inferred_complete_timeline |
| `Action_None` | 76 | 359 | 284 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 75 | 19 | inferred_complete_timeline |
| `Action_None` | 76 | 305 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 75 | 8 | inferred_complete_timeline |
| `Action_None` | 76 | 128 | 53 | inferred_complete_timeline |
| `Action_None` | 134 | 257 | 124 | inferred_complete_timeline |
| `Action_None` | 259 | 359 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 89 | 66 | inferred_complete_timeline |
| `Action_None` | 96 | 139 | 44 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 340 | 197 | inferred_complete_timeline |
| `Action_None` | 343 | 359 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 290 | 267 | inferred_complete_timeline |
| `Action_None` | 292 | 297 | 6 | inferred_complete_timeline |
| `Action_None` | 299 | 359 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 304 | 281 | inferred_complete_timeline |
| `Action_None` | 307 | 343 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 82 | 59 | inferred_complete_timeline |
| `Action_None` | 84 | 257 | 174 | inferred_complete_timeline |
| `Action_None` | 263 | 265 | 3 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 314 | 40 | inferred_complete_timeline |
| `Action_None` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_None` | 323 | 359 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 267 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SplitBlock` | 33 | 97 | 65 | inferred_complete_timeline |
| `Action_None` | 98 | 165 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 137 | 114 | inferred_complete_timeline |
| `Action_None` | 142 | 165 | 24 | inferred_complete_timeline |
| `Action_None` | 170 | 190 | 21 | inferred_complete_timeline |
| `Action_None` | 192 | 283 | 92 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 289 | 297 | 9 | inferred_complete_timeline |
| `Action_None` | 314 | 319 | 6 | inferred_complete_timeline |
| `Action_None` | 327 | 331 | 5 | inferred_complete_timeline |
| `Action_None` | 333 | 359 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–73 | 70 | 5 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–96 | 97 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–359 | 342 | 8 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–182 | 183 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–359 | 330 | 7 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–359 | 359 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–359 | 328 | 8 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 92–104 | 13 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 123–310 | 179 | 4 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 160–192 | 4 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 167–359 | 187 | 4 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 171–359 | 189 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 183–204 | 18 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 228–356 | 126 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 241–318 | 67 | 4 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 250–252 | 3 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 277–283 | 5 | 2 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 284–300 | 8 | 2 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 294–297 | 4 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 299–304 | 5 | 2 | Undefined position; Undefined team |
| `38` | `61` | Position_Unknown | Team_Unknown | 312–359 | 48 | 1 | Undefined position; Undefined team |
| `39` | `63` | Position_Unknown | Team_Unknown | 316–319 | 4 | 1 | Undefined position; Undefined team |
| `40` | `66` | Position_Unknown | Team_Unknown | 325–326 | 2 | 1 | Undefined position; Undefined team |
| `41` | `68` | Position_Unknown | Team_Unknown | 330–331 | 2 | 1 | Undefined position; Undefined team |
| `42` | `69` | Position_Unknown | Team_Unknown | 332–359 | 28 | 1 | Undefined position; Undefined team |
| `43` | `71` | Position_Unknown | Team_Unknown | 334–335 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 117 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [24-137] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-165] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-190] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-283] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-297] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-331] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-267] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-165] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-165] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-289] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-294] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-304] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-87] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-178] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-261] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-318] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-82] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-257] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-314] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-60] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-66] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-128] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-257] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-359] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-290] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-297] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-359] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-93] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-204] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-197] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-205] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-242] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-340] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-304] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-343] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [61-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [73-196] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-300] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-305] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-63] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [64-73] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-122] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-172] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-209] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-182] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-123] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-46] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-51] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-231] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-268] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-276] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-174] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-310] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-267] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-328] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-192] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-204] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-341] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-356] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-246] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-283] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-305] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-318] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-289] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.

</details>