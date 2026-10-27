# Play-Annotation-Generator Annotation Review — Counter_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_56`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `12` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 134 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `16` | `15` | 134 | START | 183 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `14` | `13` | 135 | START | 135 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `6` | `5` | 135 | START | 135 | 157 |
| ✅ EXACT | `Action_DownBlock` | LT | `7` | `6` | 135 | START | 135 | 224 |
| ✅ EXACT | `Action_PullBlock` | RG | `10` | `9` | 135 | START | 135 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `12` | `11` | 135 | START | 135 | 172 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 144 | END | 134 | 144 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 157 | START | 157 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `1` | `0` | 192 | START | 193 | 196 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 224 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–255
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_SnapReceive` | 134 | 144 | 11 | inferred_complete_timeline |
| `Action_None` | 145 | 156 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 157 | 191 | 35 | inferred_complete_timeline |
| `Action_None` | 192 | 255 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_BallCarry` | 193 | 196 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 199 | 348 | 150 | inferred_complete_timeline |
| `Action_BallCarry` | 354 | 355 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 135 | 172 | 38 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 176 | 191 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 224 | 90 | inferred_complete_timeline |
| `Action_None` | 225 | 359 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 167 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 172 | 224 | 53 | inferred_complete_timeline |
| `Action_None` | 225 | 359 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 157 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 160 | 206 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 210 | 224 | 15 | inferred_complete_timeline |
| `Action_None` | 225 | 359 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_PullBlock` | 135 | 224 | 90 | inferred_complete_timeline |
| `Action_None` | 225 | 359 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 251 | 118 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 208 | 75 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 273 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 359 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 163 | 30 | inferred_complete_timeline |
| `Action_None` | 165 | 187 | 23 | inferred_complete_timeline |
| `Action_None` | 191 | 218 | 28 | inferred_complete_timeline |
| `Action_None` | 233 | 241 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 359 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 336 | 203 | inferred_complete_timeline |
| `Action_None` | 339 | 359 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–342
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 342 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 155 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 183–359 | 174 | 3 | Undefined position; Undefined team |
| `16` | `22` | Position_Unknown | Team_Unknown | 226–359 | 134 | 1 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 236–359 | 118 | 4 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 241–255 | 6 | 2 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 245–263 | 19 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 251–359 | 107 | 2 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 255–359 | 100 | 2 | Undefined position; Undefined team |
| `22` | `34` | Position_Unknown | Team_Unknown | 275–277 | 3 | 1 | Undefined position; Undefined team |
| `23` | `37` | Position_Unknown | Team_Unknown | 294–359 | 66 | 1 | Undefined position; Undefined team |
| `24` | `38` | Position_Unknown | Team_Unknown | 316–359 | 44 | 1 | Undefined position; Undefined team |
| `25` | `41` | Position_Unknown | Team_Unknown | 327–334 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `16` (Position_Unknown): Annotated start 134 != Inferred start 183
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '15' has invalid range: start=183, end=144. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-196] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [199-348] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [354-355] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-251] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-342] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-336] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-359] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [135-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [160-206] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-187] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-218] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-241] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-208] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-273] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-359] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [157-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-255] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [135-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [176-191] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [135-167] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-155] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-251] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-328] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-346] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-263] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-298] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-262] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-359] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-334] for track '25' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>