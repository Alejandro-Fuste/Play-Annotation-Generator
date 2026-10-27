# Play-Annotation-Generator Annotation Review — Counter_182

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_182`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | OLB | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | OLB | defense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | WR4 | offense | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | CB2 | defense | `8` | `7` |
| ✅ EXACT | `Action_PullLeadBlock` | DE1 | defense | `9` | `8` |
| ✅ EXACT | `Action_PlaySideFakeStep` | CB3 | defense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | SAF2 | defense | `4` | `3` |
| ✅ EXACT | `Action_Handoff` | SAF2 | defense | `4` | `3` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | CB3 | defense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `12` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 46 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `22` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 105 |
| ✅ EXACT | `Action_BallSnap` | OLB | `13` | `12` | 106 | START | 106 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `10` | `9` | 108 | START | 108 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | OLB | `13` | `12` | 108 | START | 109 | 118 |
| ✅ EXACT | `Action_DownBlock` | WR4 | `3` | `2` | 108 | START | 108 | 202 |
| ✅ EXACT | `Action_PullBlock` | CB2 | `8` | `7` | 108 | START | 108 | 134 |
| ✅ EXACT | `Action_PullLeadBlock` | DE1 | `9` | `8` | 108 | START | 108 | 130 |
| ✅ EXACT | `Action_PlaySideFakeStep` | CB3 | `5` | `4` | 112 | START | 112 | 123 |
| ✅ EXACT | `Action_SnapReceive` | SAF2 | `4` | `3` | 120 | END | 106 | 120 |
| ✅ EXACT | `Action_Handoff` | SAF2 | `4` | `3` | 130 | START | 130 | 144 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | CB3 | `5` | `4` | 145 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 202 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 46–230
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 46 | 105 | 60 | inferred_complete_timeline |
| `Action_None` | 106 | 230 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 213 | 108 | inferred_complete_timeline |
| `Action_None` | 227 | 329 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 179 | 74 | inferred_complete_timeline |
| `Action_None` | 181 | 329 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 105 | 87 | inferred_complete_timeline |
| `Action_None` | 106 | 329 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 202 | 95 | inferred_complete_timeline |
| `Action_None` | 203 | 220 | 18 | inferred_complete_timeline |
| `Action_None` | 232 | 329 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 142 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 182–185
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 182 | 185 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 188–193
- **Visible Samples:** 6

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 188 | 193 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 124 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 146 | 202 | 57 | inferred_complete_timeline |
| `Action_None` | 203 | 329 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 108 | 130 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 275 | 170 | inferred_complete_timeline |
| `Action_None` | 278 | 324 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 105 | 98 | inferred_complete_timeline |
| `Action_None` | 106 | 131 | 26 | inferred_complete_timeline |
| `Action_None` | 133 | 244 | 112 | inferred_complete_timeline |
| `Action_None` | 247 | 329 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 174–329
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 174 | 195 | 22 | inferred_complete_timeline |
| `Action_None` | 198 | 329 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 159 | 54 | inferred_complete_timeline |
| `Action_None` | 165 | 187 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 45 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 82 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 92 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 106 | 106 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 109 | 118 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 160 | 202 | 43 | inferred_complete_timeline |
| `Action_None` | 203 | 235 | 33 | inferred_complete_timeline |
| `Action_None` | 238 | 312 | 75 | inferred_complete_timeline |
| `Action_None` | 319 | 329 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 134–329
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 134 | 142 | 9 | inferred_complete_timeline |
| `Action_None` | 148 | 188 | 41 | inferred_complete_timeline |
| `Action_None` | 196 | 329 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PullBlock` | 108 | 134 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 112 | 123 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 145–311
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 145 | 159 | 15 | inferred_complete_timeline |
| `Action_None` | 179 | 202 | 24 | inferred_complete_timeline |
| `Action_None` | 205 | 311 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_SnapReceive` | 106 | 120 | 15 | inferred_complete_timeline |
| `Action_None` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 130 | 144 | 15 | inferred_complete_timeline |
| `Action_None` | 145 | 155 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 146–329 | 175 | 8 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 195–329 | 121 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 201–329 | 120 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 240–329 | 90 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 245–329 | 85 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 267–329 | 63 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 293–294 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `5` (CB3)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 366: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '2' (WR4) duration 95 frames exceeds threshold 90 frames [start=108, end=202].
- ⚠️ Segment 'Action_BallCarry' for track '4' has invalid range: start=145, end=123. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '9' (RT) duration 95 frames exceeds threshold 90 frames [start=108, end=202].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (OLB) duration 95 frames exceeds threshold 90 frames [start=108, end=202].
- ⚠️ Action 'Action_None' range [106-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-187] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-179] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-220] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-155] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [112-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-275] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-324] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [108-134] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [108-130] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-124] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-45] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-82] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' for track '12' starts at frame 106, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallSnap' range [106-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [109-118] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [160-202] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-235] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-312] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-244] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-188] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-202] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-311] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-196] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-219] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-234] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-195] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-306] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-317] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>