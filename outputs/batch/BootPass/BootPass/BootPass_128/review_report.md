# Play-Annotation-Generator Annotation Review — BootPass_128

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_128`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `9` | `9` |
| ⚠️ END CHANGED | `Action_SnapReceive` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_FakeHandoff` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_BootAway` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `4` | `4` |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `43` | `33` |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `39` | `29` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `1` | `1` | 23 | START | 23 | 168 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RG | `12` | `12` | 23 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `13` | `13` | 23 | START | 23 | 163 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | `4` | `4` | 23 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `9` | `9` | 23 | START | 23 | 125 |
| ⚠️ END CHANGED | `Action_SnapReceive` | RG | `12` | `12` | 23 | END | 110 | 110 |
| ✅ EXACT | `Action_FakeHandoff` | RG | `12` | `12` | 47 | START | 47 | 63 |
| ✅ EXACT | `Action_BootAway` | RG | `12` | `12` | 64 | START | 64 | 97 |
| ✅ EXACT | `Action_BallSnap` | C | `4` | `4` | 110 | START | 110 | 110 |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | `43` | `33` | 146 | START | 311 | 311 |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | `39` | `29` | 188 | START | 264 | 264 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 138 | 29 | inferred_complete_timeline |
| `Action_None` | 140 | 158 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 142 | 33 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 151 | 189 | 39 | inferred_complete_timeline |
| `Action_None` | 192 | 230 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 157 | 48 | inferred_complete_timeline |
| `Action_None` | 160 | 163 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_RunBlock` | 23 | 163 | 141 | inferred_complete_timeline |
| `Action_RunBlock` | 170 | 231 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_RunBlock` | 23 | 125 | 103 | inferred_complete_timeline |
| `Action_RunBlock` | 155 | 206 | 52 | inferred_complete_timeline |
| `Action_RunBlock` | 208 | 236 | 29 | inferred_complete_timeline |
| `Action_RunBlock` | 284 | 294 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 109 | 87 | inferred_complete_timeline |
| `Action_BallSnap` | 110 | 110 | 1 | inferred_complete_timeline |
| `Action_None` | 111 | 140 | 30 | inferred_complete_timeline |
| `Action_None` | 145 | 147 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_FakeHandoff` | 47 | 63 | 17 | inferred_complete_timeline |
| `Action_BootAway` | 64 | 97 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 109 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 110 | 110 | 1 | inferred_complete_timeline |
| `Action_None` | 111 | 121 | 11 | inferred_complete_timeline |
| `Action_None` | 139 | 186 | 48 | inferred_complete_timeline |
| `Action_None` | 216 | 227 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_RunBlock` | 23 | 168 | 146 | inferred_complete_timeline |
| `Action_RunBlock` | 174 | 177 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 143 | 34 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 172 | 63 | inferred_complete_timeline |
| `Action_None` | 219 | 223 | 5 | inferred_complete_timeline |
| `Action_None` | 225 | 239 | 15 | inferred_complete_timeline |
| `Action_None` | 245 | 256 | 12 | inferred_complete_timeline |
| `Action_None` | 259 | 300 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 153 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 129 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 227 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 229 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 144 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 4–139 | 136 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 104–199 | 90 | 5 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 129–231 | 77 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 136–230 | 42 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 154–228 | 75 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 161–175 | 15 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 171–220 | 47 | 4 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 180–225 | 43 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 182–223 | 42 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 208–218 | 11 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 230–329 | 100 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 231–329 | 89 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 232–329 | 97 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 233–329 | 95 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 264–329 | 66 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 270–322 | 47 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 275–289 | 12 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 292–329 | 36 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 311–315 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `1` (2 segments found)
- ❌ Missing segment for action `Action_RunBlock` on target `12` (RG)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `13` (2 segments found)
- ❌ Missing segment for action `Action_RunBlock` on target `4` (C)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `9` (4 segments found)
- ⚠️ `Action_ThrowPass` for actor_track_id `43` (Position_Unknown): Annotated start 146 != Inferred start 311
- ⚠️ `Action_SecureCatch` for actor_track_id `39` (Position_Unknown): Annotated start 188 != Inferred start 264

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '4' has invalid range: start=110, end=23. Clamping end to start.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [110–110], lower_priority='Action_RunBlock' annotated_start=23, effective_Action_RunBlock_start=111.
- ⚠️ Overlapping action conflict at frame 23 for track '12': 'Action_RunBlock' vs 'Action_SnapReceive'. Overriding with 'Action_SnapReceive'.
- ⚠️ Segment 'Action_SnapReceive' for track '12' has invalid range: start=110, end=23. Clamping end to start.
- ⚠️ Segment 'Action_SecureCatch' for track '29' has invalid range: start=264, end=194. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '33' has invalid range: start=311, end=154. Clamping end to start.
- ⚠️ Action 'Action_None' range [110-227] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [23-168] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [174-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-157] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-140] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-229] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-239] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-256] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-300] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-153] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [23-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [155-206] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [208-236] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [284-294] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-138] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-158] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-189] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-230] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [23-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [170-231] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-228] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-198] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-225] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-223] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-250] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-245] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-248] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-311] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-322] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-284] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-323] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '33' has 1 frames without a visible bounding box.
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

</details>