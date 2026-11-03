# Play-Annotation-Generator Annotation Review — StopAndGo_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_7`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_VerticalStem` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_SellStop` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_RunGoRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `19` | `19` | 23 | START | 23 | 39 |
| ✅ EXACT | `Action_PassBlock` | LT | `11` | `11` | 26 | START | 26 | 139 |
| ✅ EXACT | `Action_PassBlock` | C | `15` | `15` | 26 | START | 26 | 226 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 26 | START | 26 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 26 | START | 26 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `7` | `7` | 26 | START | 26 | 169 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 39 | END | 23 | 39 |
| ✅ EXACT | `Action_VerticalStem` | WR3 | `0` | `0` | 39 | START | 39 | 86 |
| ✅ EXACT | `Action_SellStop` | WR3 | `0` | `0` | 87 | START | 87 | 103 |
| ✅ EXACT | `Action_RunGoRoute` | WR3 | `0` | `0` | 104 | START | 104 | 299 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 118 | START | 118 | 129 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 39 | 17 | inferred_complete_timeline |
| `Action_None` | 40 | 117 | 78 | inferred_complete_timeline |
| `Action_ThrowPass` | 118 | 129 | 12 | inferred_complete_timeline |
| `Action_None` | 130 | 136 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 245 | 223 | inferred_complete_timeline |
| `Action_None` | 247 | 273 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 170 | 148 | inferred_complete_timeline |
| `Action_None` | 174 | 269 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_VerticalStem` | 39 | 86 | 48 | inferred_complete_timeline |
| `Action_SellStop` | 87 | 103 | 17 | inferred_complete_timeline |
| `Action_RunGoRoute` | 104 | 299 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 76 | 54 | inferred_complete_timeline |
| `Action_None` | 80 | 126 | 47 | inferred_complete_timeline |
| `Action_None` | 130 | 171 | 42 | inferred_complete_timeline |
| `Action_None` | 179 | 181 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 139 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 171 | 146 | inferred_complete_timeline |
| `Action_PassBlock` | 177 | 216 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 218 | 219 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 226 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 81 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 95 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 133 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 163 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 165 | 175 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 190 | 193 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 211 | 217 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 219 | 233 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 169 | 144 | inferred_complete_timeline |
| `Action_PassBlock` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 228 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 153 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 137 | 115 | inferred_complete_timeline |
| `Action_None` | 139 | 147 | 9 | inferred_complete_timeline |
| `Action_None` | 149 | 180 | 32 | inferred_complete_timeline |
| `Action_None` | 182 | 191 | 10 | inferred_complete_timeline |
| `Action_None` | 193 | 212 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 262 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 243 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 196 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 293 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 104 | 82 | inferred_complete_timeline |
| `Action_None` | 109 | 299 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 247 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 299 | 277 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 283 | 261 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–209 | 150 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 79–146 | 36 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 90–92 | 3 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 148–170 | 23 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 148–193 | 42 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 163–206 | 44 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 188–245 | 51 | 4 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 215–216 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 232–252 | 18 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 276–277 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 284–299 | 10 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 287–298 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (11 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 11: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [23-170] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-269] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-245] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-273] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-293] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-196] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [178-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-76] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-171] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-137] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-191] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-212] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-139] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-262] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-228] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-226] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-243] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-133] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-163] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [165-175] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [177-178] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [190-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [200-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [211-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [219-233] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-283] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-158] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-209] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-247] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-171] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [177-216] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [218-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-118] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-170] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-172] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-193] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-206] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-245] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-248] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-289] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-298] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>