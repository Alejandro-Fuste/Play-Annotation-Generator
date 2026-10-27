# Play-Annotation-Generator Annotation Review — Counter_193

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_193`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 85
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT2 | defense | `12` | `11` |
| ✅ EXACT | `Action_DownBlock` | DT2 | defense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_PullLeadBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB3 | defense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `1` | `Group` | 3 | START | 3 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 3 | START | 3 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 3 | START | 3 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 3 | START | 3 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 3 | START | 3 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 3 | START | 3 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 3 | START | 3 | 81 |
| ✅ EXACT | `Action_BallSnap` | DT2 | `12` | `11` | 82 | START | 82 | 88 |
| ✅ EXACT | `Action_DownBlock` | DT2 | `12` | `11` | 89 | START | 89 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `19` | `18` | 89 | START | 89 | 122 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `22` | `21` | 89 | START | 89 | 100 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `20` | `19` | 89 | START | 89 | 137 |
| ✅ EXACT | `Action_PullLeadBlock` | LG | `6` | `5` | 89 | START | 89 | 137 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `16` | `15` | 97 | END | 82 | 97 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `16` | `15` | 104 | START | 104 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB3 | `7` | `6` | 122 | START | 122 | 235 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 137 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 141 | 60 | inferred_complete_timeline |
| `Action_None` | 143 | 158 | 16 | inferred_complete_timeline |
| `Action_None` | 163 | 299 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 243 | 162 | inferred_complete_timeline |
| `Action_None` | 248 | 299 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 299 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 3–223
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 88 | 86 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 89 | 137 | 49 | inferred_complete_timeline |
| `Action_None` | 138 | 223 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–244
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 134 | 53 | inferred_complete_timeline |
| `Action_None` | 138 | 175 | 38 | inferred_complete_timeline |
| `Action_None` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_None` | 185 | 244 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 3–279
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 236 | 155 | inferred_complete_timeline |
| `Action_None` | 241 | 279 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 152 | 71 | inferred_complete_timeline |
| `Action_None` | 169 | 299 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 299 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 299 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_BallSnap` | 82 | 88 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 89 | 137 | 49 | inferred_complete_timeline |
| `Action_None` | 138 | 299 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–266
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 266 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 299 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 121 | 119 | inferred_complete_timeline |
| `Action_BallCarry` | 122 | 235 | 114 | inferred_complete_timeline |
| `Action_BallCarry` | 246 | 256 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 261 | 289 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 291 | 299 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 3–233 | 195 | 7 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 3–219 | 217 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 3–282 | 279 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 3–276 | 265 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 3–248 | 236 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 3–239 | 237 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 3–228 | 206 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 3–242 | 162 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 150–151 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 188–191 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 194–215 | 20 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 232–256 | 19 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 268–270 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 277–297 | 15 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [82-134] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-175] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-244] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-141] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-158] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-236] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-279] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-121] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [122-235] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [246-256] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [261-289] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-152] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-233] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-237] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-282] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-276] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [89-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-248] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [89-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-179] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-242] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-215] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-247] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-286] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '28' has 2 frames without a visible bounding box.
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