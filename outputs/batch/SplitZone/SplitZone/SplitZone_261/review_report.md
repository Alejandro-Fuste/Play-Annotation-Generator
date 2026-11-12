# Play-Annotation-Generator Annotation Review — SplitZone_261

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_261`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 88
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `23` | `22` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `0` | `Group` | 20 | START | 21 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 20 | START | 21 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 20 | START | 21 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `15` | `Group` | 20 | START | 21 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 20 | START | 21 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 20 | START | 21 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 20 | START | 21 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 20 | START | 21 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 20 | START | 21 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 20 | START | 21 | 135 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 125 | START | 125 | 136 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `14` | 128 | START | 137 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 128 | START | 128 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `19` | 128 | START | 128 | 181 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 128 | START | 128 | 145 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 128 | START | 128 | 256 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 136 | END | 125 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `9` | `9` | 136 | START | 136 | 215 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 141 | START | 141 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `23` | `22` | 155 | START | 155 | 180 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `18` | `18` | 166 | START | 166 | 256 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 256 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_SnapReceive` | 125 | 136 | 12 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 141 | 154 | 14 | inferred_complete_timeline |
| `Action_None` | 155 | 299 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 182 | 58 | inferred_complete_timeline |
| `Action_None` | 186 | 299 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 135 | 115 | inferred_complete_timeline |
| `Action_SplitBlock` | 136 | 215 | 80 | inferred_complete_timeline |
| `Action_SplitBlock` | 218 | 220 | 3 | inferred_complete_timeline |
| `Action_SplitBlock` | 222 | 256 | 35 | inferred_complete_timeline |
| `Action_None` | 257 | 277 | 21 | inferred_complete_timeline |
| `Action_None` | 279 | 299 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 127 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 256 | 129 | inferred_complete_timeline |
| `Action_None` | 257 | 299 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 21–145
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 127 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 145 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 21–156
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_BallSnap` | 125 | 136 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 156 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 127 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 143 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 165 | 15 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 166 | 256 | 91 | inferred_complete_timeline |
| `Action_None` | 257 | 299 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 21–293
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 127 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 181 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 256 | 74 | inferred_complete_timeline |
| `Action_None` | 257 | 289 | 33 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 21–186
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 186 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 21–195
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 162 | 38 | inferred_complete_timeline |
| `Action_None` | 164 | 195 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 21–166
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 166 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 195 | 71 | inferred_complete_timeline |
| `Action_None` | 201 | 277 | 77 | inferred_complete_timeline |
| `Action_None` | 279 | 292 | 14 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 124 | 104 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 21–51 | 20 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 83–299 | 190 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 150–299 | 140 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 156–299 | 144 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 176–204 | 6 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 178–202 | 11 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 191–299 | 109 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 205–242 | 38 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 210–299 | 89 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 254–299 | 26 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 256–259 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `25` | `26` | 162 | 164 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 128 != Inferred start 137
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `23` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 524: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 129 frames exceeds threshold 90 frames [start=128, end=256].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [125–136], lower_priority='Action_ZoneBlock' annotated_start=128, effective_Action_ZoneBlock_start=137.
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '18' (RG) duration 91 frames exceeds threshold 90 frames [start=166, end=256].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RT) duration 129 frames exceeds threshold 90 frames [start=128, end=256].
- ⚠️ Action 'Action_None' range [125-182] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-299] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-166] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-195] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-277] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-292] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-256] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-299] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [136-215] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [218-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-277] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-299] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-156] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-289] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-145] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-37] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-51] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [155-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [192-205] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [210-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-159] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-188] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-268] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
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

</details>