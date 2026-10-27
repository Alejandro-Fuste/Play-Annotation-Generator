# Play-Annotation-Generator Annotation Review — Counter_255

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_255`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 114
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `24` | `23` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `24` | `23` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 8 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 129 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 130 | START | 130 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `16` | 133 | START | 143 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `20` | `19` | 133 | START | 133 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `24` | `23` | 133 | START | 134 | 135 |
| ✅ EXACT | `Action_PullBlock` | RG | `19` | `18` | 133 | START | 133 | 217 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `1` | `0` | 133 | START | 133 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `21` | `20` | 139 | START | 139 | 197 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 142 | END | 130 | 142 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 162 | START | 162 | 172 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `24` | `23` | 173 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 217 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_SnapReceive` | 130 | 142 | 13 | inferred_complete_timeline |
| `Action_None` | 143 | 161 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 162 | 172 | 11 | inferred_complete_timeline |
| `Action_None` | 173 | 329 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 8–288
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 138 | 131 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 139 | 197 | 59 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 200 | 203 | 4 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 283 | 285 | 3 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 287 | 288 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 199 | 70 | inferred_complete_timeline |
| `Action_None` | 201 | 329 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 329 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 133 | 203 | 71 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 209 | 213 | 5 | inferred_complete_timeline |
| `Action_None` | 226 | 231 | 6 | inferred_complete_timeline |
| `Action_None` | 239 | 245 | 7 | inferred_complete_timeline |
| `Action_None` | 247 | 257 | 11 | inferred_complete_timeline |
| `Action_None` | 266 | 271 | 6 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 278 | 307 | 30 | inferred_complete_timeline |
| `Action_None` | 309 | 314 | 6 | inferred_complete_timeline |
| `Action_None` | 317 | 329 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 329 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 150 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_BallSnap` | 130 | 142 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 143 | 158 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 160 | 175 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 190 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 197 | 217 | 21 | inferred_complete_timeline |
| `Action_None` | 218 | 329 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PullBlock` | 133 | 217 | 85 | inferred_complete_timeline |
| `Action_None` | 218 | 235 | 18 | inferred_complete_timeline |
| `Action_None` | 241 | 329 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 192 | 63 | inferred_complete_timeline |
| `Action_None` | 205 | 329 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 158 | 29 | inferred_complete_timeline |
| `Action_None` | 160 | 178 | 19 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 221 | 92 | inferred_complete_timeline |
| `Action_None` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 219 | 90 | inferred_complete_timeline |
| `Action_None` | 222 | 230 | 9 | inferred_complete_timeline |
| `Action_None` | 232 | 234 | 3 | inferred_complete_timeline |
| `Action_None` | 248 | 252 | 5 | inferred_complete_timeline |
| `Action_None` | 256 | 266 | 11 | inferred_complete_timeline |
| `Action_None` | 268 | 329 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 329 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 250 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 251 | 122 | inferred_complete_timeline |
| `Action_None` | 254 | 264 | 11 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 329 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 329 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 329 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 263 | 134 | inferred_complete_timeline |
| `Action_None` | 268 | 317 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 329 | 200 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 16–184 | 84 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 27–48 | 7 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 91–139 | 21 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 155–162 | 5 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 171–329 | 81 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 172–177 | 6 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 218–329 | 112 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 222–270 | 49 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 230–329 | 60 | 7 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 233–264 | 28 | 4 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 241–329 | 89 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 244–329 | 86 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 258–263 | 6 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 272–273 | 2 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 293–329 | 37 | 1 | Undefined position; Undefined team |
| `36` | `60` | Position_Unknown | Team_Unknown | 309–329 | 21 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `24` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `21` (4 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `24` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [130–142], lower_priority='Action_DownBlock' annotated_start=133, effective_Action_DownBlock_start=143.
- ⚠️ Segment 'Action_BallCarry' for track '23' has invalid range: start=173, end=139. Clamping end to start.
- ⚠️ Action 'Action_PullLeadBlock' range [133-203] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [205-206] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [209-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-257] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-271] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-307] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-314] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-317] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-251] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-264] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-192] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-158] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-250] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-221] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-329] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-219] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-230] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-252] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-266] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [130-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [143-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [160-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [183-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-150] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-158] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [139-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [200-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [283-285] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [287-288] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-18] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-30] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [134-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [138-139] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-176] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-270] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-244] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-275] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-311] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-319] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-263] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '34' has 1 frames without a visible bounding box.
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

</details>