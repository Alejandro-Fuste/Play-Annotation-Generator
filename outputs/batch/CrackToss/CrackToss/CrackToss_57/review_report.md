# Play-Annotation-Generator Annotation Review — CrackToss_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_57`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 123
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 1
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | DE1 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 134 |
| ⚠️ START CHANGED | `Action_BallSnap` | C | `15` | `14` | 135 | START | 147 | 147 |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | `1` | `0` | 138 | START | 138 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `4` | `3` | 138 | START | 138 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | DE1 | `11` | `10` | 147 | END | 135 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `17` | `16` | 163 | START | 163 | 194 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 187 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 78 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 162 | 80 | inferred_complete_timeline |
| `Action_BallCarry` | 163 | 194 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 203 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 207 | 267 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 110 | 77 | inferred_complete_timeline |
| `Action_None` | 144 | 158 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 163 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 132 | 20 | inferred_complete_timeline |
| `Action_None` | 135 | 192 | 58 | inferred_complete_timeline |
| `Action_None` | 197 | 205 | 9 | inferred_complete_timeline |
| `Action_None` | 208 | 232 | 25 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 185 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 287 | 153 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 61 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 103 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 131 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 147 | 147 | 1 | inferred_complete_timeline |
| `Action_None` | 148 | 199 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 163 | 29 | inferred_complete_timeline |
| `Action_None` | 171 | 299 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 137 | 67 | inferred_complete_timeline |
| `Action_PullBlock` | 138 | 169 | 32 | inferred_complete_timeline |
| `Action_PullBlock` | 174 | 185 | 12 | inferred_complete_timeline |
| `Action_None` | 190 | 199 | 10 | inferred_complete_timeline |
| `Action_None` | 203 | 207 | 5 | inferred_complete_timeline |
| `Action_None` | 209 | 218 | 10 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 251 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 73 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 125 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 133 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 139 | 147 | 9 | inferred_complete_timeline |
| `Action_None` | 148 | 159 | 12 | inferred_complete_timeline |
| `Action_None` | 163 | 191 | 29 | inferred_complete_timeline |
| `Action_None` | 193 | 235 | 43 | inferred_complete_timeline |
| `Action_None` | 268 | 299 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 147 | 13 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 163 | 186 | 24 | inferred_complete_timeline |
| `Action_None` | 189 | 220 | 32 | inferred_complete_timeline |
| `Action_None` | 223 | 299 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 183 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 208 | 74 | inferred_complete_timeline |
| `Action_None` | 213 | 234 | 22 | inferred_complete_timeline |
| `Action_None` | 237 | 243 | 7 | inferred_complete_timeline |
| `Action_None` | 246 | 250 | 5 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 222 | 88 | inferred_complete_timeline |
| `Action_None` | 224 | 255 | 32 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 134 | 17 | inferred_complete_timeline |
| `Action_None` | 135 | 150 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 282 | 148 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–266 | 266 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 22–153 | 117 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 29–91 | 33 | 7 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 59–206 | 133 | 4 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 98–276 | 110 | 4 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 99–175 | 73 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 162–246 | 84 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 182–191 | 10 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 227–299 | 73 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 229–299 | 67 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 264–296 | 23 | 3 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 279–299 | 21 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 284–297 | 11 | 3 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 297–299 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `15` (C): Annotated start 135 != Inferred start 147
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 116: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_CrackBlock' range [138-187] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-261] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-185] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [138-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [174-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-199] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-251] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-282] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-208] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-222] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-255] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-163] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-73] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-125] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [135-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-235] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-192] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-205] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-232] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-287] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-61] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-103] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-199] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-110] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [163-194] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-38] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-68] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-105] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-216] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-276] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-175] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-246] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-283] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-281] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.

</details>