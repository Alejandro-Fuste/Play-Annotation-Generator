# Play-Annotation-Generator Annotation Review — OutsideZoneRead_74

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_74`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_PressEdge` | DE1 | defense | `3` | `3` |
| ✅ EXACT | `Action_ReadEdgeDefender` | WR1 | offense | `2` | `2` |
| ✅ EXACT | `Action_Handoff` | WR1 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 270 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_ZoneBlock` | C | `12` | `12` | 18 | START | 18 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `19` | `19` | 18 | START | 18 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `20` | 18 | START | 18 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `21` | 18 | START | 18 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 18 | START | 18 | 75 |
| ✅ EXACT | `Action_PressEdge` | DE1 | `3` | `3` | 24 | START | 24 | 98 |
| ✅ EXACT | `Action_ReadEdgeDefender` | WR1 | `2` | `2` | 32 | START | 32 | 42 |
| ✅ EXACT | `Action_Handoff` | WR1 | `2` | `2` | 43 | START | 43 | 58 |

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
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 329 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 208 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 291 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 32 | 42 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 43 | 58 | 16 | inferred_complete_timeline |
| `Action_None` | 59 | 329 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 209 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 75 | 58 | inferred_complete_timeline |
| `Action_None` | 76 | 131 | 56 | inferred_complete_timeline |
| `Action_None` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_None` | 153 | 192 | 40 | inferred_complete_timeline |
| `Action_None` | 195 | 248 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 75 | 58 | inferred_complete_timeline |
| `Action_None` | 76 | 145 | 70 | inferred_complete_timeline |
| `Action_None` | 163 | 166 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 75 | 58 | inferred_complete_timeline |
| `Action_None` | 76 | 175 | 100 | inferred_complete_timeline |
| `Action_None` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_None` | 195 | 221 | 27 | inferred_complete_timeline |
| `Action_None` | 225 | 227 | 3 | inferred_complete_timeline |
| `Action_None` | 233 | 288 | 56 | inferred_complete_timeline |
| `Action_None` | 293 | 329 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 75 | 58 | inferred_complete_timeline |
| `Action_None` | 76 | 127 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 75 | 58 | inferred_complete_timeline |
| `Action_None` | 76 | 148 | 73 | inferred_complete_timeline |
| `Action_None` | 159 | 298 | 140 | inferred_complete_timeline |
| `Action_None` | 300 | 329 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PressEdge` | 24 | 98 | 75 | inferred_complete_timeline |
| `Action_None` | 99 | 141 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 216 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 219 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 173 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 187 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 258 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 264 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 294 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 329 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 256 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 292 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 316 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 328 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 188 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 267 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 329 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 205 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 264 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 274 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 320 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 267 | 268 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 274 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 161–329 | 79 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 220–329 | 101 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 223–304 | 70 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 232–329 | 96 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 234–329 | 84 | 4 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 234–329 | 96 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 242–329 | 70 | 6 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 262–329 | 68 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 283–329 | 47 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 300–329 | 25 | 3 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 308–328 | 21 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 313–328 | 13 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 316–329 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 79 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-187] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-258] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-141] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-267] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-256] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-292] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-316] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-328] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-209] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-294] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-248] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-267] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-329] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-270] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-221] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-288] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-216] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-208] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-291] for track '15' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-188] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-264] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-274] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-320] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-145] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-298] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-170] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-204] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-296] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-302] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-295] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-304] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-257] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-305] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-271] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-287] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-308] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-329] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-317] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-320] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-328] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-316] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-328] for track '34' has 1 frames without a visible bounding box.
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

</details>