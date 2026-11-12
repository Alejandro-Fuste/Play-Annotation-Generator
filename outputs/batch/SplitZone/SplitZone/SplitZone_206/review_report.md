# Play-Annotation-Generator Annotation Review — SplitZone_206

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_206`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | DT | defense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `3` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `26` | `22` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 23 | START | 24 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 23 | START | 24 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 23 | START | 24 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 23 | START | 24 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 23 | START | 24 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 23 | START | 24 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 23 | START | 24 | 98 |
| ⚠️ START CHANGED | `Action_BallSnap` | DT | `14` | `14` | 96 | START | 101 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `1` | `1` | 99 | START | 99 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `10` | 99 | START | 99 | 125 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `11` | 99 | START | 99 | 142 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `5` | 99 | START | 99 | 198 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `2` | 104 | END | 96 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `3` | `3` | 104 | START | 104 | 143 |
| ✅ EXACT | `Action_Handoff` | QB | `2` | `2` | 114 | START | 114 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 126 | START | 126 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | `26` | `22` | 173 | START | 173 | 179 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 198 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 24–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 95 | 72 | inferred_complete_timeline |
| `Action_SnapReceive` | 96 | 104 | 9 | inferred_complete_timeline |
| `Action_None` | 105 | 113 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 114 | 125 | 12 | inferred_complete_timeline |
| `Action_None` | 126 | 269 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 24–166
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 125 | 102 | inferred_complete_timeline |
| `Action_BallCarry` | 126 | 133 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 145 | 166 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 24–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 103 | 80 | inferred_complete_timeline |
| `Action_SplitBlock` | 104 | 143 | 40 | inferred_complete_timeline |
| `Action_SplitBlock` | 156 | 198 | 43 | inferred_complete_timeline |
| `Action_None` | 199 | 269 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 24–269
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 98 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 198 | 100 | inferred_complete_timeline |
| `Action_None` | 199 | 266 | 68 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 24–154
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 98 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 118 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 134 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 154 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 24–269
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 98 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 125 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 150 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 198 | 41 | inferred_complete_timeline |
| `Action_None` | 199 | 209 | 11 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 24–142
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 98 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 142 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 24–260
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 95 | 72 | inferred_complete_timeline |
| `Action_None` | 96 | 199 | 104 | inferred_complete_timeline |
| `Action_None` | 202 | 260 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 24–269
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 95 | 72 | inferred_complete_timeline |
| `Action_None` | 96 | 149 | 54 | inferred_complete_timeline |
| `Action_None` | 151 | 269 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 24–130
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 69 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_None` | 105 | 130 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 24–119
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 95 | 72 | inferred_complete_timeline |
| `Action_None` | 96 | 112 | 17 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 24–147
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 95 | 72 | inferred_complete_timeline |
| `Action_None` | 96 | 147 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 24–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 95 | 72 | inferred_complete_timeline |
| `Action_None` | 96 | 269 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 24–215
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 95 | 72 | inferred_complete_timeline |
| `Action_None` | 96 | 199 | 104 | inferred_complete_timeline |
| `Action_None` | 207 | 209 | 3 | inferred_complete_timeline |
| `Action_None` | 212 | 215 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 24–269 | 242 | 4 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 106–269 | 151 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 120–137 | 13 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 125–269 | 145 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 156–206 | 51 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 161–269 | 107 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 163–175 | 8 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 164–221 | 44 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 165–259 | 90 | 6 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 183–198 | 16 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 224–234 | 7 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 227–269 | 43 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 232–269 | 36 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 246–269 | 24 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `14` (DT): Annotated start 96 != Inferred start 101
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `26` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 414: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 100 frames exceeds threshold 90 frames [start=99, end=198].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 100 frames exceeds threshold 90 frames [start=99, end=198].
- ⚠️ Action 'Action_ZoneBlock' range [99-118] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-134] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [104-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [126-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [145-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-266] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-147] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-144] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-240] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-209] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-260] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-130] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-269] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-128] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-206] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [173-179] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [181-185] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [189-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '22' starts at frame 199, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [199-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-259] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>