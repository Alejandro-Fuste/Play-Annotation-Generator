# Play-Annotation-Generator Annotation Review — SplitZone_292

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `SplitZone_292`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 57
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 26
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadEdgeDefender` | DE1 | defense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT | defense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `2` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 124 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 105 | START | 105 | 120 |
| ✅ EXACT | `Action_SplitBlock` | HB | `2` | `2` | 115 | START | 115 | 161 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 115 | START | 115 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 115 | START | 121 | 124 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `17` | 115 | START | 115 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `18` | 115 | START | 115 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 115 | START | 115 | 125 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 120 | END | 105 | 120 |
| ✅ EXACT | `Action_PressEdge` | RB | `8` | `8` | 125 | START | 125 | 148 |
| ✅ EXACT | `Action_ReadEdgeDefender` | DE1 | `10` | `10` | 129 | START | 129 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT | `14` | `14` | 138 | START | 138 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `16` | `16` | 138 | START | 138 | 163 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 139 | START | 139 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `8` | 149 | START | 149 | 179 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_SnapReceive` | 105 | 120 | 16 | inferred_complete_timeline |
| `Action_None` | 121 | 138 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 139 | 145 | 7 | inferred_complete_timeline |
| `Action_None` | 146 | 272 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PressEdge` | 125 | 148 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 149 | 179 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 181 | 184 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 190 | 197 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 200 | 329 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_SplitBlock` | 115 | 161 | 47 | inferred_complete_timeline |
| `Action_None` | 162 | 318 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 329 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–307
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 307 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 329 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–314
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 154 | 40 | inferred_complete_timeline |
| `Action_None` | 155 | 314 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 125 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 141 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_BallSnap` | 105 | 120 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 124 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 131 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 137 | 1 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 138 | 163 | 26 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 165 | 172 | 8 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 176 | 287 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 154 | 40 | inferred_complete_timeline |
| `Action_None` | 155 | 276 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 132 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 154 | 21 | inferred_complete_timeline |
| `Action_None` | 155 | 276 | 122 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 129 | 138 | 10 | inferred_complete_timeline |
| `Action_None` | 139 | 161 | 23 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 182 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 165 | 61 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_None` | 197 | 258 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 137 | 1 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 138 | 201 | 64 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 206 | 267 | 62 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 269 | 312 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 161 | 57 | inferred_complete_timeline |
| `Action_None` | 171 | 299 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 328 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 235 | 131 | inferred_complete_timeline |
| `Action_None` | 239 | 329 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 193 | 89 | inferred_complete_timeline |
| `Action_None` | 196 | 232 | 37 | inferred_complete_timeline |
| `Action_None` | 237 | 329 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 164 | 60 | inferred_complete_timeline |
| `Action_None` | 168 | 263 | 96 | inferred_complete_timeline |
| `Action_None` | 266 | 275 | 10 | inferred_complete_timeline |
| `Action_None` | 277 | 293 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 329 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 329 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 216 | 112 | inferred_complete_timeline |
| `Action_None` | 220 | 309 | 90 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 146–261 | 89 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 198–329 | 132 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 220–223 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 3 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 3 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_BlockSecondLevel' at frame 138 targets track ID '160', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 6 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '14' (DT) duration 175 frames exceeds threshold 90 frames [start=138, end=312].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '16' (C) duration 150 frames exceeds threshold 90 frames [start=138, end=287].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [105–120], lower_priority='Action_ZoneBlock' annotated_start=115, effective_Action_ZoneBlock_start=121.
- ⚠️ Action 'Action_None' range [105-235] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-314] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-318] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-232] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-165] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-258] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [149-179] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [181-184] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-216] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-309] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [129-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-161] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-328] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-307] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [138-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [206-267] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [269-312] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-164] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-263] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-275] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-293] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [105-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-131] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [138-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [165-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [176-287] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-276] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-276] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-272] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-125] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-141] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-299] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-166] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-261] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>