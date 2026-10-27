# Play-Annotation-Generator Annotation Review — Counter_293

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_293`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 121
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `23` | `22` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 94 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `23` | `Group` | 0 | START | 96 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 153 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 154 | START | 154 | 168 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `16` | `15` | 157 | START | 179 | 185 |
| ✅ EXACT | `Action_DownBlock` | LG | `19` | `18` | 157 | START | 157 | 163 |
| ✅ EXACT | `Action_PullBlock` | RG | `20` | `19` | 157 | START | 157 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `23` | `22` | 157 | START | 159 | 162 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `6` | `5` | 163 | START | 163 | 187 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 170 | END | 154 | 170 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 181 | START | 181 | 194 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `6` | `5` | 195 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 235 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_SnapReceive` | 154 | 170 | 17 | inferred_complete_timeline |
| `Action_None` | 171 | 180 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 181 | 194 | 14 | inferred_complete_timeline |
| `Action_None` | 195 | 311 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 163 | 187 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 329 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 201 | 48 | inferred_complete_timeline |
| `Action_None` | 204 | 329 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 96–329
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 96 | 101 | 6 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 166 | 173 | 8 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 175 | 190 | 16 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 193 | 195 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 203 | 208 | 6 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 210 | 224 | 15 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 226 | 235 | 10 | inferred_complete_timeline |
| `Action_None` | 236 | 259 | 24 | inferred_complete_timeline |
| `Action_None` | 261 | 268 | 8 | inferred_complete_timeline |
| `Action_None` | 275 | 329 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 207 | 54 | inferred_complete_timeline |
| `Action_None` | 218 | 321 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_DownBlock` | 157 | 163 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_BallSnap` | 154 | 168 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 179 | 185 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PullBlock` | 157 | 235 | 79 | inferred_complete_timeline |
| `Action_None` | 236 | 311 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 94–212
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 94 | 122 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 153 | 9 | inferred_complete_timeline |
| `Action_None` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 187 | 21 | inferred_complete_timeline |
| `Action_None` | 194 | 205 | 12 | inferred_complete_timeline |
| `Action_None` | 208 | 212 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 164 | 11 | inferred_complete_timeline |
| `Action_None` | 166 | 205 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 226 | 73 | inferred_complete_timeline |
| `Action_None` | 228 | 329 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 329 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 49 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 71 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 127 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 153 | 25 | inferred_complete_timeline |
| `Action_None` | 154 | 180 | 27 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 325 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 153 | 99 | inferred_complete_timeline |
| `Action_None` | 154 | 230 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 271 | 118 | inferred_complete_timeline |
| `Action_None` | 273 | 296 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 203 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 211 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 203 | 50 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_None` | 211 | 329 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–307
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 307 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 329 | 176 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 2–329 | 320 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 190–329 | 138 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 193–241 | 48 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 200–329 | 105 | 5 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 207–212 | 6 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 220–329 | 110 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 227–329 | 103 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 237–329 | 93 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 243–329 | 86 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 248–259 | 10 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 252–304 | 34 | 5 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 256–305 | 34 | 6 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 264–329 | 66 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 266–285 | 20 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 303–328 | 24 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 317–329 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `16` (C): Annotated start 157 != Inferred start 179
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `23` (7 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `6` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 588: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '5' has invalid range: start=195, end=187. Clamping end to start.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [154–170], lower_priority='Action_DownBlock' annotated_start=157, effective_Action_DownBlock_start=171.
- ⚠️ Action 'Action_None' range [154-201] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-203] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-203] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-307] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [163-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-211] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-311] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-230] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-321] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-271] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-296] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-205] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [154-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [179-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-127] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-325] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-329] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-163] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [157-235] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-311] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-189] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [159-162] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [166-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [175-190] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [193-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [203-208] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [210-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-259] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-268] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-329] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-237] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-252] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-329] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-277] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-329] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-259] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-262] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-272] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-284] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-270] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-284] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-305] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-285] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-328] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>