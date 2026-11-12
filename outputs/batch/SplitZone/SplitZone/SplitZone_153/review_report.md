# Play-Annotation-Generator Annotation Review — SplitZone_153

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_153`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_BlockSecondLevel` | TE2 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 8 | START | 9 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 8 | START | 9 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 8 | START | 9 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 8 | START | 9 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 8 | START | 9 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 8 | START | 9 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 8 | START | 9 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 8 | START | 9 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 8 | START | 9 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 8 | START | 9 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 8 | START | 9 | 114 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 115 | START | 115 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `15` | 118 | START | 118 | 151 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `16` | `16` | 118 | START | 118 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `18` | 118 | START | 130 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `20` | 118 | START | 118 | 152 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `21` | 118 | START | 118 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `3` | `3` | 121 | START | 121 | 160 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 129 | END | 115 | 129 |
| ✅ EXACT | `Action_BlockSecondLevel` | TE2 | `1` | `1` | 139 | START | 139 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `11` | `11` | 164 | START | 164 | 245 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 237 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 9–320
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_SnapReceive` | 115 | 129 | 15 | inferred_complete_timeline |
| `Action_None` | 130 | 163 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 164 | 245 | 82 | inferred_complete_timeline |
| `Action_BallCarry` | 247 | 320 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 148 | 34 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 329 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 9–240
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 240 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 9–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 137 | 23 | inferred_complete_timeline |
| `Action_None` | 140 | 152 | 13 | inferred_complete_timeline |
| `Action_None` | 154 | 329 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 9–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 120 | 112 | inferred_complete_timeline |
| `Action_SplitBlock` | 121 | 160 | 40 | inferred_complete_timeline |
| `Action_SplitBlock` | 163 | 237 | 75 | inferred_complete_timeline |
| `Action_None` | 238 | 242 | 5 | inferred_complete_timeline |
| `Action_None` | 244 | 329 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 9–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 138 | 130 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 139 | 237 | 99 | inferred_complete_timeline |
| `Action_None` | 238 | 329 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 9–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 117 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 151 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 237 | 77 | inferred_complete_timeline |
| `Action_None` | 238 | 263 | 26 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |
| `Action_None` | 273 | 329 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 9–146
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 117 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 146 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 9–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_BallSnap` | 115 | 129 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 137 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 151 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 237 | 77 | inferred_complete_timeline |
| `Action_None` | 238 | 321 | 84 | inferred_complete_timeline |
| `Action_None` | 323 | 324 | 2 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 9–139
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 117 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 139 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 9–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 117 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 152 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 237 | 78 | inferred_complete_timeline |
| `Action_None` | 238 | 329 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 9–151
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 151 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 136 | 22 | inferred_complete_timeline |
| `Action_None` | 140 | 329 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 137 | 23 | inferred_complete_timeline |
| `Action_None` | 140 | 151 | 12 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 186 | 26 | inferred_complete_timeline |
| `Action_None` | 188 | 197 | 10 | inferred_complete_timeline |
| `Action_None` | 204 | 251 | 48 | inferred_complete_timeline |
| `Action_None` | 256 | 290 | 35 | inferred_complete_timeline |
| `Action_None` | 293 | 298 | 6 | inferred_complete_timeline |
| `Action_None` | 301 | 329 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 137 | 23 | inferred_complete_timeline |
| `Action_None` | 140 | 152 | 13 | inferred_complete_timeline |
| `Action_None` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_None` | 163 | 288 | 126 | inferred_complete_timeline |
| `Action_None` | 291 | 312 | 22 | inferred_complete_timeline |
| `Action_None` | 316 | 329 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 158 | 44 | inferred_complete_timeline |
| `Action_None` | 161 | 169 | 9 | inferred_complete_timeline |
| `Action_None` | 171 | 204 | 34 | inferred_complete_timeline |
| `Action_None` | 207 | 215 | 9 | inferred_complete_timeline |
| `Action_None` | 219 | 247 | 29 | inferred_complete_timeline |
| `Action_None` | 249 | 251 | 3 | inferred_complete_timeline |
| `Action_None` | 253 | 280 | 28 | inferred_complete_timeline |
| `Action_None` | 292 | 329 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 151 | 37 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 283 | 123 | inferred_complete_timeline |
| `Action_None` | 286 | 291 | 6 | inferred_complete_timeline |
| `Action_None` | 293 | 329 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 312 | 198 | inferred_complete_timeline |
| `Action_None` | 314 | 324 | 11 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 329 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 152 | 38 | inferred_complete_timeline |
| `Action_None` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_None` | 161 | 329 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 329 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 114 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 290 | 176 | inferred_complete_timeline |
| `Action_None` | 292 | 329 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 148–329 | 174 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 162–324 | 128 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 199–329 | 126 | 5 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 243–252 | 6 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 255–290 | 36 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '1' (TE2) duration 99 frames exceeds threshold 90 frames [start=139, end=237].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LT) duration 120 frames exceeds threshold 90 frames [start=118, end=237].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 120 frames exceeds threshold 90 frames [start=118, end=237].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [115–129], lower_priority='Action_ZoneBlock' annotated_start=118, effective_Action_ZoneBlock_start=130.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 120 frames exceeds threshold 90 frames [start=118, end=237].
- ⚠️ Action 'Action_BlockSecondLevel' for track '1' starts at frame 139, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BlockSecondLevel' range [139-237] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-137] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [121-160] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '3' starts at frame 238, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [238-242] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-148] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-240] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-290] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-329] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-151] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-283] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-329] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-312] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-324] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [164-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [247-320] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-158] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-204] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-215] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-247] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-280] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-186] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-251] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-290] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-298] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-263] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-146] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-151] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-321] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-288] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-312] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-329] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-152] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-139] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-227] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-294] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-329] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-183] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-278] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-286] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-324] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-274] for track '26' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-329] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-290] for track '28' has 1 frames without a visible bounding box.
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

</details>