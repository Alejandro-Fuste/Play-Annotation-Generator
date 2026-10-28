# Play-Annotation-Generator Annotation Review — Draw_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_31`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 126
- **Validation Warnings:** 125
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `16` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 62 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 63 | START | 63 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `14` | 66 | START | 79 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `17` | 66 | START | 66 | 109 |
| ✅ EXACT | `Action_PassBlock` | LT | `2` | `1` | 66 | START | 66 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `20` | 66 | START | 66 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `22` | `21` | 66 | START | 66 | 80 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 78 | END | 63 | 78 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `14` | `13` | 82 | START | 82 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `14` | `13` | 106 | START | 106 | 119 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 153 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_SnapReceive` | 63 | 78 | 16 | inferred_complete_timeline |
| `Action_None` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 82 | 105 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 119 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 156 | 165 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 168 | 183 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 186 | 199 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 204 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 294 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 115 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 299 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 292 | 230 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 118 | 56 | inferred_complete_timeline |
| `Action_None` | 143 | 153 | 11 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 153 | 88 | inferred_complete_timeline |
| `Action_None` | 154 | 299 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 109 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 153 | 32 | inferred_complete_timeline |
| `Action_None` | 154 | 160 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_BallSnap` | 63 | 78 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 79 | 89 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 124 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 80 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 153 | 70 | inferred_complete_timeline |
| `Action_None` | 154 | 233 | 80 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_None` | 253 | 255 | 3 | inferred_complete_timeline |
| `Action_None` | 260 | 263 | 4 | inferred_complete_timeline |
| `Action_None` | 269 | 271 | 3 | inferred_complete_timeline |
| `Action_None` | 273 | 281 | 9 | inferred_complete_timeline |
| `Action_None` | 283 | 288 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 93 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 126 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 199 | 137 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 209 | 237 | 29 | inferred_complete_timeline |
| `Action_None` | 248 | 264 | 17 | inferred_complete_timeline |
| `Action_None` | 266 | 286 | 21 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 184 | 122 | inferred_complete_timeline |
| `Action_None` | 186 | 240 | 55 | inferred_complete_timeline |
| `Action_None` | 247 | 299 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 103 | 41 | inferred_complete_timeline |
| `Action_None` | 106 | 191 | 86 | inferred_complete_timeline |
| `Action_None` | 193 | 198 | 6 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_None` | 216 | 264 | 49 | inferred_complete_timeline |
| `Action_None` | 274 | 275 | 2 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_None` | 283 | 297 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 158 | 96 | inferred_complete_timeline |
| `Action_None` | 161 | 166 | 6 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 112 | 50 | inferred_complete_timeline |
| `Action_None` | 115 | 299 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 280 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 180 | 118 | inferred_complete_timeline |
| `Action_None` | 182 | 203 | 22 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 238 | 25 | inferred_complete_timeline |
| `Action_None` | 246 | 266 | 21 | inferred_complete_timeline |
| `Action_None` | 268 | 299 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 219 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 299 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 266 | 204 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 92–299 | 182 | 7 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 113–294 | 146 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 118–141 | 24 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 131–299 | 169 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 135–299 | 165 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 144–265 | 122 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 165–166 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 186–299 | 114 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 191–299 | 106 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 206–277 | 53 | 3 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 207–216 | 8 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 218–299 | 80 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 239–299 | 61 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 285–288 | 4 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 296–298 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 91 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [63–78], lower_priority='Action_PassBlock' annotated_start=66, effective_Action_PassBlock_start=79.
- ⚠️ Action 'Action_None' range [63-115] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-299] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-292] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-294] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-126] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-240] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-264] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-286] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-103] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-191] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-264] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-297] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-299] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-166] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-280] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [156-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [168-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [186-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-204] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [79-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-153] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-266] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-153] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-203] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-238] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-266] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-219] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-93] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-233] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-281] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-288] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-242] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-270] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-282] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-183] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-255] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-264] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-294] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-265] for track '27' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-198] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-299] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-238] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-277] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-267] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '37' has 1 frames without a visible bounding box.
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