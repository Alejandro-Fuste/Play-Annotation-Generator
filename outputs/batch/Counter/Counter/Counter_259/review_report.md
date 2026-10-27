# Play-Annotation-Generator Annotation Review — Counter_259

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_259`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_PullLeadBlock` | WR3 | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB1 | defense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 77 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 78 | START | 78 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `14` | `13` | 81 | START | 81 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `18` | `17` | 81 | START | 93 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `21` | `20` | 81 | START | 81 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `20` | `19` | 81 | START | 81 | 91 |
| ✅ EXACT | `Action_PullLeadBlock` | WR3 | `3` | `2` | 81 | START | 81 | 180 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 92 | END | 78 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB1 | `7` | `6` | 123 | START | 123 | 215 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 180 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_SnapReceive` | 78 | 92 | 15 | inferred_complete_timeline |
| `Action_None` | 93 | 188 | 96 | inferred_complete_timeline |
| `Action_None` | 193 | 231 | 39 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 249 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 204 | 127 | inferred_complete_timeline |
| `Action_None` | 208 | 213 | 6 | inferred_complete_timeline |
| `Action_None` | 216 | 229 | 14 | inferred_complete_timeline |
| `Action_None` | 232 | 257 | 26 | inferred_complete_timeline |
| `Action_None` | 260 | 262 | 3 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 266 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 81 | 180 | 100 | inferred_complete_timeline |
| `Action_None` | 181 | 208 | 28 | inferred_complete_timeline |
| `Action_None` | 216 | 252 | 37 | inferred_complete_timeline |
| `Action_None` | 255 | 269 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 269 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_DownBlock` | 81 | 96 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 124 | 139 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 141 | 180 | 40 | inferred_complete_timeline |
| `Action_None` | 181 | 212 | 32 | inferred_complete_timeline |
| `Action_None` | 218 | 228 | 11 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 254 | 18 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 267 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_DownBlock` | 81 | 87 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 96 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_BallSnap` | 78 | 92 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 96 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PullBlock` | 81 | 91 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 93 | 137 | 45 | inferred_complete_timeline |
| `Action_PullBlock` | 157 | 170 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 176 | 180 | 5 | inferred_complete_timeline |
| `Action_None` | 181 | 210 | 30 | inferred_complete_timeline |
| `Action_None` | 218 | 269 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 155 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 186 | 109 | inferred_complete_timeline |
| `Action_None` | 192 | 240 | 49 | inferred_complete_timeline |
| `Action_None` | 248 | 251 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 168 | 91 | inferred_complete_timeline |
| `Action_None` | 174 | 221 | 48 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 240 | 4 | inferred_complete_timeline |
| `Action_None` | 243 | 248 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 198 | 121 | inferred_complete_timeline |
| `Action_None` | 220 | 226 | 7 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |
| `Action_None` | 241 | 244 | 4 | inferred_complete_timeline |
| `Action_None` | 246 | 269 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 114 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 236 | 159 | inferred_complete_timeline |
| `Action_None` | 241 | 258 | 18 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_BallCarry` | 123 | 215 | 93 | inferred_complete_timeline |
| `Action_BallCarry` | 218 | 229 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 164 | 87 | inferred_complete_timeline |
| `Action_None` | 167 | 269 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 201 | 124 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 269 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 225 | 148 | inferred_complete_timeline |
| `Action_None` | 249 | 269 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 229 | 152 | inferred_complete_timeline |
| `Action_None` | 234 | 251 | 18 | inferred_complete_timeline |
| `Action_None` | 255 | 258 | 4 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 7–269 | 242 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 48–269 | 222 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 107–269 | 80 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 109–269 | 155 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 110–267 | 149 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 121–269 | 149 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 135–138 | 4 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 247–250 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 520: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (LT) duration 100 frames exceeds threshold 90 frames [start=81, end=180].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [78–92], lower_priority='Action_DownBlock' annotated_start=81, effective_Action_DownBlock_start=93.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '19' (RG) duration 100 frames exceeds threshold 90 frames [start=81, end=180].
- ⚠️ Action 'Action_None' range [78-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-229] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-257] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-266] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-208] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-252] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-215] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [218-229] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-229] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-251] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-188] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-231] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-236] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-114] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-240] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [81-96] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [124-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-228] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-254] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-267] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-168] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-248] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [93-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [98-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [81-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [93-137] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [157-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [81-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [90-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [94-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-257] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-218] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-257] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-228] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-252] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-117] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-218] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-267] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>