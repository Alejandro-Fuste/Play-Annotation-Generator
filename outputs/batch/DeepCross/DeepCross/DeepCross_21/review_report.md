# Play-Annotation-Generator Annotation Review — DeepCross_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_21`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 154
- **Validation Warnings:** 161
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 136
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 23 | START | 23 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `13` | `13` | 27 | START | 39 | 43 |
| ✅ EXACT | `Action_PassBlock` | RT | `18` | `18` | 27 | START | 27 | 269 |
| ✅ EXACT | `Action_PassBlock` | RG | `20` | `20` | 27 | START | 27 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `21` | `21` | 27 | START | 27 | 77 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR1 | `0` | `0` | 38 | START | 38 | 209 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 38 | END | 23 | 38 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 148 | START | 148 | 158 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 38 | 16 | inferred_complete_timeline |
| `Action_None` | 39 | 147 | 109 | inferred_complete_timeline |
| `Action_ThrowPass` | 148 | 158 | 11 | inferred_complete_timeline |
| `Action_None` | 159 | 269 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 57 | 35 | inferred_complete_timeline |
| `Action_None` | 59 | 269 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 38 | 209 | 172 | inferred_complete_timeline |
| `Action_None` | 210 | 215 | 6 | inferred_complete_timeline |
| `Action_None` | 221 | 226 | 6 | inferred_complete_timeline |
| `Action_None` | 236 | 269 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 72 | 50 | inferred_complete_timeline |
| `Action_None` | 76 | 86 | 11 | inferred_complete_timeline |
| `Action_None` | 92 | 269 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 123 | 101 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 156 | 28 | inferred_complete_timeline |
| `Action_None` | 160 | 269 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 77 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 185 | 96 | inferred_complete_timeline |
| `Action_PassBlock` | 187 | 269 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 23 | 38 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 43 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 269 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 114 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 269 | 243 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 98 | 76 | inferred_complete_timeline |
| `Action_None` | 114 | 138 | 25 | inferred_complete_timeline |
| `Action_None` | 140 | 188 | 49 | inferred_complete_timeline |
| `Action_None` | 193 | 200 | 8 | inferred_complete_timeline |
| `Action_None` | 203 | 269 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 64 | 42 | inferred_complete_timeline |
| `Action_None` | 68 | 121 | 54 | inferred_complete_timeline |
| `Action_None` | 123 | 178 | 56 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 244 | 56 | inferred_complete_timeline |
| `Action_None` | 246 | 252 | 7 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 66 | 44 | inferred_complete_timeline |
| `Action_None` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_None` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_None` | 76 | 79 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 143 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 99 | 77 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 125 | 15 | inferred_complete_timeline |
| `Action_None` | 129 | 145 | 17 | inferred_complete_timeline |
| `Action_None` | 152 | 160 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 172 | 150 | inferred_complete_timeline |
| `Action_None` | 182 | 205 | 24 | inferred_complete_timeline |
| `Action_None` | 213 | 224 | 12 | inferred_complete_timeline |
| `Action_None` | 233 | 269 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 154 | 132 | inferred_complete_timeline |
| `Action_None` | 156 | 168 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 81 | 59 | inferred_complete_timeline |
| `Action_None` | 83 | 269 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 154 | 132 | inferred_complete_timeline |
| `Action_None` | 164 | 250 | 87 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 185 | 163 | inferred_complete_timeline |
| `Action_None` | 265 | 268 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–269 | 223 | 12 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 33–59 | 27 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 73–74 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 80–194 | 80 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 83–121 | 17 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 84–98 | 10 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 84–269 | 137 | 12 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 94–95 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 111–147 | 13 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 131–138 | 8 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 137–269 | 133 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 141–224 | 72 | 4 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 150–152 | 3 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 162–211 | 29 | 8 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 165–269 | 105 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 169–269 | 72 | 7 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 173–269 | 97 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 190–269 | 49 | 3 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 198–221 | 22 | 2 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 198–199 | 2 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 223–269 | 46 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 114 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 24: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [23–38], lower_priority='Action_PassBlock' annotated_start=27, effective_Action_PassBlock_start=39.
- ⚠️ Action 'Action_None' range [210-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-72] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-86] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-66] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-98] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-188] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-64] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-178] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-244] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-57] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-168] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-81] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-123] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-156] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [23-38] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-269] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-154] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-250] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-99] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-145] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-224] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-269] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-185] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-154] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-187] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-226] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-252] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-114] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-185] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-59] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-151] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-90] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-100] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-103] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-129] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-209] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-245] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-252] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-147] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-176] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-224] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-209] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-226] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-241] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-269] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-221] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-252] for track '42' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>