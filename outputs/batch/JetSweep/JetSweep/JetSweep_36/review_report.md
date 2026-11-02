# Play-Annotation-Generator Annotation Review — JetSweep_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_36`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 26
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 4
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-Y | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `5` | `4` |
| ✅ EXACT | `Action_LeadBlock` | TE-Y | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `22` | `21` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `13` | `12` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `13` | `12` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `22` | `21` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `22` | `21` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `9` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-Y | `3` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `4` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 82 |
| ✅ EXACT | `Action_JetMotion` | WR | `5` | `4` | 45 | START | 45 | 105 |
| ✅ EXACT | `Action_LeadBlock` | TE-Y | `3` | `2` | 83 | START | 83 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `12` | 83 | START | 83 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 83 | START | 83 | 102 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `22` | `21` | 83 | START | 83 | 140 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `9` | `8` | 83 | START | N/A | N/A |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 84 | START | 84 | 90 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 90 | END | 84 | 90 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 97 | START | 97 | 105 |
| ✅ EXACT | `Action_BallCarry` | WR | `5` | `4` | 106 | START | 106 | 274 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `13` | `12` | 110 | START | 110 | 129 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `13` | `12` | 140 | BOUNDARY | 134 | 140 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `22` | `21` | 140 | BOUNDARY | 83 | 140 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `22` | `21` | 140 | BOUNDARY | 83 | 140 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `9` | `8` | 140 | BOUNDARY | N/A | 140 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_SnapReceive` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_None` | 91 | 96 | 6 | inferred_complete_timeline |
| `Action_Toss` | 97 | 105 | 9 | inferred_complete_timeline |
| `Action_None` | 106 | 127 | 22 | inferred_complete_timeline |
| `Action_None` | 130 | 254 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 359 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 359 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 183 | 100 | inferred_complete_timeline |
| `Action_None` | 191 | 359 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_JetMotion` | 45 | 105 | 61 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 274 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>TE-Y — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_LeadBlock` | 83 | 140 | 58 | inferred_complete_timeline |
| `Action_None` | 141 | 211 | 71 | inferred_complete_timeline |
| `Action_None` | 215 | 219 | 5 | inferred_complete_timeline |
| `Action_None` | 221 | 232 | 12 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 250 | 7 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 97 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 106 | 8 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 110 | 129 | 20 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 134 | 140 | 7 | inferred_complete_timeline |
| `Action_None` | 141 | 269 | 129 | inferred_complete_timeline |
| `Action_None` | 271 | 278 | 8 | inferred_complete_timeline |
| `Action_None` | 280 | 286 | 7 | inferred_complete_timeline |
| `Action_None` | 288 | 359 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 83 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_None` | 91 | 109 | 19 | inferred_complete_timeline |
| `Action_None` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_None` | 119 | 155 | 37 | inferred_complete_timeline |
| `Action_None` | 160 | 191 | 32 | inferred_complete_timeline |
| `Action_None` | 193 | 284 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 102 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 140 | 58 | inferred_complete_timeline |
| `Action_None` | 141 | 170 | 30 | inferred_complete_timeline |
| `Action_None` | 174 | 359 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 112 | 29 | inferred_complete_timeline |
| `Action_None` | 114 | 144 | 31 | inferred_complete_timeline |
| `Action_None` | 161 | 211 | 51 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 359 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 359 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 359 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 359 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 329 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 359 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 129 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 359 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 224 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 359 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 143 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–359 | 359 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 167–354 | 177 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 179–280 | 98 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 194–292 | 95 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 223–359 | 137 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 319–348 | 26 | 4 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 334–341 | 8 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 343–359 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `9` (C)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 74: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [84–90], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=91.
- ⚠️ Action 'Action_LeadBlock' range [83-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-211] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-232] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-274] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-127] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-254] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-224] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-155] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-191] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-284] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-144] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-211] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-97] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [110-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-278] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-286] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-138] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-179] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-229] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-354] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-280] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-292] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-341] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-348] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-341] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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