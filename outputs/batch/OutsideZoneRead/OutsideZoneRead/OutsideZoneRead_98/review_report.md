# Play-Annotation-Generator Annotation Review — OutsideZoneRead_98

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_98`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | DT | defense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | TE1 | offense | `3` | `2` |
| ✅ EXACT | `Action_Keep` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 0 | START | 0 | 0 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | DT | `17` | `16` | 1 | START | 1 | 5 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `12` | 4 | START | 4 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `1` | 4 | START | 4 | 13 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 4 | START | 4 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `5` | 4 | START | 4 | 18 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 10 | END | 1 | 10 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `10` | `9` | 14 | START | 14 | 27 |
| ✅ EXACT | `Action_BlockSecondLevel` | TE1 | `3` | `2` | 23 | START | 23 | 32 |
| ✅ EXACT | `Action_Keep` | QB | `10` | `9` | 28 | START | 28 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `10` | `9` | 43 | START | 43 | 163 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 60 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 10 | 10 | inferred_complete_timeline |
| `Action_None` | 11 | 13 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 14 | 27 | 14 | inferred_complete_timeline |
| `Action_Keep` | 28 | 42 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 43 | 163 | 121 | inferred_complete_timeline |
| `Action_BallCarry` | 170 | 269 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 35 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 97 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 23 | 32 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 119 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 60 | 57 | inferred_complete_timeline |
| `Action_None` | 61 | 126 | 66 | inferred_complete_timeline |
| `Action_None` | 129 | 131 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–23
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 13 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 23 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 18 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 70 | 10 | inferred_complete_timeline |
| `Action_None` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_None` | 91 | 269 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 39 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 43 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 60 | 8 | inferred_complete_timeline |
| `Action_None` | 61 | 134 | 74 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 5 | 5 | inferred_complete_timeline |
| `Action_None` | 21 | 24 | 4 | inferred_complete_timeline |
| `Action_None` | 32 | 41 | 10 | inferred_complete_timeline |
| `Action_None` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_None` | 48 | 60 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 6 | 6 | inferred_complete_timeline |
| `Action_None` | 15 | 33 | 19 | inferred_complete_timeline |
| `Action_None` | 36 | 48 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 5 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 7 | 10 | 4 | inferred_complete_timeline |
| `Action_None` | 11 | 32 | 22 | inferred_complete_timeline |
| `Action_None` | 35 | 52 | 18 | inferred_complete_timeline |
| `Action_None` | 57 | 249 | 193 | inferred_complete_timeline |
| `Action_None` | 251 | 269 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 48 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 57 | 57 | inferred_complete_timeline |
| `Action_None` | 59 | 72 | 14 | inferred_complete_timeline |
| `Action_None` | 75 | 269 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 12 | 12 | inferred_complete_timeline |
| `Action_None` | 18 | 75 | 58 | inferred_complete_timeline |
| `Action_None` | 79 | 102 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 47 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 116 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 194 | 194 | inferred_complete_timeline |
| `Action_None` | 206 | 269 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–6 | 7 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 8–75 | 28 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 20–142 | 115 | 6 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 21–27 | 7 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 29–269 | 237 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 61–75 | 15 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 68–200 | 128 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 79–269 | 183 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 109–269 | 155 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 116–154 | 28 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 119–269 | 146 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 142–203 | 51 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 143–268 | 126 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 165–269 | 105 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 174–269 | 96 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 189–269 | 77 | 3 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 226–269 | 44 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 234–266 | 6 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 253–255 | 3 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 257–264 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 198: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [1-35] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-97] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-13] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-23] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [23-32] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-116] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-39] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-43] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-18] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-60] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-70] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-48] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-57] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-72] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-119] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [43-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-47] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-12] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-6] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-5] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-24] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [1-5] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-32] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-249] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-6] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-24] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-30] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-41] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-91] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-142] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-37] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-241] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-75] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-87] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-200] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-230] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-266] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-124] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-154] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-185] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-268] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-201] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-264] for track '36' has 1 frames without a visible bounding box.
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