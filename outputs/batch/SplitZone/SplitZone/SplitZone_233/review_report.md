# Play-Annotation-Generator Annotation Review — SplitZone_233

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_233`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 8 | START | 9 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 8 | START | 9 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 8 | START | 9 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 8 | START | 9 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 8 | START | 9 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 8 | START | 9 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 8 | START | 9 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 8 | START | 9 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 8 | START | 9 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 8 | START | 9 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 8 | START | 9 | 193 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `5` | 172 | START | 172 | 188 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `10` | 175 | START | 175 | 195 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `21` | 175 | START | 175 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `4` | 175 | START | 175 | 217 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `5` | `5` | 175 | START | 189 | 189 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `6` | 175 | START | 175 | 295 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `1` | `1` | 181 | START | 181 | 295 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 188 | END | 172 | 188 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `15` | 189 | START | 189 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `7` | 194 | START | 194 | 195 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 295 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 9–378
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_SnapReceive` | 172 | 188 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 189 | 193 | 5 | inferred_complete_timeline |
| `Action_None` | 194 | 378 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 9–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 193 | 185 | inferred_complete_timeline |
| `Action_BallCarry` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 199 | 389 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 9–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 9–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 9–357
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_None` | 172 | 357 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 9–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 180 | 172 | inferred_complete_timeline |
| `Action_SplitBlock` | 181 | 295 | 115 | inferred_complete_timeline |
| `Action_None` | 296 | 389 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–221
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 174 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 217 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 221 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 9–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 174 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 295 | 121 | inferred_complete_timeline |
| `Action_None` | 296 | 389 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 9–281
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_BallSnap` | 172 | 188 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 189 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 275 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 279 | 281 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 9–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 174 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 195 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 295 | 97 | inferred_complete_timeline |
| `Action_None` | 296 | 389 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 9–229
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 174 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 198 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 229 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–287
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_None` | 172 | 266 | 95 | inferred_complete_timeline |
| `Action_None` | 272 | 279 | 8 | inferred_complete_timeline |
| `Action_None` | 282 | 287 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 9–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 9–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 9–389
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_None` | 172 | 213 | 42 | inferred_complete_timeline |
| `Action_None` | 225 | 230 | 6 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |
| `Action_None` | 268 | 389 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 9–352
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_None` | 172 | 267 | 96 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 301 | 352 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 9–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 9–219
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_None` | 172 | 219 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 9–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 9–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 171 | 163 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 9–389 | 381 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 185–186 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 227–372 | 141 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 227–389 | 159 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 253–342 | 84 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 272–389 | 118 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 280–281 | 2 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 282–327 | 46 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 285–287 | 3 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 333–377 | 44 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 364–368 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (C) duration 107 frames exceeds threshold 90 frames [start=175, end=281].
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [172–188], lower_priority='Action_ZoneBlock' annotated_start=175, effective_Action_ZoneBlock_start=189.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LG) duration 121 frames exceeds threshold 90 frames [start=175, end=295].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 121 frames exceeds threshold 90 frames [start=175, end=295].
- ⚠️ Action 'Action_None' range [172-357] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [219-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '5' starts at frame 189, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [189-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [192-275] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [279-281] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [194-195] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-295] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-266] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-279] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-267] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-352] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-378] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-213] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-219] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-198] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-229] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-249] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-372] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-240] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-252] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-272] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-342] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-327] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-363] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-377] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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