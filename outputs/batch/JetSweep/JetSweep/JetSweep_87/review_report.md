# Play-Annotation-Generator Annotation Review — JetSweep_87

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_87`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 145
- **Validation Warnings:** 197
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 118
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `23` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | RT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_Toss` | QB | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `23` | `20` |
| ✅ EXACT | `Action_BlockSecondLevel` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 142 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 134 | START | 134 | 147 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `23` | `20` | 142 | START | 142 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `11` | `10` | 143 | START | 143 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | RT | `8` | `7` | 143 | START | 143 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `12` | 143 | START | 148 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `3` | 143 | START | 143 | 195 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `4` | 143 | START | 143 | 144 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `8` | `7` | 143 | START | N/A | N/A |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `14` | `13` | 147 | END | 134 | 136 |
| ❌ MISSING SEGMENT | `Action_Toss` | QB | `14` | `13` | 154 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `23` | `20` | 164 | START | 177 | 199 |
| ✅ EXACT | `Action_BlockSecondLevel` | RB | `11` | `10` | 164 | START | 164 | 196 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 196 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 40 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 77 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 105 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 133 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 134 | 136 | 3 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_LeadBlock` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_LeadBlock` | 148 | 163 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 164 | 196 | 33 | inferred_complete_timeline |
| `Action_None` | 197 | 252 | 56 | inferred_complete_timeline |
| `Action_None` | 256 | 281 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 195 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 137 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 142 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 144 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_BallSnap` | 134 | 147 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 162 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 174 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_SealBlock` | 143 | 172 | 30 | inferred_complete_timeline |
| `Action_SealBlock` | 241 | 293 | 53 | inferred_complete_timeline |
| `Action_SealBlock` | 298 | 343 | 46 | inferred_complete_timeline |
| `Action_SealBlock` | 345 | 389 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 141 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 133 | 116 | inferred_complete_timeline |
| `Action_None` | 134 | 148 | 15 | inferred_complete_timeline |
| `Action_None` | 155 | 190 | 36 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–2
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 248 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 166 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_None` | 135 | 154 | 20 | inferred_complete_timeline |
| `Action_None` | 183 | 266 | 84 | inferred_complete_timeline |
| `Action_None` | 275 | 291 | 17 | inferred_complete_timeline |
| `Action_None` | 294 | 297 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 133 | 130 | inferred_complete_timeline |
| `Action_None` | 134 | 216 | 83 | inferred_complete_timeline |
| `Action_None` | 230 | 272 | 43 | inferred_complete_timeline |
| `Action_None` | 281 | 304 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–210 | 168 | 6 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–223 | 174 | 13 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 5–220 | 215 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 11–203 | 178 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 27–191 | 164 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 131–151 | 21 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 142–199 | 32 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 147–389 | 197 | 6 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 156–177 | 17 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 157–233 | 77 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 158–208 | 50 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 167–206 | 28 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 169–211 | 43 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 197–389 | 147 | 4 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 210–253 | 42 | 2 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 214–292 | 75 | 2 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 217–389 | 155 | 7 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 221–240 | 20 | 1 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 246–389 | 141 | 2 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 247–282 | 36 | 1 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 256–389 | 132 | 2 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 269–289 | 14 | 2 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 270–380 | 106 | 3 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 295–355 | 61 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 308–311 | 4 | 1 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 310–340 | 31 | 1 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 313–389 | 73 | 2 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 333–337 | 5 | 1 | Undefined position; Undefined team |
| `42` | `66` | Position_Unknown | Team_Unknown | 344–389 | 46 | 1 | Undefined position; Undefined team |
| `43` | `67` | Position_Unknown | Team_Unknown | 348–389 | 42 | 1 | Undefined position; Undefined team |
| `44` | `69` | Position_Unknown | Team_Unknown | 360–389 | 30 | 1 | Undefined position; Undefined team |
| `45` | `71` | Position_Unknown | Team_Unknown | 363–373 | 11 | 1 | Undefined position; Undefined team |
| `46` | `72` | Position_Unknown | Team_Unknown | 365–389 | 24 | 2 | Undefined position; Undefined team |
| `47` | `74` | Position_Unknown | Team_Unknown | 366–389 | 24 | 1 | Undefined position; Undefined team |
| `48` | `75` | Position_Unknown | Team_Unknown | 367–389 | 23 | 1 | Undefined position; Undefined team |
| `49` | `76` | Position_Unknown | Team_Unknown | 370–374 | 5 | 1 | Undefined position; Undefined team |
| `50` | `77` | Position_Unknown | Team_Unknown | 371–389 | 19 | 1 | Undefined position; Undefined team |
| `51` | `78` | Position_Unknown | Team_Unknown | 372–389 | 18 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SealBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `8` (RT)
- ❌ Missing segment for action `Action_Toss` on target `14` (QB)
- ⚠️ `Action_BallCarry` for actor_track_id `23` (Position_Unknown): Annotated start 164 != Inferred start 177

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 116 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 176: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Overlapping action conflict at frame 143 for track '7': 'Action_ZoneBlock' vs 'Action_SealBlock'. Overriding with 'Action_SealBlock'.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [134–147], lower_priority='Action_ZoneBlock' annotated_start=143, effective_Action_ZoneBlock_start=148.
- ⚠️ Segment 'Action_Toss' for track '13' has invalid range: start=154, end=152. Clamping end to start.
- ⚠️ Action 'Action_None' range [134-166] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-291] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-142] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-144] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [143-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [241-293] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [298-343] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-248] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-216] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-272] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-304] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [143-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-252] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-281] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [134-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-154] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-23] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-62] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-79] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-192] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-223] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-220] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-50] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-66] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-122] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-203] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-43] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-191] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-151] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [142-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [177-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-224] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-262] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-365] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-233] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-203] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-223] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-254] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-301] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-253] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-237] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-292] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-253] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-298] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-315] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-330] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-348] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-240] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-286] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-282] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-342] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-389] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-280] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-345] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-373] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-380] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-355] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-340] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-323] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-337] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-373] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-376] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-389] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-374] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.

</details>