# Play-Annotation-Generator Annotation Review — SplitZone_244

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_244`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 34
- **Ball Tracks:** 1
- **Action Segments:** 104
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 1 | START | 2 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 1 | START | 2 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 1 | START | 2 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 1 | START | 2 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 1 | START | 2 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 1 | START | 2 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 1 | START | 2 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 1 | START | 2 | 154 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 121 | START | 121 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `0` | `0` | 124 | START | 124 | 162 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `11` | `11` | 124 | START | 124 | 154 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `12` | `12` | 124 | START | 136 | 239 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `4` | 124 | START | 124 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `2` | `2` | 129 | START | 129 | 163 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `3` | 135 | END | 121 | 135 |
| ✅ EXACT | `Action_Handoff` | QB | `3` | `3` | 140 | START | 140 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `9` | 155 | START | 155 | 260 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `11` | `11` | 155 | START | 155 | 202 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 239 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 2–278
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 120 | 119 | inferred_complete_timeline |
| `Action_SnapReceive` | 121 | 135 | 15 | inferred_complete_timeline |
| `Action_None` | 136 | 139 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 140 | 154 | 15 | inferred_complete_timeline |
| `Action_None` | 155 | 278 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 2–328
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 154 | 153 | inferred_complete_timeline |
| `Action_BallCarry` | 155 | 260 | 106 | inferred_complete_timeline |
| `Action_BallCarry` | 262 | 328 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 2–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 128 | 127 | inferred_complete_timeline |
| `Action_SplitBlock` | 129 | 163 | 35 | inferred_complete_timeline |
| `Action_SplitBlock` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 172 | 239 | 68 | inferred_complete_timeline |
| `Action_None` | 240 | 329 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 2–323
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 120 | 119 | inferred_complete_timeline |
| `Action_None` | 121 | 184 | 64 | inferred_complete_timeline |
| `Action_None` | 187 | 196 | 10 | inferred_complete_timeline |
| `Action_None` | 204 | 208 | 5 | inferred_complete_timeline |
| `Action_None` | 211 | 214 | 4 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 323 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 2–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 123 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 239 | 116 | inferred_complete_timeline |
| `Action_None` | 240 | 329 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 2–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 120 | 119 | inferred_complete_timeline |
| `Action_BallSnap` | 121 | 135 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 239 | 104 | inferred_complete_timeline |
| `Action_None` | 240 | 300 | 61 | inferred_complete_timeline |
| `Action_None` | 304 | 329 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 2–216
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 123 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 154 | 31 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 155 | 202 | 48 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 204 | 216 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 2–309
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 123 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 162 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 239 | 74 | inferred_complete_timeline |
| `Action_None` | 240 | 240 | 1 | inferred_complete_timeline |
| `Action_None` | 258 | 309 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 2–208
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 120 | 119 | inferred_complete_timeline |
| `Action_None` | 121 | 175 | 55 | inferred_complete_timeline |
| `Action_None` | 178 | 199 | 22 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 208 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 10–147
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 120 | 111 | inferred_complete_timeline |
| `Action_None` | 121 | 125 | 5 | inferred_complete_timeline |
| `Action_None` | 129 | 147 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 2–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 120 | 119 | inferred_complete_timeline |
| `Action_None` | 121 | 125 | 5 | inferred_complete_timeline |
| `Action_None` | 131 | 137 | 7 | inferred_complete_timeline |
| `Action_None` | 140 | 149 | 10 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–172
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 120 | 119 | inferred_complete_timeline |
| `Action_None` | 121 | 131 | 11 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 2–170
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 109 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 170 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 2–165
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 120 | 119 | inferred_complete_timeline |
| `Action_None` | 121 | 135 | 15 | inferred_complete_timeline |
| `Action_None` | 141 | 159 | 19 | inferred_complete_timeline |
| `Action_None` | 161 | 165 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 2–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 120 | 119 | inferred_complete_timeline |
| `Action_None` | 121 | 164 | 44 | inferred_complete_timeline |
| `Action_None` | 174 | 265 | 92 | inferred_complete_timeline |
| `Action_None` | 270 | 329 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 2–329 | 324 | 4 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 122–290 | 169 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 152–225 | 71 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 152–173 | 22 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 158–174 | 17 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 163–329 | 167 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 174–329 | 145 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 174–201 | 9 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 181–329 | 144 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 196–321 | 126 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 203–329 | 127 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 212–329 | 110 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 213–228 | 8 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 225–298 | 74 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 257–329 | 64 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 260–319 | 34 | 4 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 264–275 | 12 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 266–278 | 13 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 326–328 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | 20 | 120 | 82 | 81.2% | 23, 26–27, 36–51 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (C): Annotated start 124 != Inferred start 136
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 490: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (RT) duration 116 frames exceeds threshold 90 frames [start=124, end=239].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (LG) duration 116 frames exceeds threshold 90 frames [start=124, end=239].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 116 frames exceeds threshold 90 frames [start=124, end=239].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [121–135], lower_priority='Action_ZoneBlock' annotated_start=124, effective_Action_ZoneBlock_start=136.
- ⚠️ Action 'Action_ZoneBlock' range [124-162] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '0' starts at frame 240, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [240-240] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-309] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-184] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-323] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [129-163] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [165-166] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-278] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-188] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-164] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-265] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-175] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-199] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [155-260] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [262-328] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-109] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-170] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [155-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [204-216] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-300] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-290] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-174] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-271] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-294] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-311] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-329] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-321] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-254] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-303] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-298] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-300] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-319] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-275] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-278] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>