# Play-Annotation-Generator Annotation Review — Counter_235

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_235`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `26` | `24` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | offense | `4` | `3` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 0 | START | 0 | 51 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `26` | `24` | 52 | START | 109 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `14` | `13` | 54 | START | 54 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `17` | `16` | 54 | START | 54 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `22` | `21` | 54 | START | 54 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `21` | `20` | 54 | START | 54 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | `4` | `3` | 54 | START | 54 | 173 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `8` | `7` | 56 | START | 56 | 104 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 68 | END | 52 | 68 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `19` | 83 | START | 83 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `7` | 105 | START | 105 | 156 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 175 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_SnapReceive` | 52 | 68 | 17 | inferred_complete_timeline |
| `Action_None` | 69 | 82 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 83 | 104 | 22 | inferred_complete_timeline |
| `Action_None` | 105 | 299 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 56 | 104 | 49 | inferred_complete_timeline |
| `Action_BallCarry` | 105 | 156 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 159 | 168 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 170 | 271 | 102 | inferred_complete_timeline |
| `Action_BallCarry` | 275 | 299 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 236 | 185 | inferred_complete_timeline |
| `Action_None` | 244 | 269 | 26 | inferred_complete_timeline |
| `Action_None` | 274 | 299 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 299 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 172 | 121 | inferred_complete_timeline |
| `Action_None` | 174 | 299 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 54 | 173 | 120 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 175 | 175 | 1 | inferred_complete_timeline |
| `Action_None` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_DownBlock` | 54 | 94 | 41 | inferred_complete_timeline |
| `Action_DownBlock` | 96 | 175 | 80 | inferred_complete_timeline |
| `Action_None` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_DownBlock` | 54 | 130 | 77 | inferred_complete_timeline |
| `Action_DownBlock` | 148 | 175 | 28 | inferred_complete_timeline |
| `Action_None` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_DownBlock` | 54 | 88 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 95 | 98 | 4 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PullBlock` | 54 | 104 | 51 | inferred_complete_timeline |
| `Action_PullBlock` | 106 | 115 | 10 | inferred_complete_timeline |
| `Action_PullBlock` | 118 | 168 | 51 | inferred_complete_timeline |
| `Action_None` | 188 | 192 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 102 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 172 | 121 | inferred_complete_timeline |
| `Action_None` | 174 | 187 | 14 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 299 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 186 | 135 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 299 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 94 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 104 | 53 | inferred_complete_timeline |
| `Action_None` | 109 | 299 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 78 | 27 | inferred_complete_timeline |
| `Action_None` | 82 | 299 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 215 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 299 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 299 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 299 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 299 | 248 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 67–86 | 19 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 100–115 | 14 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 109–115 | 5 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 136–194 | 55 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 178–299 | 120 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 192–224 | 33 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 199–201 | 3 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 205–234 | 30 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 209–212 | 4 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 222–299 | 78 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 223–299 | 77 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 243–299 | 57 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 245–248 | 4 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 247–299 | 53 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 257–276 | 20 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 267–274 | 6 | 2 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 289–293 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `26` (Position_Unknown): Annotated start 52 != Inferred start 109
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 472: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (LT) duration 122 frames exceeds threshold 90 frames [start=54, end=175].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '16' (LG) duration 122 frames exceeds threshold 90 frames [start=54, end=175].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '20' (RG) duration 122 frames exceeds threshold 90 frames [start=54, end=175].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (C) duration 122 frames exceeds threshold 90 frames [start=54, end=175].
- ⚠️ Segment 'Action_BallSnap' for track '24' has invalid range: start=109, end=68. Clamping end to start.
- ⚠️ Action 'Action_None' range [52-172] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-187] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-104] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-299] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [54-173] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-236] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [105-156] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-168] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-271] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-299] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-102] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [54-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-186] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [54-130] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [83-104] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [54-104] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [106-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [118-168] for track '20' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [54-88] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [95-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-82] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-115] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '24' starts at frame 110, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [110-110] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-194] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-224] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-234] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-276] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>