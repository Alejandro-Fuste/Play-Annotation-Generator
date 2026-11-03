# Play-Annotation-Generator Annotation Review — OutRoutes_115

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_115`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 55
- **Validation Warnings:** 47
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 31
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `7` | `Group` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `7` | `Group` | 0 | START | 0 | 233 |
| ✅ EXACT | `Action_PassBlock` | C | `14` | `14` | 82 | START | 82 | 125 |
| ✅ EXACT | `Action_PassBlock` | LG | `16` | `16` | 82 | START | 82 | 269 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 82 | START | 82 | 217 |
| ✅ EXACT | `Action_PassBlock` | RG | `20` | `20` | 82 | START | 82 | 269 |
| ✅ EXACT | `Action_PassBlock` | LT | `6` | `6` | 82 | START | 82 | 269 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `2` | `2` | 90 | START | 90 | 161 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 90 | END | 90 | 90 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 130 | START | 130 | 141 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `2` | `2` | 162 | START | 162 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `2` | `2` | 173 | START | 173 | 239 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_SnapReceive` | 90 | 90 | 1 | inferred_complete_timeline |
| `Action_None` | 91 | 129 | 39 | inferred_complete_timeline |
| `Action_ThrowPass` | 130 | 141 | 12 | inferred_complete_timeline |
| `Action_None` | 142 | 242 | 101 | inferred_complete_timeline |
| `Action_None` | 244 | 266 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_RunOutRoute` | 90 | 161 | 72 | inferred_complete_timeline |
| `Action_SecureCatch` | 162 | 172 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 173 | 239 | 67 | inferred_complete_timeline |
| `Action_BallCarry` | 262 | 268 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 240 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 255 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 263 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 125 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 217 | 136 | inferred_complete_timeline |
| `Action_PassBlock` | 220 | 224 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 189 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 269 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 248 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 257 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 265 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 268 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 269 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 108–129 | 5 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 132–269 | 119 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 169–269 | 101 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 199–200 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 232–233 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 248–269 | 22 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 259–268 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 31 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_BallCarry' range [173-239] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [262-268] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-247] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-233] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-240] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-255] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-263] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-257] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-265] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-268] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-189] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-216] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [220-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-242] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-266] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-269] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-268] for track '28' has 1 frames without a visible bounding box.
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