# Play-Annotation-Generator Annotation Review — SplitZone_108

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_108`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 61
- **Validation Warnings:** 56
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `14` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 3 | START | 4 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 3 | START | 4 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 3 | START | 4 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 3 | START | 4 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 3 | START | 4 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 3 | START | 4 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 3 | START | 4 | 103 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 77 | START | 77 | 87 |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | `14` | `14` | 77 | START | 77 | 197 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `11` | `11` | 81 | START | 88 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 81 | START | 81 | 172 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 81 | START | 81 | 159 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `4` | 81 | START | 81 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `5` | `5` | 81 | START | 81 | 147 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 87 | END | 77 | 87 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 93 | START | 93 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `8` | 104 | START | 104 | 243 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 197 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 76 | 73 | inferred_complete_timeline |
| `Action_SnapReceive` | 77 | 87 | 11 | inferred_complete_timeline |
| `Action_None` | 88 | 92 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 93 | 103 | 11 | inferred_complete_timeline |
| `Action_None` | 104 | 269 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 103 | 100 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 243 | 140 | inferred_complete_timeline |
| `Action_BallCarry` | 245 | 269 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–159
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 80 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 159 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 4–170
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 80 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 170 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 4–218
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 76 | 73 | inferred_complete_timeline |
| `Action_BallSnap` | 77 | 87 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 197 | 110 | inferred_complete_timeline |
| `Action_None` | 198 | 218 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 80 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 147 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 197 | 46 | inferred_complete_timeline |
| `Action_None` | 198 | 269 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 80 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 172 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 197 | 24 | inferred_complete_timeline |
| `Action_None` | 198 | 269 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 4–220
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 76 | 73 | inferred_complete_timeline |
| `Action_None` | 77 | 220 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 4–222
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 76 | 73 | inferred_complete_timeline |
| `Action_None` | 77 | 166 | 90 | inferred_complete_timeline |
| `Action_None` | 174 | 222 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 76 | 73 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 4–254
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 76 | 73 | inferred_complete_timeline |
| `Action_None` | 77 | 248 | 172 | inferred_complete_timeline |
| `Action_None` | 252 | 254 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 76 | 73 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–97
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 76 | 73 | inferred_complete_timeline |
| `Action_None` | 77 | 97 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–183
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 76 | 73 | inferred_complete_timeline |
| `Action_None` | 77 | 183 | 107 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 23–269 | 246 | 4 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 89–147 | 59 | 1 | Undefined position; Undefined team |
| `16` | `22` | Position_Unknown | Team_Unknown | 191–269 | 79 | 1 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 197–269 | 69 | 3 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 211–269 | 58 | 2 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 216–269 | 54 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 225–264 | 33 | 3 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 228–269 | 42 | 1 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 244–245 | 2 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 246–269 | 24 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 258–269 | 12 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `11` (C): Annotated start 81 != Inferred start 88
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 25 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 117 frames exceeds threshold 90 frames [start=81, end=197].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RG) duration 117 frames exceeds threshold 90 frames [start=81, end=197].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 117 frames exceeds threshold 90 frames [start=81, end=197].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [77–87], lower_priority='Action_ZoneBlock' annotated_start=81, effective_Action_ZoneBlock_start=88.
- ⚠️ Action 'Action_None' range [77-248] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-172] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-170] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-147] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-166] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-222] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-243] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-220] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-183] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-215] for track '17' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-246] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-240] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-259] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '22' has 1 frames without a visible bounding box.
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

</details>