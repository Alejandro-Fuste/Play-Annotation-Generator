# Play-Annotation-Generator Annotation Review — InsideZoneRead_216

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_216`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 109
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB4 | defense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | CB1 | defense | `11` | `10` |
| ✅ EXACT | `Action_ReadDefender` | CB1 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB1 | defense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `13` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 54 |
| ✅ EXACT | `Action_BallSnap` | CB4 | `12` | `11` | 55 | START | 55 | 68 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `14` | 58 | START | 58 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 58 | START | 58 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 58 | START | 58 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 58 | START | 58 | 72 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 58 | START | 58 | 119 |
| ✅ EXACT | `Action_SnapReceive` | CB1 | `11` | `10` | 68 | END | 55 | 68 |
| ✅ EXACT | `Action_ReadDefender` | CB1 | `11` | `10` | 75 | START | 75 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB1 | `11` | `10` | 104 | START | 104 | 181 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 119 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 80 | 26 | inferred_complete_timeline |
| `Action_None` | 89 | 179 | 91 | inferred_complete_timeline |
| `Action_None` | 181 | 237 | 57 | inferred_complete_timeline |
| `Action_None` | 239 | 303 | 65 | inferred_complete_timeline |
| `Action_None` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 175 | 121 | inferred_complete_timeline |
| `Action_None` | 179 | 246 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 242 | 188 | inferred_complete_timeline |
| `Action_None` | 249 | 294 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 228 | 174 | inferred_complete_timeline |
| `Action_None` | 238 | 317 | 80 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 329 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 329 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 119 | 62 | inferred_complete_timeline |
| `Action_None` | 120 | 329 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 72 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 96 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 76 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–317
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 119 | 62 | inferred_complete_timeline |
| `Action_None` | 120 | 317 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 119 | 62 | inferred_complete_timeline |
| `Action_None` | 120 | 230 | 111 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 329 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 96 | 42 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_None` | 105 | 113 | 9 | inferred_complete_timeline |
| `Action_None` | 116 | 120 | 5 | inferred_complete_timeline |
| `Action_None` | 122 | 263 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 329 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 91 | 37 | inferred_complete_timeline |
| `Action_None` | 93 | 114 | 22 | inferred_complete_timeline |
| `Action_None` | 125 | 129 | 5 | inferred_complete_timeline |
| `Action_None` | 131 | 329 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 215 | 161 | inferred_complete_timeline |
| `Action_None` | 217 | 228 | 12 | inferred_complete_timeline |
| `Action_None` | 232 | 329 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 308 | 254 | inferred_complete_timeline |
| `Action_None` | 316 | 329 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_SnapReceive` | 55 | 68 | 14 | inferred_complete_timeline |
| `Action_None` | 69 | 74 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 75 | 103 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 181 | 78 | inferred_complete_timeline |
| `Action_BallCarry` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 329 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 103 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 329 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_BallSnap` | 55 | 68 | 14 | inferred_complete_timeline |
| `Action_None` | 69 | 329 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 189 | 135 | inferred_complete_timeline |
| `Action_None` | 191 | 216 | 26 | inferred_complete_timeline |
| `Action_None` | 218 | 329 | 112 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 81–83 | 3 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 94–106 | 5 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 102–311 | 203 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 111–329 | 219 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 112–116 | 5 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 123–329 | 189 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 160–238 | 62 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 172–180 | 5 | 2 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 221–317 | 27 | 4 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 227–257 | 12 | 4 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 250–257 | 7 | 2 | Undefined position; Undefined team |
| `33` | `53` | Position_Unknown | Team_Unknown | 255–263 | 9 | 1 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 270–291 | 8 | 2 | Undefined position; Undefined team |
| `35` | `57` | Position_Unknown | Team_Unknown | 273–274 | 2 | 1 | Undefined position; Undefined team |
| `36` | `58` | Position_Unknown | Team_Unknown | 288–289 | 2 | 1 | Undefined position; Undefined team |
| `37` | `61` | Position_Unknown | Team_Unknown | 323–325 | 3 | 1 | Undefined position; Undefined team |
| `38` | `62` | Position_Unknown | Team_Unknown | 326–327 | 2 | 1 | Undefined position; Undefined team |
| `39` | `63` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 71 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [55-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-294] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-228] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-317] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-308] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-329] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-215] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-228] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-103] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-246] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-181] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [194-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-114] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-329] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-237] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-303] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-329] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-113] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-263] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-119] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-317] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-188] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-303] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-311] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-329] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-238] for track '28' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-273] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-282] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-317] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-263] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '38' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_216'; source metadata written as null.

</details>