# Play-Annotation-Generator Annotation Review — OutRoutes_145

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_145`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `7` | `7` |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `13` | 9 | START | 9 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `15` | `15` | 9 | START | 9 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 9 | START | 9 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 9 | START | 9 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 9 | START | 9 | 14 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `7` | `7` | 19 | START | 19 | 200 |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | `8` | `8` | 19 | START | 19 | 83 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 19 | END | 19 | 19 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 57 | START | 57 | 66 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `8` | `8` | 84 | START | 84 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `8` | `8` | 94 | START | 94 | 155 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 19 | 1 | inferred_complete_timeline |
| `Action_None` | 20 | 56 | 37 | inferred_complete_timeline |
| `Action_ThrowPass` | 57 | 66 | 10 | inferred_complete_timeline |
| `Action_None` | 67 | 110 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 216 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_RunOutRoute` | 19 | 200 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_RunOutRoute` | 19 | 83 | 65 | inferred_complete_timeline |
| `Action_SecureCatch` | 84 | 93 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 155 | 62 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 181 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 239 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 64 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 82 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 217 | 128 | inferred_complete_timeline |
| `Action_PassBlock` | 227 | 235 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 14 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 107 | 91 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 219 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 21 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 69 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 77 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 31 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 36 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 60 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 65 | 57 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 163 | 97 | inferred_complete_timeline |
| `Action_PassBlock` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 170 | 173 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 187 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 229 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 239 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 223 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 209 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 78–222 | 145 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 81–239 | 159 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 156–209 | 4 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 193–218 | 22 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 196–210 | 14 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 210–213 | 4 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 212–215 | 4 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 214–232 | 19 | 1 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 216–231 | 16 | 1 | Undefined position; Undefined team |
| `31` | `55` | Position_Unknown | Team_Unknown | 227–239 | 13 | 1 | Undefined position; Undefined team |
| `32` | `57` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `33` | `59` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 52 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-211] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-227] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [19-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-181] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-205] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-209] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-223] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-163] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [165-167] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [170-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [179-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-82] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-217] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [227-235] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-229] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-21] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-77] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-31] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-36] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-14] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-107] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-218] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-213] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-231] for track '30' has 1 frames without a visible bounding box.
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