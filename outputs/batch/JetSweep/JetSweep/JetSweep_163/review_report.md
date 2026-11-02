# Play-Annotation-Generator Annotation Review — JetSweep_163

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_163`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 4 | START | 5 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 4 | START | 5 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 4 | START | 5 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 4 | START | 5 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 4 | START | 5 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 4 | START | 5 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 4 | START | 5 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 4 | START | 5 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 4 | START | 5 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 4 | START | 5 | 116 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `3` | `2` | 82 | START | 82 | 139 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 117 | START | 117 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `6` | `5` | 118 | START | 118 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `11` | 118 | START | 118 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 118 | START | 137 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 118 | START | 118 | 210 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `22` | `21` | 118 | START | 118 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `3` | 118 | START | 118 | 137 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 130 | END | 117 | 130 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 136 | START | 136 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `3` | `2` | 140 | START | 140 | 238 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 244 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 5–231
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_SnapReceive` | 117 | 130 | 14 | inferred_complete_timeline |
| `Action_None` | 131 | 135 | 5 | inferred_complete_timeline |
| `Action_Toss` | 136 | 139 | 4 | inferred_complete_timeline |
| `Action_None` | 140 | 231 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 5–205
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_None` | 117 | 205 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 5–242
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_JetMotion` | 82 | 139 | 58 | inferred_complete_timeline |
| `Action_BallCarry` | 140 | 238 | 99 | inferred_complete_timeline |
| `Action_BallCarry` | 240 | 242 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 5–202
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_None` | 117 | 202 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 5–313
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 117 | 113 | inferred_complete_timeline |
| `Action_LeadBlock` | 118 | 203 | 86 | inferred_complete_timeline |
| `Action_LeadBlock` | 205 | 212 | 8 | inferred_complete_timeline |
| `Action_LeadBlock` | 214 | 217 | 4 | inferred_complete_timeline |
| `Action_LeadBlock` | 222 | 244 | 23 | inferred_complete_timeline |
| `Action_None` | 245 | 313 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 5–201
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 117 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 201 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 5–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 117 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 210 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 5–152
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_BallSnap` | 117 | 129 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 152 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 5–227
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 117 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 131 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 227 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 5–345
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 117 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 137 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 244 | 106 | inferred_complete_timeline |
| `Action_None` | 245 | 345 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 5–229
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_None` | 117 | 190 | 74 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 205 | 5 | inferred_complete_timeline |
| `Action_None` | 208 | 229 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 5–315
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_None` | 117 | 278 | 162 | inferred_complete_timeline |
| `Action_None` | 281 | 315 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–153
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_None` | 117 | 153 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 5–203
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_None` | 117 | 203 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 5–224
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_None` | 117 | 203 | 87 | inferred_complete_timeline |
| `Action_None` | 205 | 213 | 9 | inferred_complete_timeline |
| `Action_None` | 219 | 224 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–349
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_None` | 117 | 271 | 155 | inferred_complete_timeline |
| `Action_None` | 276 | 279 | 4 | inferred_complete_timeline |
| `Action_None` | 286 | 342 | 57 | inferred_complete_timeline |
| `Action_None` | 347 | 349 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–187
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_None` | 117 | 187 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 5–201
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_None` | 117 | 193 | 77 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 5–194
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_None` | 117 | 194 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 5–319
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_None` | 117 | 319 | 203 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 5–359 | 355 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 5–176 | 164 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 156–162 | 7 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 158–223 | 66 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 158–161 | 4 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 175–229 | 55 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 198–334 | 137 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 203–227 | 25 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 243–322 | 77 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 253–346 | 85 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 262–359 | 98 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 273–346 | 69 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 289–359 | 71 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 316–359 | 44 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 344–356 | 13 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 344–359 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 328: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 328: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 127 frames exceeds threshold 90 frames [start=118, end=244].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '5' (TE) duration 127 frames exceeds threshold 90 frames [start=118, end=244].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (RG) duration 110 frames exceeds threshold 90 frames [start=118, end=227].
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [117–130], lower_priority='Action_ZoneBlock' annotated_start=118, effective_Action_ZoneBlock_start=131.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 93 frames exceeds threshold 90 frames [start=118, end=210].
- ⚠️ Action 'Action_None' range [117-202] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-193] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [140-238] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [240-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-345] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-203] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-213] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [118-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [205-212] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [214-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-313] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-203] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-231] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-319] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-205] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-271] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-342] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-278] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-315] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-229] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [117-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-210] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-223] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-229] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-334] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-265] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-322] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-327] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-346] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-337] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-346] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-356] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>