# Play-Annotation-Generator Annotation Review — SplitZone_119

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_119`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 5 | START | 6 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 5 | START | 6 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 5 | START | 6 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 5 | START | 6 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 5 | START | 6 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 5 | START | 6 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 5 | START | 6 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 5 | START | 54 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 5 | START | 6 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 5 | START | 6 | 143 |
| ✅ EXACT | `Action_BallSnap` | RG | `13` | `13` | 144 | START | 144 | 146 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `10` | `10` | 147 | START | 147 | 243 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 147 | START | 147 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `15` | 147 | START | 147 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `16` | `16` | 147 | START | 147 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 147 | START | 147 | 175 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `21` | `21` | 147 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 154 | END | 144 | 154 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 158 | START | 158 | 171 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `5` | 172 | START | 172 | 271 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 243 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_SnapReceive` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 158 | 171 | 14 | inferred_complete_timeline |
| `Action_None` | 172 | 299 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 6–271
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 171 | 166 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 271 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 299 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 299 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 146 | 141 | inferred_complete_timeline |
| `Action_SplitBlock` | 147 | 243 | 97 | inferred_complete_timeline |
| `Action_None` | 244 | 299 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 146 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 191 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 198 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 200 | 217 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 225 | 243 | 19 | inferred_complete_timeline |
| `Action_None` | 244 | 256 | 13 | inferred_complete_timeline |
| `Action_None` | 276 | 299 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 146 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 175 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 198 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 217 | 241 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 243 | 243 | 1 | inferred_complete_timeline |
| `Action_None` | 244 | 299 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 54–57
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 54 | 57 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 6–267
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_BallSnap` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 163 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 211 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 146 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 189 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 213 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 243 | 24 | inferred_complete_timeline |
| `Action_None` | 244 | 299 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 211 | 68 | inferred_complete_timeline |
| `Action_None` | 220 | 258 | 39 | inferred_complete_timeline |
| `Action_None` | 261 | 299 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 6–297
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 185 | 42 | inferred_complete_timeline |
| `Action_None` | 194 | 294 | 101 | inferred_complete_timeline |
| `Action_None` | 296 | 297 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 6–158
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 158 | 15 | inferred_complete_timeline |
| `Action_None` | 167 | 299 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 6–202
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 187 | 44 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 6–204
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 204 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 299 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 299 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 264 | 121 | inferred_complete_timeline |
| `Action_None` | 267 | 289 | 23 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 265 | 122 | inferred_complete_timeline |
| `Action_None` | 268 | 299 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 6–290
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 143 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 290 | 147 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 6–247 | 238 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 167–299 | 122 | 5 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 209–268 | 60 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 237–299 | 62 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 245–273 | 19 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 274–299 | 26 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 274–290 | 17 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 276–299 | 24 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 284–286 | 3 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (5 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (C)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 240: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 97 frames exceeds threshold 90 frames [start=147, end=243].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LT) duration 97 frames exceeds threshold 90 frames [start=147, end=243].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (RT) duration 97 frames exceeds threshold 90 frames [start=147, end=243].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 97 frames exceeds threshold 90 frames [start=147, end=243].
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=147, end=57. Clamping end to start.
- ⚠️ Action 'Action_None' range [144-185] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-294] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-211] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-258] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-271] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-299] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-290] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [198-211] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [241-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-187] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [200-217] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [220-221] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-256] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [192-213] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-264] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-289] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-204] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-238] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [217-241] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-224] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-255] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-263] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-268] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-297] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-273] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-290] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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