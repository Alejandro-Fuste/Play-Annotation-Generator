# Play-Annotation-Generator Annotation Review — OutsideZoneRead_100

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_100`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_Keep` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 13 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `16` | `14` | 11 | START | 25 | 25 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `0` | 14 | START | 14 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 14 | START | 14 | 32 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 14 | START | 14 | 42 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 21 | END | 11 | 21 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `10` | `9` | 31 | START | 31 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | `5` | `4` | 43 | START | 43 | 47 |
| ✅ EXACT | `Action_Keep` | QB | `10` | `9` | 46 | START | 46 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `10` | `9` | 58 | START | 58 | 117 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 88 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–174
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 21 | 11 | inferred_complete_timeline |
| `Action_None` | 22 | 28 | 7 | inferred_complete_timeline |
| `Action_None` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_Keep` | 46 | 57 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 58 | 117 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 147 | 168 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 174 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 78 | 68 | inferred_complete_timeline |
| `Action_None` | 83 | 180 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 104 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 84 | 71 | inferred_complete_timeline |
| `Action_None` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 116 | 121 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 32 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 42 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 49 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 88 | 35 | inferred_complete_timeline |
| `Action_None` | 89 | 94 | 6 | inferred_complete_timeline |
| `Action_None` | 97 | 158 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 42 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 43 | 47 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 52 | 88 | 37 | inferred_complete_timeline |
| `Action_None` | 89 | 132 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 17 | 7 | inferred_complete_timeline |
| `Action_None` | 21 | 80 | 60 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 40 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 26 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 46 | 36 | inferred_complete_timeline |
| `Action_None` | 48 | 62 | 15 | inferred_complete_timeline |
| `Action_None` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_None` | 86 | 133 | 48 | inferred_complete_timeline |
| `Action_None` | 168 | 180 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 76 | 66 | inferred_complete_timeline |
| `Action_None` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–169 | 164 | 3 | Undefined position; Undefined team |
| `12` | `14` | Position_Unknown | Team_Unknown | 11–110 | 94 | 2 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 23–158 | 128 | 4 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 25–87 | 57 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 34–180 | 41 | 4 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 50–53 | 4 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 55–144 | 86 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 70–77 | 8 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 79–86 | 8 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 80–180 | 44 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 83–180 | 95 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 108–111 | 4 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 108–180 | 64 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 122–180 | 59 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 126–142 | 17 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 136–168 | 30 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 139–157 | 18 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 150–180 | 31 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 161–180 | 20 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 163–170 | 8 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 170–180 | 11 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 177–180 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `16` (Position_Unknown): Annotated start 11 != Inferred start 25
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '14' has invalid range: start=25, end=21. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [14-84] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-104] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-78] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-180] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [14-32] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-42] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-49] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-94] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [43-47] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-46] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-133] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-36] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-26] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-40] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-28] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [58-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [147-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-17] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-44] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-148] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-30] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-157] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-144] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-86] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-114] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-155] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-157] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>