# Play-Annotation-Generator Annotation Review — InsideZoneRead_175

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_175`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 85
- **Validation Warnings:** 115
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 1
- **Group Expanded Events:** 3
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `29` | `22` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `13` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 21 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 21 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `29` | `22` | 30 | START | 161 | 161 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `1` | `0` | 33 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `9` | 33 | START | 33 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `13` | 33 | START | 58 | 59 |
| ✅ EXACT | `Action_SnapReceive` | RG | `1` | `0` | 47 | END | 30 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | RG | `1` | `0` | 53 | START | 53 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | `1` | `0` | 70 | START | 70 | 91 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 86 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 21–53
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 32 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 49 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 53 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 58–247
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_None` | 88 | 221 | 134 | inferred_complete_timeline |
| `Action_None` | 225 | 242 | 18 | inferred_complete_timeline |
| `Action_None` | 245 | 247 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 21–194
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 29 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 30 | 47 | 18 | inferred_complete_timeline |
| `Action_None` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 91 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 121 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 137 | 146 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 153 | 186 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 190 | 194 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 21–85
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 29 | 9 | inferred_complete_timeline |
| `Action_None` | 30 | 80 | 51 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 21–77
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 29 | 9 | inferred_complete_timeline |
| `Action_None` | 30 | 77 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 21–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 29 | 9 | inferred_complete_timeline |
| `Action_None` | 30 | 269 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 21–250
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 29 | 9 | inferred_complete_timeline |
| `Action_None` | 30 | 199 | 170 | inferred_complete_timeline |
| `Action_None` | 201 | 250 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 21–78
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 29 | 9 | inferred_complete_timeline |
| `Action_None` | 30 | 75 | 46 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 21–269
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 29 | 9 | inferred_complete_timeline |
| `Action_None` | 30 | 253 | 224 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 21–191 | 161 | 4 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 21–143 | 114 | 5 | Undefined position; Undefined team |
| `10` | `14` | Position_Unknown | Team_Unknown | 38–91 | 54 | 1 | Undefined position; Undefined team |
| `11` | `15` | Position_Unknown | Team_Unknown | 38–269 | 210 | 6 | Undefined position; Undefined team |
| `12` | `16` | Position_Unknown | Team_Unknown | 54–168 | 105 | 5 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 74–269 | 190 | 4 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 114–269 | 103 | 2 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 115–188 | 62 | 2 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 135–269 | 135 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 141–176 | 27 | 2 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 142–224 | 83 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 158–195 | 38 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 158–186 | 19 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 161–269 | 109 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 164–198 | 35 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 166–234 | 45 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 187–269 | 82 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 212–269 | 58 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 249–255 | 7 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 260–269 | 10 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `27` | `34` | 189 | 189 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `29` (Position_Unknown): Annotated start 30 != Inferred start 161
- ❌ Missing segment for action `Action_ZoneBlock` on target `1` (RG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 350: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '0' has invalid range: start=33, end=29. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '22' has invalid range: start=161, end=47. Clamping end to start.
- ⚠️ Action 'Action_ReadDefender' for track '0' starts at frame 53, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ReadDefender' range [53-53] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-91] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [97-121] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [137-146] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [153-186] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-194] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-80] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-87] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-146] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-191] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-75] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-253] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-199] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-77] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-23] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-108] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-117] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-143] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-32] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-49] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-53] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-91] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-211] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-247] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-91] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-146] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-168] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-221] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-208] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-188] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-224] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-195] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-174] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-242] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-255] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_175'; source metadata written as null.

</details>