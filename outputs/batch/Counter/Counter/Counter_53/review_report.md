# Play-Annotation-Generator Annotation Review — Counter_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_53`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `6` | `5` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `2` | `1` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 89 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 90 | START | 90 | 103 |
| ✅ EXACT | `Action_DownBlock` | RG | `22` | `21` | 97 | START | 97 | 116 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `6` | `5` | 97 | START | 97 | 182 |
| ✅ EXACT | `Action_PullBlock` | LG | `15` | `14` | 97 | START | 97 | 182 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `2` | `1` | 97 | START | 97 | 164 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `4` | `3` | 102 | START | 102 | 129 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 103 | END | 90 | 103 |
| ✅ EXACT | `Action_Handoff` | QB | `3` | `2` | 116 | START | 116 | 129 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `3` | 130 | START | 130 | 238 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 182 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_SnapReceive` | 90 | 103 | 14 | inferred_complete_timeline |
| `Action_None` | 104 | 115 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 116 | 129 | 14 | inferred_complete_timeline |
| `Action_None` | 130 | 239 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 102 | 129 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 238 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 238 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 97 | 164 | 68 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 171 | 182 | 12 | inferred_complete_timeline |
| `Action_None` | 183 | 239 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PullBlock` | 97 | 182 | 86 | inferred_complete_timeline |
| `Action_None` | 183 | 239 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_BallSnap` | 90 | 103 | 14 | inferred_complete_timeline |
| `Action_None` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_None` | 117 | 154 | 38 | inferred_complete_timeline |
| `Action_None` | 156 | 238 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 116 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 161 | 72 | inferred_complete_timeline |
| `Action_None` | 165 | 174 | 10 | inferred_complete_timeline |
| `Action_None` | 179 | 239 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 156 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 220 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 181 | 92 | inferred_complete_timeline |
| `Action_None` | 186 | 224 | 39 | inferred_complete_timeline |
| `Action_None` | 228 | 236 | 9 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 141 | 52 | inferred_complete_timeline |
| `Action_None` | 143 | 155 | 13 | inferred_complete_timeline |
| `Action_None` | 165 | 221 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–239 | 240 | 3 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–29 | 13 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 146–239 | 94 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 173–239 | 64 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 192–214 | 14 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 217–239 | 23 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 222–239 | 12 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 223–227 | 5 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 227–239 | 7 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 229–239 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 34 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 108: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [90-238] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [97-164] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [171-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [97-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-154] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-238] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-220] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-239] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-221] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-181] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-236] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [97-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-9] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-29] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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