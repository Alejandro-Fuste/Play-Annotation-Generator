# Play-Annotation-Generator Annotation Review — Counter_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_23`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_DownBlock` | WR2 | offense | `1` | `0` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `19` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `14` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 102 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 103 | START | 103 | 116 |
| ✅ EXACT | `Action_DownBlock` | WR2 | `1` | `0` | 113 | START | 113 | 218 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `10` | `9` | 113 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `20` | `19` | 113 | START | 113 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `18` | `17` | 113 | START | 113 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `19` | `18` | 113 | START | 190 | 195 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 118 | END | 103 | 118 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 132 | START | 132 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 147 | START | 147 | 168 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 218 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_SnapReceive` | 103 | 118 | 16 | inferred_complete_timeline |
| `Action_None` | 119 | 131 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 132 | 146 | 15 | inferred_complete_timeline |
| `Action_None` | 147 | 287 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_BallCarry` | 147 | 168 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 177 | 286 | 110 | inferred_complete_timeline |
| `Action_BallCarry` | 291 | 294 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 299 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 218 | 106 | inferred_complete_timeline |
| `Action_None` | 219 | 299 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 115 | 13 | inferred_complete_timeline |
| `Action_None` | 203 | 231 | 29 | inferred_complete_timeline |
| `Action_None` | 233 | 235 | 3 | inferred_complete_timeline |
| `Action_None` | 238 | 269 | 32 | inferred_complete_timeline |
| `Action_None` | 276 | 294 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 113 | 11 | inferred_complete_timeline |
| `Action_None` | 139 | 144 | 6 | inferred_complete_timeline |
| `Action_None` | 148 | 180 | 33 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 138 | 141 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_BallSnap` | 103 | 116 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PullBlock` | 113 | 115 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 135 | 144 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 190 | 195 | 6 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 201 | 218 | 18 | inferred_complete_timeline |
| `Action_None` | 219 | 231 | 13 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 294 | 55 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 127 | 25 | inferred_complete_timeline |
| `Action_None` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_None` | 135 | 144 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 121 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 112 | 10 | inferred_complete_timeline |
| `Action_None` | 202 | 231 | 30 | inferred_complete_timeline |
| `Action_None` | 240 | 244 | 5 | inferred_complete_timeline |
| `Action_None` | 246 | 299 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 142 | 40 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 173 | 181 | 9 | inferred_complete_timeline |
| `Action_None` | 183 | 187 | 5 | inferred_complete_timeline |
| `Action_None` | 201 | 277 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 159 | 57 | inferred_complete_timeline |
| `Action_None` | 205 | 224 | 20 | inferred_complete_timeline |
| `Action_None` | 244 | 273 | 30 | inferred_complete_timeline |
| `Action_None` | 275 | 299 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 174 | 72 | inferred_complete_timeline |
| `Action_None` | 177 | 187 | 11 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 193 | 199 | 7 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_None` | 205 | 221 | 17 | inferred_complete_timeline |
| `Action_None` | 227 | 297 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 299 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 299 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 198 | 96 | inferred_complete_timeline |
| `Action_None` | 202 | 206 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 299 | 197 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 3–297 | 190 | 8 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 48–299 | 156 | 7 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 135–141 | 5 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 151–152 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 174–182 | 7 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 183–286 | 103 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 202–299 | 98 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 203–299 | 95 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 206–298 | 81 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 210–293 | 83 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 217–288 | 71 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 240–268 | 22 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `10` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 48: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '0' (WR2) duration 106 frames exceeds threshold 90 frames [start=113, end=218].
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [103–116], lower_priority='Action_DownBlock' annotated_start=113, effective_Action_DownBlock_start=117.
- ⚠️ Action 'Action_None' range [103-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-273] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [147-168] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [177-286] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [291-294] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-174] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-221] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-297] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-198] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-287] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [103-116] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-231] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-269] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-294] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-127] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-113] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-231] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-277] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [113-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [117-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [135-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [190-195] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-231] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-294] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [138-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-75] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-108] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-277] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-297] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-211] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-231] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-192] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-286] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-231] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-213] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-266] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-293] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-290] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-231] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-288] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-258] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '31' has 1 frames without a visible bounding box.
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