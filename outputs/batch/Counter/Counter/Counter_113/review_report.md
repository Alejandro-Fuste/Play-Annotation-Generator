# Play-Annotation-Generator Annotation Review — Counter_113

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_113`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `13` | `12` |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | offense | `19` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_BallCarry` | DT1 | defense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `22` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 109 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 110 | START | 110 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `12` | `11` | 113 | START | 113 | 137 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `15` | `14` | 113 | START | 122 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `4` | `3` | 113 | START | 113 | 139 |
| ✅ EXACT | `Action_PullBlock` | RG | `13` | `12` | 113 | START | 113 | 209 |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | `19` | `18` | 113 | START | 113 | 209 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 121 | END | 110 | 121 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 133 | START | 133 | 149 |
| ✅ EXACT | `Action_BallCarry` | DT1 | `11` | `10` | 150 | START | 150 | 248 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 209 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_SnapReceive` | 110 | 121 | 12 | inferred_complete_timeline |
| `Action_None` | 122 | 132 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 133 | 149 | 17 | inferred_complete_timeline |
| `Action_None` | 150 | 329 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 194 | 85 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 207 | 237 | 31 | inferred_complete_timeline |
| `Action_None` | 239 | 329 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 304 | 195 | inferred_complete_timeline |
| `Action_None` | 316 | 329 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 295 | 186 | inferred_complete_timeline |
| `Action_None` | 297 | 329 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 113 | 209 | 97 | inferred_complete_timeline |
| `Action_None` | 210 | 329 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 139 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 153 | 154 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 137 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 142 | 163 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 168 | 200 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 202 | 209 | 8 | inferred_complete_timeline |
| `Action_None` | 210 | 272 | 63 | inferred_complete_timeline |
| `Action_None` | 280 | 329 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_BallSnap` | 110 | 121 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 122 | 143 | 22 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PullBlock` | 113 | 209 | 97 | inferred_complete_timeline |
| `Action_None` | 210 | 247 | 38 | inferred_complete_timeline |
| `Action_None` | 277 | 279 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 129 | 20 | inferred_complete_timeline |
| `Action_None` | 131 | 158 | 28 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 158 | 49 | inferred_complete_timeline |
| `Action_None` | 164 | 207 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 159 | 50 | inferred_complete_timeline |
| `Action_None` | 163 | 175 | 13 | inferred_complete_timeline |
| `Action_None` | 182 | 329 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_BallCarry` | 150 | 248 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 133 | 24 | inferred_complete_timeline |
| `Action_None` | 148 | 280 | 133 | inferred_complete_timeline |
| `Action_None` | 293 | 329 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 197 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 197 | 88 | inferred_complete_timeline |
| `Action_None` | 199 | 252 | 54 | inferred_complete_timeline |
| `Action_None` | 255 | 329 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 282 | 173 | inferred_complete_timeline |
| `Action_None` | 289 | 301 | 13 | inferred_complete_timeline |
| `Action_None` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 329 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 286 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 231 | 122 | inferred_complete_timeline |
| `Action_None` | 237 | 329 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 329 | 220 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–329 | 325 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 11–12 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 152–323 | 120 | 10 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 156–206 | 35 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 196–329 | 134 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 211–329 | 105 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 215–329 | 103 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 227–329 | 103 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 246–329 | 84 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 267–329 | 62 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 270–329 | 60 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 271–273 | 3 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 271–319 | 7 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 289–329 | 34 | 4 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 317–318 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (4 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `15` (C): Annotated start 113 != Inferred start 122
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 228: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (LG) duration 97 frames exceeds threshold 90 frames [start=113, end=209].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '12' (RG) duration 97 frames exceeds threshold 90 frames [start=113, end=209].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '14' (C) duration 97 frames exceeds threshold 90 frames [start=113, end=209].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [110–121], lower_priority='Action_DownBlock' annotated_start=113, effective_Action_DownBlock_start=122.
- ⚠️ Action 'Action_None' range [110-235] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-133] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-280] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-154] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-282] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-301] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-197] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-304] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-194] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-237] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-137] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [142-163] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [168-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [202-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-272] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-247] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [122-143] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-231] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-252] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-286] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-295] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-191] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-207] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-224] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-276] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-305] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-178] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-329] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-252] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-296] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-238] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-267] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-292] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-295] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-308] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>