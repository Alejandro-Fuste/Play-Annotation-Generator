# Play-Annotation-Generator Annotation Review — JetSweep_114

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_114`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 57
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Toss` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 3 | START | 3 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 3 | START | 3 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 3 | START | 3 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 3 | START | 3 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 3 | START | 3 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 3 | START | 3 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 3 | START | 3 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 3 | START | 3 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 3 | START | 3 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 3 | START | 3 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 3 | START | 3 | 77 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `3` | `2` | 51 | START | 51 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `21` | `20` | 76 | START | 76 | 87 |
| ✅ EXACT | `Action_LeadBlock` | TE | `6` | `5` | 78 | START | 78 | 145 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `13` | 78 | START | 78 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 78 | START | 91 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 78 | START | 78 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `3` | 78 | START | 78 | 145 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 78 | START | 78 | 145 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 90 | END | 76 | 90 |
| ✅ EXACT | `Action_Toss` | QB | `17` | `16` | 93 | START | 93 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `3` | `2` | 104 | START | 104 | 257 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 145 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 3–277
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_SnapReceive` | 76 | 90 | 15 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_Toss` | 93 | 103 | 11 | inferred_complete_timeline |
| `Action_None` | 104 | 277 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 3–290
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 290 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 185 | 110 | inferred_complete_timeline |
| `Action_None` | 188 | 236 | 49 | inferred_complete_timeline |
| `Action_None` | 247 | 299 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 50 | 48 | inferred_complete_timeline |
| `Action_JetMotion` | 51 | 103 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 257 | 154 | inferred_complete_timeline |
| `Action_BallCarry` | 263 | 294 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 299 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 3–176
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 77 | 75 | inferred_complete_timeline |
| `Action_LeadBlock` | 78 | 145 | 68 | inferred_complete_timeline |
| `Action_None` | 146 | 176 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 77 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 145 | 68 | inferred_complete_timeline |
| `Action_None` | 146 | 299 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 3–296
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 77 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 145 | 68 | inferred_complete_timeline |
| `Action_None` | 146 | 296 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_BallSnap` | 76 | 87 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 127 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 145 | 14 | inferred_complete_timeline |
| `Action_None` | 146 | 296 | 151 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 3–95
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 77 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 95 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 3–283
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 77 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 145 | 68 | inferred_complete_timeline |
| `Action_None` | 146 | 283 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 299 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 299 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 108 | 33 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 162 | 49 | inferred_complete_timeline |
| `Action_None` | 172 | 179 | 8 | inferred_complete_timeline |
| `Action_None` | 193 | 199 | 7 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_None` | 218 | 228 | 11 | inferred_complete_timeline |
| `Action_None` | 230 | 237 | 8 | inferred_complete_timeline |
| `Action_None` | 240 | 299 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 299 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 299 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 257 | 182 | inferred_complete_timeline |
| `Action_None` | 259 | 282 | 24 | inferred_complete_timeline |
| `Action_None` | 286 | 299 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 283 | 208 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 235 | 160 | inferred_complete_timeline |
| `Action_None` | 238 | 260 | 23 | inferred_complete_timeline |
| `Action_None` | 262 | 284 | 23 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 294 | 219 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 196 | 121 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 299 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 76 | 299 | 224 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 107–134 | 28 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 172–189 | 9 | 2 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 177–299 | 123 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 187–299 | 113 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 225–227 | 3 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 269–272 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [76–90], lower_priority='Action_ZoneBlock' annotated_start=78, effective_Action_ZoneBlock_start=91.
- ⚠️ Action 'Action_None' range [76-185] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-236] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-257] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [263-294] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-283] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-176] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-235] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-260] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-284] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-283] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-290] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-257] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-282] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-294] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-296] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-108] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-228] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-237] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-277] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-299] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-196] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [76-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-296] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-95] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '28' has 1 frames without a visible bounding box.
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

</details>