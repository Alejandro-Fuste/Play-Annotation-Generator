# Play-Annotation-Generator Annotation Review — SplitZone_220

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_220`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | LB1 | defense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_BallCarry` | RG | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 54 |
| ✅ EXACT | `Action_BallSnap` | LT | `8` | `8` | 55 | START | 55 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `10` | 58 | START | 58 | 116 |
| ✅ EXACT | `Action_ZoneBlock` | C | `11` | `11` | 58 | START | 58 | 144 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `3` | 58 | START | 58 | 192 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `7` | `7` | 58 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 58 | START | 58 | 192 |
| ✅ EXACT | `Action_SplitBlock` | LB1 | `6` | `6` | 64 | START | 64 | 192 |
| ✅ EXACT | `Action_SnapReceive` | RG | `7` | `7` | 71 | END | 55 | 71 |
| ✅ EXACT | `Action_BallCarry` | RG | `7` | `7` | 93 | START | 93 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 192 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 210 | 156 | inferred_complete_timeline |
| `Action_None` | 217 | 241 | 25 | inferred_complete_timeline |
| `Action_None` | 246 | 269 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 47 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 54 | 5 | inferred_complete_timeline |
| `Action_None` | 55 | 74 | 20 | inferred_complete_timeline |
| `Action_None` | 76 | 86 | 11 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 118 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 269 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_BallSnap` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 192 | 135 | inferred_complete_timeline |
| `Action_None` | 193 | 269 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 116 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 192 | 65 | inferred_complete_timeline |
| `Action_None` | 193 | 269 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 144 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_SnapReceive` | 55 | 71 | 17 | inferred_complete_timeline |
| `Action_None` | 72 | 92 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 93 | 269 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 192 | 135 | inferred_complete_timeline |
| `Action_None` | 193 | 231 | 39 | inferred_complete_timeline |
| `Action_None` | 236 | 269 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 269 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 269 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 149 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 78 | 24 | inferred_complete_timeline |
| `Action_None` | 80 | 86 | 7 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SplitBlock` | 64 | 192 | 129 | inferred_complete_timeline |
| `Action_None` | 193 | 269 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 93 | 39 | inferred_complete_timeline |
| `Action_None` | 96 | 173 | 78 | inferred_complete_timeline |
| `Action_None` | 175 | 269 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 138 | 84 | inferred_complete_timeline |
| `Action_None` | 142 | 145 | 4 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 269 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–98 | 99 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 113–269 | 157 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 116–118 | 3 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 129–269 | 128 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 141–269 | 129 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 143–151 | 9 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 146–269 | 123 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 163–238 | 75 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 219–269 | 41 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 219–229 | 11 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 228–235 | 8 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 246–269 | 21 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 248–269 | 22 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 257–263 | 7 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 264–266 | 3 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 264–269 | 6 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 265–269 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `7` (RG)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 135 frames exceeds threshold 90 frames [start=58, end=192].
- ⚠️ Segment 'Action_ZoneBlock' for track '7' has invalid range: start=58, end=54. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (LT) duration 135 frames exceeds threshold 90 frames [start=58, end=192].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (LG) duration 135 frames exceeds threshold 90 frames [start=58, end=192].
- ⚠️ Action 'Action_None' range [55-138] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-93] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-173] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-47] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-74] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-86] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-118] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-241] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-269] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-192] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-208] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-234] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-254] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '31' has 1 frames without a visible bounding box.
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

</details>