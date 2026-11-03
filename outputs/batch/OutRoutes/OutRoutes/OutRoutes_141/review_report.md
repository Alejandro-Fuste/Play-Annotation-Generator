# Play-Annotation-Generator Annotation Review — OutRoutes_141

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_141`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_RunOutRoute` | TE | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_SecureCatch` | TE | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | TE | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `14` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `16` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `11` | `11` | 14 | START | 14 | 32 |
| ✅ EXACT | `Action_PassBlock` | LT | `19` | `19` | 14 | START | 14 | 126 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 14 | START | 14 | 122 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `21` | `21` | 14 | START | 27 | 28 |
| ✅ EXACT | `Action_PassBlock` | RT | `3` | `3` | 14 | START | 14 | 51 |
| ✅ EXACT | `Action_RunOutRoute` | TE | `8` | `8` | 19 | START | 19 | 80 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 19 | END | 19 | 19 |
| ✅ EXACT | `Action_ThrowPass` | QB | `5` | `5` | 57 | START | 57 | 65 |
| ✅ EXACT | `Action_SecureCatch` | TE | `8` | `8` | 81 | START | 81 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | TE | `8` | `8` | 88 | START | 88 | 155 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 19 | 1 | inferred_complete_timeline |
| `Action_None` | 20 | 56 | 37 | inferred_complete_timeline |
| `Action_ThrowPass` | 57 | 65 | 9 | inferred_complete_timeline |
| `Action_None` | 66 | 117 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

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
<summary>WR3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 173 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_RunOutRoute` | 19 | 80 | 62 | inferred_complete_timeline |
| `Action_SecureCatch` | 81 | 87 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 155 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 126 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 122 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–28
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 12 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 28 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 32 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 135 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 51 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

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
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 133 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 183 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 163 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 216 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 208 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 269 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 269 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 229 | 230 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 252 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 234 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 269 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 36–75 | 39 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 63–70 | 8 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 78–138 | 35 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 148–211 | 64 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 170–180 | 5 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 191–192 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 198–256 | 58 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 198–208 | 11 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 210–269 | 55 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 217–269 | 44 | 3 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 223–247 | 25 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 251–269 | 19 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 263–267 | 5 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (3 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `21` (C): Annotated start 14 != Inferred start 27
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 56 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-51] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-154] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-208] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [161-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-32] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-43] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-183] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-216] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-252] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-12] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-41] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-70] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-85] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-107] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-122] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-211] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-172] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-252] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-256] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-208] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-238] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-247] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-267] for track '35' has 1 frames without a visible bounding box.
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

</details>