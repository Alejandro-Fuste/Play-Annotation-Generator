# Play-Annotation-Generator Annotation Review — SplitZone_279

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_279`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 196
- **Validation Warnings:** 222
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 169
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `2` | `2` |
| ✅ EXACT | `Action_SplitBlock` | RT | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 74 |
| ✅ EXACT | `Action_BallSnap` | C | `2` | `2` | 157 | START | 157 | 171 |
| ✅ EXACT | `Action_SplitBlock` | RT | `0` | `0` | 164 | START | 164 | 172 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 171 | END | 157 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `0` | `0` | 173 | START | 173 | 213 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `2` | `2` | 173 | START | 173 | 187 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `3` | 173 | START | 173 | 199 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `4` | 173 | START | 173 | 225 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `9` | 173 | START | 173 | 199 |
| ✅ EXACT | `Action_PressEdge` | RB | `7` | `7` | 180 | START | 180 | 202 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `6` | 188 | START | 188 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `3` | `3` | 200 | START | 200 | 227 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `7` | 203 | START | 203 | 258 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 156 | 91 | inferred_complete_timeline |
| `Action_SnapReceive` | 157 | 171 | 15 | inferred_complete_timeline |
| `Action_None` | 172 | 187 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 188 | 201 | 14 | inferred_complete_timeline |
| `Action_None` | 202 | 269 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PressEdge` | 180 | 202 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 258 | 56 | inferred_complete_timeline |
| `Action_BallCarry` | 260 | 278 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 281 | 294 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 298 | 305 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 319 | 323 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 156 | 56 | inferred_complete_timeline |
| `Action_None` | 157 | 195 | 39 | inferred_complete_timeline |
| `Action_None` | 197 | 246 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 172 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 199 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 225 | 25 | inferred_complete_timeline |
| `Action_None` | 226 | 241 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 172 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 199 | 27 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 200 | 227 | 28 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 229 | 229 | 1 | inferred_complete_timeline |
| `Action_None` | 230 | 248 | 19 | inferred_complete_timeline |
| `Action_None` | 251 | 253 | 3 | inferred_complete_timeline |
| `Action_None` | 255 | 258 | 4 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 156 | 60 | inferred_complete_timeline |
| `Action_BallSnap` | 157 | 171 | 15 | inferred_complete_timeline |
| `Action_None` | 172 | 172 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 187 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 216 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 172 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 225 | 53 | inferred_complete_timeline |
| `Action_None` | 226 | 246 | 21 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_None` | 326 | 328 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 163 | 46 | inferred_complete_timeline |
| `Action_SplitBlock` | 164 | 172 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 213 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 225 | 11 | inferred_complete_timeline |
| `Action_None` | 233 | 324 | 92 | inferred_complete_timeline |
| `Action_None` | 333 | 337 | 5 | inferred_complete_timeline |
| `Action_None` | 344 | 389 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 29 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 113 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 129 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 145 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 174 | 18 | inferred_complete_timeline |
| `Action_None` | 240 | 251 | 12 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_None` | 281 | 285 | 5 | inferred_complete_timeline |
| `Action_None` | 301 | 308 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 156 | 56 | inferred_complete_timeline |
| `Action_None` | 157 | 204 | 48 | inferred_complete_timeline |
| `Action_None` | 239 | 245 | 7 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |
| `Action_None` | 271 | 294 | 24 | inferred_complete_timeline |
| `Action_None` | 297 | 321 | 25 | inferred_complete_timeline |
| `Action_None` | 347 | 385 | 39 | inferred_complete_timeline |
| `Action_None` | 387 | 389 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–30
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 180 | 24 | inferred_complete_timeline |
| `Action_None` | 189 | 195 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 60 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 74 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 86 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 94 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 118 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 156 | 37 | inferred_complete_timeline |
| `Action_None` | 157 | 201 | 45 | inferred_complete_timeline |
| `Action_None` | 278 | 287 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 214 | 58 | inferred_complete_timeline |
| `Action_None` | 216 | 259 | 44 | inferred_complete_timeline |
| `Action_None` | 262 | 271 | 10 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 109–301 | 175 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 111–174 | 64 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 189–304 | 67 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 194–389 | 122 | 13 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 206–300 | 47 | 5 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 214–389 | 104 | 9 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 224–389 | 127 | 9 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 229–319 | 56 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 238–252 | 15 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 240–388 | 71 | 6 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 256–364 | 70 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 267–272 | 5 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 282–315 | 24 | 4 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 287–389 | 76 | 6 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 304–389 | 86 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 316–388 | 8 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 323–357 | 19 | 4 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 328–331 | 4 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 336–344 | 9 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 337–387 | 37 | 4 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 348–389 | 29 | 5 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 355–387 | 33 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 360–379 | 11 | 2 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 362–383 | 16 | 2 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 363–385 | 21 | 3 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 370–388 | 16 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 169 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-213] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [215-225] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-324] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-337] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-97] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-195] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-246] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-187] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [200-227] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-248] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-225] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-174] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-251] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-308] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-258] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [260-278] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [281-294] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [298-305] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [319-323] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-241] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-259] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-271] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-204] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-294] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-321] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-385] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-195] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-60] for track '13' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-201] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-287] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-29] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-113] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-120] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-287] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-195] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-295] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-304] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-204] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-294] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-303] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-314] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-353] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-367] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-385] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-235] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-255] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-278] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-286] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-294] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-302] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-256] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-331] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-353] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-261] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-282] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-252] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-267] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-383] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-388] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-309] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-319] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-364] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-303] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-335] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-361] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-385] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-389] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-381] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-328] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-338] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-344] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-361] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-369] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-353] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-367] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-383] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-389] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-387] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-367] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-379] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-367] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-383] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-372] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-379] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-385] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-383] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '40' has 1 frames without a visible bounding box.
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

</details>