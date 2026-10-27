# Play-Annotation-Generator Annotation Review — Counter_265

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_265`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 49
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB1 | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `14` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `15` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 79 | START | 79 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `1` | `0` | 82 | START | 82 | 102 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `21` | `20` | 82 | START | 94 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `22` | `21` | 82 | START | 82 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB1 | `14` | `13` | 82 | START | 82 | 131 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 93 | END | 79 | 93 |
| ✅ EXACT | `Action_BallCarry` | QB | `19` | `18` | 117 | START | 117 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 170 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_SnapReceive` | 79 | 93 | 15 | inferred_complete_timeline |
| `Action_None` | 94 | 116 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 117 | 269 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 82 | 131 | 50 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 136 | 170 | 35 | inferred_complete_timeline |
| `Action_None` | 171 | 251 | 81 | inferred_complete_timeline |
| `Action_None` | 253 | 269 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 156 | 78 | inferred_complete_timeline |
| `Action_None` | 162 | 240 | 79 | inferred_complete_timeline |
| `Action_None` | 242 | 269 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 269 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 269 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 269 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 269 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PullBlock` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 89 | 170 | 82 | inferred_complete_timeline |
| `Action_None` | 171 | 188 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_BallSnap` | 79 | 93 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 170 | 77 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 95 | 17 | inferred_complete_timeline |
| `Action_None` | 97 | 237 | 141 | inferred_complete_timeline |
| `Action_None` | 239 | 269 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_DownBlock` | 82 | 102 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 114 | 170 | 57 | inferred_complete_timeline |
| `Action_None` | 171 | 178 | 8 | inferred_complete_timeline |
| `Action_None` | 181 | 211 | 31 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 221 | 5 | inferred_complete_timeline |
| `Action_None` | 225 | 269 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 126 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 269 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 129 | 51 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 269 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 269 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 269 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 152 | 74 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 269 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 269 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 269 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 201 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 269 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 197 | 119 | inferred_complete_timeline |
| `Action_None` | 225 | 269 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 124–125 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 149–151 | 3 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 177–178 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 184–269 | 74 | 5 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 202–269 | 67 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 205–269 | 65 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 247–261 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (3 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `21` (C): Annotated start 82 != Inferred start 94
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 33 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [79–93], lower_priority='Action_DownBlock' annotated_start=82, effective_Action_DownBlock_start=94.
- ⚠️ Action 'Action_DownBlock' range [82-102] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [104-105] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-178] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-211] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-269] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-269] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-197] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [82-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-240] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-237] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [82-84] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-202] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-253] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-266] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-261] for track '28' has 1 frames without a visible bounding box.
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