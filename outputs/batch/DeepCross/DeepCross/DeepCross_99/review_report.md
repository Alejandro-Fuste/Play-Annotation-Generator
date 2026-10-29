# Play-Annotation-Generator Annotation Review — DeepCross_99

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_99`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Completion`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 4 | START | 4 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 14 | START | 27 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 14 | START | 14 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `17` | 14 | START | 14 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `18` | `18` | 14 | START | 14 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 14 | START | 14 | 53 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR3 | `0` | `0` | 26 | START | 26 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 26 | END | 4 | 26 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 110 | START | 110 | 119 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_None` | 27 | 109 | 83 | inferred_complete_timeline |
| `Action_ThrowPass` | 110 | 119 | 10 | inferred_complete_timeline |
| `Action_None` | 120 | 218 | 99 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 235 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 169 | 166 | inferred_complete_timeline |
| `Action_None` | 172 | 185 | 14 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 223 | 28 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 168 | 165 | inferred_complete_timeline |
| `Action_None` | 172 | 185 | 14 | inferred_complete_timeline |
| `Action_None` | 189 | 193 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 239 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 26 | 150 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 187 | 174 | inferred_complete_timeline |
| `Action_PassBlock` | 189 | 239 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 155 | 142 | inferred_complete_timeline |
| `Action_PassBlock` | 157 | 193 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 214 | 223 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 230 | 233 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 31 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 169 | 136 | inferred_complete_timeline |
| `Action_PassBlock` | 171 | 226 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 21 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 35 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 44 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 53 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 103 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 73 | 70 | inferred_complete_timeline |
| `Action_None` | 86 | 205 | 120 | inferred_complete_timeline |
| `Action_None` | 208 | 239 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 84 | 81 | inferred_complete_timeline |
| `Action_None` | 97 | 155 | 59 | inferred_complete_timeline |
| `Action_None` | 157 | 239 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 47 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 56 | 53 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 160 | 157 | inferred_complete_timeline |
| `Action_None` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 155 | 152 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 82 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 139 | 136 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 155 | 3 | inferred_complete_timeline |
| `Action_None` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–239 | 225 | 6 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–179 | 169 | 5 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–237 | 238 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–239 | 237 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 52–57 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 52–143 | 92 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 88–89 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 91–239 | 145 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 91–239 | 137 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 162–239 | 76 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 175–239 | 61 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 177–179 | 3 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 178–239 | 57 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 181–239 | 38 | 5 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 186–235 | 38 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 202–231 | 18 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 231–239 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 102: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 102: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [4–26], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=27.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [26-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-82] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-239] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-185] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-155] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-145] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-169] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-169] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-185] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-223] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-73] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-205] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-31] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [171-226] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [231-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-237] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [157-193] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [214-223] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [230-233] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-21] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-35] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-44] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-218] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-107] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-239] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-57] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-143] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-155] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-185] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-239] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-152] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-222] for track '26' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-239] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-185] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-234] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-193] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-225] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-205] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-235] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-217] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>