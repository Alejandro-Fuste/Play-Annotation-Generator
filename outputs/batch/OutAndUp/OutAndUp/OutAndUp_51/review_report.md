# Play-Annotation-Generator Annotation Review — OutAndUp_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_51`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_SellOut` | WR1 | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_RunGoRoute` | WR1 | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 24 | START | 24 | 38 |
| ✅ EXACT | `Action_PassBlock` | LT | `12` | `12` | 27 | START | 27 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 27 | START | 39 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 27 | START | 27 | 152 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 27 | START | 27 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `4` | `4` | 27 | START | 27 | 186 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 38 | END | 24 | 38 |
| ✅ EXACT | `Action_SellOut` | WR1 | `16` | `16` | 74 | START | 74 | 94 |
| ⚠️ START CHANGED | `Action_RunGoRoute` | WR1 | `16` | `16` | 97 | START | 98 | 179 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 110 | START | 110 | 119 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 38 | 15 | inferred_complete_timeline |
| `Action_None` | 39 | 109 | 71 | inferred_complete_timeline |
| `Action_ThrowPass` | 110 | 119 | 10 | inferred_complete_timeline |
| `Action_None` | 120 | 143 | 24 | inferred_complete_timeline |
| `Action_None` | 145 | 154 | 10 | inferred_complete_timeline |
| `Action_None` | 167 | 227 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 75 | 52 | inferred_complete_timeline |
| `Action_None` | 79 | 241 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SellOut` | 74 | 94 | 21 | inferred_complete_timeline |
| `Action_RunGoRoute` | 98 | 179 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 226 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 227 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 220 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 172 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 152 | 126 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 167 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 38 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 138 | 100 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 146 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 171 | 183 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 189 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 50 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 186 | 160 | inferred_complete_timeline |
| `Action_PassBlock` | 193 | 240 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 60 | 37 | inferred_complete_timeline |
| `Action_None` | 70 | 142 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 249 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 90 | 67 | inferred_complete_timeline |
| `Action_None` | 94 | 165 | 72 | inferred_complete_timeline |
| `Action_None` | 169 | 186 | 18 | inferred_complete_timeline |
| `Action_None` | 188 | 234 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 143 | 120 | inferred_complete_timeline |
| `Action_None` | 145 | 164 | 20 | inferred_complete_timeline |
| `Action_None` | 178 | 186 | 9 | inferred_complete_timeline |
| `Action_None` | 196 | 203 | 8 | inferred_complete_timeline |
| `Action_None` | 205 | 237 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 252 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 212 | 189 | inferred_complete_timeline |
| `Action_None` | 214 | 242 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 269 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 252 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 225 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 269 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 266 | 243 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 54–241 | 171 | 7 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 81–84 | 4 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 121–130 | 6 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 151–236 | 84 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 167–169 | 3 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 170–174 | 5 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 173–227 | 55 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 191–198 | 8 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 209–225 | 16 | 2 | Undefined position; Undefined team |
| `31` | `63` | Position_Unknown | Team_Unknown | 234–269 | 36 | 1 | Undefined position; Undefined team |
| `32` | `70` | Position_Unknown | Team_Unknown | 237–269 | 33 | 1 | Undefined position; Undefined team |
| `33` | `86` | Position_Unknown | Team_Unknown | 245–248 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)
- ⚠️ `Action_RunGoRoute` for actor_track_id `16` (WR1): Annotated start 97 != Inferred start 98

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [24–38], lower_priority='Action_PassBlock' annotated_start=27, effective_Action_PassBlock_start=39.
- ⚠️ Action 'Action_None' range [24-227] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-220] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-60] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-249] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [193-240] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-226] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-186] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-234] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-252] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-143] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-186] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-237] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-266] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-242] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-252] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellOut' range [74-94] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [98-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-227] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-146] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [157-160] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [168-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [171-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-189] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [196-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-152] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-79] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-130] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-241] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-236] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-227] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-198] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-222] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-269] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '33' has 1 frames without a visible bounding box.
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