# Play-Annotation-Generator Annotation Review — SplitZone_219

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_219`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 145
- **Validation Warnings:** 142
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 126
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB2 | defense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SplitBlock` | WR3 | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | offense | `21` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 26 | START | 29 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 26 | START | 29 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 26 | START | 29 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 26 | START | 29 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 26 | START | 29 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 26 | START | 29 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 26 | START | 29 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 26 | START | 29 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 26 | START | 29 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 26 | START | 29 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 26 | START | 29 | 137 |
| ✅ EXACT | `Action_BallSnap` | CB2 | `9` | `9` | 127 | START | 127 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `10` | 130 | START | 130 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `14` | 130 | START | 130 | 185 |
| ✅ EXACT | `Action_ZoneBlock` | C | `17` | `17` | 130 | START | 130 | 290 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `18` | 130 | START | 130 | 290 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `21` | `21` | 130 | START | N/A | N/A |
| ✅ EXACT | `Action_SplitBlock` | WR3 | `8` | `8` | 138 | START | 138 | 245 |
| ✅ EXACT | `Action_SnapReceive` | RG | `21` | `21` | 143 | END | 127 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | `21` | `21` | 164 | START | 164 | 259 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 290 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 29–359
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 157 | 31 | inferred_complete_timeline |
| `Action_None` | 162 | 185 | 24 | inferred_complete_timeline |
| `Action_None` | 189 | 207 | 19 | inferred_complete_timeline |
| `Action_None` | 220 | 225 | 6 | inferred_complete_timeline |
| `Action_None` | 228 | 234 | 7 | inferred_complete_timeline |
| `Action_None` | 238 | 359 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 29–359
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 200 | 74 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |
| `Action_None` | 214 | 219 | 6 | inferred_complete_timeline |
| `Action_None` | 224 | 231 | 8 | inferred_complete_timeline |
| `Action_None` | 234 | 298 | 65 | inferred_complete_timeline |
| `Action_None` | 300 | 317 | 18 | inferred_complete_timeline |
| `Action_None` | 328 | 330 | 3 | inferred_complete_timeline |
| `Action_None` | 332 | 334 | 3 | inferred_complete_timeline |
| `Action_None` | 336 | 359 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 29–306
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 255 | 129 | inferred_complete_timeline |
| `Action_None` | 269 | 302 | 34 | inferred_complete_timeline |
| `Action_None` | 304 | 306 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 29–203
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 156 | 30 | inferred_complete_timeline |
| `Action_None` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 203 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 29–245
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 137 | 109 | inferred_complete_timeline |
| `Action_SplitBlock` | 138 | 245 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 29–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 330 | 204 | inferred_complete_timeline |
| `Action_None` | 333 | 359 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 29–359
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 129 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 154 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 178 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 185 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 217 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 228 | 235 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 240 | 266 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 277 | 290 | 14 | inferred_complete_timeline |
| `Action_None` | 291 | 359 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 29–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 129 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 290 | 161 | inferred_complete_timeline |
| `Action_None` | 291 | 359 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 29–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 129 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 290 | 161 | inferred_complete_timeline |
| `Action_None` | 291 | 359 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 29–316
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_SnapReceive` | 127 | 143 | 17 | inferred_complete_timeline |
| `Action_None` | 144 | 156 | 13 | inferred_complete_timeline |
| `Action_None` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 164 | 259 | 96 | inferred_complete_timeline |
| `Action_BallCarry` | 265 | 286 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 293 | 316 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 29–359
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 129 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 185 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 213 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 290 | 73 | inferred_complete_timeline |
| `Action_None` | 291 | 359 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 29–297
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 297 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 29–209
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 209 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 29–359
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 320 | 194 | inferred_complete_timeline |
| `Action_None` | 323 | 330 | 8 | inferred_complete_timeline |
| `Action_None` | 334 | 359 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 29–311
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 311 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 29–280
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 186 | 60 | inferred_complete_timeline |
| `Action_None` | 188 | 231 | 44 | inferred_complete_timeline |
| `Action_None` | 239 | 241 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 274 | 32 | inferred_complete_timeline |
| `Action_None` | 277 | 280 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 29–211
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 165 | 39 | inferred_complete_timeline |
| `Action_None` | 168 | 192 | 25 | inferred_complete_timeline |
| `Action_None` | 197 | 211 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 29–359
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 318 | 192 | inferred_complete_timeline |
| `Action_None` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_None` | 324 | 326 | 3 | inferred_complete_timeline |
| `Action_None` | 328 | 359 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 29–359
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 173 | 47 | inferred_complete_timeline |
| `Action_None` | 178 | 186 | 9 | inferred_complete_timeline |
| `Action_None` | 188 | 207 | 20 | inferred_complete_timeline |
| `Action_None` | 220 | 225 | 6 | inferred_complete_timeline |
| `Action_None` | 228 | 234 | 7 | inferred_complete_timeline |
| `Action_None` | 236 | 336 | 101 | inferred_complete_timeline |
| `Action_None` | 342 | 359 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 29–359
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_BallSnap` | 127 | 143 | 17 | inferred_complete_timeline |
| `Action_None` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 231 | 28 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 253 | 17 | inferred_complete_timeline |
| `Action_None` | 276 | 320 | 45 | inferred_complete_timeline |
| `Action_None` | 334 | 359 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 29–181
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 148 | 22 | inferred_complete_timeline |
| `Action_None` | 150 | 181 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 29–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 126 | 98 | inferred_complete_timeline |
| `Action_None` | 127 | 359 | 233 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 201–276 | 11 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 201–335 | 94 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 244–339 | 82 | 9 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 275–359 | 85 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 277–298 | 22 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 278–313 | 36 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 289–293 | 5 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 297–355 | 36 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 312–358 | 37 | 6 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 317–359 | 43 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 317–359 | 33 | 3 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 319–330 | 6 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 319–322 | 4 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 335–359 | 25 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 348–359 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (8 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (RG)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 106 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (LT) duration 161 frames exceeds threshold 90 frames [start=130, end=290].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RT) duration 161 frames exceeds threshold 90 frames [start=130, end=290].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (C) duration 161 frames exceeds threshold 90 frames [start=130, end=290].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LG) duration 161 frames exceeds threshold 90 frames [start=130, end=290].
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=130, end=126. Clamping end to start.
- ⚠️ Action 'Action_None' range [127-255] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-302] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-209] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-311] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-330] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-203] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-186] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-231] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-274] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-320] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-330] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [138-245] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-231] for track '9' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-320] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [224-225] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [228-235] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [240-266] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-207] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-336] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-318] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-185] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [218-290] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-192] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-211] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-185] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-207] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-359] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-290] for track '18' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-181] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-219] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-231] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-298] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-317] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-334] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-156] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [164-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [265-286] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [293-316] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-208] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-330] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-273] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-318] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-330] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-339] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-359] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-298] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-313] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-293] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-339] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-355] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-326] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-347] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-358] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-359] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '34' has 2 frames without a visible bounding box.
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

</details>