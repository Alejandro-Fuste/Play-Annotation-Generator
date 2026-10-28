# Play-Annotation-Generator Annotation Review — Draw_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_37`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 124
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 104
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `12` | `11` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 65 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `22` | `21` | 66 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `12` | `11` | 69 | START | 69 | 145 |
| ✅ EXACT | `Action_PassBlock` | RT | `13` | `12` | 69 | START | 69 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `20` | 69 | START | 69 | 105 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 79 | END | 66 | 79 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `5` | `4` | 84 | START | 84 | 101 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 102 | START | 102 | 117 |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `9` | 118 | START | 118 | 135 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 145 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_SnapReceive` | 66 | 79 | 14 | inferred_complete_timeline |
| `Action_None` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 84 | 101 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 102 | 117 | 16 | inferred_complete_timeline |
| `Action_None` | 118 | 276 | 159 | inferred_complete_timeline |
| `Action_None` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_BallCarry` | 118 | 135 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 299 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 130 | 65 | inferred_complete_timeline |
| `Action_None` | 133 | 214 | 82 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 299 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 299 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 163 | 98 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 145 | 77 | inferred_complete_timeline |
| `Action_None` | 146 | 226 | 81 | inferred_complete_timeline |
| `Action_None` | 228 | 235 | 8 | inferred_complete_timeline |
| `Action_None` | 238 | 260 | 23 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |
| `Action_None` | 271 | 284 | 14 | inferred_complete_timeline |
| `Action_None` | 286 | 299 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 105 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 145 | 39 | inferred_complete_timeline |
| `Action_None` | 146 | 153 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 145 | 77 | inferred_complete_timeline |
| `Action_None` | 146 | 275 | 130 | inferred_complete_timeline |
| `Action_None` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 103 | 38 | inferred_complete_timeline |
| `Action_None` | 105 | 184 | 80 | inferred_complete_timeline |
| `Action_None` | 188 | 251 | 64 | inferred_complete_timeline |
| `Action_None` | 253 | 299 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 84 | 19 | inferred_complete_timeline |
| `Action_None` | 87 | 94 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 95 | 30 | inferred_complete_timeline |
| `Action_None` | 140 | 271 | 132 | inferred_complete_timeline |
| `Action_None` | 273 | 276 | 4 | inferred_complete_timeline |
| `Action_None` | 282 | 299 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 99 | 34 | inferred_complete_timeline |
| `Action_None` | 101 | 257 | 157 | inferred_complete_timeline |
| `Action_None` | 265 | 280 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 144 | 79 | inferred_complete_timeline |
| `Action_None` | 146 | 182 | 37 | inferred_complete_timeline |
| `Action_None` | 184 | 197 | 14 | inferred_complete_timeline |
| `Action_None` | 199 | 214 | 16 | inferred_complete_timeline |
| `Action_None` | 224 | 299 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 102 | 37 | inferred_complete_timeline |
| `Action_None` | 104 | 127 | 24 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 150 | 85 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 193 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 150 | 85 | inferred_complete_timeline |
| `Action_None` | 165 | 299 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 131 | 66 | inferred_complete_timeline |
| `Action_None` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 146 | 6 | inferred_complete_timeline |
| `Action_None` | 148 | 299 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 212 | 147 | inferred_complete_timeline |
| `Action_None` | 225 | 299 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 103 | 38 | inferred_complete_timeline |
| `Action_None` | 148 | 299 | 152 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–193 | 191 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 35–53 | 19 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 105–299 | 178 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 115–138 | 24 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 117–299 | 175 | 6 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 143–299 | 157 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 171–299 | 129 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 180–299 | 79 | 10 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 185–299 | 113 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 207–299 | 88 | 3 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 237–299 | 62 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 275–285 | 11 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `22` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 74: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '21' has invalid range: start=66, end=53. Clamping end to start.
- ⚠️ Action 'Action_None' range [66-163] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-214] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-276] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-193] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-182] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-197] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-214] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-127] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [118-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-260] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-284] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-275] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-168] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-251] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-95] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-271] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-257] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-280] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-105] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [107-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-168] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-191] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-205] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-262] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-138] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-132] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-181] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-219] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-261] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-273] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-286] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-276] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-249] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-285] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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