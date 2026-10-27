# Play-Annotation-Generator Annotation Review — Counter_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_3`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 153
- **Validation Warnings:** 178
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 122
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB3 | defense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE1 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | offense | `1` | `0` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | LB3 | defense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_BallSnap` | CB3 | `13` | `12` | 82 | START | 82 | 96 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 96 | END | 82 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `15` | `14` | 99 | START | 99 | 109 |
| ✅ EXACT | `Action_DownBlock` | LG | `20` | `19` | 99 | START | 99 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE1 | `3` | `2` | 99 | START | 99 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `22` | `21` | 103 | START | 103 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | `1` | `0` | 103 | START | 103 | 164 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 111 | START | 111 | 124 |
| ✅ EXACT | `Action_BallCarry` | LB3 | `5` | `4` | 125 | START | 125 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 176 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_SnapReceive` | 82 | 96 | 15 | inferred_complete_timeline |
| `Action_None` | 97 | 110 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 111 | 124 | 14 | inferred_complete_timeline |
| `Action_None` | 125 | 247 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 250 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 264 | 183 | inferred_complete_timeline |
| `Action_None` | 267 | 273 | 7 | inferred_complete_timeline |
| `Action_None` | 276 | 329 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_DownBlock` | 99 | 130 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 134 | 136 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 103 | 164 | 62 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 177 | 282 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_DownBlock` | 99 | 109 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 111 | 114 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 119 | 176 | 58 | inferred_complete_timeline |
| `Action_None` | 177 | 259 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_DownBlock` | 99 | 110 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 96 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PullBlock` | 103 | 166 | 64 | inferred_complete_timeline |
| `Action_PullBlock` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 177 | 329 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 100 | 19 | inferred_complete_timeline |
| `Action_None` | 140 | 147 | 8 | inferred_complete_timeline |
| `Action_None` | 155 | 245 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 106 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 142 | 61 | inferred_complete_timeline |
| `Action_None` | 146 | 157 | 12 | inferred_complete_timeline |
| `Action_None` | 159 | 260 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 124 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 297 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 215 | 134 | inferred_complete_timeline |
| `Action_None` | 218 | 229 | 12 | inferred_complete_timeline |
| `Action_None` | 231 | 233 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 124 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 125 | 329 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 329 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 133 | 52 | inferred_complete_timeline |
| `Action_None` | 145 | 148 | 4 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_None` | 156 | 182 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_BallSnap` | 82 | 96 | 15 | inferred_complete_timeline |
| `Action_None` | 97 | 329 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 277 | 196 | inferred_complete_timeline |
| `Action_None` | 279 | 282 | 4 | inferred_complete_timeline |
| `Action_None` | 284 | 329 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 329 | 248 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–146 | 147 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 41–258 | 59 | 14 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 130–277 | 128 | 3 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 152–261 | 110 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 161–258 | 96 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 170–247 | 69 | 5 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 170–208 | 11 | 4 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 176–211 | 21 | 3 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 197–216 | 16 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 198–229 | 8 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 206–295 | 13 | 5 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 209–271 | 30 | 9 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 214–222 | 9 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 216–273 | 58 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 218–297 | 13 | 4 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 221–258 | 38 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 222–271 | 44 | 2 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 227–329 | 103 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 232–300 | 34 | 5 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 232–251 | 20 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 234–329 | 89 | 2 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 240–246 | 6 | 2 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 248–259 | 5 | 2 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 257–329 | 73 | 1 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 259–329 | 71 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 274–277 | 4 | 1 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 281–282 | 2 | 1 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 293–294 | 2 | 1 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 317–325 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 116 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 8: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PullLeadBlock' range [103-164] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-282] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-157] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-260] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [99-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [134-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [146-147] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [150-151] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-250] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-297] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-264] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-273] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-146] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-124] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-247] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [99-109] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [111-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-259] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-215] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-229] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-245] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-277] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-329] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [99-110] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-182] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [103-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-46] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-74] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '22' starts at frame 82, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [82-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-271] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-261] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-197] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-229] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-247] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-205] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-205] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-271] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-222] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-273] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-258] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-260] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-271] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-242] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-289] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-251] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-329] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.

</details>