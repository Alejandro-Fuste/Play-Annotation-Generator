# Play-Annotation-Generator Annotation Review — Counter_132

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_132`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | TE | offense | `14` | `13` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 170 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 166 | START | 166 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `1` | `0` | 168 | START | 168 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 168 | START | 182 | 185 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | TE | `14` | `13` | 168 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | RG | `8` | `7` | 168 | START | 168 | 244 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `14` | `13` | 168 | START | 168 | 245 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `9` | `8` | 171 | START | 171 | 218 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 181 | END | 166 | 181 |
| ✅ EXACT | `Action_Handoff` | QB | `3` | `2` | 200 | START | 200 | 220 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `8` | 221 | START | 221 | 261 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 273 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_SnapReceive` | 166 | 181 | 16 | inferred_complete_timeline |
| `Action_None` | 182 | 199 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 200 | 220 | 21 | inferred_complete_timeline |
| `Action_None` | 221 | 329 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 171 | 218 | 48 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 220 | 220 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 221 | 261 | 41 | inferred_complete_timeline |
| `Action_BallCarry` | 263 | 324 | 62 | inferred_complete_timeline |
| `Action_BallCarry` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 168 | 245 | 78 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 249 | 273 | 25 | inferred_complete_timeline |
| `Action_None` | 274 | 290 | 17 | inferred_complete_timeline |
| `Action_None` | 302 | 329 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_DownBlock` | 168 | 205 | 38 | inferred_complete_timeline |
| `Action_DownBlock` | 207 | 221 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 224 | 228 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 235 | 265 | 31 | inferred_complete_timeline |
| `Action_None` | 298 | 329 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 220 | 55 | inferred_complete_timeline |
| `Action_None` | 223 | 255 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_BallSnap` | 166 | 181 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 182 | 185 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 207 | 213 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PullBlock` | 168 | 244 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 171 | 6 | inferred_complete_timeline |
| `Action_None` | 174 | 229 | 56 | inferred_complete_timeline |
| `Action_None` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_None` | 242 | 329 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 232 | 67 | inferred_complete_timeline |
| `Action_None` | 241 | 243 | 3 | inferred_complete_timeline |
| `Action_None` | 246 | 329 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 233 | 68 | inferred_complete_timeline |
| `Action_None` | 235 | 308 | 74 | inferred_complete_timeline |
| `Action_None` | 311 | 329 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 260 | 95 | inferred_complete_timeline |
| `Action_None` | 262 | 266 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 284 | 119 | inferred_complete_timeline |
| `Action_None` | 299 | 329 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 329 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | Position_Unknown | Team_Unknown | 20–196 | 146 | 7 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 27–210 | 87 | 8 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 45–329 | 284 | 3 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 126–301 | 176 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 192–289 | 97 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 196–250 | 55 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 219–250 | 24 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 250–329 | 60 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 260–311 | 36 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 270–329 | 60 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 272–326 | 53 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 275–329 | 55 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 277–329 | 42 | 6 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 294–329 | 36 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 303–329 | 26 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 307–329 | 21 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 312–329 | 3 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 317–329 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `14` (TE)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '0' (LT) duration 106 frames exceeds threshold 90 frames [start=168, end=273].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [166–181], lower_priority='Action_DownBlock' annotated_start=168, effective_Action_DownBlock_start=182.
- ⚠️ Overlapping action conflict at frame 168 for track '13': 'Action_DownBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
- ⚠️ Action 'Action_DownBlock' range [168-205] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [207-221] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [224-228] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [235-265] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-232] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-233] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-308] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-260] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [168-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [171-218] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [221-261] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [263-324] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [327-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-284] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-220] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-255] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [182-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [207-213] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-229] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [168-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [249-273] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-290] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-35] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-42] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-105] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-90] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-320] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-301] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-276] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-289] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-250] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-238] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-258] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-273] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-283] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-311] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-321] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-301] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-313] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '30' has 1 frames without a visible bounding box.
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

</details>