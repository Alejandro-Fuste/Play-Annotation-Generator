# Play-Annotation-Generator Annotation Review — Counter_319

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_319`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT2 | defense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `15` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 100 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 98 | START | 98 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `21` | `20` | 101 | START | 101 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `22` | `21` | 101 | START | 109 | 146 |
| ✅ EXACT | `Action_PullBlock` | RG | `9` | `8` | 101 | START | 101 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT2 | `17` | `16` | 101 | START | 101 | 136 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 108 | END | 98 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `19` | `18` | 131 | START | 131 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `15` | 151 | START | 151 | 293 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 203 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–270
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_SnapReceive` | 98 | 108 | 11 | inferred_complete_timeline |
| `Action_None` | 109 | 130 | 22 | inferred_complete_timeline |
| `Action_Handoff` | 131 | 138 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 140 | 150 | 11 | inferred_complete_timeline |
| `Action_None` | 151 | 196 | 46 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 270 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 150 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 151 | 293 | 143 | inferred_complete_timeline |
| `Action_BallCarry` | 295 | 299 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 263 | 166 | inferred_complete_timeline |
| `Action_None` | 265 | 279 | 15 | inferred_complete_timeline |
| `Action_None` | 281 | 289 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 272 | 175 | inferred_complete_timeline |
| `Action_None` | 283 | 299 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 299 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 299 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 160 | 63 | inferred_complete_timeline |
| `Action_None` | 164 | 175 | 12 | inferred_complete_timeline |
| `Action_None` | 177 | 192 | 16 | inferred_complete_timeline |
| `Action_None` | 196 | 220 | 25 | inferred_complete_timeline |
| `Action_None` | 229 | 234 | 6 | inferred_complete_timeline |
| `Action_None` | 236 | 259 | 24 | inferred_complete_timeline |
| `Action_None` | 267 | 272 | 6 | inferred_complete_timeline |
| `Action_None` | 274 | 299 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_DownBlock` | 101 | 133 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 137 | 144 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 146 | 203 | 58 | inferred_complete_timeline |
| `Action_None` | 204 | 251 | 48 | inferred_complete_timeline |
| `Action_None` | 267 | 273 | 7 | inferred_complete_timeline |
| `Action_None` | 278 | 283 | 6 | inferred_complete_timeline |
| `Action_None` | 288 | 289 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_BallSnap` | 98 | 108 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 109 | 146 | 38 | inferred_complete_timeline |
| `Action_DownBlock` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 155 | 203 | 49 | inferred_complete_timeline |
| `Action_None` | 204 | 274 | 71 | inferred_complete_timeline |
| `Action_None` | 277 | 281 | 5 | inferred_complete_timeline |
| `Action_None` | 284 | 296 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PullBlock` | 101 | 203 | 103 | inferred_complete_timeline |
| `Action_None` | 204 | 299 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 207 | 110 | inferred_complete_timeline |
| `Action_None` | 209 | 299 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 168 | 71 | inferred_complete_timeline |
| `Action_None` | 170 | 197 | 28 | inferred_complete_timeline |
| `Action_None` | 200 | 230 | 31 | inferred_complete_timeline |
| `Action_None` | 234 | 236 | 3 | inferred_complete_timeline |
| `Action_None` | 259 | 263 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 233 | 136 | inferred_complete_timeline |
| `Action_None` | 235 | 241 | 7 | inferred_complete_timeline |
| `Action_None` | 244 | 293 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 299 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 101 | 136 | 36 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 138 | 139 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 195 | 98 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 299 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 265 | 168 | inferred_complete_timeline |
| `Action_None` | 273 | 295 | 23 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 278 | 181 | inferred_complete_timeline |
| `Action_None` | 282 | 287 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 145–154 | 7 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 156–157 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 193–299 | 103 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 239–299 | 61 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 261–299 | 23 | 5 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 265–276 | 10 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 268–293 | 24 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '8' (RG) duration 103 frames exceeds threshold 90 frames [start=101, end=203].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (LG) duration 103 frames exceeds threshold 90 frames [start=101, end=203].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (C) duration 103 frames exceeds threshold 90 frames [start=101, end=203].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [98–108], lower_priority='Action_DownBlock' annotated_start=101, effective_Action_DownBlock_start=109.
- ⚠️ Action 'Action_None' range [98-278] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-265] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-295] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-279] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-289] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-197] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-195] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-207] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-272] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-299] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-241] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-293] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [151-293] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [101-136] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [138-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-175] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-192] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-220] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-259] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-272] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [131-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-196] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-270] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [101-133] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [137-144] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [146-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-251] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-273] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-283] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [109-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [148-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [155-203] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-274] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-296] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-271] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-290] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-275] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-276] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-285] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-293] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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