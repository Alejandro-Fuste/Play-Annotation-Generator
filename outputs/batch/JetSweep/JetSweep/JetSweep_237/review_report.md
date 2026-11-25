# Play-Annotation-Generator Annotation Review — JetSweep_237

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_237`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 135
- **Validation Warnings:** 150
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `1` | `0` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | RB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 77 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `1` | `0` | 49 | START | 49 | 102 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 78 | START | 78 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `5` | `4` | 79 | START | 79 | 215 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `11` | 79 | START | 79 | 241 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `16` | `15` | 79 | START | 79 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 79 | START | 92 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 79 | START | 79 | 134 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 79 | START | 79 | 241 |
| ✅ EXACT | `Action_SnapReceive` | RB | `7` | `6` | 91 | END | 78 | 91 |
| ✅ EXACT | `Action_Toss` | RB | `7` | `6` | 98 | START | 98 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `1` | `0` | 103 | START | 103 | 204 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 241 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 176 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_SnapReceive` | 78 | 91 | 14 | inferred_complete_timeline |
| `Action_None` | 92 | 97 | 6 | inferred_complete_timeline |
| `Action_Toss` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_None` | 103 | 238 | 136 | inferred_complete_timeline |
| `Action_None` | 241 | 318 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_JetMotion` | 49 | 102 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 204 | 102 | inferred_complete_timeline |
| `Action_BallCarry` | 208 | 211 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 231 | 154 | inferred_complete_timeline |
| `Action_None` | 240 | 329 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 243 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_LeadBlock` | 79 | 215 | 137 | inferred_complete_timeline |
| `Action_LeadBlock` | 218 | 219 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 241 | 163 | inferred_complete_timeline |
| `Action_None` | 242 | 296 | 55 | inferred_complete_timeline |
| `Action_None` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_None` | 306 | 311 | 6 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 134 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 241 | 101 | inferred_complete_timeline |
| `Action_None` | 242 | 329 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_BallSnap` | 78 | 91 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 103 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 116 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 241 | 124 | inferred_complete_timeline |
| `Action_None` | 242 | 329 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 241 | 163 | inferred_complete_timeline |
| `Action_None` | 242 | 329 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 131 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 241 | 109 | inferred_complete_timeline |
| `Action_None` | 242 | 255 | 14 | inferred_complete_timeline |
| `Action_None` | 257 | 267 | 11 | inferred_complete_timeline |
| `Action_None` | 269 | 275 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 112 | 35 | inferred_complete_timeline |
| `Action_None` | 117 | 329 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 207 | 130 | inferred_complete_timeline |
| `Action_None` | 221 | 257 | 37 | inferred_complete_timeline |
| `Action_None` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 127 | 50 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 296 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 298 | 221 | inferred_complete_timeline |
| `Action_None` | 300 | 329 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 116 | 39 | inferred_complete_timeline |
| `Action_None` | 123 | 260 | 138 | inferred_complete_timeline |
| `Action_None` | 265 | 329 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 97 | 20 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 199 | 96 | inferred_complete_timeline |
| `Action_None` | 205 | 311 | 107 | inferred_complete_timeline |
| `Action_None` | 322 | 323 | 2 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 329 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 199 | 122 | inferred_complete_timeline |
| `Action_None` | 204 | 329 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 196 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 224 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 177 | 100 | inferred_complete_timeline |
| `Action_None` | 180 | 202 | 23 | inferred_complete_timeline |
| `Action_None` | 205 | 216 | 12 | inferred_complete_timeline |
| `Action_None` | 228 | 239 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 85–144 | 13 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 162–164 | 3 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 179–182 | 4 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 200–319 | 118 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 209–294 | 65 | 7 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 216–259 | 43 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 237–240 | 4 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 242–251 | 10 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 244–271 | 18 | 4 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 253–329 | 64 | 3 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 258–262 | 5 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 267–329 | 56 | 2 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 276–277 | 2 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 278–280 | 3 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 280–282 | 3 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 285–308 | 16 | 4 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 289–329 | 31 | 2 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 291–329 | 35 | 4 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 301–329 | 27 | 2 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 304–324 | 13 | 3 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 324–329 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF3` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 98 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '4' (TE) duration 141 frames exceeds threshold 90 frames [start=79, end=219].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 163 frames exceeds threshold 90 frames [start=79, end=241].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (RG) duration 163 frames exceeds threshold 90 frames [start=79, end=241].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RT) duration 163 frames exceeds threshold 90 frames [start=79, end=241].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (C) duration 163 frames exceeds threshold 90 frames [start=79, end=241].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [78–91], lower_priority='Action_ZoneBlock' annotated_start=79, effective_Action_ZoneBlock_start=92.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LG) duration 163 frames exceeds threshold 90 frames [start=79, end=241].
- ⚠️ Action 'Action_BallCarry' range [103-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [208-211] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-231] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-243] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-199] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [79-215] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [218-219] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-296] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-311] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-238] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-318] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-127] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-296] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-176] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-224] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-196] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-116] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-260] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-241] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-255] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-267] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-275] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-177] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-202] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-216] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-241] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-298] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-199] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-311] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-257] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-312] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-266] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-285] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-256] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-251] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-262] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-261] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-291] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-305] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-294] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-302] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-313] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-326] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-311] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-329] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-307] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-324] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '43' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.

</details>