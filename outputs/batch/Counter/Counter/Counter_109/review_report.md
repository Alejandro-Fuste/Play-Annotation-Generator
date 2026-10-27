# Play-Annotation-Generator Annotation Review — Counter_109

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_109`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 46
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF | defense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_PullLeadBlock` | DT1 | defense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 86 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 87 | START | 87 | 100 |
| ✅ EXACT | `Action_DownBlock` | LT | `13` | `12` | 87 | START | 87 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF | `5` | `4` | 87 | START | 87 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `19` | `18` | 89 | START | 101 | 146 |
| ✅ EXACT | `Action_PullLeadBlock` | DT1 | `2` | `1` | 89 | START | 89 | 176 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 100 | END | 87 | 100 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `3` | 124 | START | 124 | 138 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `5` | 139 | START | 139 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 176 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_SnapReceive` | 87 | 100 | 14 | inferred_complete_timeline |
| `Action_None` | 101 | 123 | 23 | inferred_complete_timeline |
| `Action_Handoff` | 124 | 138 | 15 | inferred_complete_timeline |
| `Action_None` | 139 | 188 | 50 | inferred_complete_timeline |
| `Action_None` | 193 | 198 | 6 | inferred_complete_timeline |
| `Action_None` | 200 | 239 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_BallCarry` | 139 | 239 | 101 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_DownBlock` | 87 | 176 | 90 | inferred_complete_timeline |
| `Action_None` | 177 | 201 | 25 | inferred_complete_timeline |
| `Action_None` | 203 | 239 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_BallSnap` | 87 | 100 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 101 | 146 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_None` | 177 | 239 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 126 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 199 | 113 | inferred_complete_timeline |
| `Action_None` | 201 | 239 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 89 | 176 | 88 | inferred_complete_timeline |
| `Action_None` | 177 | 182 | 6 | inferred_complete_timeline |
| `Action_None` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_None` | 188 | 239 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 190 | 104 | inferred_complete_timeline |
| `Action_None` | 195 | 239 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 205 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_DownBlock` | 87 | 142 | 56 | inferred_complete_timeline |
| `Action_DownBlock` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 150 | 164 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 166 | 176 | 11 | inferred_complete_timeline |
| `Action_None` | 177 | 233 | 57 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 215 | 129 | inferred_complete_timeline |
| `Action_None` | 218 | 229 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–239 | 237 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 211–237 | 15 | 3 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 214–239 | 21 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `19` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 31 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 220: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 220: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 220: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [87–100], lower_priority='Action_PullBlock' annotated_start=89, effective_Action_PullBlock_start=101.
- ⚠️ Action 'Action_None' range [177-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-126] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-188] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [87-142] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [146-148] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [150-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [166-176] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-233] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [139-239] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-215] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-239] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [101-146] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [148-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [158-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [172-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-226] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>