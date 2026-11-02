# Play-Annotation-Generator Annotation Review — JetSweep_235

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_235`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 131
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 104
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Toss` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 122 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `3` | `2` | 88 | START | 88 | 148 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 121 | START | 121 | 132 |
| ✅ EXACT | `Action_LeadBlock` | TE | `7` | `6` | 123 | START | 123 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 123 | START | 137 | 142 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 123 | START | 123 | 165 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `13` | 123 | START | 123 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `16` | 123 | START | 123 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `22` | `21` | 123 | START | 123 | 165 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 132 | END | 121 | 132 |
| ✅ EXACT | `Action_Toss` | QB | `4` | `3` | 141 | START | 141 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `3` | `2` | 149 | START | 149 | 288 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 165 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_SnapReceive` | 121 | 132 | 12 | inferred_complete_timeline |
| `Action_None` | 133 | 140 | 8 | inferred_complete_timeline |
| `Action_Toss` | 141 | 148 | 8 | inferred_complete_timeline |
| `Action_None` | 149 | 329 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 165 | 45 | inferred_complete_timeline |
| `Action_None` | 168 | 201 | 34 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 305 | 90 | inferred_complete_timeline |
| `Action_None` | 310 | 329 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 305 | 185 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 317 | 329 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_JetMotion` | 88 | 148 | 61 | inferred_complete_timeline |
| `Action_BallCarry` | 149 | 288 | 140 | inferred_complete_timeline |
| `Action_BallCarry` | 290 | 291 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 302 | 182 | inferred_complete_timeline |
| `Action_None` | 306 | 316 | 11 | inferred_complete_timeline |
| `Action_None` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_LeadBlock` | 123 | 165 | 43 | inferred_complete_timeline |
| `Action_None` | 166 | 329 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 165 | 43 | inferred_complete_timeline |
| `Action_None` | 166 | 173 | 8 | inferred_complete_timeline |
| `Action_None` | 186 | 190 | 5 | inferred_complete_timeline |
| `Action_None` | 192 | 197 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 165 | 43 | inferred_complete_timeline |
| `Action_None` | 166 | 175 | 10 | inferred_complete_timeline |
| `Action_None` | 195 | 205 | 11 | inferred_complete_timeline |
| `Action_None` | 208 | 217 | 10 | inferred_complete_timeline |
| `Action_None` | 221 | 317 | 97 | inferred_complete_timeline |
| `Action_None` | 322 | 329 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_BallSnap` | 121 | 132 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 142 | 6 | inferred_complete_timeline |
| `Action_None` | 198 | 277 | 80 | inferred_complete_timeline |
| `Action_None` | 282 | 287 | 6 | inferred_complete_timeline |
| `Action_None` | 293 | 295 | 3 | inferred_complete_timeline |
| `Action_None` | 297 | 327 | 31 | inferred_complete_timeline |
| `Action_None` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 133 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 156 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 186 | 21 | inferred_complete_timeline |
| `Action_None` | 197 | 279 | 83 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 307 | 318 | 12 | inferred_complete_timeline |
| `Action_None` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 142 | 20 | inferred_complete_timeline |
| `Action_None` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_None` | 195 | 202 | 8 | inferred_complete_timeline |
| `Action_None` | 211 | 307 | 97 | inferred_complete_timeline |
| `Action_None` | 309 | 329 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 329 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 165 | 45 | inferred_complete_timeline |
| `Action_None` | 168 | 173 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 279 | 159 | inferred_complete_timeline |
| `Action_None` | 281 | 289 | 9 | inferred_complete_timeline |
| `Action_None` | 291 | 305 | 15 | inferred_complete_timeline |
| `Action_None` | 311 | 329 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 153 | 33 | inferred_complete_timeline |
| `Action_None` | 177 | 188 | 12 | inferred_complete_timeline |
| `Action_None` | 192 | 205 | 14 | inferred_complete_timeline |
| `Action_None` | 208 | 217 | 10 | inferred_complete_timeline |
| `Action_None` | 221 | 329 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 226 | 106 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 248 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 183 | 63 | inferred_complete_timeline |
| `Action_None` | 203 | 208 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 278 | 158 | inferred_complete_timeline |
| `Action_None` | 283 | 286 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 282 | 162 | inferred_complete_timeline |
| `Action_None` | 285 | 329 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 266 | 146 | inferred_complete_timeline |
| `Action_None` | 271 | 274 | 4 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 329 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 228 | 108 | inferred_complete_timeline |
| `Action_None` | 231 | 267 | 37 | inferred_complete_timeline |
| `Action_None` | 278 | 329 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 280 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 171–329 | 129 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 187–190 | 4 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 188–329 | 125 | 8 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 229–266 | 13 | 6 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 250–329 | 68 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 286–329 | 44 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 308–321 | 13 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [121–132], lower_priority='Action_ZoneBlock' annotated_start=123, effective_Action_ZoneBlock_start=133.
- ⚠️ Action 'Action_None' range [121-305] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-165] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-305] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [149-288] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [290-291] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-302] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-316] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-282] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-228] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-267] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-266] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [121-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-142] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-277] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-327] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-205] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-217] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-317] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-280] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-278] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-202] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-307] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-165] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [152-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-186] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-279] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-318] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-226] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-279] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-289] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-305] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-188] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-217] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-329] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-224] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-251] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-290] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-314] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-297] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-329] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-321] for track '29' has 1 frames without a visible bounding box.
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