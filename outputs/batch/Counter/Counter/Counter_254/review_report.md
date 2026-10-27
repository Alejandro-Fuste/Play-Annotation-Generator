# Play-Annotation-Generator Annotation Review — Counter_254

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_254`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_DownBlock` | LB1 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | OLB2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | offense | `15` | `14` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `18` | `16` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `16` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `15` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 10 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 142 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `19` | `17` | 143 | START | 169 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `12` | `11` | 152 | START | 152 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `16` | `15` | 152 | START | 154 | 162 |
| ✅ EXACT | `Action_DownBlock` | LB1 | `9` | `8` | 152 | START | 152 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | OLB2 | `11` | `10` | 152 | START | 152 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | `15` | `14` | 152 | START | 152 | 209 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `18` | `16` | 153 | END | 143 | 152 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `14` | `13` | 158 | START | 158 | 188 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `16` | 174 | START | 174 | 196 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `14` | `13` | 197 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 236 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 10–243
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 20 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 27 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 40 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 142 | 79 | inferred_complete_timeline |
| `Action_SnapReceive` | 143 | 152 | 10 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_None` | 165 | 171 | 7 | inferred_complete_timeline |
| `Action_None` | 173 | 173 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 174 | 196 | 23 | inferred_complete_timeline |
| `Action_None` | 197 | 243 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 158 | 188 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 152 | 209 | 58 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 216 | 223 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 52 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 84 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 154 | 162 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 164 | 165 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 173 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 188 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 226 | 236 | 11 | inferred_complete_timeline |
| `Action_None` | 237 | 254 | 18 | inferred_complete_timeline |
| `Action_None` | 256 | 329 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–304
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 159 | 17 | inferred_complete_timeline |
| `Action_None` | 161 | 165 | 5 | inferred_complete_timeline |
| `Action_None` | 195 | 225 | 31 | inferred_complete_timeline |
| `Action_None` | 232 | 237 | 6 | inferred_complete_timeline |
| `Action_None` | 251 | 304 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 203 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 178 | 36 | inferred_complete_timeline |
| `Action_None` | 184 | 188 | 5 | inferred_complete_timeline |
| `Action_None` | 242 | 245 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 198 | 56 | inferred_complete_timeline |
| `Action_None` | 205 | 233 | 29 | inferred_complete_timeline |
| `Action_None` | 236 | 241 | 6 | inferred_complete_timeline |
| `Action_None` | 244 | 266 | 23 | inferred_complete_timeline |
| `Action_None` | 270 | 329 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 173 | 22 | inferred_complete_timeline |
| `Action_None` | 248 | 254 | 7 | inferred_complete_timeline |
| `Action_None` | 265 | 268 | 4 | inferred_complete_timeline |
| `Action_None` | 270 | 311 | 42 | inferred_complete_timeline |
| `Action_None` | 314 | 329 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 221 | 79 | inferred_complete_timeline |
| `Action_None` | 239 | 255 | 17 | inferred_complete_timeline |
| `Action_None` | 260 | 267 | 8 | inferred_complete_timeline |
| `Action_None` | 269 | 270 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PullBlock` | 152 | 177 | 26 | inferred_complete_timeline |
| `Action_PullBlock` | 185 | 196 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 198 | 236 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 228 | 86 | inferred_complete_timeline |
| `Action_None` | 232 | 254 | 23 | inferred_complete_timeline |
| `Action_None` | 259 | 269 | 11 | inferred_complete_timeline |
| `Action_None` | 272 | 329 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 16 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 115 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 142 | 20 | inferred_complete_timeline |
| `Action_None` | 143 | 239 | 97 | inferred_complete_timeline |
| `Action_None` | 241 | 296 | 56 | inferred_complete_timeline |
| `Action_None` | 299 | 329 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–266 | 267 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 169–214 | 35 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 169–329 | 161 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 171–329 | 158 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 190–212 | 23 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 195–244 | 34 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 215–329 | 111 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 229–329 | 98 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 234–258 | 20 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 251–314 | 59 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 260–262 | 3 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 261–329 | 69 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 267–303 | 35 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 275–329 | 55 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 308–329 | 22 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 309–329 | 21 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `19` (Position_Unknown): Annotated start 143 != Inferred start 169
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `15` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `14` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 509: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 510: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '13' has invalid range: start=197, end=188. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=169, end=153. Clamping end to start.
- ⚠️ Action 'Action_None' range [143-266] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-221] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-255] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-267] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-178] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-225] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-237] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-304] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-16] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-115] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-296] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [152-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-254] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-311] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-228] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-254] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [152-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [185-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [198-236] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [152-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-188] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-254] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-266] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [158-188] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [152-209] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [216-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-52] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [154-162] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [164-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-20] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-40] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [143-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-243] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-214] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-212] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-224] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-282] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-245] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-314] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-329] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-294] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-303] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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