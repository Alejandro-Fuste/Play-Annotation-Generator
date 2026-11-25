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
- **Action Segments:** 89
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 4
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
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
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `18` | `17` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | C | offense | `18` | `17` |
| ❌ MISSING SEGMENT | `Action_Keep` | C | offense | `18` | `17` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | C | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `19` | `18` | 16 | START | 16 | 33 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 19 | START | 19 | 49 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 19 | START | 19 | 26 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `18` | `17` | 19 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `8` | 19 | START | 19 | 100 |
| ✅ EXACT | `Action_SnapReceive` | C | `18` | `17` | 33 | END | 16 | 33 |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | C | `18` | `17` | 40 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Keep` | C | `18` | `17` | 49 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | C | `18` | `17` | 65 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 100 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 48 | 33 | inferred_complete_timeline |
| `Action_None` | 50 | 60 | 11 | inferred_complete_timeline |
| `Action_None` | 66 | 210 | 145 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 50 | 35 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 110 | 95 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 90 | 75 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 26 | 8 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 49 | 31 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 33 | 18 | inferred_complete_timeline |
| `Action_None` | 34 | 39 | 6 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 100 | 82 | inferred_complete_timeline |
| `Action_None` | 101 | 210 | 110 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 148 | 133 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 53 | 38 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 108 | 93 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 199 | 184 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 102 | 87 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 84 | 69 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 84 | 69 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–118 | 118 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 2–85 | 82 | 4 | Undefined position; Undefined team |
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

- ❌ Missing segment for action `Action_ZoneBlock` on target `18` (C)
- ❌ Missing segment for action `Action_ReadDefender` on target `18` (C)
- ❌ Missing segment for action `Action_Keep` on target `18` (C)
- ❌ Missing segment for action `Action_BallCarry` on target `18` (C)

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
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 5 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 564: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '17' has invalid range: start=19, end=15. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '17' has invalid range: start=40, end=39. Clamping end to start.
- ⚠️ Segment 'Action_Keep' for track '17' has invalid range: start=49, end=39. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '17' has invalid range: start=65, end=39. Clamping end to start.
- ⚠️ Action 'Action_None' range [16-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-84] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-84] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-110] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-102] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-49] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-50] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-53] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-76] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [16-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-39] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [16-33] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-53] for track '18' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_282'; source metadata written as null.

</details>