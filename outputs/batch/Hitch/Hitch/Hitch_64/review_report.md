# Play-Annotation-Generator Annotation Review — Hitch_64

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_64`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 99
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_RunHitchRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 59 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 60 | START | 60 | 66 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `10` | `10` | 63 | START | 67 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `13` | `13` | 63 | START | 63 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 63 | START | 63 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 63 | START | 63 | 78 |
| ✅ EXACT | `Action_PassBlock` | RT | `21` | `21` | 63 | START | 63 | 77 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 66 | END | 60 | 66 |
| ✅ EXACT | `Action_RunHitchRoute` | WR1 | `0` | `0` | 76 | START | 76 | 151 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 139 | START | 139 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `0` | `0` | 189 | START | 189 | 230 |

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
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_SnapReceive` | 60 | 66 | 7 | inferred_complete_timeline |
| `Action_None` | 67 | 138 | 72 | inferred_complete_timeline |
| `Action_ThrowPass` | 139 | 145 | 7 | inferred_complete_timeline |
| `Action_None` | 146 | 259 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 185 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 76 | 151 | 76 | inferred_complete_timeline |
| `Action_None` | 152 | 188 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 189 | 230 | 42 | inferred_complete_timeline |
| `Action_BallCarry` | 233 | 249 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 252 | 259 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 257 | 198 | inferred_complete_timeline |
| `Action_None` | 267 | 291 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 194 | 135 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 91 | 32 | inferred_complete_timeline |
| `Action_None` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_None` | 104 | 134 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 179 | 117 | inferred_complete_timeline |
| `Action_PassBlock` | 189 | 197 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 201 | 329 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 80 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 95 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 143 | 145 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 149 | 329 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_BallSnap` | 60 | 66 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 75 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 78 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 110 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 118 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 77 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 182 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 302 | 243 | inferred_complete_timeline |
| `Action_None` | 308 | 322 | 15 | inferred_complete_timeline |
| `Action_None` | 325 | 329 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 166 | 107 | inferred_complete_timeline |
| `Action_None` | 169 | 220 | 52 | inferred_complete_timeline |
| `Action_None` | 225 | 229 | 5 | inferred_complete_timeline |
| `Action_None` | 232 | 329 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 80 | 21 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_None` | 99 | 247 | 149 | inferred_complete_timeline |
| `Action_None` | 249 | 329 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 314 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 161 | 102 | inferred_complete_timeline |
| `Action_None` | 167 | 220 | 54 | inferred_complete_timeline |
| `Action_None` | 227 | 329 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 229 | 170 | inferred_complete_timeline |
| `Action_None` | 231 | 249 | 19 | inferred_complete_timeline |
| `Action_None` | 253 | 259 | 7 | inferred_complete_timeline |
| `Action_None` | 264 | 283 | 20 | inferred_complete_timeline |
| `Action_None` | 287 | 297 | 11 | inferred_complete_timeline |
| `Action_None` | 299 | 329 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 220 | 161 | inferred_complete_timeline |
| `Action_None` | 222 | 225 | 4 | inferred_complete_timeline |
| `Action_None` | 228 | 329 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 125 | 66 | inferred_complete_timeline |
| `Action_None` | 128 | 223 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 302 | 243 | inferred_complete_timeline |
| `Action_None` | 313 | 314 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–149 | 150 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 14–19 | 6 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 142–144 | 3 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 159–272 | 113 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 190–329 | 126 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 195–276 | 73 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 202–299 | 98 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 202–329 | 128 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 233–255 | 23 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 242–243 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 251–255 | 5 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 255–329 | 67 | 4 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 274–329 | 56 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `10` (C): Annotated start 63 != Inferred start 67
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [60–66], lower_priority='Action_PassBlock' annotated_start=63, effective_Action_PassBlock_start=67.
- ⚠️ Action 'Action_BallCarry' range [189-230] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [233-249] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [252-259] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-257] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-291] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-185] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-223] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-229] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-249] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-259] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-283] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-297] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-194] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-322] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-220] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-314] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-166] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-179] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [189-197] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [201-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-161] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-220] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-91] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-134] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-247] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-182] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-80] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-95] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [143-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-78] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-19] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-272] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-203] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-230] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-276] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-299] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-255] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-261] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-291] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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