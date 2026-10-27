# Play-Annotation-Generator Annotation Review — Dagger_34

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_34`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 299
- **Player Tracks:** 21
- **Ball Tracks:** 0
- **Action Segments:** 67
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 4
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BreakInside` | WR | offense | `5` | `5` |
| ✅ EXACT | `Action_ClearToEdge` | Position_Unknown | Team_Unknown | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 2 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 138 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 139 | START | 139 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `9` | `9` | 142 | START | 144 | 146 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 143 | END | 139 | 143 |
| ✅ EXACT | `Action_BreakInside` | WR | `5` | `5` | 158 | START | 158 | 278 |
| ✅ EXACT | `Action_ClearToEdge` | Position_Unknown | `16` | `15` | 158 | START | 158 | 160 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `12` | `12` | 232 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 2–220
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 8 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 16 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 27 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 32 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 138 | 84 | inferred_complete_timeline |
| `Action_SnapReceive` | 139 | 143 | 5 | inferred_complete_timeline |
| `Action_None` | 144 | 174 | 31 | inferred_complete_timeline |
| `Action_None` | 176 | 220 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 173 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_BreakInside` | 158 | 278 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 182 | 44 | inferred_complete_timeline |
| `Action_None` | 189 | 299 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_BallSnap` | 139 | 143 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 150 | 152 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 155 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 18 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_None` | 139 | 299 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 167 | 29 | inferred_complete_timeline |
| `Action_None` | 170 | 173 | 4 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 12–33
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 33 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 138 | 127 | inferred_complete_timeline |
| `Action_None` | 139 | 299 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 299 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 299 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 296 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 290 | 152 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 259 | 121 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 299 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–170 | 118 | 5 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 42–160 | 55 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 157–225 | 55 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 169–299 | 116 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 178–299 | 110 | 3 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 282–299 | 16 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (3 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `12` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [139–143], lower_priority='Action_PassBlock' annotated_start=142, effective_Action_PassBlock_start=144.
- ⚠️ Segment 'Action_ThrowPass' for track '12' has invalid range: start=232, end=220. Clamping end to start.
- ⚠️ Action 'Action_None' range [139-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-167] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-182] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-296] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [158-278] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-290] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-259] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-299] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [144-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [150-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [154-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-299] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-18] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-161] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-8] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-16] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-18] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-33] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-56] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-77] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-100] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ClearToEdge' for track '15' starts at frame 158, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ClearToEdge' range [158-160] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-173] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-225] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-286] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>