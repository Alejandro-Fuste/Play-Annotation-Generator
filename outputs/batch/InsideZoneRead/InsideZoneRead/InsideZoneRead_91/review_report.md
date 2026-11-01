# Play-Annotation-Generator Annotation Review — InsideZoneRead_91

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_91`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 124
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `2` | `1` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `12` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 3 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 7 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 13 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 13 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 16 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `9` | `Group` | 0 | START | 0 | 139 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 140 | START | 140 | 151 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `13` | 142 | START | 142 | 152 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `16` | `15` | 142 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 142 | START | 142 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 142 | START | 142 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `8` | `7` | 142 | START | 142 | 160 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 156 | END | 140 | 156 |
| ✅ EXACT | `Action_ReadDefender` | QB | `2` | `1` | 160 | START | 160 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `16` | `15` | 166 | START | 190 | 196 |
| ✅ EXACT | `Action_Handoff` | QB | `2` | `1` | 174 | START | 174 | 180 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `22` | `21` | 181 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 239 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_SnapReceive` | 140 | 156 | 17 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 160 | 173 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 174 | 180 | 7 | inferred_complete_timeline |
| `Action_None` | 181 | 329 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 16–163
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 19 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 163 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 329 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 329 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 168 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 329 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 160 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 206 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 217 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 239 | 21 | inferred_complete_timeline |
| `Action_None` | 240 | 329 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 13–204
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 141 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 153 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 204 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 7–329
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 139 | 133 | inferred_complete_timeline |
| `Action_BallSnap` | 140 | 151 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 190 | 196 | 7 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 201 | 206 | 6 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 226 | 229 | 4 | inferred_complete_timeline |
| `Action_None` | 248 | 329 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 3–152
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 141 | 139 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 152 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 13–152
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 141 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 152 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 7–217
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 139 | 133 | inferred_complete_timeline |
| `Action_None` | 140 | 171 | 32 | inferred_complete_timeline |
| `Action_None` | 179 | 184 | 6 | inferred_complete_timeline |
| `Action_None` | 186 | 217 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 12–329
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 139 | 128 | inferred_complete_timeline |
| `Action_None` | 140 | 152 | 13 | inferred_complete_timeline |
| `Action_None` | 155 | 160 | 6 | inferred_complete_timeline |
| `Action_None` | 182 | 329 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 13–329
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 139 | 127 | inferred_complete_timeline |
| `Action_None` | 140 | 151 | 12 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_None` | 216 | 261 | 46 | inferred_complete_timeline |
| `Action_None` | 263 | 289 | 27 | inferred_complete_timeline |
| `Action_None` | 291 | 296 | 6 | inferred_complete_timeline |
| `Action_None` | 298 | 329 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 13–208
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 139 | 127 | inferred_complete_timeline |
| `Action_None` | 140 | 151 | 12 | inferred_complete_timeline |
| `Action_None` | 176 | 184 | 9 | inferred_complete_timeline |
| `Action_None` | 186 | 190 | 5 | inferred_complete_timeline |
| `Action_None` | 202 | 208 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 176 | 37 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 211 | 12 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 229 | 3 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 329 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 177 | 38 | inferred_complete_timeline |
| `Action_None` | 182 | 196 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 281 | 142 | inferred_complete_timeline |
| `Action_None` | 287 | 329 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 197 | 58 | inferred_complete_timeline |
| `Action_None` | 199 | 329 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 329 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–303
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 303 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 329 | 190 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 186–294 | 95 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 191–239 | 31 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 202–329 | 119 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 214–329 | 116 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 232–329 | 88 | 4 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 262–329 | 67 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 263–329 | 63 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 267–279 | 6 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 268–329 | 48 | 6 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 286–289 | 4 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 289–290 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 300–329 | 26 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 301–329 | 29 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 307–324 | 14 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `16` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (7 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `16` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `22` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 88 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 98 frames exceeds threshold 90 frames [start=142, end=239].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [140–156], lower_priority='Action_ZoneBlock' annotated_start=142, effective_Action_ZoneBlock_start=157.
- ⚠️ Segment 'Action_BallCarry' for track '21' has invalid range: start=181, end=163. Clamping end to start.
- ⚠️ Action 'Action_None' range [140-197] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-303] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-281] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-329] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-176] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-211] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-195] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [197-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [201-206] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [211-217] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-329] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-196] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-141] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-152] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-217] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [140-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [190-196] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [201-206] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [226-229] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-151] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-261] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-289] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-296] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-153] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-204] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-19] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-163] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-196] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-221] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-279] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-294] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-300] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-242] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-287] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-322] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-289] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-284] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-300] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-312] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-310] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-316] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-329] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-314] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-324] for track '35' has 1 frames without a visible bounding box.
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