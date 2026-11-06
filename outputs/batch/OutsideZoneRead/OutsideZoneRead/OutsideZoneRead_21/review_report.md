# Play-Annotation-Generator Annotation Review — OutsideZoneRead_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_21`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 142
- **Validation Warnings:** 156
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 120
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 284 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 233 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 377 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 131 | START | 131 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `16` | 131 | START | 131 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `18` | 131 | START | 131 | 132 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `19` | 131 | START | 131 | 142 |
| ✅ EXACT | `Action_PressEdge` | RB | `7` | `7` | 135 | START | 135 | 194 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `17` | `17` | 137 | START | 137 | 147 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `17` | 148 | START | 148 | 163 |

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
- **Visible Frames:** 0–365
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 137 | 147 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 148 | 163 | 16 | inferred_complete_timeline |
| `Action_None` | 164 | 365 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_PressEdge` | 135 | 194 | 60 | inferred_complete_timeline |
| `Action_None` | 195 | 199 | 5 | inferred_complete_timeline |
| `Action_None` | 224 | 236 | 13 | inferred_complete_timeline |
| `Action_None` | 250 | 389 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 284 | 285 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 389 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 377 | 378 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 389 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 389 | 390 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 244 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 129 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 151 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 167 | 5 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 207 | 6 | inferred_complete_timeline |
| `Action_None` | 220 | 347 | 128 | inferred_complete_timeline |
| `Action_None` | 350 | 389 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 137 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 155 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 136 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_None` | 175 | 182 | 8 | inferred_complete_timeline |
| `Action_None` | 207 | 355 | 149 | inferred_complete_timeline |
| `Action_None` | 379 | 382 | 4 | inferred_complete_timeline |
| `Action_None` | 386 | 389 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 142 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 182 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 152 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 182 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 196 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 265 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 327 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 389 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 167 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 182 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 195 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 285 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 350 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 389 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 276 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 285 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 344 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 350 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 365 | 389 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 170 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 195 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 229 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–387
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 267 | 268 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 275 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 357 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 366 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 380 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 382 | 384 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 387 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 389 | 390 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 389 | 390 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 299 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 314 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 322 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 389 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 316 | 317 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 320 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 325 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 335 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 337 | 341 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 351 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 362 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 371 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 389 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 7–217 | 190 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 13–129 | 117 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 166–215 | 14 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 230–389 | 157 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 231–389 | 149 | 4 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 237–389 | 122 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 237–254 | 18 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 238–389 | 145 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 239–388 | 94 | 5 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 262–352 | 83 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 275–276 | 2 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 283–291 | 9 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 284–389 | 103 | 3 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 315–376 | 37 | 5 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 342–348 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 125 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-284] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-389] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-316] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-320] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-325] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-335] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-341] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-351] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-362] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-371] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-377] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-299] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-308] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-314] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-322] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-267] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-357] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-366] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-380] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-384] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-387] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-236] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-167] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-285] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-350] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-389] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-182] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-233] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-244] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-152] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-182] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-196] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-218] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-327] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-389] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-136] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-355] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-228] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-276] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-285] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-344] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-350] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-151] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-365] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-151] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-347] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-129] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-142] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-155] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-186] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-217] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-193] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-215] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-285] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-389] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-295] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-278] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-345] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-354] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-254] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-288] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-305] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-283] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-295] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-307] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-349] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-388] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-282] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-352] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-291] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-288] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-294] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-389] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-317] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-345] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-364] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-376] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-348] for track '34' has 2 frames without a visible bounding box.
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

</details>