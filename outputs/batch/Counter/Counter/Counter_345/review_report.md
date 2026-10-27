# Play-Annotation-Generator Annotation Review — Counter_345

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_345`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `2` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_BallSnap` | C | `3` | `2` | 22 | START | 22 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `18` | `17` | 25 | START | 25 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `19` | `18` | 25 | START | 25 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `3` | `2` | 25 | START | 37 | 39 |
| ✅ EXACT | `Action_PullBlock` | LG | `22` | `21` | 25 | START | 25 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | `2` | `1` | 25 | START | 25 | 91 |
| ✅ EXACT | `Action_SnapReceive` | RB | `15` | `14` | 36 | END | 22 | 36 |
| ✅ EXACT | `Action_Handoff` | RB | `15` | `14` | 44 | START | 44 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `13` | `12` | 72 | START | 72 | 193 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 120 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 36 | 15 | inferred_complete_timeline |
| `Action_None` | 37 | 43 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 44 | 71 | 28 | inferred_complete_timeline |
| `Action_None` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 25 | 91 | 67 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 93 | 98 | 6 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 101 | 108 | 8 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 121 | 121 | 1 | inferred_complete_timeline |
| `Action_None` | 138 | 239 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PullBlock` | 25 | 120 | 96 | inferred_complete_timeline |
| `Action_None` | 121 | 239 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 36 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 37 | 39 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 49 | 55 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 73 | 92 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 106 | 120 | 15 | inferred_complete_timeline |
| `Action_None` | 121 | 227 | 107 | inferred_complete_timeline |
| `Action_None` | 231 | 233 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 25 | 73 | 49 | inferred_complete_timeline |
| `Action_DownBlock` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 102 | 105 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 25 | 69 | 45 | inferred_complete_timeline |
| `Action_DownBlock` | 89 | 100 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 120 | 9 | inferred_complete_timeline |
| `Action_None` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_None` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 94 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 107 | 86 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 114 | 124 | 11 | inferred_complete_timeline |
| `Action_None` | 126 | 137 | 12 | inferred_complete_timeline |
| `Action_None` | 139 | 160 | 22 | inferred_complete_timeline |
| `Action_None` | 164 | 189 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 118 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 129 | 108 | inferred_complete_timeline |
| `Action_None` | 133 | 153 | 21 | inferred_complete_timeline |
| `Action_None` | 155 | 166 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 131 | 110 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 201 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 204 | 183 | inferred_complete_timeline |
| `Action_None` | 206 | 219 | 14 | inferred_complete_timeline |
| `Action_None` | 223 | 239 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–239 | 220 | 4 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–239 | 236 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 60–114 | 13 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 98–113 | 16 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 127–239 | 113 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 142–239 | 77 | 7 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 157–239 | 80 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 169–234 | 64 | 3 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 203–239 | 32 | 2 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 208–239 | 32 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 211–213 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `2` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 691: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 692: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 692: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '2' (C) duration 96 frames exceeds threshold 90 frames [start=25, end=120].
- ⚠️ Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [22–36], lower_priority='Action_DownBlock' annotated_start=25, effective_Action_DownBlock_start=37.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (RT) duration 96 frames exceeds threshold 90 frames [start=25, end=120].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '21' (LG) duration 96 frames exceeds threshold 90 frames [start=25, end=120].
- ⚠️ Action 'Action_PullLeadBlock' range [25-91] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [93-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [101-108] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '1' starts at frame 121, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [121-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [37-39] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [49-55] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [73-92] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [106-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-227] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-118] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-124] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-160] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-189] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [72-193] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [197-211] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [229-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-94] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [25-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [80-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [102-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [25-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [89-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [112-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-219] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-185] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-179] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-231] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>