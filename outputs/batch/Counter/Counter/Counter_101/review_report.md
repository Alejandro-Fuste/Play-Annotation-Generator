# Play-Annotation-Generator Annotation Review — Counter_101

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_101`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | DT2 | defense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 91 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | DT2 | `22` | `21` | 92 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 97 | START | 97 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `19` | `18` | 97 | START | 97 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `17` | `16` | 97 | START | 97 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `20` | `19` | 97 | START | 97 | 103 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 107 | END | 92 | 107 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 127 | START | 127 | 145 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `16` | `15` | 146 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 192 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_SnapReceive` | 92 | 107 | 16 | inferred_complete_timeline |
| `Action_None` | 108 | 126 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 127 | 145 | 19 | inferred_complete_timeline |
| `Action_None` | 146 | 329 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 170 | 79 | inferred_complete_timeline |
| `Action_None` | 185 | 329 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 300 | 209 | inferred_complete_timeline |
| `Action_None` | 302 | 305 | 4 | inferred_complete_timeline |
| `Action_None` | 307 | 311 | 5 | inferred_complete_timeline |
| `Action_None` | 314 | 319 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 131 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 105 | 14 | inferred_complete_timeline |
| `Action_None` | 110 | 131 | 22 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 329 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 105 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 117 | 128 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 147 | 192 | 46 | inferred_complete_timeline |
| `Action_None` | 193 | 269 | 77 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 307 | 33 | inferred_complete_timeline |
| `Action_None` | 309 | 329 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 111 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 114 | 126 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PullBlock` | 97 | 103 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 112 | 134 | 23 | inferred_complete_timeline |
| `Action_PullBlock` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 151 | 160 | 10 | inferred_complete_timeline |
| `Action_PullBlock` | 165 | 192 | 28 | inferred_complete_timeline |
| `Action_None` | 193 | 224 | 32 | inferred_complete_timeline |
| `Action_None` | 230 | 241 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 97 | 103 | 7 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 109 | 134 | 26 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 145 | 185 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 103 | 12 | inferred_complete_timeline |
| `Action_None` | 115 | 131 | 17 | inferred_complete_timeline |
| `Action_None` | 151 | 213 | 63 | inferred_complete_timeline |
| `Action_None` | 215 | 329 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 104 | 13 | inferred_complete_timeline |
| `Action_None` | 107 | 329 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_None` | 119 | 128 | 10 | inferred_complete_timeline |
| `Action_None` | 147 | 239 | 93 | inferred_complete_timeline |
| `Action_None` | 241 | 329 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 134 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 154 | 63 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 215 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 329 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 197 | 106 | inferred_complete_timeline |
| `Action_None` | 200 | 329 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 329 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 211 | 120 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 329 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 311 | 220 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–329 | 322 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 142–296 | 135 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 150–329 | 176 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 152–329 | 177 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 153–329 | 175 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 160–174 | 15 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 180–304 | 124 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 196–329 | 117 | 5 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 224–329 | 98 | 3 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 244–329 | 86 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 326–327 | 2 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `22` (DT2)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `17` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `20` (4 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `16` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 204: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '15' has invalid range: start=146, end=131. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '16' (RG) duration 96 frames exceeds threshold 90 frames [start=97, end=192].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (LG) duration 96 frames exceeds threshold 90 frames [start=97, end=192].
- ⚠️ Action 'Action_None' range [92-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-215] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-134] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-211] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-300] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-305] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-311] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-311] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-245] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-313] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-320] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [97-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [114-126] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-213] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-131] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-131] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [97-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [107-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [112-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [137-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [146-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [151-160] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-224] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-241] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [97-105] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [114-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-128] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [147-192] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-307] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [97-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [109-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [137-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [145-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-239] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-269] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-276] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-307] for track '23' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-316] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-329] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-286] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-304] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-227] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-282] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-307] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-253] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-329] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>