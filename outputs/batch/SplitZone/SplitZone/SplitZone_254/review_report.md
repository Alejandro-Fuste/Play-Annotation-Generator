# Play-Annotation-Generator Annotation Review — SplitZone_254

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_254`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 0
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `17` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 2 | START | 3 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 2 | START | 3 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 2 | START | 3 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 2 | START | 3 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 2 | START | 28 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 2 | START | 3 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 2 | START | 3 | 132 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `17` | `15` | 130 | START | 135 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `0` | `0` | 132 | START | 132 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `10` | 133 | START | 133 | 159 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `12` | `12` | 133 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 133 | START | 133 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `7` | 133 | START | 133 | 179 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `15` | `14` | 138 | END | 131 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `15` | `14` | 168 | START | 168 | 170 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 219 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 28–389
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 124 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 131 | 137 | 7 | inferred_complete_timeline |
| `Action_None` | 142 | 156 | 15 | inferred_complete_timeline |
| `Action_None` | 161 | 167 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 168 | 170 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 222 | 389 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–229
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 129 | 127 | inferred_complete_timeline |
| `Action_None` | 130 | 165 | 36 | inferred_complete_timeline |
| `Action_None` | 173 | 178 | 6 | inferred_complete_timeline |
| `Action_None` | 181 | 229 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 3–255
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 131 | 129 | inferred_complete_timeline |
| `Action_SplitBlock` | 132 | 160 | 29 | inferred_complete_timeline |
| `Action_SplitBlock` | 187 | 196 | 10 | inferred_complete_timeline |
| `Action_SplitBlock` | 198 | 219 | 22 | inferred_complete_timeline |
| `Action_None` | 220 | 245 | 26 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 3–216
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 132 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 179 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 216 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 3–214
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 27 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 132 | 104 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 159 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 214 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 3–17
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 14 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–214
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 132 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 142 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 157 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 168 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 214 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 129 | 127 | inferred_complete_timeline |
| `Action_None` | 130 | 179 | 50 | inferred_complete_timeline |
| `Action_None` | 181 | 371 | 191 | inferred_complete_timeline |
| `Action_None` | 378 | 379 | 2 | inferred_complete_timeline |
| `Action_None` | 384 | 389 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–212
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 129 | 127 | inferred_complete_timeline |
| `Action_None` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_None` | 138 | 212 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–212
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 129 | 127 | inferred_complete_timeline |
| `Action_None` | 130 | 149 | 20 | inferred_complete_timeline |
| `Action_None` | 153 | 212 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–183
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 129 | 127 | inferred_complete_timeline |
| `Action_None` | 130 | 183 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 3–213
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 129 | 127 | inferred_complete_timeline |
| `Action_None` | 130 | 174 | 45 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 192 | 7 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 213 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–389
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 129 | 127 | inferred_complete_timeline |
| `Action_None` | 130 | 136 | 7 | inferred_complete_timeline |
| `Action_None` | 144 | 196 | 53 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |
| `Action_None` | 215 | 233 | 19 | inferred_complete_timeline |
| `Action_None` | 235 | 240 | 6 | inferred_complete_timeline |
| `Action_None` | 242 | 389 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–161
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 129 | 127 | inferred_complete_timeline |
| `Action_None` | 130 | 161 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 3–22 | 20 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 135–201 | 60 | 5 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 161–191 | 31 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 161–178 | 18 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 172–179 | 7 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 173–214 | 41 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 175–261 | 85 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 177–286 | 108 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 200–209 | 10 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 220–223 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 244–289 | 41 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 250–389 | 126 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 294–296 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 300–389 | 90 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 310–332 | 23 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 348–389 | 38 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 352–389 | 38 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 383–389 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `17` (Position_Unknown): Annotated start 130 != Inferred start 135
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `0` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `12` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 510: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '12' has invalid range: start=133, end=17. Clamping end to start.
- ⚠️ Action 'Action_SplitBlock' range [132-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [187-196] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-245] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-165] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-229] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-214] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-212] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-196] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-233] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-240] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-389] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-179] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-371] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-216] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-212] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-27] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-132] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [161-214] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-22] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-14] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-183] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [131-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-156] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [168-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [222-389] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [135-138] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-189] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-178] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-214] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-261] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-286] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-282] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-340] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-361] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-370] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-332] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-373] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-377] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>