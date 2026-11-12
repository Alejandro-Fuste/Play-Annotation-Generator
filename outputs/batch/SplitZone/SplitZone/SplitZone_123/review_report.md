# Play-Annotation-Generator Annotation Review — SplitZone_123

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_123`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 92
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `15` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 14 | START | 15 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 14 | START | 15 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 14 | START | 15 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 14 | START | 15 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 14 | START | 15 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 14 | START | 15 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 14 | START | 15 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 14 | START | 15 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 14 | START | 15 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 14 | START | 15 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 14 | START | 15 | 114 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 111 | START | 111 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `16` | `16` | 114 | START | 114 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `18` | 114 | START | 123 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 114 | START | 114 | 129 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `20` | 114 | START | 114 | 202 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 114 | START | 114 | 120 |
| ✅ EXACT | `Action_SplitBlock` | TE | `6` | `6` | 115 | START | 115 | 158 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 122 | END | 111 | 122 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `13` | 133 | START | 133 | 137 |
| ✅ EXACT | `Action_BallCarry` | RB | `15` | `15` | 138 | START | 138 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 202 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 15–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_SnapReceive` | 111 | 122 | 12 | inferred_complete_timeline |
| `Action_None` | 123 | 132 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 133 | 137 | 5 | inferred_complete_timeline |
| `Action_None` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 15–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 137 | 123 | inferred_complete_timeline |
| `Action_BallCarry` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 15–329
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 176 | 66 | inferred_complete_timeline |
| `Action_None` | 202 | 329 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 15–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 329 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 15–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 227 | 117 | inferred_complete_timeline |
| `Action_None` | 229 | 329 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 15–158
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 114 | 100 | inferred_complete_timeline |
| `Action_SplitBlock` | 115 | 158 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 15–284
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 113 | 99 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 202 | 89 | inferred_complete_timeline |
| `Action_None` | 203 | 284 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 15–329
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 113 | 99 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 120 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 135 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 161 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 202 | 15 | inferred_complete_timeline |
| `Action_None` | 203 | 299 | 97 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 311 | 329 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 15–329
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_BallSnap` | 111 | 122 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 129 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 163 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 184 | 12 | inferred_complete_timeline |
| `Action_None` | 226 | 329 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 15–251
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 113 | 99 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 129 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 180 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 185 | 202 | 18 | inferred_complete_timeline |
| `Action_None` | 203 | 251 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 15–329
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 113 | 99 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 150 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 202 | 49 | inferred_complete_timeline |
| `Action_None` | 203 | 286 | 84 | inferred_complete_timeline |
| `Action_None` | 291 | 292 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 305 | 10 | inferred_complete_timeline |
| `Action_None` | 307 | 316 | 10 | inferred_complete_timeline |
| `Action_None` | 318 | 329 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 15–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 158 | 48 | inferred_complete_timeline |
| `Action_None` | 162 | 329 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 15–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 143 | 33 | inferred_complete_timeline |
| `Action_None` | 146 | 176 | 31 | inferred_complete_timeline |
| `Action_None` | 180 | 210 | 31 | inferred_complete_timeline |
| `Action_None` | 212 | 275 | 64 | inferred_complete_timeline |
| `Action_None` | 277 | 329 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 15–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 329 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 15–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 206 | 96 | inferred_complete_timeline |
| `Action_None` | 216 | 262 | 47 | inferred_complete_timeline |
| `Action_None` | 264 | 329 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 15–162
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 162 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 15–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 329 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 15–301
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 158 | 48 | inferred_complete_timeline |
| `Action_None` | 160 | 169 | 10 | inferred_complete_timeline |
| `Action_None` | 172 | 235 | 64 | inferred_complete_timeline |
| `Action_None` | 238 | 280 | 43 | inferred_complete_timeline |
| `Action_None` | 300 | 301 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 15–329
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 170 | 60 | inferred_complete_timeline |
| `Action_None` | 192 | 195 | 4 | inferred_complete_timeline |
| `Action_None` | 204 | 227 | 24 | inferred_complete_timeline |
| `Action_None` | 230 | 291 | 62 | inferred_complete_timeline |
| `Action_None` | 293 | 308 | 16 | inferred_complete_timeline |
| `Action_None` | 312 | 313 | 2 | inferred_complete_timeline |
| `Action_None` | 315 | 329 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 15–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 299 | 189 | inferred_complete_timeline |
| `Action_None` | 301 | 329 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 15–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 329 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 15–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 111 | 329 | 219 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 161–329 | 143 | 4 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 204–207 | 4 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 223–225 | 3 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 235–329 | 95 | 1 | Undefined position; Undefined team |
| `26` | `41` | Position_Unknown | Team_Unknown | 249–329 | 81 | 1 | Undefined position; Undefined team |
| `27` | `43` | Position_Unknown | Team_Unknown | 256–264 | 9 | 1 | Undefined position; Undefined team |
| `28` | `46` | Position_Unknown | Team_Unknown | 274–329 | 56 | 1 | Undefined position; Undefined team |
| `29` | `49` | Position_Unknown | Team_Unknown | 283–302 | 20 | 1 | Undefined position; Undefined team |
| `30` | `51` | Position_Unknown | Team_Unknown | 290–293 | 4 | 1 | Undefined position; Undefined team |
| `31` | `54` | Position_Unknown | Team_Unknown | 319–324 | 5 | 2 | Undefined position; Undefined team |
| `32` | `55` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (9 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [111–122], lower_priority='Action_ZoneBlock' annotated_start=114, effective_Action_ZoneBlock_start=123.
- ⚠️ Action 'Action_None' range [111-176] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-227] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-162] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-235] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-280] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [115-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-206] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-262] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-291] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-308] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-275] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-202] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-286] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-305] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-316] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-129] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-163] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-171] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-184] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-146] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [149-151] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [185-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-251] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-284] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-135] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-181] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-299] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-294] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-326] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-329] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-264] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-302] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '31' has 1 frames without a visible bounding box.
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

</details>