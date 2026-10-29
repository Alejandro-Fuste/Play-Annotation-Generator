# Play-Annotation-Generator Annotation Review — DeepCross_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_19`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Completion`
- **Result Frame:** 269
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 16 | START | 16 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `12` | `12` | 19 | START | 19 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `13` | 19 | START | 19 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 19 | START | 29 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `19` | `19` | 19 | START | 19 | 189 |
| ✅ EXACT | `Action_PassBlock` | LG | `21` | `21` | 19 | START | 19 | 267 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR1 | `0` | `0` | 28 | START | 28 | 202 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 28 | END | 16 | 28 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 121 | START | 121 | 131 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 28 | 13 | inferred_complete_timeline |
| `Action_None` | 29 | 120 | 92 | inferred_complete_timeline |
| `Action_ThrowPass` | 121 | 131 | 11 | inferred_complete_timeline |
| `Action_None` | 132 | 140 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 107 | 92 | inferred_complete_timeline |
| `Action_None` | 113 | 133 | 21 | inferred_complete_timeline |
| `Action_None` | 135 | 140 | 6 | inferred_complete_timeline |
| `Action_None` | 143 | 149 | 7 | inferred_complete_timeline |
| `Action_None` | 157 | 269 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 28 | 202 | 175 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 135 | 120 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 189 | 171 | inferred_complete_timeline |
| `Action_PassBlock` | 191 | 199 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 204 | 224 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 245 | 251 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 267 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 28 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 36 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 44 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 204 | 132 | inferred_complete_timeline |
| `Action_PassBlock` | 206 | 208 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 130 | 112 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 163 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 191 | 195 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 213 | 215 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 86 | 68 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 171 | 82 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 182 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 90 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 244 | 229 | inferred_complete_timeline |
| `Action_None` | 246 | 266 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 142 | 127 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 155 | 140 | inferred_complete_timeline |
| `Action_None` | 157 | 182 | 26 | inferred_complete_timeline |
| `Action_None` | 184 | 261 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 111 | 96 | inferred_complete_timeline |
| `Action_None` | 113 | 208 | 96 | inferred_complete_timeline |
| `Action_None` | 210 | 230 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 164 | 149 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 54–62 | 6 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 84–88 | 5 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 86–269 | 179 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 103–104 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 117–148 | 18 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 146–148 | 3 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 190–254 | 46 | 5 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 209–212 | 4 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 219–221 | 3 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 226–227 | 2 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 241–255 | 15 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 249–262 | 13 | 2 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 261–269 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [16–28], lower_priority='Action_PassBlock' annotated_start=19, effective_Action_PassBlock_start=29.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [28-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [206-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-244] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-266] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-155] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-182] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-142] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-133] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-163] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [191-195] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [213-215] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-171] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-182] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-44] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [206-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-140] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-111] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-230] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [191-199] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [201-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [204-224] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [245-251] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-267] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-62] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-91] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-251] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-255] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-256] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '39' has 1 frames without a visible bounding box.
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

</details>