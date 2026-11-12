# Play-Annotation-Generator Annotation Review — SplitZone_120

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_120`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 18 | START | 19 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 18 | START | 19 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 18 | START | 19 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 18 | START | 19 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 18 | START | 19 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 18 | START | 19 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 18 | START | 19 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 18 | START | 19 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 18 | START | 19 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `14` | `14` | 145 | START | 145 | 156 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `10` | `10` | 148 | START | 148 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 148 | START | 159 | 174 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `15` | 148 | START | 148 | 221 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `3` | 148 | START | 148 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `4` | 148 | START | 148 | 178 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 148 | START | 148 | 221 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 158 | END | 145 | 158 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 164 | START | 164 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `6` | `6` | 178 | START | 178 | 251 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 221 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 19–277
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 144 | 126 | inferred_complete_timeline |
| `Action_SnapReceive` | 145 | 158 | 14 | inferred_complete_timeline |
| `Action_None` | 159 | 163 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 164 | 177 | 14 | inferred_complete_timeline |
| `Action_None` | 178 | 271 | 94 | inferred_complete_timeline |
| `Action_None` | 273 | 277 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 19–72
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 23 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 46 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 65 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 72 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 19–297
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 144 | 126 | inferred_complete_timeline |
| `Action_None` | 145 | 297 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 19–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 147 | 129 | inferred_complete_timeline |
| `Action_SplitBlock` | 148 | 221 | 74 | inferred_complete_timeline |
| `Action_None` | 222 | 329 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 19–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 147 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 178 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 185 | 221 | 37 | inferred_complete_timeline |
| `Action_None` | 222 | 329 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 19–308
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 147 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 221 | 74 | inferred_complete_timeline |
| `Action_None` | 222 | 251 | 30 | inferred_complete_timeline |
| `Action_None` | 254 | 308 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 19–329
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 144 | 126 | inferred_complete_timeline |
| `Action_BallSnap` | 145 | 156 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 158 | 158 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 174 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 190 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 216 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 221 | 3 | inferred_complete_timeline |
| `Action_None` | 222 | 224 | 3 | inferred_complete_timeline |
| `Action_None` | 226 | 304 | 79 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 311 | 329 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 19–303
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 147 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 221 | 74 | inferred_complete_timeline |
| `Action_None` | 222 | 303 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 19–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 147 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 221 | 74 | inferred_complete_timeline |
| `Action_None` | 222 | 329 | 108 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 19–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 144 | 126 | inferred_complete_timeline |
| `Action_None` | 145 | 201 | 57 | inferred_complete_timeline |
| `Action_None` | 207 | 213 | 7 | inferred_complete_timeline |
| `Action_None` | 215 | 320 | 106 | inferred_complete_timeline |
| `Action_None` | 322 | 329 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 19–329
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 144 | 126 | inferred_complete_timeline |
| `Action_None` | 145 | 241 | 97 | inferred_complete_timeline |
| `Action_None` | 244 | 304 | 61 | inferred_complete_timeline |
| `Action_None` | 306 | 308 | 3 | inferred_complete_timeline |
| `Action_None` | 315 | 316 | 2 | inferred_complete_timeline |
| `Action_None` | 326 | 329 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 19–224
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 144 | 126 | inferred_complete_timeline |
| `Action_None` | 145 | 224 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 19–237
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 144 | 126 | inferred_complete_timeline |
| `Action_None` | 145 | 207 | 63 | inferred_complete_timeline |
| `Action_None` | 212 | 233 | 22 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 19–256
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 144 | 126 | inferred_complete_timeline |
| `Action_None` | 145 | 187 | 43 | inferred_complete_timeline |
| `Action_None` | 192 | 206 | 15 | inferred_complete_timeline |
| `Action_None` | 254 | 256 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 19–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 144 | 126 | inferred_complete_timeline |
| `Action_None` | 145 | 329 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 19–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 144 | 126 | inferred_complete_timeline |
| `Action_None` | 145 | 265 | 121 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |
| `Action_None` | 271 | 329 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 19–329 | 306 | 5 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 134–329 | 196 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 188–197 | 9 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 194–329 | 136 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 206–212 | 7 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 215–329 | 115 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 228–304 | 77 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 231–283 | 53 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 237–240 | 4 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 248–329 | 80 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 266–329 | 62 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 266–278 | 11 | 2 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 291–325 | 27 | 3 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 308–316 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [145–158], lower_priority='Action_ZoneBlock' annotated_start=148, effective_Action_ZoneBlock_start=159.
- ⚠️ Action 'Action_None' range [145-201] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-320] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-265] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-241] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-304] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-303] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-178] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [185-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-221] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-251] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-308] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-251] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [254-259] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [262-291] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-187] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-206] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-297] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-224] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-271] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-207] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [145-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-174] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-190] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [212-216] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-304] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-46] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-65] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-72] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-304] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-283] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-323] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-273] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-297] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-316] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>