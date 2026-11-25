# Play-Annotation-Generator Annotation Review — InsideZoneRead_156

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_156`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | SAF1 | defense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | SAF1 | defense | `14` | `13` |
| ✅ EXACT | `Action_BlockSecondLevel` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 10 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 10 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 10 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 10 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 10 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 10 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 10 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 10 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 10 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 10 | 174 |
| ✅ EXACT | `Action_BallSnap` | RT | `13` | `12` | 130 | START | 130 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `12` | 133 | START | 133 | 143 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `16` | `15` | 133 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 133 | START | 133 | 229 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 133 | START | 133 | 229 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | `22` | `21` | 133 | START | 138 | 141 |
| ✅ EXACT | `Action_SnapReceive` | SAF1 | `14` | `13` | 145 | END | 130 | 145 |
| ✅ EXACT | `Action_BallCarry` | SAF1 | `14` | `13` | 169 | START | 169 | 269 |
| ✅ EXACT | `Action_BlockSecondLevel` | RB | `9` | `8` | 175 | START | 175 | 229 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 229 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 10–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 214 | 85 | inferred_complete_timeline |
| `Action_None` | 216 | 235 | 20 | inferred_complete_timeline |
| `Action_None` | 240 | 269 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 174 | 165 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 175 | 229 | 55 | inferred_complete_timeline |
| `Action_None` | 230 | 269 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 229 | 100 | inferred_complete_timeline |
| `Action_None` | 232 | 248 | 17 | inferred_complete_timeline |
| `Action_None` | 255 | 269 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 269 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 10–154
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 148 | 19 | inferred_complete_timeline |
| `Action_None` | 150 | 154 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 132 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 229 | 97 | inferred_complete_timeline |
| `Action_None` | 230 | 244 | 15 | inferred_complete_timeline |
| `Action_None` | 246 | 269 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 132 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 229 | 97 | inferred_complete_timeline |
| `Action_None` | 230 | 245 | 16 | inferred_complete_timeline |
| `Action_None` | 248 | 269 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 10–127
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 122 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 127 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 10–141
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 53 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 108 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 119 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 141 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_BallSnap` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 143 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 229 | 85 | inferred_complete_timeline |
| `Action_None` | 230 | 269 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 269 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 269 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 201 | 72 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_None` | 208 | 269 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 172 | 43 | inferred_complete_timeline |
| `Action_None` | 177 | 245 | 69 | inferred_complete_timeline |
| `Action_None` | 253 | 269 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 10–253
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 243 | 114 | inferred_complete_timeline |
| `Action_None` | 246 | 253 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 10–241
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 241 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 269 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 269 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 150 | 21 | inferred_complete_timeline |
| `Action_None` | 154 | 269 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_SnapReceive` | 130 | 145 | 16 | inferred_complete_timeline |
| `Action_None` | 146 | 168 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 269 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 130 | 269 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 10–269 | 256 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 49–269 | 193 | 6 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 143–185 | 40 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 153–269 | 116 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 165–169 | 5 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 172–269 | 77 | 5 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 231–233 | 3 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 249–251 | 3 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `16` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `22` (RG): Annotated start 133 != Inferred start 138

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 97 frames exceeds threshold 90 frames [start=133, end=229].
- ⚠️ Segment 'Action_ZoneBlock' for track '15' has invalid range: start=133, end=127. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 97 frames exceeds threshold 90 frames [start=133, end=229].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 97 frames exceeds threshold 90 frames [start=133, end=229].
- ⚠️ Action 'Action_None' range [130-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-241] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-229] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-248] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [175-229] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-243] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-143] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-214] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-245] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-244] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-245] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-53] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-119] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-141] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-73] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-128] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-252] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_156'; source metadata written as null.

</details>