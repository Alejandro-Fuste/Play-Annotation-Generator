# Play-Annotation-Generator Annotation Review — InsideZoneRead_346

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_346`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `5` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `20` | `18` |
| ✅ EXACT | `Action_Keep` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 15 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `19` | `17` | 13 | START | 64 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `11` | 16 | START | 16 | 79 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 16 | START | 16 | 89 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `3` | 16 | START | 16 | 89 |
| ✅ EXACT | `Action_ZoneBlock` | C | `8` | `7` | 16 | START | 16 | 89 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 27 | END | 13 | 27 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `5` | 32 | START | 32 | 37 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | Position_Unknown | `20` | `18` | 38 | START | 78 | 84 |
| ✅ EXACT | `Action_Keep` | QB | `6` | `5` | 38 | START | 38 | 58 |
| ✅ EXACT | `Action_BallCarry` | QB | `6` | `5` | 59 | START | 59 | 205 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 89 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 13 | 27 | 15 | inferred_complete_timeline |
| `Action_None` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 32 | 37 | 6 | inferred_complete_timeline |
| `Action_Keep` | 38 | 58 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 59 | 205 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 58 | 46 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 89 | 74 | inferred_complete_timeline |
| `Action_None` | 90 | 107 | 18 | inferred_complete_timeline |
| `Action_None` | 113 | 210 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 79 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 89 | 8 | inferred_complete_timeline |
| `Action_None` | 90 | 210 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 89 | 74 | inferred_complete_timeline |
| `Action_None` | 90 | 198 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 89 | 74 | inferred_complete_timeline |
| `Action_None` | 90 | 210 | 121 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 43 | 31 | inferred_complete_timeline |
| `Action_None` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_None` | 63 | 82 | 20 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 49 | 37 | inferred_complete_timeline |
| `Action_None` | 52 | 55 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 32 | 136 | 105 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 123 | 111 | inferred_complete_timeline |
| `Action_None` | 125 | 148 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 138 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 116 | 104 | inferred_complete_timeline |
| `Action_None` | 118 | 210 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 39 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 55–210 | 145 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 64–147 | 84 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 78–210 | 119 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 94–210 | 106 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 100–210 | 111 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 131–142 | 11 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 152–210 | 59 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 165–197 | 33 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 166–210 | 45 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 168–205 | 38 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 183–201 | 19 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 195–210 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `19` (Position_Unknown): Annotated start 13 != Inferred start 64
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `20` (Position_Unknown): Annotated start 38 != Inferred start 78

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 692: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=64, end=27. Clamping end to start.
- ⚠️ Action 'Action_None' range [13-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-107] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-210] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-58] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [59-205] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-123] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-198] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-29] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-136] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-49] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-55] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-82] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-210] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-60] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [78-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-210] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-197] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-201] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_346'; source metadata written as null.

</details>