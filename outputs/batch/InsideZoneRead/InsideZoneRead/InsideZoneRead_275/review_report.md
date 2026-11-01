# Play-Annotation-Generator Annotation Review — InsideZoneRead_275

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_275`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_Keep` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 10 | START | 10 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `14` | 13 | START | 13 | 41 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `17` | 13 | START | 13 | 131 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `20` | 13 | START | 13 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `5` | 13 | START | 13 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `8` | `7` | 13 | START | 28 | 47 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 27 | END | 10 | 27 |
| ✅ EXACT | `Action_ReadDefender` | QB | `11` | `10` | 38 | START | 38 | 44 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `21` | `20` | 45 | START | 45 | 131 |
| ✅ EXACT | `Action_Keep` | QB | `11` | `10` | 45 | START | 45 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `11` | `10` | 61 | START | 61 | 296 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 131 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 27 | 18 | inferred_complete_timeline |
| `Action_None` | 28 | 37 | 10 | inferred_complete_timeline |
| `Action_ReadDefender` | 38 | 44 | 7 | inferred_complete_timeline |
| `Action_Keep` | 45 | 60 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 61 | 296 | 236 | inferred_complete_timeline |
| `Action_BallCarry` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 286 | 277 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 191 | 182 | inferred_complete_timeline |
| `Action_None` | 194 | 211 | 18 | inferred_complete_timeline |
| `Action_None` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_None` | 222 | 270 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_None` | 132 | 291 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 44 | 32 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 45 | 131 | 87 | inferred_complete_timeline |
| `Action_None` | 132 | 163 | 32 | inferred_complete_timeline |
| `Action_None` | 165 | 329 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 27 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 47 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 79 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 41 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 47 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 66 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 131 | 60 | inferred_complete_timeline |
| `Action_None` | 132 | 329 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 88 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 131 | 42 | inferred_complete_timeline |
| `Action_None` | 132 | 286 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 78 | 69 | inferred_complete_timeline |
| `Action_None` | 82 | 111 | 30 | inferred_complete_timeline |
| `Action_None` | 113 | 329 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 71 | 62 | inferred_complete_timeline |
| `Action_None` | 77 | 329 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 298 | 289 | inferred_complete_timeline |
| `Action_None` | 300 | 329 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 138 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 106 | 97 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 232 | 223 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 10–35 | 21 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 51–137 | 84 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 68–70 | 3 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 80–329 | 247 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 105–329 | 155 | 15 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 118–329 | 206 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 128–150 | 22 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 143–329 | 183 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 155–196 | 22 | 3 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 175–195 | 15 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 197–274 | 78 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 234–329 | 96 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 288–329 | 36 | 3 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 298–329 | 32 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 304–329 | 26 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 318–319 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 550: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 119 frames exceeds threshold 90 frames [start=13, end=131].
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [10–27], lower_priority='Action_ZoneBlock' annotated_start=13, effective_Action_ZoneBlock_start=28.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 119 frames exceeds threshold 90 frames [start=13, end=131].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (LT) duration 119 frames exceeds threshold 90 frames [start=13, end=131].
- ⚠️ Action 'Action_None' range [10-191] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-211] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-270] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-88] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-131] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-286] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-329] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-47] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-79] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-78] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-329] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-298] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [61-296] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-232] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-71] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-41] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-47] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-66] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-329] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-286] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 132, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [132-291] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [45-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-163] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-11] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-22] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-30] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-35] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-137] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-110] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-126] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-178] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-232] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-281] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-294] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-126] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-268] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-136] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-160] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-185] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-182] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-274] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-329] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-302] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>