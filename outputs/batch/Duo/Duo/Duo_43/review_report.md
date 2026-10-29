# Play-Annotation-Generator Annotation Review — Duo_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_43`
- **Frame Range:** 0 to 298 (299 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 298
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `24` | `23` |
| ✅ EXACT | `Action_ComboBlock` | CB3 | defense | `3` | `3` |
| ✅ EXACT | `Action_ComboBlock` | CB1 | defense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | DE1 | defense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | DE1 | defense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 278 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 227 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `24` | `Group` | 0 | START | 80 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `24` | `23` | 149 | START | 149 | 169 |
| ✅ EXACT | `Action_ComboBlock` | CB3 | `3` | `3` | 149 | START | 149 | 201 |
| ✅ EXACT | `Action_ComboBlock` | CB1 | `5` | `5` | 149 | START | 149 | 201 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | DE1 | `7` | `7` | 149 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | DE1 | `7` | `7` | 172 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 201 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–242
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 131 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 137 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 218 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 242 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 228 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 285 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 292 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 298 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 231 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 245 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 298 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 160 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 169 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 183 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 205 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 284 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 278 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 80–261
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 80 | 134 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 148 | 13 | inferred_complete_timeline |
| `Action_ComboBlock` | 149 | 169 | 21 | inferred_complete_timeline |
| `Action_ComboBlock` | 172 | 201 | 30 | inferred_complete_timeline |
| `Action_None` | 202 | 237 | 36 | inferred_complete_timeline |
| `Action_None` | 242 | 261 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 161 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 150 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 258 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 280 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 246 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 298 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 231 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 245 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 267 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 7–186
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 109 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 151 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 186 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_ComboBlock` | 149 | 201 | 53 | inferred_complete_timeline |
| `Action_None` | 202 | 233 | 32 | inferred_complete_timeline |
| `Action_None` | 235 | 298 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 216 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 298 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_ComboBlock` | 149 | 201 | 53 | inferred_complete_timeline |
| `Action_None` | 202 | 216 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 298 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 203 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 233 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 298 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–216 | 201 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–64 | 63 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 23–233 | 44 | 8 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 55–56 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 161–236 | 70 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 182–222 | 30 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 183–275 | 92 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 194–203 | 10 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 212–298 | 71 | 3 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 229–298 | 70 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 229–249 | 21 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 236–293 | 56 | 2 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 238–298 | 61 | 1 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 255–287 | 33 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `24` (2 segments found)
- ❌ Missing segment for action `Action_ComboBlock` on target `7` (DE1)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `7` (DE1)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 87 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 87: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ Row 88: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '7' has invalid range: start=149, end=147. Clamping end to start.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '7' has invalid range: start=172, end=147. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-278] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-298] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-231] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-233] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-298] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-258] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-280] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-246] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-298] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-203] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-233] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-188] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-204] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-219] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-285] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-292] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-161] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-231] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-245] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-267] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-137] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-218] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-242] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-169] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-183] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-284] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-64] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-109] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-186] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-133] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-224] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [149-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [172-201] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-237] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-261] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-192] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-236] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-222] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-199] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-275] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-203] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-222] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-244] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-298] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-249] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-289] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-287] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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

</details>