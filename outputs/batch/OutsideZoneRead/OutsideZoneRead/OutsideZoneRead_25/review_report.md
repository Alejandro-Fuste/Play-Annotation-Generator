# Play-Annotation-Generator Annotation Review — OutsideZoneRead_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_25`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_ReadEdgeDefender` | WR2 | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 94 |
| ✅ EXACT | `Action_PressEdge` | RB | `18` | `18` | 93 | START | 93 | 131 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `13` | 93 | START | 93 | 132 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `15` | 93 | START | 93 | 139 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `17` | 93 | START | 93 | 139 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 93 | START | 93 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `21` | 93 | START | 93 | 116 |
| ✅ EXACT | `Action_ReadEdgeDefender` | WR2 | `6` | `6` | 95 | START | 95 | 109 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `16` | 110 | START | 110 | 121 |

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
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_Handoff` | 110 | 121 | 12 | inferred_complete_timeline |
| `Action_None` | 122 | 329 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PressEdge` | 93 | 131 | 39 | inferred_complete_timeline |
| `Action_None` | 132 | 149 | 18 | inferred_complete_timeline |
| `Action_None` | 154 | 274 | 121 | inferred_complete_timeline |
| `Action_None` | 276 | 279 | 4 | inferred_complete_timeline |
| `Action_None` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 319 | 27 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 95 | 109 | 15 | inferred_complete_timeline |
| `Action_None` | 110 | 211 | 102 | inferred_complete_timeline |
| `Action_None` | 227 | 256 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 265 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 280 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 329 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 132 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 139 | 47 | inferred_complete_timeline |
| `Action_None` | 140 | 266 | 127 | inferred_complete_timeline |
| `Action_None` | 268 | 279 | 12 | inferred_complete_timeline |
| `Action_None` | 281 | 282 | 2 | inferred_complete_timeline |
| `Action_None` | 297 | 329 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 116 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 127 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 139 | 10 | inferred_complete_timeline |
| `Action_None` | 140 | 266 | 127 | inferred_complete_timeline |
| `Action_None` | 268 | 329 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 139 | 47 | inferred_complete_timeline |
| `Action_None` | 140 | 243 | 104 | inferred_complete_timeline |
| `Action_None` | 245 | 264 | 20 | inferred_complete_timeline |
| `Action_None` | 268 | 281 | 14 | inferred_complete_timeline |
| `Action_None` | 291 | 329 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 139 | 47 | inferred_complete_timeline |
| `Action_None` | 140 | 260 | 121 | inferred_complete_timeline |
| `Action_None` | 262 | 265 | 4 | inferred_complete_timeline |
| `Action_None` | 271 | 329 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 329 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 125 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 146 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 329 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 209 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 256 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 329 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 241 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 329 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 329 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 235 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 241 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 266 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 232 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 121–124 | 4 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 135–258 | 97 | 7 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 141–143 | 3 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 143–241 | 96 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 144–147 | 4 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 152–329 | 163 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 158–160 | 3 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 182–221 | 24 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 208–323 | 116 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 231–329 | 99 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 240–280 | 8 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 247–329 | 75 | 3 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 273–277 | 5 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 276–329 | 37 | 3 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 281–329 | 37 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 286–287 | 2 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 294–329 | 25 | 2 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 318–319 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 80 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-265] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-266] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-211] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-256] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-256] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-230] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-241] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-235] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-280] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-287] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-225] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-232] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-260] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-243] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-264] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-281] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-274] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-319] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-146] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-266] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-279] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-116] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-266] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-124] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-153] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-171] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-200] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-223] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-245] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-258] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-143] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-151] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-236] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-241] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-160] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-195] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-323] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-243] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-280] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-266] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-292] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-277] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-279] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-307] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '40' has 1 frames without a visible bounding box.
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