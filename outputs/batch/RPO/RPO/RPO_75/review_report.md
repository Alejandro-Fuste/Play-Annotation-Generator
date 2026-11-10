# Play-Annotation-Generator Annotation Review — RPO_75

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_75`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 144
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `0` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 118
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_RunBlock` | C | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_RunBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_PullBall` | RB | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 86 |
| ✅ EXACT | `Action_RunBlock` | C | `16` | `16` | 88 | START | 88 | 93 |
| ⚠️ START CHANGED | `Action_RunBlock` | LG | `19` | `19` | 88 | START | 90 | 147 |
| ✅ EXACT | `Action_RunBlock` | RT | `20` | `20` | 88 | START | 88 | 147 |
| ✅ EXACT | `Action_RunBlock` | RG | `21` | `21` | 88 | START | 88 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `7` | `7` | 88 | START | 88 | 96 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `8` | 94 | START | 94 | 127 |
| ✅ EXACT | `Action_PullBall` | RB | `4` | `4` | 97 | START | 97 | 106 |
| ✅ EXACT | `Action_ThrowPass` | RB | `4` | `4` | 140 | START | 140 | 147 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 93 | 7 | inferred_complete_timeline |
| `Action_ReadDefender` | 94 | 127 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 96 | 10 | inferred_complete_timeline |
| `Action_PullBall` | 97 | 106 | 10 | inferred_complete_timeline |
| `Action_None` | 107 | 139 | 33 | inferred_complete_timeline |
| `Action_ThrowPass` | 140 | 147 | 8 | inferred_complete_timeline |
| `Action_None` | 148 | 278 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 320 | 234 | inferred_complete_timeline |
| `Action_None` | 324 | 328 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 294 | 208 | inferred_complete_timeline |
| `Action_None` | 296 | 308 | 13 | inferred_complete_timeline |
| `Action_None` | 310 | 329 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 329 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 131 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 87 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 96 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 100 | 147 | 48 | inferred_complete_timeline |
| `Action_None` | 148 | 329 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 83 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 90 | 147 | 58 | inferred_complete_timeline |
| `Action_None` | 148 | 195 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 87 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 93 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 87 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 147 | 60 | inferred_complete_timeline |
| `Action_None` | 148 | 276 | 129 | inferred_complete_timeline |
| `Action_None` | 279 | 289 | 11 | inferred_complete_timeline |
| `Action_None` | 292 | 296 | 5 | inferred_complete_timeline |
| `Action_None` | 299 | 308 | 10 | inferred_complete_timeline |
| `Action_None` | 310 | 312 | 3 | inferred_complete_timeline |
| `Action_None` | 314 | 322 | 9 | inferred_complete_timeline |
| `Action_None` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 87 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 147 | 60 | inferred_complete_timeline |
| `Action_None` | 148 | 275 | 128 | inferred_complete_timeline |
| `Action_None` | 280 | 297 | 18 | inferred_complete_timeline |
| `Action_None` | 300 | 312 | 13 | inferred_complete_timeline |
| `Action_None` | 322 | 328 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 138 | 52 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 115 | 29 | inferred_complete_timeline |
| `Action_None` | 117 | 322 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 93 | 7 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 108 | 115 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–288
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 243 | 157 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 262 | 3 | inferred_complete_timeline |
| `Action_None` | 281 | 288 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 151 | 65 | inferred_complete_timeline |
| `Action_None` | 156 | 163 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 117 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 281 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 288 | 202 | inferred_complete_timeline |
| `Action_None` | 298 | 329 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 290 | 204 | inferred_complete_timeline |
| `Action_None` | 294 | 329 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 267 | 181 | inferred_complete_timeline |
| `Action_None` | 269 | 318 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 113 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 111–329 | 217 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 112–207 | 96 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 122–309 | 173 | 6 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 122–270 | 143 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 144–316 | 145 | 5 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 148–262 | 114 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 150–158 | 9 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 154–165 | 4 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 191–329 | 22 | 5 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 191–210 | 19 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 206–329 | 123 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 206–304 | 74 | 5 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 219–221 | 3 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 226–291 | 66 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 231–297 | 61 | 3 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 234–266 | 27 | 4 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 272–288 | 12 | 2 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 280–300 | 13 | 2 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 301–329 | 28 | 2 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 308–313 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_RunBlock` for actor_track_id `19` (LG): Annotated start 88 != Inferred start 90
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 101 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [87-320] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-138] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-294] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-308] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-131] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-278] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [88-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [94-127] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-281] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-322] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-163] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-243] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-288] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-93] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-115] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-267] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-318] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-288] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [88-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-290] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-113] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-195] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-275] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-297] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-312] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-328] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-276] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-289] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-308] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-322] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-276] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-278] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-289] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-309] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-136] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-260] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-290] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-316] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-258] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-158] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-203] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-255] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-329] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-257] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-269] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-304] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-291] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-276] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-288] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-297] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-245] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-262] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-288] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-300] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-317] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-329] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-313] for track '42' has 1 frames without a visible bounding box.
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

</details>