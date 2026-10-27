# Play-Annotation-Generator Annotation Review — Counter_135

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_135`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 86
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | WR2 | offense | `2` | `1` |
| ✅ EXACT | `Action_PullBlock` | CB1 | defense | `17` | `16` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | DT | defense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | DT | defense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 3 | START | 3 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `13` | `Group` | 3 | START | 3 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 3 | START | 3 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 3 | START | 3 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 3 | START | 3 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 3 | START | 3 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 3 | START | 3 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 3 | START | 3 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 3 | START | 3 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `9` | `Group` | 3 | START | 3 | 122 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 74 | START | 74 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `14` | `13` | 79 | START | 79 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `15` | `14` | 79 | START | 87 | 156 |
| ✅ EXACT | `Action_DownBlock` | WR2 | `2` | `1` | 79 | START | 79 | 178 |
| ✅ EXACT | `Action_PullBlock` | CB1 | `17` | `16` | 79 | START | 79 | 178 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `21` | `20` | 79 | START | 79 | 147 |
| ✅ EXACT | `Action_SnapReceive` | DT | `18` | `17` | 86 | END | 74 | 86 |
| ✅ EXACT | `Action_Handoff` | DT | `18` | `17` | 97 | START | 97 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | `9` | `8` | 123 | START | 123 | 161 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 178 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 122 | 120 | inferred_complete_timeline |
| `Action_BallCarry` | 123 | 161 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 173 | 202 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 208 | 269 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 3–214
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 211 | 138 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 78 | 76 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 178 | 100 | inferred_complete_timeline |
| `Action_None` | 179 | 269 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 3–147
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 78 | 76 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 79 | 147 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 229 | 156 | inferred_complete_timeline |
| `Action_None` | 236 | 244 | 9 | inferred_complete_timeline |
| `Action_None` | 246 | 250 | 5 | inferred_complete_timeline |
| `Action_None` | 253 | 269 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 3–221
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 86 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 87 | 156 | 70 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 178 | 18 | inferred_complete_timeline |
| `Action_None` | 179 | 221 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 3–255
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 123 | 50 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 144 | 6 | inferred_complete_timeline |
| `Action_None` | 148 | 163 | 16 | inferred_complete_timeline |
| `Action_None` | 165 | 200 | 36 | inferred_complete_timeline |
| `Action_None` | 204 | 247 | 44 | inferred_complete_timeline |
| `Action_None` | 252 | 255 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 78 | 76 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 178 | 100 | inferred_complete_timeline |
| `Action_None` | 179 | 269 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 104 | 31 | inferred_complete_timeline |
| `Action_None` | 107 | 269 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 141 | 68 | inferred_complete_timeline |
| `Action_None` | 143 | 166 | 24 | inferred_complete_timeline |
| `Action_None` | 169 | 252 | 84 | inferred_complete_timeline |
| `Action_None` | 255 | 269 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 86 | 13 | inferred_complete_timeline |
| `Action_None` | 87 | 96 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 97 | 122 | 26 | inferred_complete_timeline |
| `Action_None` | 123 | 269 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 216 | 143 | inferred_complete_timeline |
| `Action_None` | 218 | 245 | 28 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–228
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 168 | 95 | inferred_complete_timeline |
| `Action_None` | 171 | 220 | 50 | inferred_complete_timeline |
| `Action_None` | 225 | 228 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 78 | 76 | inferred_complete_timeline |
| `Action_PullBlock` | 79 | 178 | 100 | inferred_complete_timeline |
| `Action_None` | 179 | 269 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 74 | 243 | 170 | inferred_complete_timeline |
| `Action_None` | 255 | 269 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 3–136 | 120 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 110–112 | 3 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 170–269 | 99 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 205–269 | 64 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 215–269 | 53 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 219–267 | 23 | 4 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 226–228 | 3 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 228–269 | 39 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 229–269 | 33 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 256–265 | 8 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 269–269 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 272: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '1' (WR2) duration 100 frames exceeds threshold 90 frames [start=79, end=178].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (RT) duration 100 frames exceeds threshold 90 frames [start=79, end=178].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '14' (C) duration 100 frames exceeds threshold 90 frames [start=79, end=178].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [74–86], lower_priority='Action_DownBlock' annotated_start=79, effective_Action_DownBlock_start=87.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '16' (CB1) duration 100 frames exceeds threshold 90 frames [start=79, end=178].
- ⚠️ Action 'Action_None' range [74-269] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-220] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-122] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [173-202] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [205-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [208-269] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-243] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-269] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-245] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-211] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-269] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [87-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-178] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-221] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-229] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-244] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-166] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-252] for track '19' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [79-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-163] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-200] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-247] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-186] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-250] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-250] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-258] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-263] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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