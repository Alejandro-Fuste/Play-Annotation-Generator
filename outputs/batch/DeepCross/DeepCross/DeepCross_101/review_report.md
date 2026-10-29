# Play-Annotation-Generator Annotation Review — DeepCross_101

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_101`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Completion`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 86
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
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | TE | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_BallCarry` | TE | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `19` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `8` | 23 | START | 23 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `10` | `10` | 26 | START | 26 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `14` | `14` | 26 | START | 26 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `15` | `15` | 26 | START | 26 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 26 | START | 26 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `8` | `8` | 26 | START | 39 | 143 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | TE | `2` | `2` | 38 | START | 38 | 177 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 38 | END | 23 | 38 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 110 | START | 110 | 119 |
| ✅ EXACT | `Action_BallCarry` | TE | `2` | `2` | 184 | START | 184 | 219 |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 38 | 16 | inferred_complete_timeline |
| `Action_None` | 39 | 109 | 71 | inferred_complete_timeline |
| `Action_ThrowPass` | 110 | 119 | 10 | inferred_complete_timeline |
| `Action_None` | 120 | 239 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 38 | 177 | 140 | inferred_complete_timeline |
| `Action_None` | 178 | 183 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 184 | 219 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 143 | 118 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 159 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 162 | 203 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 47 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 81 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 161 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 163 | 186 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 188 | 209 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 23 | 38 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 143 | 105 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 161 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 163 | 186 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 196 | 199 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 48 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 143 | 93 | inferred_complete_timeline |
| `Action_PassBlock` | 147 | 186 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 228 | 237 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 46 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 200 | 153 | inferred_complete_timeline |
| `Action_PassBlock` | 230 | 233 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 127 | 105 | inferred_complete_timeline |
| `Action_None` | 134 | 143 | 10 | inferred_complete_timeline |
| `Action_None` | 147 | 159 | 13 | inferred_complete_timeline |
| `Action_None` | 161 | 239 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 84 | 62 | inferred_complete_timeline |
| `Action_None` | 87 | 134 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 144 | 122 | inferred_complete_timeline |
| `Action_None` | 147 | 159 | 13 | inferred_complete_timeline |
| `Action_None` | 161 | 171 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 103 | 81 | inferred_complete_timeline |
| `Action_None` | 105 | 133 | 29 | inferred_complete_timeline |
| `Action_None` | 136 | 155 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 215 | 193 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 189 | 167 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 4–7 | 4 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 74–78 | 5 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 80–203 | 118 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 108–109 | 2 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 151–239 | 55 | 6 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 174–239 | 65 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 186–203 | 18 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 209–239 | 22 | 3 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 210–211 | 2 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 225–237 | 13 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 233–235 | 3 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [23–38], lower_priority='Action_PassBlock' annotated_start=26, effective_Action_PassBlock_start=39.
- ⚠️ Action 'Action_BallCarry' range [184-219] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-84] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-134] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-215] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-127] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-143] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-161] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [163-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [196-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-200] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [230-233] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-189] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-47] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-81] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-161] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [163-186] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [188-209] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [222-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-143] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-159] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [162-203] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-133] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-155] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [147-186] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [190-191] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [228-237] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-7] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-78] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-159] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-200] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-160] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-206] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-227] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-185] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-237] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '32' has 1 frames without a visible bounding box.
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