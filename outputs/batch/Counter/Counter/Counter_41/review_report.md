# Play-Annotation-Generator Annotation Review — Counter_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_41`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 125 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 126 | START | 126 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `13` | `12` | 129 | START | 129 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `18` | `17` | 129 | START | 144 | 149 |
| ✅ EXACT | `Action_PullBlock` | LG | `21` | `20` | 129 | START | 129 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `5` | `4` | 129 | START | 129 | 204 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `4` | `3` | 131 | START | 131 | 173 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 143 | END | 126 | 143 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `18` | 153 | START | 153 | 173 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `3` | 174 | START | 174 | 273 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 235 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_SnapReceive` | 126 | 143 | 18 | inferred_complete_timeline |
| `Action_None` | 144 | 152 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 153 | 173 | 21 | inferred_complete_timeline |
| `Action_None` | 174 | 268 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 131 | 173 | 43 | inferred_complete_timeline |
| `Action_BallCarry` | 174 | 273 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 299 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 265 | 140 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_None` | 277 | 299 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 265 | 140 | inferred_complete_timeline |
| `Action_None` | 270 | 277 | 8 | inferred_complete_timeline |
| `Action_None` | 283 | 299 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 129 | 204 | 76 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 211 | 235 | 25 | inferred_complete_timeline |
| `Action_None` | 236 | 242 | 7 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 287 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 299 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_PullBlock` | 129 | 235 | 107 | inferred_complete_timeline |
| `Action_None` | 236 | 299 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_BallSnap` | 126 | 143 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 149 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 202 | 235 | 34 | inferred_complete_timeline |
| `Action_None` | 236 | 299 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 149 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 208 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 179 | 54 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 209 | 19 | inferred_complete_timeline |
| `Action_None` | 215 | 299 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 230 | 105 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |
| `Action_None` | 239 | 241 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 144 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 147 | 22 | inferred_complete_timeline |
| `Action_None` | 154 | 159 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 299 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 279 | 154 | inferred_complete_timeline |
| `Action_None` | 281 | 283 | 3 | inferred_complete_timeline |
| `Action_None` | 294 | 297 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 203 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 299 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 299 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 246 | 121 | inferred_complete_timeline |
| `Action_None` | 252 | 264 | 13 | inferred_complete_timeline |
| `Action_None` | 273 | 275 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 259 | 134 | inferred_complete_timeline |
| `Action_None` | 261 | 263 | 3 | inferred_complete_timeline |
| `Action_None` | 265 | 267 | 3 | inferred_complete_timeline |
| `Action_None` | 270 | 288 | 19 | inferred_complete_timeline |
| `Action_None` | 291 | 294 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 270 | 145 | inferred_complete_timeline |
| `Action_None` | 272 | 281 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 148–299 | 80 | 7 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 173–299 | 118 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 239–299 | 47 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 243–299 | 57 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 247–262 | 5 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 288–299 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (C) duration 107 frames exceeds threshold 90 frames [start=129, end=235].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [126–143], lower_priority='Action_DownBlock' annotated_start=129, effective_Action_DownBlock_start=144.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '20' (LG) duration 107 frames exceeds threshold 90 frames [start=129, end=235].
- ⚠️ Action 'Action_None' range [126-265] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [174-273] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [129-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [211-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-242] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-287] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-277] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-246] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-264] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-279] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [171-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [185-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-208] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-288] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-270] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-281] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-203] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [144-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [153-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-179] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-189] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-265] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-252] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-299] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '27' has 1 frames without a visible bounding box.
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

</details>