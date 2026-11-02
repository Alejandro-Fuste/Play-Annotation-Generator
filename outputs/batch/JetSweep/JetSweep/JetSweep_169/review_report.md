# Play-Annotation-Generator Annotation Review — JetSweep_169

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_169`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_LeadBlock` | WR3 | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 142 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `2` | `1` | 81 | START | 81 | 169 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 143 | START | 143 | 154 |
| ✅ EXACT | `Action_LeadBlock` | WR3 | `4` | `3` | 144 | START | 144 | 175 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `9` | 144 | START | 144 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `15` | 144 | START | 144 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 144 | START | 144 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 144 | START | 157 | 158 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `22` | `21` | 144 | START | 144 | 175 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 154 | END | 143 | 154 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 158 | START | 158 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `2` | `1` | 170 | START | 170 | 358 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 175 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–386
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_SnapReceive` | 143 | 154 | 12 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_Toss` | 158 | 169 | 12 | inferred_complete_timeline |
| `Action_None` | 170 | 341 | 172 | inferred_complete_timeline |
| `Action_None` | 345 | 347 | 3 | inferred_complete_timeline |
| `Action_None` | 350 | 386 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 245 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 267 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_JetMotion` | 81 | 169 | 89 | inferred_complete_timeline |
| `Action_BallCarry` | 170 | 358 | 189 | inferred_complete_timeline |
| `Action_BallCarry` | 363 | 371 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 377 | 382 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 384 | 389 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_LeadBlock` | 144 | 175 | 32 | inferred_complete_timeline |
| `Action_None` | 176 | 389 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 389 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 165 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 175 | 32 | inferred_complete_timeline |
| `Action_None` | 176 | 240 | 65 | inferred_complete_timeline |
| `Action_None` | 243 | 246 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_BallSnap` | 143 | 154 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 167 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 216 | 31 | inferred_complete_timeline |
| `Action_None` | 223 | 389 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 169 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 157 | 14 | inferred_complete_timeline |
| `Action_None` | 197 | 389 | 193 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 389 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 213 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 315 | 173 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–387
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 164 | 22 | inferred_complete_timeline |
| `Action_None` | 166 | 214 | 49 | inferred_complete_timeline |
| `Action_None` | 222 | 387 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 192 | 50 | inferred_complete_timeline |
| `Action_None` | 194 | 221 | 28 | inferred_complete_timeline |
| `Action_None` | 227 | 233 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 201 | 59 | inferred_complete_timeline |
| `Action_None` | 228 | 389 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 265 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 215 | 73 | inferred_complete_timeline |
| `Action_None` | 217 | 266 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 389 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–362
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 362 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 273 | 131 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 157–389 | 230 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 201–204 | 4 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 201–389 | 188 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 216–389 | 159 | 7 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 227–245 | 7 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 247–389 | 140 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 251–389 | 137 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 253–255 | 3 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 254–389 | 124 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 261–263 | 3 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 267–389 | 120 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 295–321 | 27 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 303–389 | 87 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 320–328 | 8 | 2 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 330–389 | 50 | 2 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 336–350 | 15 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 344–389 | 45 | 2 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 355–356 | 2 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 363–370 | 8 | 1 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 367–389 | 21 | 2 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 389–389 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [143–154], lower_priority='Action_ZoneBlock' annotated_start=144, effective_Action_ZoneBlock_start=155.
- ⚠️ Action 'Action_None' range [143-267] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-358] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [363-371] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [377-382] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-201] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-266] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-362] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-213] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-341] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-347] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-386] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-265] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-245] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-221] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-273] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-389] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-389] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-164] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-214] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-387] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-315] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-165] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [143-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [170-171] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-216] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-240] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-227] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-285] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-328] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-365] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-383] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-274] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-260] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-334] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-319] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-321] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-328] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-347] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-350] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-389] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-370] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-382] for track '41' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>