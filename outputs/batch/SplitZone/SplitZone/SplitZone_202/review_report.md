# Play-Annotation-Generator Annotation Review — SplitZone_202

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_202`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `20` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 36 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 18 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `9` | `9` | 143 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `12` | 146 | START | 146 | 200 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `20` | `18` | 146 | START | 154 | 292 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `3` | 146 | START | 146 | 175 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 146 | START | 146 | 233 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 146 | START | 146 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `17` | `17` | 152 | START | 152 | 171 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 160 | END | 143 | 160 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 165 | START | 165 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `11` | 175 | START | 175 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `3` | `3` | 176 | START | 176 | 198 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 312 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_SnapReceive` | 143 | 160 | 18 | inferred_complete_timeline |
| `Action_None` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 165 | 173 | 9 | inferred_complete_timeline |
| `Action_None` | 178 | 184 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 180 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 189 | 216 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 220 | 268 | 49 | inferred_complete_timeline |
| `Action_BallCarry` | 272 | 329 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 36–329
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 49 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 76 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 91 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 100 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 143 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 151 | 7 | inferred_complete_timeline |
| `Action_SplitBlock` | 152 | 171 | 20 | inferred_complete_timeline |
| `Action_SplitBlock` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 180 | 198 | 19 | inferred_complete_timeline |
| `Action_SplitBlock` | 202 | 312 | 111 | inferred_complete_timeline |
| `Action_None` | 313 | 329 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 233 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 200 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 202 | 205 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 154–292
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 154 | 292 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 145 | 104 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 175 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 176 | 198 | 23 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 200 | 264 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 145 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 246 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–307
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 232 | 90 | inferred_complete_timeline |
| `Action_None` | 241 | 307 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 142 | 82 | inferred_complete_timeline |
| `Action_None` | 143 | 239 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 142 | 131 | inferred_complete_timeline |
| `Action_None` | 143 | 220 | 78 | inferred_complete_timeline |
| `Action_None` | 224 | 230 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 10–257
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 56 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 142 | 78 | inferred_complete_timeline |
| `Action_None` | 143 | 148 | 6 | inferred_complete_timeline |
| `Action_None` | 150 | 182 | 33 | inferred_complete_timeline |
| `Action_None` | 184 | 216 | 33 | inferred_complete_timeline |
| `Action_None` | 228 | 257 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 223 | 81 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |
| `Action_None` | 230 | 241 | 12 | inferred_complete_timeline |
| `Action_None` | 249 | 329 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 29–316
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 142 | 114 | inferred_complete_timeline |
| `Action_None` | 143 | 316 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 184 | 42 | inferred_complete_timeline |
| `Action_None` | 193 | 242 | 50 | inferred_complete_timeline |
| `Action_None` | 247 | 255 | 9 | inferred_complete_timeline |
| `Action_None` | 291 | 329 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–5 | 6 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–65 | 66 | 1 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 11–84 | 74 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 176–329 | 136 | 9 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 193–329 | 130 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 224–282 | 59 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 240–261 | 22 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 247–329 | 83 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 248–329 | 82 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 250–253 | 4 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 256–306 | 51 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 256–329 | 70 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 265–268 | 4 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 285–327 | 38 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 290–292 | 3 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 314–329 | 16 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 320–325 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `9` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `20` (C): Annotated start 146 != Inferred start 154
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 101 frames exceeds threshold 90 frames [start=146, end=246].
- ⚠️ Segment 'Action_BallSnap' for track '9' has invalid range: start=143, end=65. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 139 frames exceeds threshold 90 frames [start=154, end=292].
- ⚠️ Action 'Action_None' range [143-223] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-241] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-255] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [176-198] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [200-264] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-145] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-233] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [165-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-246] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-232] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-307] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [175-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [189-216] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [202-205] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-56] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-216] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-257] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-316] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-49] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-143] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [152-171] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [174-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [180-198] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-292] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-274] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-283] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-296] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-315] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-282] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-261] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-306] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-264] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-320] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-325] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>