# Play-Annotation-Generator Annotation Review — Slants0to10_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_17`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_PassBlock` | C | `17` | `17` | 2 | START | 2 | 264 |
| ✅ EXACT | `Action_PassBlock` | LG | `19` | `19` | 2 | START | 2 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 2 | START | 2 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 2 | START | 2 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `3` | `3` | 2 | START | 2 | 94 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 6 | END | 6 | 6 |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | `2` | `2` | 9 | START | 9 | 53 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 43 | START | 43 | 52 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `2` | `2` | 84 | START | 84 | 140 |

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
- **Visible Frames:** 0–120
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 6 | 6 | 1 | inferred_complete_timeline |
| `Action_None` | 7 | 23 | 17 | inferred_complete_timeline |
| `Action_None` | 27 | 42 | 16 | inferred_complete_timeline |
| `Action_ThrowPass` | 43 | 52 | 10 | inferred_complete_timeline |
| `Action_None` | 53 | 120 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 116 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 271 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 313 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 319 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 9 | 53 | 45 | inferred_complete_timeline |
| `Action_None` | 54 | 83 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 84 | 140 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 128 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 329 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 94 | 93 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 134 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 143 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 145 | 329 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–18
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 18 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 264 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 14 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 29 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 33 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 20 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 30 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 47 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 82 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 128 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 138 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 284 | 144 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 272 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 70 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–310
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 310 | 311 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 165 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 328 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 329 | 196 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 43–71 | 16 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 66–329 | 264 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 90–257 | 168 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 111–329 | 162 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 152–158 | 7 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 153–329 | 177 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 207–209 | 3 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 210–211 | 2 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 210–329 | 110 | 2 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 230–231 | 2 | 1 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 288–289 | 2 | 1 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 301–329 | 29 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 302–321 | 12 | 4 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 304–305 | 2 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 323–329 | 7 | 1 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 327–328 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 65 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-298] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-298] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-313] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-319] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-140] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-94] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-134] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [145-329] for track '3' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-165] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-328] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-70] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-272] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-310] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-116] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-271] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-264] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-128] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-18] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-14] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-29] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-33] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-20] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-30] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-82] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-128] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [130-138] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-284] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-49] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-257] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-123] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-158] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-286] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-231] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-289] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-303] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-305] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-309] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-318] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-305] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '39' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>