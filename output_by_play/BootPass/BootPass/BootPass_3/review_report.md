# Play-Annotation-Generator Annotation Review — BootPass_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_3`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 128
- **Validation Warnings:** 159
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `52` | `35` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 117 |
| ✅ EXACT | `Action_RunBlock` | LT | `13` | `13` | 17 | START | 17 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `19` | `19` | 17 | START | 17 | 19 |
| ✅ EXACT | `Action_RunBlock` | RG | `20` | `20` | 17 | START | 17 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `21` | `21` | 17 | START | 17 | 40 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 27 | END | 27 | 27 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `11` | `11` | 32 | START | 32 | 52 |
| ✅ EXACT | `Action_BootAway` | QB | `11` | `11` | 55 | START | 55 | 113 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `11` | `11` | 155 | START | N/A | N/A |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `52` | `35` | 225 | START | 225 | 235 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_None` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_FakeHandoff` | 32 | 52 | 21 | inferred_complete_timeline |
| `Action_None` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_BootAway` | 55 | 113 | 59 | inferred_complete_timeline |
| `Action_None` | 114 | 141 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 177 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 110 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 182 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 254 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 305 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 312 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 327 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 335 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 343 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 359 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 17 | 102 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 17 | 19 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 24 | 65 | 42 | inferred_complete_timeline |
| `Action_RunBlock` | 74 | 106 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 17 | 131 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 17 | 40 | 24 | inferred_complete_timeline |
| `Action_RunBlock` | 42 | 119 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 120 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 147 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 159 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 66 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 107 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 113 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 155 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 168 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 48 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 294 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 313 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 331 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 359 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 110 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 292 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 319 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 322 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 327 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 359 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 196 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 210 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 299 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 334 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 359 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–297 | 288 | 4 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–147 | 126 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 54–55 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 63–119 | 54 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 65–78 | 11 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 100–167 | 38 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 108–159 | 48 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 111–117 | 7 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 112–190 | 77 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 145–155 | 11 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 149–161 | 11 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 200–281 | 19 | 4 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 210–359 | 141 | 4 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 216–359 | 144 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 220–359 | 128 | 6 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 234–309 | 63 | 5 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 274–292 | 19 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 274–281 | 6 | 2 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 295–298 | 4 | 1 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 322–327 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `11` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF3` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 112 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 8: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 8: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_ThrowPass' for track '11' has invalid range: start=155, end=141. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-254] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-305] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-312] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-327] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-331] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-335] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-343] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-120] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-159] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-297] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-177] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-196] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-299] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-334] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-131] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-155] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [17-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-292] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-319] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-322] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-327] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-202] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-294] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-313] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-331] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-194] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [17-19] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [24-65] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [74-106] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [17-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [17-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [42-119] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-109] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-119] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-102] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-121] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-110] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-151] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-159] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-117] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-150] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-184] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-190] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-155] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-153] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-161] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-210] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-215] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-281] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-214] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-303] for track '33' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-331] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-359] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-264] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-341] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-348] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-260] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-265] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-270] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-296] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-309] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-292] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-277] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-281] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-298] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-327] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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