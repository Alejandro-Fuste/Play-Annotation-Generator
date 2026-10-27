# Play-Annotation-Generator Annotation Review — Counter_339

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_339`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `21` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | defense | `22` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `17` | `16` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 11 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 29 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `14` | `13` | 76 | START | 76 | 80 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `14` | `13` | 79 | START | 123 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | `16` | `15` | 79 | START | 79 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `21` | `18` | 79 | START | 79 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | `22` | `19` | 79 | START | 95 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `17` | `16` | 79 | START | 79 | 80 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `9` | `8` | 85 | START | 85 | 111 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 87 | END | 76 | 87 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 108 | START | 108 | 118 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `9` | `8` | 119 | START | 132 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 194 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_SnapReceive` | 76 | 87 | 12 | inferred_complete_timeline |
| `Action_None` | 88 | 107 | 20 | inferred_complete_timeline |
| `Action_Handoff` | 108 | 118 | 11 | inferred_complete_timeline |
| `Action_None` | 119 | 132 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 85 | 111 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 132 | 239 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 224 | 149 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 222 | 147 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 239 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 19 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 41 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 78 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 85 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 132 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 75 | 6 | inferred_complete_timeline |
| `Action_None` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_None` | 116 | 151 | 36 | inferred_complete_timeline |
| `Action_None` | 155 | 220 | 66 | inferred_complete_timeline |
| `Action_None` | 228 | 239 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 29–156
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 32 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 39 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 156 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_BallSnap` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 123 | 149 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 11–114
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 39 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 94 | 114 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 239 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `22`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 29–239
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 32 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 95 | 111 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 115 | 150 | 36 | inferred_complete_timeline |
| `Action_PullBlock` | 153 | 194 | 42 | inferred_complete_timeline |
| `Action_None` | 195 | 239 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 111 | 36 | inferred_complete_timeline |
| `Action_None` | 117 | 127 | 11 | inferred_complete_timeline |
| `Action_None` | 132 | 237 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–37
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 30 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 37 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 75 | 52 | inferred_complete_timeline |
| `Action_None` | 76 | 101 | 26 | inferred_complete_timeline |
| `Action_None` | 106 | 193 | 88 | inferred_complete_timeline |
| `Action_None` | 196 | 199 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 202 | 127 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_None` | 214 | 218 | 5 | inferred_complete_timeline |
| `Action_None` | 231 | 234 | 4 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 239 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 239 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 223 | 148 | inferred_complete_timeline |
| `Action_None` | 228 | 239 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 11–239 | 135 | 6 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 52–239 | 167 | 6 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 96–106 | 10 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 102–162 | 47 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 116–238 | 101 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 117–239 | 122 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 118–239 | 115 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 142–239 | 93 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 163–238 | 75 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 172–239 | 63 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 181–239 | 59 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 210–217 | 8 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 230–231 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 232–239 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `14` (2 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `14` (C): Annotated start 79 != Inferred start 123
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `17` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `9` (RB): Annotated start 119 != Inferred start 132

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 680: Duplicate assignment for track ID '22' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [76–87], lower_priority='Action_DownBlock' annotated_start=79, effective_Action_DownBlock_start=88.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '19' (DT1) duration 116 frames exceeds threshold 90 frames [start=79, end=194].
- ⚠️ Action 'Action_None' range [76-222] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-202] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-224] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-30] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-37] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [85-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-101] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-193] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-111] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-237] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [76-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [83-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [123-149] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 76, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [76-80] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-151] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-220] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-19] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-41] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-85] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-19] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [79-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [94-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-15] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-108] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-32] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-39] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [82-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [95-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [115-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [153-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-172] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-220] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-228] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-239] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-203] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-213] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-238] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-217] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>