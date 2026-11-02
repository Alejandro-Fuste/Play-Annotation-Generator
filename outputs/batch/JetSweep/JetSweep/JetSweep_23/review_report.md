# Play-Annotation-Generator Annotation Review — JetSweep_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_23`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 26
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 4
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | RB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `9` | `8` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `15` | `14` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `17` | `16` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `17` | `16` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `19` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `14` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 5 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `4` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `9` | `Group` | 0 | START | 0 | 53 |
| ✅ EXACT | `Action_JetMotion` | WR | `9` | `8` | 54 | START | 54 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `15` | `14` | 75 | START | 75 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | QB | `10` | `9` | 77 | START | 77 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 77 | START | 87 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `15` | 77 | START | 77 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `17` | `16` | 77 | START | 77 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `18` | 77 | START | 77 | 102 |
| ✅ EXACT | `Action_SnapReceive` | RB | `7` | `6` | 86 | END | 75 | 86 |
| ✅ EXACT | `Action_Toss` | RB | `7` | `6` | 92 | START | 92 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | `17` | `16` | 98 | START | 98 | 98 |
| ✅ EXACT | `Action_BallCarry` | WR | `9` | `8` | 106 | START | 106 | 219 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `15` | `14` | 144 | BOUNDARY | 111 | 144 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `17` | `16` | 144 | BOUNDARY | 104 | 144 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `17` | `16` | 144 | BOUNDARY | 104 | 144 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `19` | `18` | 144 | BOUNDARY | 134 | 144 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_LeadBlock` | 77 | 133 | 57 | inferred_complete_timeline |
| `Action_LeadBlock` | 137 | 144 | 8 | inferred_complete_timeline |
| `Action_None` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_None` | 158 | 239 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_SnapReceive` | 75 | 86 | 12 | inferred_complete_timeline |
| `Action_None` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_Toss` | 92 | 105 | 14 | inferred_complete_timeline |
| `Action_None` | 106 | 239 | 134 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 239 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 237 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_JetMotion` | 54 | 105 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 219 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 168 | 94 | inferred_complete_timeline |
| `Action_None` | 177 | 198 | 22 | inferred_complete_timeline |
| `Action_None` | 201 | 215 | 15 | inferred_complete_timeline |
| `Action_None` | 217 | 221 | 5 | inferred_complete_timeline |
| `Action_None` | 224 | 228 | 5 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 5–148
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 102 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 123 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 144 | 11 | inferred_complete_timeline |
| `Action_None` | 145 | 148 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 98 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 123 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_BallSnap` | 75 | 80 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 86 | 86 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 87 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 144 | 34 | inferred_complete_timeline |
| `Action_None` | 145 | 239 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 97 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 98 | 98 | 1 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 104 | 144 | 41 | inferred_complete_timeline |
| `Action_None` | 146 | 239 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 239 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 155 | 81 | inferred_complete_timeline |
| `Action_None` | 164 | 216 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 144 | 70 | inferred_complete_timeline |
| `Action_None` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_None` | 154 | 183 | 30 | inferred_complete_timeline |
| `Action_None` | 187 | 199 | 13 | inferred_complete_timeline |
| `Action_None` | 201 | 229 | 29 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 190 | 116 | inferred_complete_timeline |
| `Action_None` | 192 | 218 | 27 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 229 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 239 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 212 | 138 | inferred_complete_timeline |
| `Action_None` | 215 | 236 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 151 | 77 | inferred_complete_timeline |
| `Action_None` | 153 | 239 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 4–239 | 213 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 5–236 | 215 | 7 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 5–105 | 89 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 28–239 | 163 | 10 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 111–239 | 103 | 8 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 136–239 | 104 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 157–181 | 25 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 163–239 | 77 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 209–212 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [75–86], lower_priority='Action_ZoneBlock' annotated_start=77, effective_Action_ZoneBlock_start=87.
- ⚠️ Action 'Action_None' range [75-190] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-218] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-237] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-212] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-236] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-219] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [77-133] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-229] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-183] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-168] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-198] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-215] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [75-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [82-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '14' starts at frame 87, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [87-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-98] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' for track '16' starts at frame 98, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BlockSecondLevel' range [98-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [104-144] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-91] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-229] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-102] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-69] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-87] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-153] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-208] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-236] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-66] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-91] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-32] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-62] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-146] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-226] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-181] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>