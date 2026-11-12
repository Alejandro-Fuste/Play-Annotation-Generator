# Play-Annotation-Generator Annotation Review — SplitZone_132

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_132`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 138
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT | defense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 64 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 137 |
| ✅ EXACT | `Action_BallSnap` | DT | `6` | `6` | 138 | START | 138 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `1` | 141 | START | 141 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 141 | START | 141 | 224 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `4` | 141 | START | 141 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `5` | 141 | START | 141 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `3` | `3` | 148 | START | 148 | 286 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 153 | END | 138 | 153 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 159 | START | 159 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `16` | `15` | 174 | START | 174 | 179 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 306 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_SnapReceive` | 138 | 153 | 16 | inferred_complete_timeline |
| `Action_None` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 159 | 173 | 15 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_SplitBlock` | 148 | 286 | 139 | inferred_complete_timeline |
| `Action_SplitBlock` | 289 | 306 | 18 | inferred_complete_timeline |
| `Action_None` | 307 | 321 | 15 | inferred_complete_timeline |
| `Action_None` | 324 | 325 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 153 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 169 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 236 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 243 | 254 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 256 | 277 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 163 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 64–309
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 64 | 81 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 140 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 224 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 233 | 247 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 250 | 306 | 57 | inferred_complete_timeline |
| `Action_None` | 307 | 309 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 162 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 218 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 169 | 32 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 224 | 47 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 66 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 122 | 48 | inferred_complete_timeline |
| `Action_None` | 174 | 212 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–288
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 137 | 41 | inferred_complete_timeline |
| `Action_BallSnap` | 138 | 153 | 16 | inferred_complete_timeline |
| `Action_None` | 154 | 227 | 74 | inferred_complete_timeline |
| `Action_None` | 230 | 288 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 237 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 172 | 35 | inferred_complete_timeline |
| `Action_None` | 180 | 329 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 25–206
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 64 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 82 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 105 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 137 | 31 | inferred_complete_timeline |
| `Action_None` | 138 | 206 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–103 | 66 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 26–190 | 136 | 6 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 157–283 | 127 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 159–329 | 150 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 159–327 | 142 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 166–180 | 15 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 167–175 | 9 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 176–210 | 24 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 179–202 | 24 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 205–329 | 120 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 211–329 | 88 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 220–265 | 25 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 229–329 | 98 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 232–329 | 98 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 236–288 | 48 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 239–329 | 87 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 248–328 | 65 | 4 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 253–294 | 37 | 4 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 259–329 | 71 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 260–274 | 10 | 2 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 264–329 | 66 | 1 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 271–329 | 59 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 282–329 | 42 | 3 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 284–329 | 46 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 313–329 | 17 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 317–329 | 13 | 1 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 323–329 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 137 frames exceeds threshold 90 frames [start=141, end=277].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 166 frames exceeds threshold 90 frames [start=141, end=306].
- ⚠️ Action 'Action_None' range [138-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-236] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [243-254] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [256-277] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [148-286] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-321] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-163] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [198-218] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-227] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-288] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-66] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-212] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-237] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-64] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-82] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-105] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-206] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-99] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-153] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-190] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-224] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [233-247] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-283] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [174-179] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [200-235] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-281] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-327] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-182] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-202] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-275] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-260] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-284] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-239] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-262] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-268] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-251] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-276] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-298] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-315] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-328] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-278] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-274] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-312] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-329] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>