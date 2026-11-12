# Play-Annotation-Generator Annotation Review — SplitZone_129

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_129`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 23 | START | 24 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 23 | START | 24 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 23 | START | 24 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 23 | START | 24 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 23 | START | 24 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 23 | START | 24 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 23 | START | 24 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 23 | START | 24 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 23 | START | 24 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 23 | START | 24 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 23 | START | 24 | 119 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 114 | START | 114 | 128 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `13` | 117 | START | 129 | 271 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `17` | 117 | START | 117 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `18` | 117 | START | 117 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `19` | 117 | START | 117 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `21` | 117 | START | 117 | 255 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `6` | `6` | 120 | START | 120 | 260 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 128 | END | 114 | 128 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `16` | 130 | START | 130 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 142 | START | 142 | 240 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 271 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 24–329
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_SnapReceive` | 114 | 128 | 15 | inferred_complete_timeline |
| `Action_None` | 129 | 129 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 130 | 141 | 12 | inferred_complete_timeline |
| `Action_None` | 142 | 329 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 24–296
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 141 | 118 | inferred_complete_timeline |
| `Action_BallCarry` | 142 | 240 | 99 | inferred_complete_timeline |
| `Action_BallCarry` | 243 | 296 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 24–329
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 329 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 24–329
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 329 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 24–326
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 119 | 96 | inferred_complete_timeline |
| `Action_SplitBlock` | 120 | 260 | 141 | inferred_complete_timeline |
| `Action_SplitBlock` | 264 | 271 | 8 | inferred_complete_timeline |
| `Action_None` | 272 | 280 | 9 | inferred_complete_timeline |
| `Action_None` | 284 | 303 | 20 | inferred_complete_timeline |
| `Action_None` | 310 | 312 | 3 | inferred_complete_timeline |
| `Action_None` | 318 | 321 | 4 | inferred_complete_timeline |
| `Action_None` | 323 | 326 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 24–321
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 256 | 143 | inferred_complete_timeline |
| `Action_None` | 258 | 261 | 4 | inferred_complete_timeline |
| `Action_None` | 263 | 311 | 49 | inferred_complete_timeline |
| `Action_None` | 316 | 321 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 24–329
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 116 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 255 | 139 | inferred_complete_timeline |
| `Action_ZoneBlock` | 258 | 261 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_None` | 278 | 329 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 24–257
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 116 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 134 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 252 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 254 | 257 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 24–317
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_BallSnap` | 114 | 128 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 271 | 143 | inferred_complete_timeline |
| `Action_None` | 272 | 311 | 40 | inferred_complete_timeline |
| `Action_None` | 313 | 317 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 24–329
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 116 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 125 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 271 | 140 | inferred_complete_timeline |
| `Action_None` | 272 | 329 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 24–329
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 116 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 177 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 271 | 91 | inferred_complete_timeline |
| `Action_None` | 272 | 317 | 46 | inferred_complete_timeline |
| `Action_None` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 24–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 148 | 35 | inferred_complete_timeline |
| `Action_None` | 150 | 329 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 24–150
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 150 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 24–329
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 236 | 123 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 253 | 5 | inferred_complete_timeline |
| `Action_None` | 258 | 276 | 19 | inferred_complete_timeline |
| `Action_None` | 278 | 329 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 24–329
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 133 | 20 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 246 | 98 | inferred_complete_timeline |
| `Action_None` | 248 | 256 | 9 | inferred_complete_timeline |
| `Action_None` | 258 | 272 | 15 | inferred_complete_timeline |
| `Action_None` | 280 | 329 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 24–328
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 309 | 196 | inferred_complete_timeline |
| `Action_None` | 321 | 328 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 24–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 321 | 208 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 24–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 308 | 195 | inferred_complete_timeline |
| `Action_None` | 310 | 329 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 24–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 261 | 148 | inferred_complete_timeline |
| `Action_None` | 266 | 271 | 6 | inferred_complete_timeline |
| `Action_None` | 273 | 329 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 24–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 264 | 151 | inferred_complete_timeline |
| `Action_None` | 267 | 271 | 5 | inferred_complete_timeline |
| `Action_None` | 275 | 329 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 24–329
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 250 | 137 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 270 | 11 | inferred_complete_timeline |
| `Action_None` | 272 | 282 | 11 | inferred_complete_timeline |
| `Action_None` | 285 | 304 | 20 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 317 | 329 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 24–308
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 308 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 66–137 | 43 | 4 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 156–329 | 161 | 4 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `26` | `42` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |
| `27` | `47` | Position_Unknown | Team_Unknown | 288–289 | 2 | 1 | Undefined position; Undefined team |
| `28` | `48` | Position_Unknown | Team_Unknown | 298–329 | 28 | 3 | Undefined position; Undefined team |
| `29` | `52` | Position_Unknown | Team_Unknown | 311–329 | 8 | 3 | Undefined position; Undefined team |
| `30` | `53` | Position_Unknown | Team_Unknown | 317–319 | 3 | 1 | Undefined position; Undefined team |
| `31` | `54` | Position_Unknown | Team_Unknown | 324–326 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 117 != Inferred start 129
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 155 frames exceeds threshold 90 frames [start=117, end=271].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [114–128], lower_priority='Action_ZoneBlock' annotated_start=117, effective_Action_ZoneBlock_start=129.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 155 frames exceeds threshold 90 frames [start=117, end=271].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 155 frames exceeds threshold 90 frames [start=117, end=271].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 141 frames exceeds threshold 90 frames [start=117, end=257].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LT) duration 155 frames exceeds threshold 90 frames [start=117, end=271].
- ⚠️ Action 'Action_None' range [114-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-329] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-308] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-329] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [142-240] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [243-296] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-264] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-271] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [120-260] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [264-271] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-280] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-303] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-321] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-246] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-272] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-329] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-309] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-328] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-256] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-311] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-321] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-236] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-276] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-261] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-271] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-271] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-311] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-317] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-250] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-270] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-282] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-304] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-329] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-308] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-329] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-271] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-317] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-252] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [254-257] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-255] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [258-261] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [269-270] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-95] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-208] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-280] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-329] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-329] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '31' has 1 frames without a visible bounding box.
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

</details>