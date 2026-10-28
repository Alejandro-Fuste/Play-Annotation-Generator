# Play-Annotation-Generator Annotation Review — Draw_48

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_48`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 55
- **Validation Warnings:** 54
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 36
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 31 | START | 31 | 44 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `13` | `12` | 34 | START | 45 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `3` | `2` | 34 | START | 34 | 109 |
| ✅ EXACT | `Action_PassBlock` | RT | `4` | `3` | 34 | START | 34 | 109 |
| ✅ EXACT | `Action_PassBlock` | LG | `6` | `5` | 34 | START | 34 | 97 |
| ✅ EXACT | `Action_PassBlock` | RG | `8` | `7` | 34 | START | 34 | 109 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 44 | END | 31 | 44 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `2` | `1` | 49 | START | 49 | 85 |
| ✅ EXACT | `Action_BallCarry` | QB | `2` | `1` | 86 | START | 86 | 96 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 109 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 44 | 14 | inferred_complete_timeline |
| `Action_None` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 49 | 85 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 86 | 96 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 123 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 109 | 76 | inferred_complete_timeline |
| `Action_None` | 110 | 242 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 97 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 44 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 109 | 65 | inferred_complete_timeline |
| `Action_None` | 110 | 237 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 109 | 76 | inferred_complete_timeline |
| `Action_None` | 110 | 280 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 109 | 76 | inferred_complete_timeline |
| `Action_None` | 110 | 271 | 162 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 228 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 110 | 80 | inferred_complete_timeline |
| `Action_None` | 112 | 299 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 91 | 61 | inferred_complete_timeline |
| `Action_None` | 99 | 263 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 148 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 155 | 125 | inferred_complete_timeline |
| `Action_None` | 159 | 279 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 256 | 226 | inferred_complete_timeline |
| `Action_None` | 260 | 275 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 107 | 77 | inferred_complete_timeline |
| `Action_None` | 110 | 257 | 148 | inferred_complete_timeline |
| `Action_None` | 274 | 299 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `19` | Position_Unknown | Team_Unknown | 90–271 | 178 | 2 | Undefined position; Undefined team |
| `15` | `21` | Position_Unknown | Team_Unknown | 100–295 | 196 | 1 | Undefined position; Undefined team |
| `16` | `24` | Position_Unknown | Team_Unknown | 151–299 | 149 | 1 | Undefined position; Undefined team |
| `17` | `25` | Position_Unknown | Team_Unknown | 158–263 | 106 | 1 | Undefined position; Undefined team |
| `18` | `32` | Position_Unknown | Team_Unknown | 190–299 | 110 | 1 | Undefined position; Undefined team |
| `19` | `34` | Position_Unknown | Team_Unknown | 191–192 | 2 | 1 | Undefined position; Undefined team |
| `20` | `35` | Position_Unknown | Team_Unknown | 193–299 | 98 | 2 | Undefined position; Undefined team |
| `21` | `40` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `22` | `41` | Position_Unknown | Team_Unknown | 229–299 | 71 | 1 | Undefined position; Undefined team |
| `23` | `42` | Position_Unknown | Team_Unknown | 240–247 | 8 | 1 | Undefined position; Undefined team |
| `24` | `43` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `13` (C): Annotated start 34 != Inferred start 45
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 30 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [31–44], lower_priority='Action_PassBlock' annotated_start=34, effective_Action_PassBlock_start=45.
- ⚠️ Action 'Action_None' range [31-256] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-275] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [86-96] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-109] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-271] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-155] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-279] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-280] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-228] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-257] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-237] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-148] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-271] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-295] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-247] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-247] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>