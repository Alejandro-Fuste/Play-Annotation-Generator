# Play-Annotation-Generator Annotation Review — Dagger_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_24`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_BreakInside` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 132 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 130 | START | 130 | 134 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `12` | `12` | 133 | START | 135 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `17` | 133 | START | 133 | 142 |
| ✅ EXACT | `Action_PassBlock` | RG | `19` | `19` | 133 | START | 133 | 144 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 133 | START | 133 | 144 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 134 | END | 130 | 134 |
| ✅ EXACT | `Action_BreakInside` | WR2 | `0` | `0` | 147 | START | 147 | 269 |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | `1` | `1` | 147 | START | 147 | 232 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | `18` | `18` | 221 | START | 221 | 223 |

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
- **Visible Frames:** 0–246
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_SnapReceive` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_None` | 135 | 145 | 11 | inferred_complete_timeline |
| `Action_None` | 147 | 154 | 8 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 220 | 58 | inferred_complete_timeline |
| `Action_ThrowPass` | 221 | 223 | 3 | inferred_complete_timeline |
| `Action_ThrowPass` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_ThrowPass` | 230 | 232 | 3 | inferred_complete_timeline |
| `Action_None` | 233 | 246 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 180 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_ClearToEdge` | 147 | 232 | 86 | inferred_complete_timeline |
| `Action_None` | 233 | 247 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_BreakInside` | 147 | 269 | 123 | inferred_complete_timeline |
| `Action_None` | 270 | 285 | 16 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |
| `Action_None` | 294 | 298 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 145 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 142 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 173 | 319 | 147 | inferred_complete_timeline |
| `Action_PassBlock` | 322 | 324 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 144 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_BallSnap` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 144 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 144 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 144 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 144 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 145 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 306 | 177 | inferred_complete_timeline |
| `Action_None` | 314 | 317 | 4 | inferred_complete_timeline |
| `Action_None` | 319 | 329 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 329 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 171 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 155 | 26 | inferred_complete_timeline |
| `Action_None` | 159 | 165 | 7 | inferred_complete_timeline |
| `Action_None` | 168 | 185 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 329 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 308 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 212 | 83 | inferred_complete_timeline |
| `Action_None` | 215 | 222 | 8 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 237 | 3 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 329 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 247 | 118 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–148 | 149 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 29–247 | 202 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 178–203 | 22 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 200–203 | 4 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 203–274 | 67 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 209–226 | 13 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 221–252 | 18 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 266–274 | 9 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 276–329 | 54 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 278–329 | 52 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 283–284 | 2 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `12` (C): Annotated start 133 != Inferred start 135
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 26: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [130–134], lower_priority='Action_PassBlock' annotated_start=133, effective_Action_PassBlock_start=135.
- ⚠️ Action 'Action_None' range [270-285] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-298] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-247] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-148] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-308] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-155] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-185] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-212] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-306] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [173-319] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [322-324] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [328-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [221-223] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [225-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-246] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-144] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-247] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-203] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-274] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-215] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-235] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-274] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-329] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.

</details>