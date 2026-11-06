# Play-Annotation-Generator Annotation Review — OutsideZoneRead_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_7`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 166
- **Validation Warnings:** 213
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 135
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `4` | `4` |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 18 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 130 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `14` | `14` | 125 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `18` | `18` | 125 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `4` | `4` | 125 | START | 133 | 134 |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | `3` | `3` | 132 | START | 132 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `5` | `5` | 143 | START | 143 | 156 |
| ✅ EXACT | `Action_PressEdge` | RB | `3` | `3` | 171 | START | 171 | 172 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 142 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 143 | 156 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 158 | 181 | 24 | inferred_complete_timeline |
| `Action_None` | 182 | 359 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 132 | 143 | 12 | inferred_complete_timeline |
| `Action_None` | 144 | 170 | 27 | inferred_complete_timeline |
| `Action_PressEdge` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 187 | 15 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 321 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 325 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 348 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 359 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 49 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 88 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 117 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 182 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 190 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 18–359
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 26 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 49 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 59 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 83 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 117 | 24 | inferred_complete_timeline |
| `Action_None` | 163 | 351 | 189 | inferred_complete_timeline |
| `Action_None` | 354 | 359 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_None` | 158 | 359 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–9
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 201 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 261 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 265 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 156 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 163 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 227 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 205 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 203 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 248 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 80 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 116 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 210 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 255 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 277 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 194 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 210 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 220 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 308 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 236 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 30 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 60 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–359 | 287 | 13 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 6–88 | 60 | 8 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 13–321 | 278 | 9 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 112–185 | 18 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 126–296 | 167 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 145–316 | 159 | 6 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 147–154 | 8 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 148–158 | 11 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 148–253 | 106 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 160–291 | 127 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 162–359 | 130 | 9 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 179–274 | 82 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 208–307 | 67 | 7 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 208–359 | 138 | 4 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 211–239 | 20 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 223–287 | 63 | 3 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 230–317 | 82 | 4 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 240–243 | 4 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 249–312 | 64 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 264–327 | 63 | 2 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 288–307 | 11 | 3 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 307–310 | 4 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 311–355 | 45 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 331–336 | 6 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 355–359 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `14` (RT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `18` (LT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 153 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 16: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 16: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '14' has invalid range: start=125, end=9. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-30] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-60] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-203] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-248] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [143-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-173] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-182] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-194] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-220] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-308] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-201] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-261] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-265] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-255] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-277] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-227] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-321] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-325] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-348] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-206] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-236] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-49] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-88] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-182] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-190] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-28] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-49] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-88] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-115] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-154] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-199] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-227] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-248] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-35] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-59] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-69] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-88] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-134] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-143] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-158] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-187] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-224] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-267] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-317] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-321] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-26] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-49] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-59] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-91] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-117] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-351] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-185] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-130] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-138] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-296] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-278] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-285] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-289] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-304] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-308] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-316] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-154] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-253] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-291] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-239] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-283] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-291] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-302] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-314] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-274] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-201] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-269] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-294] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-307] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-216] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-277] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-286] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-359] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-224] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-233] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-261] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-287] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-240] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-310] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-243] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-312] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-274] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-327] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-293] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-299] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-307] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-310] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-355] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-336] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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