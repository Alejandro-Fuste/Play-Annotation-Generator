# Play-Annotation-Generator Annotation Review — SplitZone_143

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_143`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `22` | `21` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 15 | START | 16 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 15 | START | 16 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 15 | START | 16 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 15 | START | 16 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 15 | START | 16 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 15 | START | 16 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 15 | START | 16 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 15 | START | 16 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 15 | START | 16 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 15 | START | 16 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 15 | START | 16 | 84 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `7` | 85 | START | 85 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 88 | START | 88 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `19` | 88 | START | 88 | 134 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 88 | START | 88 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `22` | `21` | 88 | START | 88 | 190 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `7` | `7` | 88 | START | 97 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `5` | `5` | 95 | START | 95 | 136 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `4` | 96 | END | 85 | 96 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `4` | 100 | START | 100 | 125 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `20` | `20` | 112 | START | 112 | 190 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `3` | `3` | 126 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 190 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 16–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_SnapReceive` | 85 | 96 | 12 | inferred_complete_timeline |
| `Action_None` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 100 | 125 | 26 | inferred_complete_timeline |
| `Action_None` | 126 | 299 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 16–118
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 118 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 16–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 285 | 201 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 16–276
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 270 | 186 | inferred_complete_timeline |
| `Action_None` | 272 | 276 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 16–177
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 94 | 79 | inferred_complete_timeline |
| `Action_SplitBlock` | 95 | 136 | 42 | inferred_complete_timeline |
| `Action_SplitBlock` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_SplitBlock` | 150 | 154 | 5 | inferred_complete_timeline |
| `Action_SplitBlock` | 156 | 177 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 16–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 185 | 101 | inferred_complete_timeline |
| `Action_None` | 187 | 299 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 16–152
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 87 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 134 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 152 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 16–144
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 87 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 111 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 144 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 16–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_BallSnap` | 85 | 96 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 190 | 94 | inferred_complete_timeline |
| `Action_None` | 191 | 299 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 16–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 87 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 111 | 24 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 112 | 190 | 79 | inferred_complete_timeline |
| `Action_None` | 191 | 299 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 16–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 87 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 190 | 103 | inferred_complete_timeline |
| `Action_None` | 191 | 299 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 299 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 224 | 140 | inferred_complete_timeline |
| `Action_None` | 228 | 299 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 246 | 162 | inferred_complete_timeline |
| `Action_None` | 249 | 255 | 7 | inferred_complete_timeline |
| `Action_None` | 257 | 299 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 109 | 25 | inferred_complete_timeline |
| `Action_None` | 114 | 175 | 62 | inferred_complete_timeline |
| `Action_None` | 177 | 299 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 174 | 90 | inferred_complete_timeline |
| `Action_None` | 180 | 299 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 299 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 299 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 299 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 174 | 90 | inferred_complete_timeline |
| `Action_None` | 181 | 185 | 5 | inferred_complete_timeline |
| `Action_None` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_None` | 202 | 299 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 16–293
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 293 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 84 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 165 | 81 | inferred_complete_timeline |
| `Action_None` | 170 | 299 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 122–299 | 178 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 137–150 | 11 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 163–228 | 66 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 170–299 | 130 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 176–299 | 124 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 207–299 | 81 | 5 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 231–233 | 3 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 236–299 | 64 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 247–299 | 49 | 3 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `7` (C): Annotated start 88 != Inferred start 97
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `5` (4 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `3` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '3' has invalid range: start=126, end=118. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (C) duration 103 frames exceeds threshold 90 frames [start=88, end=190].
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [85–96], lower_priority='Action_ZoneBlock' annotated_start=88, effective_Action_ZoneBlock_start=97.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 103 frames exceeds threshold 90 frames [start=88, end=190].
- ⚠️ Action 'Action_None' range [85-270] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-285] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [95-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [141-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [150-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [156-177] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-185] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-293] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-224] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-299] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-174] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-246] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-255] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-134] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-228] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-299] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-225] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-244] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-254] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-283] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-261] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-299] for track '30' has 2 frames without a visible bounding box.
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