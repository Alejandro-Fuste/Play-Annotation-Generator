# Play-Annotation-Generator Annotation Review — Counter_271

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_271`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 15 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `3` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 95 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 96 | START | 96 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | `18` | `17` | 99 | START | 99 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `20` | `19` | 99 | START | 112 | 126 |
| ✅ EXACT | `Action_DownBlock` | LT | `22` | `21` | 99 | START | 99 | 112 |
| ✅ EXACT | `Action_PullBlock` | RG | `21` | `20` | 99 | START | 99 | 168 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | `3` | `2` | 99 | START | 99 | 155 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 111 | END | 96 | 111 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 128 | START | 128 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `2` | `1` | 139 | START | 139 | 181 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 168 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_SnapReceive` | 96 | 111 | 16 | inferred_complete_timeline |
| `Action_None` | 112 | 127 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 128 | 138 | 11 | inferred_complete_timeline |
| `Action_None` | 139 | 239 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_BallCarry` | 139 | 181 | 43 | inferred_complete_timeline |
| `Action_BallCarry` | 189 | 239 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 99 | 155 | 57 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 158 | 168 | 11 | inferred_complete_timeline |
| `Action_None` | 169 | 239 | 71 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 239 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 239 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_DownBlock` | 99 | 159 | 61 | inferred_complete_timeline |
| `Action_DownBlock` | 162 | 168 | 7 | inferred_complete_timeline |
| `Action_None` | 169 | 191 | 23 | inferred_complete_timeline |
| `Action_None` | 195 | 239 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 15–112
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 98 | 84 | inferred_complete_timeline |
| `Action_DownBlock` | 99 | 112 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 104 | 9 | inferred_complete_timeline |
| `Action_None` | 109 | 135 | 27 | inferred_complete_timeline |
| `Action_None` | 138 | 143 | 6 | inferred_complete_timeline |
| `Action_None` | 148 | 239 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_BallSnap` | 96 | 111 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 126 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 128 | 132 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 136 | 157 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 186 | 14 | inferred_complete_timeline |
| `Action_None` | 195 | 197 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_PullBlock` | 99 | 168 | 70 | inferred_complete_timeline |
| `Action_None` | 169 | 230 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 118 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 118 | 23 | inferred_complete_timeline |
| `Action_None` | 125 | 130 | 6 | inferred_complete_timeline |
| `Action_None` | 138 | 141 | 4 | inferred_complete_timeline |
| `Action_None` | 145 | 157 | 13 | inferred_complete_timeline |
| `Action_None` | 159 | 239 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 224 | 129 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 239 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 239 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 107 | 12 | inferred_complete_timeline |
| `Action_None` | 109 | 129 | 21 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 239 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 166 | 71 | inferred_complete_timeline |
| `Action_None` | 171 | 180 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 188 | 93 | inferred_complete_timeline |
| `Action_None` | 191 | 200 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 239 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 239 | 144 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 159–239 | 81 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 173–239 | 67 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 182–206 | 19 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 190–224 | 24 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 197–239 | 43 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 208–239 | 32 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 222–231 | 7 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 544: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [96–111], lower_priority='Action_DownBlock' annotated_start=99, effective_Action_DownBlock_start=112.
- ⚠️ Action 'Action_BallCarry' range [139-181] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [99-155] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-224] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-239] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-129] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-118] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-157] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-188] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-200] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [99-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-191] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-135] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [112-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [128-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [136-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [99-112] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '28' has 1 frames without a visible bounding box.
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

</details>