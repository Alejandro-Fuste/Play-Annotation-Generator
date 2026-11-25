# Play-Annotation-Generator Annotation Review — InsideZoneRead_221

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_221`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 4
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | RG | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | RG | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_Handoff` | RG | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 12 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 31 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 64 |
| ✅ EXACT | `Action_BallSnap` | QB | `10` | `9` | 65 | START | 65 | 82 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `11` | `10` | 68 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `13` | 68 | START | 68 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 68 | START | 68 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `2` | 68 | START | 68 | 155 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `5` | 68 | START | 68 | 162 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | RG | `11` | `10` | 82 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | RG | `11` | `10` | 86 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Handoff` | RG | `11` | `10` | 103 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `21` | `16` | 110 | START | 143 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | QB | `10` | `9` | 115 | START | 115 | 132 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 162 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_BallSnap` | 65 | 82 | 18 | inferred_complete_timeline |
| `Action_None` | 83 | 114 | 32 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 115 | 132 | 18 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 135 | 162 | 28 | inferred_complete_timeline |
| `Action_None` | 163 | 254 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 270 | 206 | inferred_complete_timeline |
| `Action_None` | 272 | 283 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 155 | 88 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 158 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 67 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 162 | 95 | inferred_complete_timeline |
| `Action_None` | 163 | 180 | 18 | inferred_complete_timeline |
| `Action_None` | 185 | 189 | 5 | inferred_complete_timeline |
| `Action_None` | 191 | 208 | 18 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 299 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 31–299
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 54 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 71 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 103 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 162 | 29 | inferred_complete_timeline |
| `Action_None` | 163 | 264 | 102 | inferred_complete_timeline |
| `Action_None` | 268 | 299 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 162 | 95 | inferred_complete_timeline |
| `Action_None` | 163 | 181 | 19 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 299 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 154 | 90 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 278 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 153 | 89 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 299 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 158 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 299 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 129 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–299 | 299 | 3 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 132–299 | 164 | 2 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 143–299 | 157 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 170–299 | 128 | 2 | Undefined position; Undefined team |
| `18` | `26` | Position_Unknown | Team_Unknown | 174–294 | 120 | 2 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 174–299 | 126 | 1 | Undefined position; Undefined team |
| `20` | `31` | Position_Unknown | Team_Unknown | 190–299 | 110 | 1 | Undefined position; Undefined team |
| `21` | `34` | Position_Unknown | Team_Unknown | 208–297 | 90 | 1 | Undefined position; Undefined team |
| `22` | `35` | Position_Unknown | Team_Unknown | 208–276 | 13 | 3 | Undefined position; Undefined team |
| `23` | `36` | Position_Unknown | Team_Unknown | 209–280 | 71 | 2 | Undefined position; Undefined team |
| `24` | `38` | Position_Unknown | Team_Unknown | 216–271 | 53 | 3 | Undefined position; Undefined team |
| `25` | `40` | Position_Unknown | Team_Unknown | 225–299 | 75 | 1 | Undefined position; Undefined team |
| `26` | `41` | Position_Unknown | Team_Unknown | 226–231 | 6 | 1 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 235–299 | 65 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 240–244 | 4 | 2 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 248–267 | 10 | 2 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 269–299 | 31 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 273–299 | 26 | 2 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 273–274 | 2 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 291–295 | 5 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `11` (RG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `11` (RG)
- ❌ Missing segment for action `Action_ReadDefender` on target `11` (RG)
- ❌ Missing segment for action `Action_Handoff` on target `11` (RG)
- ⚠️ `Action_BallCarry` for actor_track_id `21` (Position_Unknown): Annotated start 110 != Inferred start 143
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 8 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 91 frames exceeds threshold 90 frames [start=68, end=158].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 95 frames exceeds threshold 90 frames [start=68, end=162].
- ⚠️ Segment 'Action_ZoneBlock' for track '10' has invalid range: start=68, end=7. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '10' has invalid range: start=65, end=7. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '10' has invalid range: start=86, end=7. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '10' has invalid range: start=103, end=7. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LG) duration 95 frames exceeds threshold 90 frames [start=68, end=162].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 95 frames exceeds threshold 90 frames [start=68, end=162].
- ⚠️ Action 'Action_None' range [65-135] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-278] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-270] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-283] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [115-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-254] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-208] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-162] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 163, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [163-264] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-272] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [143-299] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-282] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-294] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-297] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-277] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-227] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-271] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-293] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-295] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_221'; source metadata written as null.

</details>