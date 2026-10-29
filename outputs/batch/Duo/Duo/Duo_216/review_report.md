# Play-Annotation-Generator Annotation Review — Duo_216

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_216`
- **Frame Range:** 0 to 324 (325 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 324
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 25
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `26` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `30` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `31` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | WR3 | offense | `30` | `24` |
| ✅ EXACT | `Action_ComboBlock` | LT | offense | `8` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 17 | START | 17 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 17 | START | 17 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 17 | START | 17 | 270 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `23` | `Group` | 17 | START | 17 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `24` | `Group` | 17 | START | 17 | 270 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `25` | `Group` | 17 | START | 17 | 324 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `26` | `Group` | 17 | START | 19 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `30` | `Group` | 17 | START | 60 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `31` | `Group` | 17 | START | 123 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 17 | START | 17 | 251 |
| ✅ EXACT | `Action_ComboBlock` | WR3 | `30` | `24` | 252 | START | 252 | 282 |
| ✅ EXACT | `Action_ComboBlock` | LT | `8` | `5` | 252 | START | 252 | 285 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 285 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `25`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 17–324
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 324 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 17–306
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 268 | 252 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 306 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `31`</summary>

- **xml_track_id:** `25`
- **actor_track_id:** `31`
- **team_side:** `offense`
- **Visible Frames:** 123–240
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 123 | 195 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 205 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 212 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 240 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `23`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 17–324
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 54 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 75 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 95 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 324 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `30`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `30`
- **team_side:** `offense`
- **Visible Frames:** 60–282
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 60 | 77 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 251 | 172 | inferred_complete_timeline |
| `Action_ComboBlock` | 252 | 282 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 17–324
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 251 | 235 | inferred_complete_timeline |
| `Action_ComboBlock` | 252 | 285 | 34 | inferred_complete_timeline |
| `Action_None` | 286 | 294 | 9 | inferred_complete_timeline |
| `Action_None` | 305 | 324 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `24`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 17–324
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 270 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 277 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 310 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 324 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 17–296
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 270 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 296 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `26`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `26`
- **team_side:** `offense`
- **Visible Frames:** 19–324
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 22 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 218 | 174 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 324 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 17–324
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 38 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 324 | 284 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 17–324
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 324 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 17–324
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 324 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `22`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 17–244
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 244 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 17–240
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 240 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 17–324
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 256 | 240 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 324 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 17–324
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 119 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 291 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 304 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 324 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `15`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 17–324
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 324 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 111 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 203 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 245 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 7–324
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 10 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 324 | 309 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–8 | 9 | 1 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 4–10 | 7 | 1 | Undefined position; Undefined team |
| `4` | `7` | Position_Unknown | Team_Unknown | 15–16 | 2 | 1 | Undefined position; Undefined team |
| `6` | `9` | Position_Unknown | Team_Unknown | 17–43 | 27 | 1 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 17–56 | 39 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 17–37 | 21 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 17–35 | 19 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 176–197 | 19 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 249–324 | 51 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 262–285 | 24 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 291–302 | 12 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 302–324 | 23 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 307–324 | 12 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 318–324 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 53 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 324 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-111] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-245] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-10] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-10] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-251] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-294] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-324] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-43] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-38] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-324] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-268] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-306] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-119] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-291] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-304] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-256] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-324] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-324] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-37] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-270] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-296] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-35] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-240] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-244] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-75] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-95] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-270] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-277] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-310] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-324] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-22] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-218] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-77] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [252-282] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-195] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-240] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-183] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-290] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-285] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-302] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-311] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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