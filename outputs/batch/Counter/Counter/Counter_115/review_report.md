# Play-Annotation-Generator Annotation Review — Counter_115

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_115`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | SAF1 | defense | `17` | `16` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 3 | START | 3 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 3 | START | 3 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 3 | START | 3 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 3 | START | 3 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 3 | START | 3 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 3 | START | 3 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 3 | START | 3 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 3 | START | 3 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 3 | START | 3 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 3 | START | 3 | 138 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 136 | START | 136 | 151 |
| ✅ EXACT | `Action_DownBlock` | RT | `12` | `11` | 139 | START | 139 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 139 | START | 152 | 226 |
| ✅ EXACT | `Action_DownBlock` | RG | `22` | `21` | 139 | START | 139 | 148 |
| ✅ EXACT | `Action_PullBlock` | SAF1 | `17` | `16` | 139 | START | 139 | 239 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `6` | `5` | 139 | START | 139 | 239 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 151 | END | 136 | 151 |
| ✅ EXACT | `Action_BallCarry` | QB | `11` | `10` | 170 | START | 170 | 298 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 239 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 3–298
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_SnapReceive` | 136 | 151 | 16 | inferred_complete_timeline |
| `Action_None` | 152 | 169 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 170 | 298 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 299 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 265 | 130 | inferred_complete_timeline |
| `Action_None` | 270 | 299 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 3–296
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 296 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 138 | 136 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 139 | 239 | 101 | inferred_complete_timeline |
| `Action_None` | 240 | 299 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 3–216
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 216 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 3–200
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 200 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_BallSnap` | 136 | 151 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 226 | 75 | inferred_complete_timeline |
| `Action_DownBlock` | 228 | 239 | 12 | inferred_complete_timeline |
| `Action_None` | 240 | 297 | 58 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 3–148
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 138 | 136 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 148 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 138 | 136 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 239 | 101 | inferred_complete_timeline |
| `Action_None` | 240 | 299 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 175 | 40 | inferred_complete_timeline |
| `Action_None` | 183 | 299 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 3–174
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 174 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–189
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 171 | 36 | inferred_complete_timeline |
| `Action_None` | 186 | 189 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 200 | 65 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 299 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 299 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 213 | 78 | inferred_complete_timeline |
| `Action_None` | 216 | 299 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 299 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 3–252
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 223 | 88 | inferred_complete_timeline |
| `Action_None` | 229 | 252 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 299 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 138 | 136 | inferred_complete_timeline |
| `Action_PullBlock` | 139 | 239 | 101 | inferred_complete_timeline |
| `Action_None` | 240 | 299 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 136 | 299 | 164 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 3–299 | 294 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 144–299 | 132 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 173–299 | 125 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 216–233 | 18 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 220–299 | 73 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 238–242 | 5 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 246–260 | 15 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 250–253 | 4 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 253–294 | 37 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 257–299 | 28 | 5 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 273–299 | 27 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 278–287 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (RT) duration 101 frames exceeds threshold 90 frames [start=139, end=239].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (C) duration 101 frames exceeds threshold 90 frames [start=139, end=239].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [136–151], lower_priority='Action_DownBlock' annotated_start=139, effective_Action_DownBlock_start=152.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '16' (SAF1) duration 101 frames exceeds threshold 90 frames [start=139, end=239].
- ⚠️ Action 'Action_None' range [136-174] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-296] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-233] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-276] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-265] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-223] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-252] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-171] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-298] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [152-226] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-297] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-299] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-216] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [139-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-198] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-299] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-233] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-260] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-294] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-292] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>