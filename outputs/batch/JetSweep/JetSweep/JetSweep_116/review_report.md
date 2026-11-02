# Play-Annotation-Generator Annotation Review — JetSweep_116

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_116`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `11` | `10` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 142 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `11` | `10` | 102 | START | 102 | 170 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 143 | START | 143 | 155 |
| ✅ EXACT | `Action_LeadBlock` | RB | `7` | `6` | 145 | START | 145 | 195 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `11` | 145 | START | 145 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `15` | 145 | START | 145 | 161 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `16` | 145 | START | 145 | 160 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `18` | `17` | 145 | START | 156 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 145 | START | 145 | 161 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 155 | END | 143 | 155 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 158 | START | 158 | 170 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `11` | `10` | 171 | START | 171 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 198 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_SnapReceive` | 143 | 155 | 13 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_Toss` | 158 | 170 | 13 | inferred_complete_timeline |
| `Action_None` | 171 | 329 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_LeadBlock` | 145 | 195 | 51 | inferred_complete_timeline |
| `Action_None` | 219 | 273 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_JetMotion` | 102 | 170 | 69 | inferred_complete_timeline |
| `Action_BallCarry` | 171 | 329 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 255 | 113 | inferred_complete_timeline |
| `Action_None` | 260 | 263 | 4 | inferred_complete_timeline |
| `Action_None` | 273 | 275 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 186 | 44 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 195 | 5 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 169 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 170 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 160 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 191 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_BallSnap` | 143 | 155 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_None` | 211 | 329 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 161 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 169 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 161 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 173 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 160 | 18 | inferred_complete_timeline |
| `Action_None` | 168 | 174 | 7 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 200 | 58 | inferred_complete_timeline |
| `Action_None` | 209 | 329 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 161 | 19 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 329 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 160 | 18 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 213 | 32 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 225 | 230 | 6 | inferred_complete_timeline |
| `Action_None` | 238 | 310 | 73 | inferred_complete_timeline |
| `Action_None` | 315 | 319 | 5 | inferred_complete_timeline |
| `Action_None` | 326 | 329 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 169 | 27 | inferred_complete_timeline |
| `Action_None` | 172 | 186 | 15 | inferred_complete_timeline |
| `Action_None` | 197 | 329 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 166 | 24 | inferred_complete_timeline |
| `Action_None` | 168 | 177 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 209 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 237 | 95 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |
| `Action_None` | 244 | 289 | 46 | inferred_complete_timeline |
| `Action_None` | 291 | 293 | 3 | inferred_complete_timeline |
| `Action_None` | 295 | 326 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 191–316 | 78 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 193–329 | 130 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 204–205 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 205–329 | 125 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 208–329 | 122 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 211–329 | 119 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 216–329 | 114 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 216–329 | 114 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 233–329 | 95 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 237–329 | 93 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 242–243 | 2 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 250–294 | 35 | 3 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 271–273 | 3 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 282–303 | 22 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 285–329 | 45 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 294–306 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (C): Annotated start 145 != Inferred start 156
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [143–155], lower_priority='Action_ZoneBlock' annotated_start=145, effective_Action_ZoneBlock_start=156.
- ⚠️ Action 'Action_None' range [143-166] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-177] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-255] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [145-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-273] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-213] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-310] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-237] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-289] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-326] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-161] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-161] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-169] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-160] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-191] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-174] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-231] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-288] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-316] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-266] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-284] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-294] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-303] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '37' has 1 frames without a visible bounding box.
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

</details>