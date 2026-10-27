# Play-Annotation-Generator Annotation Review — Counter_248

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_248`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 147
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `18` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `15` | `14` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 11 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 103 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `16` | 102 | START | 102 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `18` | `16` | 104 | START | 116 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `6` | `5` | 104 | START | 104 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `9` | `8` | 104 | START | 104 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `15` | `14` | 104 | START | 104 | 121 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `8` | `7` | 104 | START | 104 | 163 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 115 | END | 102 | 115 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 130 | START | 130 | 150 |
| ✅ EXACT | `Action_BallCarry` | RB | `16` | `15` | 151 | START | 151 | 181 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 206 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_SnapReceive` | 102 | 115 | 14 | inferred_complete_timeline |
| `Action_None` | 116 | 129 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 130 | 150 | 21 | inferred_complete_timeline |
| `Action_None` | 151 | 248 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_BallCarry` | 151 | 181 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 104 | 163 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_DownBlock` | 104 | 139 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 154 | 182 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 184 | 201 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_DownBlock` | 104 | 128 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 141 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 11–198
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 101 | 91 | inferred_complete_timeline |
| `Action_BallSnap` | 102 | 115 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 137 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 145 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 149 | 158 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 162 | 169 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 189 | 194 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 196 | 198 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PullBlock` | 104 | 121 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 124 | 127 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 135 | 139 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 142 | 206 | 65 | inferred_complete_timeline |
| `Action_None` | 207 | 329 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 195 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 138 | 37 | inferred_complete_timeline |
| `Action_None` | 141 | 155 | 15 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_None` | 187 | 189 | 3 | inferred_complete_timeline |
| `Action_None` | 193 | 233 | 41 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 246 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 196 | 95 | inferred_complete_timeline |
| `Action_None` | 201 | 329 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 131 | 30 | inferred_complete_timeline |
| `Action_None` | 133 | 223 | 91 | inferred_complete_timeline |
| `Action_None` | 225 | 230 | 6 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 186 | 85 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 223 | 33 | inferred_complete_timeline |
| `Action_None` | 228 | 329 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 125 | 24 | inferred_complete_timeline |
| `Action_None` | 128 | 261 | 134 | inferred_complete_timeline |
| `Action_None` | 270 | 329 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 268 | 167 | inferred_complete_timeline |
| `Action_None` | 270 | 329 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 137 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–189 | 172 | 3 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–240 | 241 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 91–156 | 62 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 107–316 | 204 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 117–188 | 8 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 128–329 | 189 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 161–257 | 81 | 6 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 181–329 | 149 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 183–192 | 10 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 184–328 | 132 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 196–329 | 131 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 199–329 | 128 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 199–329 | 131 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 223–252 | 30 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 230–312 | 55 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 244–245 | 2 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 251–327 | 77 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 291–323 | 24 | 7 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 291–329 | 39 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 294–329 | 36 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 298–304 | 7 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 304–305 | 2 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 309–317 | 9 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 315–318 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (7 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `15` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 90 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 498: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '5' (LT) duration 98 frames exceeds threshold 90 frames [start=104, end=201].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '14' (RG) duration 103 frames exceeds threshold 90 frames [start=104, end=206].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '16' (C) duration 95 frames exceeds threshold 90 frames [start=104, end=198].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [102–115], lower_priority='Action_DownBlock' annotated_start=104, effective_Action_DownBlock_start=116.
- ⚠️ Action 'Action_None' range [102-196] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-138] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-155] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-233] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-137] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-195] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-131] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-223] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [104-139] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [145-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [151-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [154-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [184-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-189] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [104-163] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [104-128] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [132-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [135-141] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-268] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-240] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-248] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-186] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-223] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [104-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [124-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [131-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [135-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [151-181] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-137] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [139-145] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [149-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [162-169] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [184-186] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [189-194] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [196-198] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-117] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-316] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-172] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-209] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-257] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-328] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-221] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-252] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-282] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-327] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-298] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-323] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-317] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>