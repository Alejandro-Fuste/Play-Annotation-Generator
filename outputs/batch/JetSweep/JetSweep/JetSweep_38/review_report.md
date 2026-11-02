# Play-Annotation-Generator Annotation Review — JetSweep_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_38`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 57
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 28
- **Exact Matches:** 10
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `5` | `4` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | LB | defense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | LB | defense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `5` | `4` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `18` | `17` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `18` | `17` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `19` | `18` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `7` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_JetMotion` | WR | `5` | `4` | 60 | START | 60 | 110 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 81 | START | 81 | 90 |
| ✅ EXACT | `Action_LeadBlock` | RB | `15` | `14` | 82 | START | 82 | 162 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `13` | 82 | START | 82 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 82 | START | 91 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `18` | 82 | START | 82 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `19` | 82 | START | 82 | 162 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `6` | 82 | START | 82 | 162 |
| ✅ EXACT | `Action_SnapReceive` | LB | `16` | `15` | 90 | END | 81 | 90 |
| ✅ EXACT | `Action_Toss` | LB | `16` | `15` | 96 | START | 96 | 110 |
| ✅ EXACT | `Action_BallCarry` | WR | `5` | `4` | 111 | START | 111 | 239 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `18` | `17` | 111 | START | 111 | 162 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `14` | `13` | 162 | BOUNDARY | 82 | 162 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `18` | `17` | 162 | BOUNDARY | 111 | 162 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `19` | `18` | 162 | BOUNDARY | 112 | 162 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `20` | `19` | 162 | BOUNDARY | 82 | 162 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `7` | `6` | 162 | BOUNDARY | 82 | 162 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_LeadBlock` | 82 | 162 | 81 | inferred_complete_timeline |
| `Action_None` | 163 | 234 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 221 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 239 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 205 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_JetMotion` | 60 | 110 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 111 | 239 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 109 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 162 | 51 | inferred_complete_timeline |
| `Action_None` | 163 | 230 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 162 | 81 | inferred_complete_timeline |
| `Action_None` | 163 | 239 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_BallSnap` | 81 | 90 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 93 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 110 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 111 | 162 | 52 | inferred_complete_timeline |
| `Action_None` | 163 | 239 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 162 | 81 | inferred_complete_timeline |
| `Action_None` | 163 | 239 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 162 | 81 | inferred_complete_timeline |
| `Action_None` | 163 | 239 | 77 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 238 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 239 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 239 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 114 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 155 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 225 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 146 | 66 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 230 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_SnapReceive` | 81 | 90 | 10 | inferred_complete_timeline |
| `Action_None` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_Toss` | 96 | 110 | 15 | inferred_complete_timeline |
| `Action_None` | 111 | 222 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 185 | 105 | inferred_complete_timeline |
| `Action_None` | 187 | 195 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 213 | 133 | inferred_complete_timeline |
| `Action_None` | 218 | 224 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 239 | 159 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–207 | 208 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 67–97 | 31 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 140–230 | 83 | 6 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 198–239 | 36 | 2 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 208–237 | 30 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 210–219 | 9 | 2 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 223–239 | 17 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 78: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [81–90], lower_priority='Action_ZoneBlock' annotated_start=82, effective_Action_ZoneBlock_start=91.
- ⚠️ Action 'Action_None' range [81-221] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-155] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-213] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-195] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-234] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-222] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-109] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-230] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-114] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-215] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-227] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>