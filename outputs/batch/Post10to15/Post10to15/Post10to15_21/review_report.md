# Play-Annotation-Generator Annotation Review — Post10to15_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_21`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 95
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
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `19` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `7` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 32 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 22 | START | 22 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `13` | `13` | 33 | START | 41 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `15` | `15` | 33 | START | 33 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 33 | START | 33 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 33 | START | 33 | 54 |
| ✅ EXACT | `Action_PassBlock` | RT | `8` | `8` | 33 | START | 33 | 210 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 40 | END | 22 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR3 | `0` | `0` | 49 | START | 49 | 145 |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 89 | START | 89 | 99 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 40 | 19 | inferred_complete_timeline |
| `Action_None` | 41 | 88 | 48 | inferred_complete_timeline |
| `Action_ThrowPass` | 89 | 99 | 11 | inferred_complete_timeline |
| `Action_None` | 100 | 201 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 204 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 193 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 210 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 210 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_RunPostRoute` | 49 | 145 | 97 | inferred_complete_timeline |
| `Action_RunPostRoute` | 149 | 164 | 16 | inferred_complete_timeline |
| `Action_RunPostRoute` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 154 | 122 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 206 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 49 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 105 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 156 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 164 | 165 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 40 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 96 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 98 | 193 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 54 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 62 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 210 | 178 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 101 | 80 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 132 | 12 | inferred_complete_timeline |
| `Action_None` | 134 | 210 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 193 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 124 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 193 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 210 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 193 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 210 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 182 | 161 | inferred_complete_timeline |
| `Action_None` | 193 | 210 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 210 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 210 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 210 | 189 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 64–95 | 32 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 74–210 | 119 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 85–210 | 37 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 113–157 | 7 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 134–193 | 45 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 136–138 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 144–146 | 3 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 176–202 | 7 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 180–193 | 14 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 180–210 | 31 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 195–210 | 14 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunPostRoute` and target `0` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [22–40], lower_priority='Action_PassBlock' annotated_start=33, effective_Action_PassBlock_start=41.
- ⚠️ Action 'Action_RunPostRoute' range [49-145] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [149-164] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [167-168] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-193] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-132] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-193] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-124] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-96] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [98-193] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-105] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-156] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-159] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [164-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-54] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-201] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-167] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-193] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '37' has 1 frames without a visible bounding box.
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