# Play-Annotation-Generator Annotation Review — Counter_156

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_156`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | DE1 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE1 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR1 | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF | defense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB1 | defense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `10` | `9` |
| ✅ EXACT | `Action_PullLeadBlock` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | TE | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `22` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 60 |
| ⚠️ START CHANGED | `Action_BallSnap` | DE1 | `13` | `12` | 61 | START | 64 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE1 | `13` | `12` | 66 | START | 66 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR1 | `2` | `1` | 66 | START | 66 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF | `3` | `2` | 66 | START | 66 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB1 | `8` | `7` | 66 | START | 66 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `10` | `9` | 66 | START | 66 | 70 |
| ✅ EXACT | `Action_PullLeadBlock` | QB | `6` | `5` | 66 | START | 66 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | TE | `4` | `3` | 70 | START | 70 | 98 |
| ✅ EXACT | `Action_SnapReceive` | RT | `7` | `6` | 75 | END | 61 | 75 |
| ✅ EXACT | `Action_Handoff` | RT | `7` | `6` | 85 | START | 85 | 103 |
| ✅ EXACT | `Action_BallCarry` | TE | `4` | `3` | 104 | START | 104 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 149 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 66 | 130 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 186 | 126 | inferred_complete_timeline |
| `Action_None` | 193 | 218 | 26 | inferred_complete_timeline |
| `Action_None` | 221 | 239 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_DownBlock` | 66 | 130 | 65 | inferred_complete_timeline |
| `Action_DownBlock` | 136 | 149 | 14 | inferred_complete_timeline |
| `Action_None` | 150 | 239 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 68 | 8 | inferred_complete_timeline |
| `Action_None` | 76 | 106 | 31 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 133 | 239 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 123 | 63 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 142 | 239 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 70 | 98 | 29 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 239 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 106–239
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 106 | 239 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 97–101
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 97 | 101 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PullBlock` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 77 | 87 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 107 | 149 | 43 | inferred_complete_timeline |
| `Action_None` | 150 | 226 | 77 | inferred_complete_timeline |
| `Action_None` | 228 | 239 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_SnapReceive` | 61 | 75 | 15 | inferred_complete_timeline |
| `Action_None` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 85 | 103 | 19 | inferred_complete_timeline |
| `Action_None` | 104 | 239 | 136 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 66 | 111 | 46 | inferred_complete_timeline |
| `Action_DownBlock` | 115 | 149 | 35 | inferred_complete_timeline |
| `Action_None` | 150 | 239 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 2–3
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 3 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 110 | 50 | inferred_complete_timeline |
| `Action_None` | 114 | 119 | 6 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 71 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_DownBlock` | 66 | 95 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 98 | 140 | 43 | inferred_complete_timeline |
| `Action_None` | 150 | 239 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_DownBlock` | 66 | 85 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 87 | 149 | 63 | inferred_complete_timeline |
| `Action_None` | 150 | 182 | 33 | inferred_complete_timeline |
| `Action_None` | 188 | 239 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `24` | Position_Unknown | Team_Unknown | 125–239 | 115 | 1 | Undefined position; Undefined team |
| `17` | `25` | Position_Unknown | Team_Unknown | 128–239 | 92 | 2 | Undefined position; Undefined team |
| `18` | `27` | Position_Unknown | Team_Unknown | 149–183 | 35 | 1 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 152–239 | 66 | 3 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 154–239 | 85 | 2 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 164–239 | 66 | 5 | Undefined position; Undefined team |
| `22` | `34` | Position_Unknown | Team_Unknown | 186–239 | 54 | 1 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 193–208 | 16 | 1 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 205–209 | 5 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 212–239 | 25 | 2 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 227–239 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `13` (DE1): Annotated start 61 != Inferred start 64
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '20' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [61-123] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [66-130] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [66-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [70-98] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-186] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-218] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [66-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [66-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [98-140] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-106] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [66-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [77-87] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-226] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-110] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-119] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-71] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [66-111] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-3] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-239] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-193] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-208] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-208] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-225] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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