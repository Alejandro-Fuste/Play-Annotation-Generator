# Play-Annotation-Generator Annotation Review — InsideZoneRead_166

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_166`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 132
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | CB4 | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | CB4 | defense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_Handoff` | CB4 | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 82 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 83 | START | 83 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 86 | START | 96 | 104 |
| ✅ EXACT | `Action_SnapReceive` | CB4 | `14` | `13` | 95 | END | 83 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | CB4 | `14` | `13` | 100 | START | 100 | 100 |
| ❌ MISSING SEGMENT | `Action_Handoff` | CB4 | `14` | `13` | 117 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 126 | START | 126 | 138 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 173 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 126 | 138 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 140 | 141 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 162 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 286 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 175 | 93 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 299 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_BallSnap` | 83 | 95 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 104 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 130 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 159 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 170 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 150 | 68 | inferred_complete_timeline |
| `Action_None` | 179 | 192 | 14 | inferred_complete_timeline |
| `Action_None` | 194 | 203 | 10 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 211 | 273 | 63 | inferred_complete_timeline |
| `Action_None` | 276 | 299 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 95 | 13 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 130 | 12 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 81 | 4 | inferred_complete_timeline |
| `Action_None` | 98 | 107 | 10 | inferred_complete_timeline |
| `Action_None` | 109 | 141 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 257 | 175 | inferred_complete_timeline |
| `Action_None` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_None` | 265 | 284 | 20 | inferred_complete_timeline |
| `Action_None` | 288 | 291 | 4 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 96 | 14 | inferred_complete_timeline |
| `Action_None` | 98 | 116 | 19 | inferred_complete_timeline |
| `Action_None` | 119 | 125 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 200 | 118 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 231 | 25 | inferred_complete_timeline |
| `Action_None` | 233 | 299 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_SnapReceive` | 83 | 95 | 13 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 100 | 100 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 105 | 106 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 215 | 133 | inferred_complete_timeline |
| `Action_None` | 219 | 275 | 57 | inferred_complete_timeline |
| `Action_None` | 285 | 288 | 4 | inferred_complete_timeline |
| `Action_None` | 291 | 299 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–297 | 298 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–18 | 19 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 120–135 | 13 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 120–291 | 112 | 10 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 123–124 | 2 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 123–128 | 6 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 123–135 | 6 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 125–299 | 175 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 150–152 | 3 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 170–269 | 91 | 3 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 192–253 | 54 | 4 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 202–299 | 98 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 204–299 | 91 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 207–299 | 91 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 209–213 | 5 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 215–299 | 85 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 219–299 | 81 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 220–299 | 76 | 3 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 221–270 | 43 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 235–299 | 65 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 238–280 | 38 | 3 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 283–295 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `14` (2 segments found)
- ❌ Missing segment for action `Action_Handoff` on target `14` (CB4)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 332: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_Handoff' for track '13' has invalid range: start=117, end=106. Clamping end to start.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [83–95], lower_priority='Action_ZoneBlock' annotated_start=86, effective_Action_ZoneBlock_start=96.
- ⚠️ Action 'Action_None' range [83-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-231] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-162] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-121] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [126-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [140-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-257] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-284] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-286] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-215] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-275] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-81] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-141] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' for track '13' starts at frame 100, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ReadDefender' range [100-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [105-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [119-130] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [165-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-192] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-203] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-130] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-130] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-192] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-208] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-249] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-262] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-291] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-128] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-299] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-191] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-269] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-236] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-253] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-287] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-288] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-236] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-253] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-270] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-254] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-280] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-295] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>