# Play-Annotation-Generator Annotation Review — Counter_162

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_162`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 50
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | WR1 | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR1 | offense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | WR2 | offense | `1` | `0` |
| ✅ EXACT | `Action_PullLeadBlock` | DE2 | defense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | SAF1 | defense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | SAF1 | defense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `24` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_BallSnap` | WR1 | `8` | `7` | 31 | START | 31 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | QB | `7` | `6` | 37 | START | 37 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR1 | `8` | `7` | 37 | START | 37 | 57 |
| ✅ EXACT | `Action_PullBlock` | WR2 | `1` | `0` | 37 | START | 37 | 120 |
| ✅ EXACT | `Action_PullLeadBlock` | DE2 | `10` | `9` | 37 | START | 37 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `4` | `3` | 40 | START | 40 | 82 |
| ✅ EXACT | `Action_SnapReceive` | SAF1 | `13` | `12` | 45 | END | 31 | 45 |
| ✅ EXACT | `Action_Handoff` | SAF1 | `13` | `12` | 65 | START | 65 | 86 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `3` | 87 | START | 87 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 120 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_DownBlock` | 37 | 120 | 84 | inferred_complete_timeline |
| `Action_None` | 121 | 239 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 40 | 82 | 43 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 36 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 59 | 120 | 62 | inferred_complete_timeline |
| `Action_None` | 121 | 239 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PullBlock` | 37 | 120 | 84 | inferred_complete_timeline |
| `Action_None` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_None` | 129 | 239 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 81 | 51 | inferred_complete_timeline |
| `Action_None` | 89 | 239 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 239 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `24`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 107–239
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 107 | 239 | 133 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 49 | 19 | inferred_complete_timeline |
| `Action_None` | 82 | 87 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 37 | 120 | 84 | inferred_complete_timeline |
| `Action_None` | 121 | 239 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 239 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 239 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 169 | 139 | inferred_complete_timeline |
| `Action_None` | 171 | 239 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 88 | 58 | inferred_complete_timeline |
| `Action_None` | 91 | 239 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 113 | 83 | inferred_complete_timeline |
| `Action_None` | 133 | 239 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 73 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 239 | 165 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 239 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_None` | 46 | 64 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 65 | 86 | 22 | inferred_complete_timeline |
| `Action_None` | 87 | 153 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 221 | 191 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–239 | 239 | 3 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 99–239 | 140 | 2 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 124–239 | 116 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 125–127 | 3 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 137–239 | 103 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 145–146 | 2 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 150–239 | 90 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 25 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '22' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '20' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [121-123] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-81] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-88] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [40-82] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [84-86] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-221] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [37-57] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-73] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-169] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-113] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-153] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-239] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>