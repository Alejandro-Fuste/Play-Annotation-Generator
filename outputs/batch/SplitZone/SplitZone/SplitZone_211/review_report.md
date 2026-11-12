# Play-Annotation-Generator Annotation Review — SplitZone_211

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_211`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_SplitBlock` | RT | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ⚠️ END CHANGED | `Action_SnapReceive` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_BlockSecondLevel` | SAF2 | defense | `4` | `4` |
| ✅ EXACT | `Action_BallCarry` | RG | offense | `21` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 28 | START | 29 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 28 | START | 29 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 28 | START | 29 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 28 | START | 29 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 28 | START | 29 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 28 | START | 29 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 28 | START | 29 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 28 | START | 29 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 28 | START | 29 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 28 | START | 29 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 28 | START | 29 | 145 |
| ✅ EXACT | `Action_BallSnap` | LT | `19` | `19` | 146 | START | 146 | 148 |
| ✅ EXACT | `Action_SplitBlock` | RT | `12` | `12` | 148 | START | 148 | 148 |
| ✅ EXACT | `Action_ZoneBlock` | C | `10` | `10` | 149 | START | 149 | 206 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `12` | 149 | START | 149 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `15` | 149 | START | 149 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `19` | 149 | START | 149 | 159 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `21` | `21` | 149 | START | N/A | N/A |
| ⚠️ END CHANGED | `Action_SnapReceive` | RG | `21` | `21` | 158 | END | 146 | 152 |
| ✅ EXACT | `Action_BlockSecondLevel` | SAF2 | `4` | `4` | 170 | START | 170 | 224 |
| ✅ EXACT | `Action_BallCarry` | RG | `21` | `21` | 187 | START | 187 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 224 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 29–292
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 211 | 66 | inferred_complete_timeline |
| `Action_None` | 213 | 251 | 39 | inferred_complete_timeline |
| `Action_None` | 253 | 259 | 7 | inferred_complete_timeline |
| `Action_None` | 273 | 292 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 29–329
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 217 | 72 | inferred_complete_timeline |
| `Action_None` | 238 | 329 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 29–329
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 217 | 72 | inferred_complete_timeline |
| `Action_None` | 235 | 237 | 3 | inferred_complete_timeline |
| `Action_None` | 244 | 249 | 6 | inferred_complete_timeline |
| `Action_None` | 260 | 262 | 3 | inferred_complete_timeline |
| `Action_None` | 274 | 287 | 14 | inferred_complete_timeline |
| `Action_None` | 289 | 329 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 29–208
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 208 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 29–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 329 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 29–329
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 215 | 70 | inferred_complete_timeline |
| `Action_None` | 273 | 299 | 27 | inferred_complete_timeline |
| `Action_None` | 301 | 329 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 29–206
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_BallSnap` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 159 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 176 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 194 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 204 | 206 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 29–329
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 148 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 167 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 212 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 214 | 221 | 8 | inferred_complete_timeline |
| `Action_None` | 233 | 266 | 34 | inferred_complete_timeline |
| `Action_None` | 268 | 329 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 29–206
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 148 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 206 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 29–329
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 79 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 145 | 65 | inferred_complete_timeline |
| `Action_SnapReceive` | 146 | 152 | 7 | inferred_complete_timeline |
| `Action_None` | 162 | 168 | 7 | inferred_complete_timeline |
| `Action_None` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_None` | 180 | 186 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 187 | 329 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 29–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 147 | 119 | inferred_complete_timeline |
| `Action_SplitBlock` | 148 | 148 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 224 | 76 | inferred_complete_timeline |
| `Action_None` | 225 | 329 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 29–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 329 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 29–292
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 196 | 51 | inferred_complete_timeline |
| `Action_None` | 207 | 292 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 29–295
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 167 | 22 | inferred_complete_timeline |
| `Action_None` | 208 | 281 | 74 | inferred_complete_timeline |
| `Action_None` | 283 | 295 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 29–180
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 152 | 7 | inferred_complete_timeline |
| `Action_None` | 155 | 167 | 13 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 29–198
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 152 | 7 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_None` | 179 | 191 | 13 | inferred_complete_timeline |
| `Action_None` | 197 | 198 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 29–329
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 250 | 105 | inferred_complete_timeline |
| `Action_None` | 253 | 329 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 29–329
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 221 | 76 | inferred_complete_timeline |
| `Action_None` | 228 | 250 | 23 | inferred_complete_timeline |
| `Action_None` | 254 | 329 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 29–329
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 214 | 69 | inferred_complete_timeline |
| `Action_None` | 222 | 329 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 29–244
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 161 | 16 | inferred_complete_timeline |
| `Action_None` | 175 | 191 | 17 | inferred_complete_timeline |
| `Action_None` | 199 | 244 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 29–167
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 146 | 167 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 29–329
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 169 | 141 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 170 | 224 | 55 | inferred_complete_timeline |
| `Action_None` | 225 | 234 | 10 | inferred_complete_timeline |
| `Action_None` | 237 | 263 | 27 | inferred_complete_timeline |
| `Action_None` | 275 | 280 | 6 | inferred_complete_timeline |
| `Action_None` | 283 | 329 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 180–329 | 150 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 191–209 | 19 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 205–329 | 119 | 3 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 224–328 | 103 | 2 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 241–318 | 78 | 1 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 248–329 | 79 | 2 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 249–256 | 8 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 259–329 | 68 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (RG)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=149, end=145. Clamping end to start.
- ⚠️ Action 'Action_None' range [146-215] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-250] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-234] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-263] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-329] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-217] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-287] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-217] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-250] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [149-206] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-208] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-161] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-191] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-244] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [149-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-212] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [214-221] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-266] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-211] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-251] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-259] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-292] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-196] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-292] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-281] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-295] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [149-159] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-176] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-194] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [204-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [146-152] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [187-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-209] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-263] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-328] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-318] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-264] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-256] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-264] for track '29' has 1 frames without a visible bounding box.
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