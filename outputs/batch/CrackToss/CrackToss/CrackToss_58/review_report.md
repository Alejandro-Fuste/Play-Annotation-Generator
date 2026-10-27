# Play-Annotation-Generator Annotation Review — CrackToss_58

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_58`
- **Frame Range:** 0 to 324 (325 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Touchdown`
- **Result Frame:** 324
- **Player Tracks:** 32
- **Ball Tracks:** 2
- **Action Segments:** 83
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_CrackBlock` | TE2 | offense | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `17` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 153 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 154 | START | 154 | 167 |
| ✅ EXACT | `Action_CrackBlock` | TE2 | `7` | `6` | 157 | START | 157 | 207 |
| ✅ EXACT | `Action_PullBlock` | RT | `10` | `9` | 157 | START | 157 | 195 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 167 | END | 154 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `8` | `7` | 182 | START | 182 | 213 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 207 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_SnapReceive` | 154 | 167 | 14 | inferred_complete_timeline |
| `Action_None` | 168 | 181 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 182 | 213 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 220 | 310 | 91 | inferred_complete_timeline |
| `Action_BallCarry` | 317 | 318 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 115 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 129 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 223 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 168 | 15 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 212 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 153 | 29 | inferred_complete_timeline |
| `Action_None` | 154 | 180 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_CrackBlock` | 157 | 207 | 51 | inferred_complete_timeline |
| `Action_None` | 208 | 324 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 181 | 28 | inferred_complete_timeline |
| `Action_None` | 183 | 198 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 163 | 10 | inferred_complete_timeline |
| `Action_None` | 165 | 299 | 135 | inferred_complete_timeline |
| `Action_None` | 303 | 305 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_BallSnap` | 154 | 167 | 14 | inferred_complete_timeline |
| `Action_None` | 168 | 183 | 16 | inferred_complete_timeline |
| `Action_None` | 188 | 191 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 188 | 35 | inferred_complete_timeline |
| `Action_None` | 190 | 269 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PullBlock` | 157 | 195 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 263 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 191 | 38 | inferred_complete_timeline |
| `Action_None` | 193 | 220 | 28 | inferred_complete_timeline |
| `Action_None` | 225 | 269 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 324 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 304 | 151 | inferred_complete_timeline |
| `Action_None` | 307 | 324 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 220 | 67 | inferred_complete_timeline |
| `Action_None` | 234 | 324 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–303
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 303 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 293 | 140 | inferred_complete_timeline |
| `Action_None` | 301 | 308 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 173 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 49–90 | 42 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 200–230 | 20 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 202–324 | 122 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 204–268 | 65 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 205–300 | 93 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 207–320 | 114 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 259–262 | 4 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 266–267 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 266–313 | 32 | 5 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 282–285 | 4 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 315–323 | 6 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 324–324 | 1 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 324–324 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | 3 | 4 | 2 | 100.0% | None |
| `20` | `22` | 102 | 110 | 9 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 59 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 324 as fallback play end.
- ⚠️ Action 'Action_None' range [154-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-293] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-308] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-181] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-198] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-303] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-181] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-213] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-310] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [317-318] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-188] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [157-195] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-263] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-304] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-324] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-299] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-324] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-212] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-115] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-223] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-213] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-312] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-268] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-268] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-281] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-300] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-320] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-313] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>