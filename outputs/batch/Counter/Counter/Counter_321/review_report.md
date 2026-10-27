# Play-Annotation-Generator Annotation Review — Counter_321

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_321`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `23` | `22` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 0 | START | 13 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 110 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 111 | START | 111 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `17` | `16` | 114 | START | 114 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `18` | `17` | 114 | START | 114 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `9` | `8` | 114 | START | 125 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `23` | `22` | 114 | START | 114 | 149 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `13` | `12` | 114 | START | 114 | 220 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 124 | END | 111 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `10` | `9` | 151 | START | 151 | 200 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 220 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_SnapReceive` | 111 | 124 | 14 | inferred_complete_timeline |
| `Action_None` | 125 | 150 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 151 | 200 | 50 | inferred_complete_timeline |
| `Action_BallCarry` | 202 | 299 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 219 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 299 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 299 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 264 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 156 | 180 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_DownBlock` | 114 | 126 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 220 | 86 | inferred_complete_timeline |
| `Action_None` | 221 | 264 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_BallSnap` | 111 | 124 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 144 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 146 | 220 | 75 | inferred_complete_timeline |
| `Action_None` | 221 | 261 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 13–200
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 113 | 101 | inferred_complete_timeline |
| `Action_PullBlock` | 114 | 149 | 36 | inferred_complete_timeline |
| `Action_PullBlock` | 168 | 200 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 114 | 220 | 107 | inferred_complete_timeline |
| `Action_None` | 221 | 299 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 158 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 133 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 160 | 50 | inferred_complete_timeline |
| `Action_None` | 172 | 176 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 156 | 46 | inferred_complete_timeline |
| `Action_None` | 158 | 178 | 21 | inferred_complete_timeline |
| `Action_None` | 185 | 299 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 173 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 185 | 75 | inferred_complete_timeline |
| `Action_None` | 208 | 299 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 169 | 59 | inferred_complete_timeline |
| `Action_None` | 173 | 185 | 13 | inferred_complete_timeline |
| `Action_None` | 187 | 259 | 73 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 299 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 189 | 79 | inferred_complete_timeline |
| `Action_None` | 192 | 196 | 5 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 206 | 299 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 299 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 110 | 7 | inferred_complete_timeline |
| `Action_None` | 111 | 117 | 7 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 196 | 69 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 206 | 290 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 299 | 189 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–299 | 283 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–14 | 15 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 146–156 | 11 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 148–162 | 13 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 166–266 | 87 | 4 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 188–299 | 112 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 207–299 | 93 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 208–299 | 92 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 208–299 | 92 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 253–254 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 253–255 | 3 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 253–254 | 2 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `23` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (C) duration 107 frames exceeds threshold 90 frames [start=114, end=220].
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [111–124], lower_priority='Action_DownBlock' annotated_start=114, effective_Action_DownBlock_start=125.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '16' (LG) duration 107 frames exceeds threshold 90 frames [start=114, end=220].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (Unknown) duration 107 frames exceeds threshold 90 frames [start=114, end=220].
- ⚠️ Action 'Action_None' range [111-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-185] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-259] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-299] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-185] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [125-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [146-220] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-261] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [151-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [202-299] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [114-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-130] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-264] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [114-157] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [172-178] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [182-220] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-110] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 111, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [111-117] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-290] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [114-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [168-200] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-157] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-178] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-266] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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