# Play-Annotation-Generator Annotation Review — Counter_121

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_121`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 176 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 173 | START | 173 | 188 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `11` | `10` | 177 | START | 177 | 199 |
| ✅ EXACT | `Action_DownBlock` | LT | `14` | `13` | 177 | START | 177 | 255 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `20` | `19` | 177 | START | 189 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `22` | `21` | 177 | START | 177 | 217 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `9` | `8` | 177 | START | 177 | 261 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 188 | END | 173 | 188 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `18` | 195 | START | 195 | 218 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `18` | `17` | 219 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 261 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–376
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_SnapReceive` | 173 | 188 | 16 | inferred_complete_timeline |
| `Action_None` | 189 | 194 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 195 | 218 | 24 | inferred_complete_timeline |
| `Action_None` | 219 | 376 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 177 | 261 | 85 | inferred_complete_timeline |
| `Action_None` | 262 | 309 | 48 | inferred_complete_timeline |
| `Action_None` | 315 | 389 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_DownBlock` | 177 | 255 | 79 | inferred_complete_timeline |
| `Action_None` | 273 | 389 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_DownBlock` | 177 | 199 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 210 | 261 | 52 | inferred_complete_timeline |
| `Action_None` | 262 | 307 | 46 | inferred_complete_timeline |
| `Action_None` | 309 | 389 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_BallSnap` | 173 | 188 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 219 | 261 | 43 | inferred_complete_timeline |
| `Action_None` | 262 | 389 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 176 | 139 | inferred_complete_timeline |
| `Action_PullBlock` | 177 | 217 | 41 | inferred_complete_timeline |
| `Action_PullBlock` | 220 | 261 | 42 | inferred_complete_timeline |
| `Action_None` | 262 | 389 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–346
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 172 | 154 | inferred_complete_timeline |
| `Action_None` | 173 | 238 | 66 | inferred_complete_timeline |
| `Action_None` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 346 | 102 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 221 | 49 | inferred_complete_timeline |
| `Action_None` | 237 | 245 | 9 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 258 | 389 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 255 | 83 | inferred_complete_timeline |
| `Action_None` | 257 | 389 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 202 | 30 | inferred_complete_timeline |
| `Action_None` | 235 | 295 | 61 | inferred_complete_timeline |
| `Action_None` | 297 | 355 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 238 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 220 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–385
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 259 | 87 | inferred_complete_timeline |
| `Action_None` | 271 | 381 | 111 | inferred_complete_timeline |
| `Action_None` | 384 | 385 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–358 | 359 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–301 | 301 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 205–315 | 55 | 9 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 206–315 | 100 | 8 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 208–381 | 172 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 210–228 | 15 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 213–240 | 8 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 228–246 | 19 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 239–365 | 60 | 6 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 241–301 | 13 | 4 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 245–389 | 145 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 345–389 | 45 | 1 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 389–389 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `18` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 244: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '17' has invalid range: start=219, end=206. Clamping end to start.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [173–188], lower_priority='Action_DownBlock' annotated_start=177, effective_Action_DownBlock_start=189.
- ⚠️ Action 'Action_None' range [173-255] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-389] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-358] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-238] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [177-261] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-309] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [177-199] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [210-261] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-307] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-295] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-355] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [177-255] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-220] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-259] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-381] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-238] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-346] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-206] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-376] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [189-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [219-261] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-245] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [177-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-297] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-234] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-265] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-242] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-284] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-308] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-381] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-218] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-218] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-246] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-365] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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