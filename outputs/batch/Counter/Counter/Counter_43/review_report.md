# Play-Annotation-Generator Annotation Review — Counter_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_43`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | RB2 | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `10` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `12` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 37 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 32 | START | 32 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `16` | `15` | 38 | START | 48 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `21` | `20` | 38 | START | 38 | 76 |
| ✅ EXACT | `Action_PullBlock` | RG | `20` | `19` | 38 | START | 38 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `3` | `2` | 38 | START | 38 | 97 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 47 | END | 32 | 47 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `16` | 57 | START | 57 | 79 |
| ✅ EXACT | `Action_BallCarry` | RB2 | `10` | `9` | 80 | START | 80 | 224 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 130 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 47 | 16 | inferred_complete_timeline |
| `Action_None` | 48 | 56 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 57 | 79 | 23 | inferred_complete_timeline |
| `Action_None` | 80 | 142 | 63 | inferred_complete_timeline |
| `Action_None` | 147 | 233 | 87 | inferred_complete_timeline |
| `Action_None` | 235 | 245 | 11 | inferred_complete_timeline |
| `Action_None` | 247 | 254 | 8 | inferred_complete_timeline |
| `Action_None` | 256 | 259 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 100 | 69 | inferred_complete_timeline |
| `Action_None` | 103 | 269 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_BallCarry` | 80 | 224 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 38 | 97 | 60 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 99 | 130 | 32 | inferred_complete_timeline |
| `Action_None` | 131 | 139 | 9 | inferred_complete_timeline |
| `Action_None` | 141 | 149 | 9 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_None` | 162 | 269 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 56 | 25 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_None` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_None` | 69 | 269 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_DownBlock` | 38 | 76 | 39 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 83 | 130 | 48 | inferred_complete_timeline |
| `Action_None` | 131 | 269 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 47 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 48 | 66 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 85 | 130 | 46 | inferred_complete_timeline |
| `Action_None` | 131 | 269 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PullBlock` | 38 | 130 | 93 | inferred_complete_timeline |
| `Action_None` | 131 | 252 | 122 | inferred_complete_timeline |
| `Action_None` | 254 | 269 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 85 | 54 | inferred_complete_timeline |
| `Action_None` | 92 | 95 | 4 | inferred_complete_timeline |
| `Action_None` | 98 | 107 | 10 | inferred_complete_timeline |
| `Action_None` | 109 | 119 | 11 | inferred_complete_timeline |
| `Action_None` | 123 | 219 | 97 | inferred_complete_timeline |
| `Action_None` | 222 | 269 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 69 | 38 | inferred_complete_timeline |
| `Action_None` | 72 | 81 | 10 | inferred_complete_timeline |
| `Action_None` | 97 | 100 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 69 | 38 | inferred_complete_timeline |
| `Action_None` | 84 | 109 | 26 | inferred_complete_timeline |
| `Action_None` | 115 | 269 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 171 | 140 | inferred_complete_timeline |
| `Action_None` | 178 | 269 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 180 | 149 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 269 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 269 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 231 | 200 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 269 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 269 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 89 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 247 | 216 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–268 | 249 | 6 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 98–269 | 166 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 100–269 | 169 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 105–147 | 14 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 208–255 | 7 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 247–248 | 2 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 251–269 | 19 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 260–269 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (C) duration 93 frames exceeds threshold 90 frames [start=38, end=130].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [32–47], lower_priority='Action_DownBlock' annotated_start=38, effective_Action_DownBlock_start=48.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '19' (RG) duration 93 frames exceeds threshold 90 frames [start=38, end=130].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (LG) duration 93 frames exceeds threshold 90 frames [start=38, end=130].
- ⚠️ Action 'Action_None' range [32-69] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-81] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-69] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-109] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [38-97] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-89] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [80-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-100] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-85] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-119] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-219] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [48-66] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [69-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [85-130] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-233] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-245] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-254] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-247] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-231] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [38-130] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-252] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [38-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-81] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [83-130] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-235] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-168] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-116] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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