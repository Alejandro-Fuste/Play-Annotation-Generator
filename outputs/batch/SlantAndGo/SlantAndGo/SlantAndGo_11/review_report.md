# Play-Annotation-Generator Annotation Review — SlantAndGo_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_11`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_SellRoute` | WR1 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 29 | START | 29 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `10` | `10` | 31 | START | 31 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `11` | `11` | 31 | START | 31 | 188 |
| ✅ EXACT | `Action_PassBlock` | LG | `17` | `17` | 31 | START | 31 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 31 | START | 46 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `9` | `9` | 31 | START | 31 | 167 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 45 | END | 29 | 45 |
| ✅ EXACT | `Action_SellRoute` | WR1 | `0` | `0` | 47 | START | 47 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR1 | `0` | `0` | 85 | START | 85 | 205 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 122 | START | 122 | 132 |

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
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 45 | 17 | inferred_complete_timeline |
| `Action_None` | 46 | 121 | 76 | inferred_complete_timeline |
| `Action_ThrowPass` | 122 | 132 | 11 | inferred_complete_timeline |
| `Action_None` | 133 | 176 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SellRoute` | 47 | 84 | 38 | inferred_complete_timeline |
| `Action_VerticalStem` | 85 | 205 | 121 | inferred_complete_timeline |
| `Action_VerticalStem` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 195 | 167 | inferred_complete_timeline |
| `Action_None` | 198 | 201 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 149 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 188 | 158 | inferred_complete_timeline |
| `Action_PassBlock` | 200 | 210 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 210 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_BallSnap` | 29 | 45 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 190 | 145 | inferred_complete_timeline |
| `Action_PassBlock` | 192 | 196 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 198 | 203 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 107 | 77 | inferred_complete_timeline |
| `Action_PassBlock` | 109 | 120 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 158 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 167 | 137 | inferred_complete_timeline |
| `Action_PassBlock` | 169 | 197 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 204 | 208 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 166 | 138 | inferred_complete_timeline |
| `Action_None` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 205 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 190 | 162 | inferred_complete_timeline |
| `Action_None` | 193 | 195 | 3 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 203 | 175 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 28 | 2 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 95 | 67 | inferred_complete_timeline |
| `Action_None` | 98 | 210 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 31 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 28 | 1 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |
| `Action_None` | 182 | 198 | 17 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–15 | 16 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 64–71 | 8 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 83–210 | 127 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 101–102 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 101–102 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 148–156 | 5 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 157–193 | 22 | 6 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 173–200 | 11 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 185–187 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [29–45], lower_priority='Action_PassBlock' annotated_start=31, effective_Action_PassBlock_start=46.
- ⚠️ Action 'Action_VerticalStem' range [85-205] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [208-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-195] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-203] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-149] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-190] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-205] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-167] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [169-197] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [204-208] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [109-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-188] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [200-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-198] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-210] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-190] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [192-196] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [198-203] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [205-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-71] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-200] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '30' has 1 frames without a visible bounding box.
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

</details>