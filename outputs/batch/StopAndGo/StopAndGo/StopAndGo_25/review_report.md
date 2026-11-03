# Play-Annotation-Generator Annotation Review — StopAndGo_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_25`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB1 | offense | `14` | `14` |
| ✅ EXACT | `Action_VerticalStem` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SellStop` | WR2 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB1 | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `14` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | `15` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `21` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 18 | START | 18 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `17` | `17` | 25 | START | 25 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 25 | START | 26 | 55 |
| ✅ EXACT | `Action_PassBlock` | LG | `19` | `19` | 25 | START | 25 | 203 |
| ✅ EXACT | `Action_PassBlock` | RG | `20` | `20` | 25 | START | 25 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `9` | 25 | START | 25 | 96 |
| ✅ EXACT | `Action_SnapReceive` | QB1 | `14` | `14` | 25 | END | 18 | 25 |
| ✅ EXACT | `Action_VerticalStem` | WR2 | `1` | `1` | 35 | START | 35 | 92 |
| ✅ EXACT | `Action_SellStop` | WR2 | `1` | `1` | 93 | START | 93 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR2 | `1` | `1` | 112 | START | 112 | 112 |
| ✅ EXACT | `Action_ThrowPass` | QB1 | `14` | `14` | 117 | START | 117 | 128 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 25 | 8 | inferred_complete_timeline |
| `Action_None` | 26 | 116 | 91 | inferred_complete_timeline |
| `Action_ThrowPass` | 117 | 128 | 12 | inferred_complete_timeline |
| `Action_None` | 129 | 183 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>QB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 191 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 215 | 198 | inferred_complete_timeline |
| `Action_None` | 230 | 238 | 9 | inferred_complete_timeline |
| `Action_None` | 241 | 269 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_VerticalStem` | 35 | 92 | 58 | inferred_complete_timeline |
| `Action_SellStop` | 93 | 111 | 19 | inferred_complete_timeline |
| `Action_RunGoRoute` | 112 | 112 | 1 | inferred_complete_timeline |
| `Action_RunGoRoute` | 115 | 212 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 65 | 48 | inferred_complete_timeline |
| `Action_None` | 76 | 94 | 19 | inferred_complete_timeline |
| `Action_None` | 96 | 148 | 53 | inferred_complete_timeline |
| `Action_None` | 151 | 223 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 136 | 119 | inferred_complete_timeline |
| `Action_None` | 140 | 146 | 7 | inferred_complete_timeline |
| `Action_None` | 150 | 202 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 96 | 72 | inferred_complete_timeline |
| `Action_PassBlock` | 155 | 192 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 203 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_BallSnap` | 18 | 25 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 55 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 63 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 151 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 89 | 65 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 104 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 109 | 207 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 219 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 205 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 43 | 26 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_None` | 50 | 134 | 85 | inferred_complete_timeline |
| `Action_None` | 148 | 156 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 38 | 21 | inferred_complete_timeline |
| `Action_None` | 41 | 269 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 269 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 240 | 223 | inferred_complete_timeline |
| `Action_None` | 242 | 269 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 254 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 233 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 48 | 31 | inferred_complete_timeline |
| `Action_None` | 54 | 57 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 269 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 217 | 200 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 61–119 | 14 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 70–269 | 179 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 72–269 | 198 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 97–98 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 103–189 | 84 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 158–159 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 181–269 | 89 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 249–258 | 10 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 262–265 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF3` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [18–25], lower_priority='Action_PassBlock' annotated_start=25, effective_Action_PassBlock_start=26.
- ⚠️ Action 'Action_None' range [18-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-238] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' for track '1' starts at frame 112, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_RunGoRoute' range [112-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [115-212] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-240] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-205] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-254] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [155-192] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-233] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-134] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-191] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-89] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-104] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [109-207] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-63] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-203] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-69] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-176] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-185] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-258] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '30' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>