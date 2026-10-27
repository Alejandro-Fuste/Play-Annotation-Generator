# Play-Annotation-Generator Annotation Review — Counter_139

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_139`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 84
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
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT1 | defense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 58 | START | 58 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `19` | `18` | 62 | START | 62 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `20` | `19` | 62 | START | 73 | 78 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `9` | `8` | 62 | START | 62 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `22` | `21` | 62 | START | 62 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT1 | `14` | `13` | 62 | START | 62 | 104 |
| ✅ EXACT | `Action_SnapReceive` | RB | `21` | `20` | 72 | END | 58 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `21` | `20` | 97 | START | 97 | 126 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 159 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 72 | 15 | inferred_complete_timeline |
| `Action_None` | 73 | 96 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 126 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 139 | 239 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 132 | 75 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 213 | 156 | inferred_complete_timeline |
| `Action_None` | 219 | 239 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 80 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 83 | 108 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 181 | 183 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_BallSnap` | 58 | 72 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 73 | 78 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 81 | 101 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 105 | 159 | 55 | inferred_complete_timeline |
| `Action_None` | 160 | 239 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PullBlock` | 62 | 72 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 89 | 107 | 19 | inferred_complete_timeline |
| `Action_PullBlock` | 109 | 118 | 10 | inferred_complete_timeline |
| `Action_PullBlock` | 120 | 159 | 40 | inferred_complete_timeline |
| `Action_None` | 160 | 239 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 103 | 46 | inferred_complete_timeline |
| `Action_None` | 176 | 179 | 4 | inferred_complete_timeline |
| `Action_None` | 181 | 187 | 7 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 239 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 179 | 122 | inferred_complete_timeline |
| `Action_None` | 181 | 192 | 12 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 62 | 104 | 43 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 106 | 159 | 54 | inferred_complete_timeline |
| `Action_None` | 160 | 224 | 65 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 81 | 24 | inferred_complete_timeline |
| `Action_None` | 89 | 239 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 177 | 120 | inferred_complete_timeline |
| `Action_None` | 210 | 222 | 13 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 237 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 157 | 100 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 211 | 154 | inferred_complete_timeline |
| `Action_None` | 217 | 239 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–116 | 117 | 2 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–236 | 237 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 71–222 | 122 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 93–239 | 133 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 120–239 | 120 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 129–239 | 99 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 131–134 | 4 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 218–237 | 20 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 225–237 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 280: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ Row 280: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (Unknown) duration 98 frames exceeds threshold 90 frames [start=62, end=159].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (LG) duration 98 frames exceeds threshold 90 frames [start=62, end=159].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (C) duration 98 frames exceeds threshold 90 frames [start=62, end=159].
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [58–72], lower_priority='Action_DownBlock' annotated_start=62, effective_Action_DownBlock_start=73.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '21' (RG) duration 98 frames exceeds threshold 90 frames [start=62, end=159].
- ⚠️ Action 'Action_None' range [58-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-132] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-213] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-237] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-192] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-236] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-211] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-103] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [62-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-224] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [83-108] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [118-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [58-72] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [73-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [81-101] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [97-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [139-239] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [62-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [85-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [89-107] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [109-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-218] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-208] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-227] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-239] for track '25' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-237] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-237] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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