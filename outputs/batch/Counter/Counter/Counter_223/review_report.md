# Play-Annotation-Generator Annotation Review — Counter_223

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_223`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `14` | `13` |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | offense | `10` | `9` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 31 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 32 | START | 32 | 48 |
| ✅ EXACT | `Action_DownBlock` | RT | `13` | `12` | 35 | START | 35 | 137 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `21` | `20` | 35 | START | 49 | 137 |
| ✅ EXACT | `Action_PullBlock` | RG | `14` | `13` | 35 | START | 35 | 111 |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | `10` | `9` | 35 | START | 35 | 90 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `11` | `10` | 38 | START | 38 | 77 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 48 | END | 32 | 48 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `15` | 71 | START | 71 | 83 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `11` | `10` | 84 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 137 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_None` | 49 | 70 | 22 | inferred_complete_timeline |
| `Action_Handoff` | 71 | 83 | 13 | inferred_complete_timeline |
| `Action_None` | 84 | 239 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 38 | 77 | 40 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 103 | 72 | inferred_complete_timeline |
| `Action_None` | 105 | 129 | 25 | inferred_complete_timeline |
| `Action_None` | 131 | 146 | 16 | inferred_complete_timeline |
| `Action_None` | 149 | 239 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 35 | 90 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 100 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 49 | 137 | 89 | inferred_complete_timeline |
| `Action_None` | 138 | 239 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PullBlock` | 35 | 111 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 35 | 137 | 103 | inferred_complete_timeline |
| `Action_None` | 138 | 184 | 47 | inferred_complete_timeline |
| `Action_None` | 192 | 239 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 85 | 54 | inferred_complete_timeline |
| `Action_None` | 93 | 131 | 39 | inferred_complete_timeline |
| `Action_None` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_None` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_None` | 149 | 158 | 10 | inferred_complete_timeline |
| `Action_None` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 79 | 48 | inferred_complete_timeline |
| `Action_None` | 81 | 239 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 92 | 61 | inferred_complete_timeline |
| `Action_None` | 97 | 119 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 128 | 97 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 164 | 133 | inferred_complete_timeline |
| `Action_None` | 174 | 239 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 180 | 149 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–93 | 76 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 48–61 | 7 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 70–239 | 86 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 76–239 | 163 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 84–91 | 8 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 87–169 | 51 | 6 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 95–96 | 2 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 96–239 | 144 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 116–239 | 124 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 119–122 | 4 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 120–239 | 41 | 8 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 123–238 | 116 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 125–191 | 67 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 131–178 | 9 | 3 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 136–166 | 9 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 155–239 | 84 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 177–221 | 22 | 3 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 181–239 | 55 | 2 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 183–239 | 54 | 2 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 183–184 | 2 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 211–216 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `21` (C): Annotated start 35 != Inferred start 49
- ❌ Missing segment for action `Action_BallCarry` on target `11` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 448: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '10' has invalid range: start=84, end=77. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (RT) duration 103 frames exceeds threshold 90 frames [start=35, end=137].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (C) duration 103 frames exceeds threshold 90 frames [start=35, end=137].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [32–48], lower_priority='Action_DownBlock' annotated_start=35, effective_Action_DownBlock_start=49.
- ⚠️ Action 'Action_None' range [32-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-103] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-129] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-128] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-92] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [35-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [38-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-184] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [35-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-131] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-239] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-100] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-61] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-174] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-91] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-105] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-148] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-138] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-214] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-238] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-191] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-166] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-191] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-221] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-232] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-191] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>