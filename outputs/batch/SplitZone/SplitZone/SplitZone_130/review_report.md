# Play-Annotation-Generator Annotation Review — SplitZone_130

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_130`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `1` | `1` |
| ✅ EXACT | `Action_BallCarry` | CB1 | defense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 2 | START | 22 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `1` | `Group` | 2 | START | 22 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 2 | START | 22 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 2 | START | 22 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 2 | START | 22 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 2 | START | 22 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 2 | START | 22 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 2 | START | 22 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `8` | `Group` | 2 | START | 22 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 2 | START | 22 | 143 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 141 | START | 141 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `0` | `0` | 144 | START | 144 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `12` | 144 | START | 144 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 144 | START | 151 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `7` | 144 | START | 144 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `9` | 144 | START | 144 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `1` | `1` | 147 | START | 147 | 181 |
| ✅ EXACT | `Action_BallCarry` | CB1 | `2` | `2` | 148 | START | 148 | 196 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 150 | END | 141 | 150 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `18` | 155 | START | 155 | 264 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 242 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 22–264
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 82 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 140 | 53 | inferred_complete_timeline |
| `Action_SnapReceive` | 141 | 150 | 10 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 155 | 264 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 22–177
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 140 | 119 | inferred_complete_timeline |
| `Action_None` | 141 | 177 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 22–314
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 140 | 119 | inferred_complete_timeline |
| `Action_None` | 141 | 314 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 22–294
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 146 | 125 | inferred_complete_timeline |
| `Action_SplitBlock` | 147 | 181 | 35 | inferred_complete_timeline |
| `Action_SplitBlock` | 186 | 242 | 57 | inferred_complete_timeline |
| `Action_None` | 243 | 285 | 43 | inferred_complete_timeline |
| `Action_None` | 287 | 294 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 22–243
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 140 | 119 | inferred_complete_timeline |
| `Action_None` | 141 | 243 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 22–316
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 143 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 189 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 242 | 50 | inferred_complete_timeline |
| `Action_None` | 243 | 308 | 66 | inferred_complete_timeline |
| `Action_None` | 312 | 316 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 22–316
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 143 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 164 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 242 | 74 | inferred_complete_timeline |
| `Action_None` | 243 | 255 | 13 | inferred_complete_timeline |
| `Action_None` | 257 | 260 | 4 | inferred_complete_timeline |
| `Action_None` | 264 | 316 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 22–329
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 140 | 119 | inferred_complete_timeline |
| `Action_BallSnap` | 141 | 150 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 171 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 242 | 69 | inferred_complete_timeline |
| `Action_None` | 243 | 329 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 22–261
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 143 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 174 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 242 | 57 | inferred_complete_timeline |
| `Action_None` | 243 | 261 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 22–329
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 143 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 170 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 181 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 220 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 225 | 242 | 18 | inferred_complete_timeline |
| `Action_None` | 243 | 329 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 22–329
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 140 | 119 | inferred_complete_timeline |
| `Action_None` | 141 | 225 | 85 | inferred_complete_timeline |
| `Action_None` | 239 | 325 | 87 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 22–155
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 140 | 119 | inferred_complete_timeline |
| `Action_None` | 141 | 155 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 22–198
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 129 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 140 | 6 | inferred_complete_timeline |
| `Action_None` | 141 | 144 | 4 | inferred_complete_timeline |
| `Action_None` | 147 | 156 | 10 | inferred_complete_timeline |
| `Action_None` | 189 | 198 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 22–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 140 | 119 | inferred_complete_timeline |
| `Action_None` | 141 | 199 | 59 | inferred_complete_timeline |
| `Action_None` | 204 | 263 | 60 | inferred_complete_timeline |
| `Action_None` | 270 | 329 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 22–238
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 140 | 119 | inferred_complete_timeline |
| `Action_None` | 141 | 238 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 22–196
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 147 | 126 | inferred_complete_timeline |
| `Action_BallCarry` | 148 | 196 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 22–237
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 140 | 119 | inferred_complete_timeline |
| `Action_None` | 141 | 237 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 22–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 140 | 119 | inferred_complete_timeline |
| `Action_None` | 141 | 239 | 99 | inferred_complete_timeline |
| `Action_None` | 243 | 329 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 22–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 140 | 119 | inferred_complete_timeline |
| `Action_None` | 141 | 329 | 189 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 161–268 | 84 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 175–222 | 48 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 192–252 | 61 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 210–217 | 8 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 225–329 | 105 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 232–329 | 98 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 250–329 | 78 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 277–279 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (5 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (LT) duration 99 frames exceeds threshold 90 frames [start=144, end=242].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RG) duration 99 frames exceeds threshold 90 frames [start=144, end=242].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 99 frames exceeds threshold 90 frames [start=144, end=242].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (LG) duration 99 frames exceeds threshold 90 frames [start=144, end=242].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 99 frames exceeds threshold 90 frames [start=144, end=242].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [141–150], lower_priority='Action_ZoneBlock' annotated_start=144, effective_Action_ZoneBlock_start=151.
- ⚠️ Action 'Action_ZoneBlock' range [144-189] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-308] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-316] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [147-181] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [186-242] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-285] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-294] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [148-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-177] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-325] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-263] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-243] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-261] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-314] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-170] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [176-181] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-185] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-237] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-255] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-316] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-238] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-155] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-171] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-242] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [155-264] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-215] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-268] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-222] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-252] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-217] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '27' has 1 frames without a visible bounding box.
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

</details>