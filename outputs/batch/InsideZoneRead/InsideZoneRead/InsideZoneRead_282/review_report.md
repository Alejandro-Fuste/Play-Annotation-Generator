# Play-Annotation-Generator Annotation Review — InsideZoneRead_282

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_282`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 3 | START | 3 | 17 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 6 | START | 6 | 49 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 6 | START | 6 | 26 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `18` | `17` | 6 | START | 18 | 39 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `8` | 6 | START | 6 | 84 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 17 | END | 3 | 17 |
| ✅ EXACT | `Action_ReadDefender` | QB | `10` | `9` | 22 | START | 22 | 31 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `8` | `7` | 24 | START | 24 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `10` | `9` | 32 | START | 32 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `10` | `9` | 55 | START | 55 | 60 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 84 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_None` | 18 | 21 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 22 | 31 | 10 | inferred_complete_timeline |
| `Action_Keep` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_Keep` | 50 | 54 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 55 | 60 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 66 | 210 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 50 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 110 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 90 | 88 | inferred_complete_timeline |
| `Action_None` | 116 | 210 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 26 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–49
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 49 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 39 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 84 | 79 | inferred_complete_timeline |
| `Action_None` | 85 | 210 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 148 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 53 | 51 | inferred_complete_timeline |
| `Action_None` | 62 | 76 | 15 | inferred_complete_timeline |
| `Action_None` | 79 | 84 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 108 | 106 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 210 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 199 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 102 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 84 | 82 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 122 | 124 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 84 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–118 | 118 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 2–85 | 82 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 29–159 | 115 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 36–106 | 71 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 41–210 | 164 | 6 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 55–210 | 156 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 55–198 | 102 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 63–142 | 80 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 89–169 | 81 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 115–210 | 96 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 115–210 | 96 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 133–208 | 58 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 139–144 | 4 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 141–152 | 8 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 180–210 | 31 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 181–209 | 17 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 192–195 | 4 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 194–197 | 4 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 198–210 | 12 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (C): Annotated start 6 != Inferred start 18
- ⚠️ Ambiguous match for action `Action_Keep` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 564: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [3–17], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=18.
- ⚠️ Action 'Action_None' range [3-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-84] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-84] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-110] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-102] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 85, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [85-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [32-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [55-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [66-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-49] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-50] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-53] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-76] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-39] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-53] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-48] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-159] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-46] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-190] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-142] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-169] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-197] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-192] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>