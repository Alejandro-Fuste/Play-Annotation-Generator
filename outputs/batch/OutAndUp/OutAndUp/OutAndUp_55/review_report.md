# Play-Annotation-Generator Annotation Review — OutAndUp_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_55`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_SellOut` | WR3 | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | offense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 19 | START | 19 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `10` | `10` | 22 | START | 22 | 92 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `17` | `17` | 22 | START | 34 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 22 | START | 22 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 22 | START | 22 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 22 | START | 22 | 62 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `2` | 33 | END | 19 | 33 |
| ✅ EXACT | `Action_SellOut` | WR3 | `5` | `5` | 65 | START | 65 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | `5` | `5` | 92 | START | 92 | 222 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `2` | `2` | 117 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 33 | 15 | inferred_complete_timeline |
| `Action_None` | 34 | 83 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 69 | 51 | inferred_complete_timeline |
| `Action_None` | 77 | 184 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 260 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 240 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_SellOut` | 65 | 91 | 27 | inferred_complete_timeline |
| `Action_RunGoRoute` | 92 | 222 | 131 | inferred_complete_timeline |
| `Action_RunGoRoute` | 225 | 227 | 3 | inferred_complete_timeline |
| `Action_RunGoRoute` | 229 | 261 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 227 | 209 | inferred_complete_timeline |
| `Action_None` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 156 | 135 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 218 | 61 | inferred_complete_timeline |
| `Action_PassBlock` | 220 | 225 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 231 | 232 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 62 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 91 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 33 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 74 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 59 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 130 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 180 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 182 | 260 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 92 | 71 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 108 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 144 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 151 | 162 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 179 | 210 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 68 | 50 | inferred_complete_timeline |
| `Action_None` | 81 | 87 | 7 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 152 | 60 | inferred_complete_timeline |
| `Action_None` | 158 | 206 | 49 | inferred_complete_timeline |
| `Action_None` | 208 | 216 | 9 | inferred_complete_timeline |
| `Action_None` | 218 | 222 | 5 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 98 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 169 | 151 | inferred_complete_timeline |
| `Action_None` | 171 | 266 | 96 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 212 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 87 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 156 | 138 | inferred_complete_timeline |
| `Action_None` | 158 | 221 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 203 | 185 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_None` | 211 | 269 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 86–87 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 89–235 | 145 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 111–240 | 111 | 6 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 115–237 | 121 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 140–203 | 63 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (8 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `17` (C): Annotated start 22 != Inferred start 34
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `5` (3 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `2` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_ThrowPass' for track '2' has invalid range: start=117, end=83. Clamping end to start.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [19–33], lower_priority='Action_PassBlock' annotated_start=22, effective_Action_PassBlock_start=34.
- ⚠️ Action 'Action_None' range [19-227] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-83] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-260] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [92-222] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [225-227] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [229-261] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-212] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-240] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-184] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-92] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [117-144] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [151-162] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [165-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [179-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-221] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-206] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-87] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-269] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-169] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-266] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-59] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-130] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-136] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [182-260] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-218] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [220-225] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [231-232] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-227] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-199] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-203] for track '26' has 1 frames without a visible bounding box.
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

</details>