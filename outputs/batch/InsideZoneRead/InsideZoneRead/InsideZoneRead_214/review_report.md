# Play-Annotation-Generator Annotation Review — InsideZoneRead_214

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_214`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 17 | START | 12 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 17 | START | 12 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 17 | START | 12 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `17` | `Group` | 17 | START | 12 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 17 | START | 12 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 17 | START | 12 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 17 | START | 12 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 17 | START | 12 | 124 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 122 | START | 122 | 136 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `12` | 125 | START | 125 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 125 | START | 145 | 146 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 125 | START | 125 | 193 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 137 | END | 122 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `12` | `11` | 144 | START | 144 | 154 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `13` | `12` | 161 | START | 161 | 193 |
| ✅ EXACT | `Action_BallCarry` | QB | `12` | `11` | 167 | START | 167 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 193 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_SnapReceive` | 122 | 137 | 16 | inferred_complete_timeline |
| `Action_None` | 138 | 143 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_ReadDefender` | 159 | 166 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 167 | 299 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 12–275
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 275 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 237 | 116 | inferred_complete_timeline |
| `Action_None` | 243 | 299 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 12–162
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 162 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 124 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 160 | 36 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 161 | 193 | 33 | inferred_complete_timeline |
| `Action_None` | 194 | 206 | 13 | inferred_complete_timeline |
| `Action_None` | 211 | 233 | 23 | inferred_complete_timeline |
| `Action_None` | 235 | 299 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 12–189
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_BallSnap` | 122 | 136 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 184 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 189 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 124 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 193 | 69 | inferred_complete_timeline |
| `Action_None` | 194 | 299 | 106 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 12–251
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 239 | 118 | inferred_complete_timeline |
| `Action_None` | 241 | 251 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 12–221
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 209 | 88 | inferred_complete_timeline |
| `Action_None` | 219 | 221 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–268
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 268 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 209 | 88 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 299 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 121 | 110 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 12–299 | 288 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 12–299 | 288 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 12–285 | 209 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 12–298 | 170 | 14 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 191–202 | 8 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 195–299 | 105 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 253–299 | 41 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 257–286 | 30 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 277–281 | 5 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 280–299 | 18 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 285–294 | 9 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 428: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ Row 428: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ Row 428: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [122–137], lower_priority='Action_ZoneBlock' annotated_start=125, effective_Action_ZoneBlock_start=138.
- ⚠️ Action 'Action_None' range [122-237] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-299] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-209] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-251] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [144-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-233] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-177] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-231] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-162] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [122-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [149-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [188-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-275] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-14] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-29] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-41] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-50] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-58] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-115] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '22' starts at frame 122, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [122-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-231] for track '22' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-264] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-286] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-294] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>