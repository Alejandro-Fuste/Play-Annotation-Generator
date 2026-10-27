# Play-Annotation-Generator Annotation Review — Counter_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_61`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 61
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `16` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 131 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 127 | START | 127 | 148 |
| ✅ EXACT | `Action_DownBlock` | LT | `15` | `14` | 132 | START | 132 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `18` | `17` | 132 | START | 149 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 132 | START | 132 | 142 |
| ✅ EXACT | `Action_PullBlock` | LG | `22` | `21` | 132 | START | 132 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `6` | `5` | 132 | START | 132 | 190 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 148 | END | 127 | 148 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 153 | START | 153 | 168 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `13` | `12` | 169 | START | 169 | 252 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 212 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_SnapReceive` | 127 | 148 | 22 | inferred_complete_timeline |
| `Action_None` | 149 | 152 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 153 | 168 | 16 | inferred_complete_timeline |
| `Action_None` | 169 | 269 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 252 | 84 | inferred_complete_timeline |
| `Action_BallCarry` | 254 | 255 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 269 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 269 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 132 | 190 | 59 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 197 | 212 | 16 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 212 | 81 | inferred_complete_timeline |
| `Action_None` | 213 | 230 | 18 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |
| `Action_None` | 237 | 269 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_PullBlock` | 132 | 212 | 81 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_BallSnap` | 127 | 148 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 149 | 163 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 168 | 173 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 175 | 181 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 142 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 151 | 25 | inferred_complete_timeline |
| `Action_None` | 153 | 198 | 46 | inferred_complete_timeline |
| `Action_None` | 210 | 256 | 47 | inferred_complete_timeline |
| `Action_None` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 198 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 269 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 176 | 50 | inferred_complete_timeline |
| `Action_None` | 180 | 269 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 260 | 134 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 197 | 71 | inferred_complete_timeline |
| `Action_None` | 218 | 269 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 203 | 77 | inferred_complete_timeline |
| `Action_None` | 206 | 266 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 246 | 120 | inferred_complete_timeline |
| `Action_None` | 249 | 254 | 6 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 269 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 269 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 219 | 93 | inferred_complete_timeline |
| `Action_None` | 222 | 269 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–269 | 268 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–267 | 268 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 202–269 | 68 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 220–269 | 50 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 223–269 | 45 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 232–269 | 20 | 4 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 247–248 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 124: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 124: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [127–148], lower_priority='Action_DownBlock' annotated_start=132, effective_Action_DownBlock_start=149.
- ⚠️ Action 'Action_None' range [127-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-260] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-198] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [132-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-246] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-254] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-266] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-269] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-252] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [254-255] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-198] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-256] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [149-163] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [165-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [168-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [175-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-267] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [132-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [156-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [132-212] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-237] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>