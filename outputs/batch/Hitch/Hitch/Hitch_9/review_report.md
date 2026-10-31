# Play-Annotation-Generator Annotation Review — Hitch_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_9`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `0` | `0` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_RunHitchRoute` | WR | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `0` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `9` | `Group` | 0 | START | 0 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `16` | `16` | 25 | START | 25 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `0` | `0` | 28 | START | 28 | 125 |
| ✅ EXACT | `Action_PassBlock` | LG | `1` | `1` | 28 | START | 28 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `13` | 28 | START | 28 | 110 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `16` | `16` | 28 | START | 39 | 67 |
| ✅ EXACT | `Action_PassBlock` | LT | `6` | `6` | 28 | START | 28 | 37 |
| ✅ EXACT | `Action_RunHitchRoute` | WR | `9` | `9` | 35 | START | 35 | 135 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 38 | END | 25 | 38 |
| ✅ EXACT | `Action_ThrowPass` | QB | `10` | `10` | 104 | START | 104 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `9` | `9` | 136 | START | 136 | 136 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 38 | 14 | inferred_complete_timeline |
| `Action_None` | 39 | 69 | 31 | inferred_complete_timeline |
| `Action_None` | 72 | 100 | 29 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_ThrowPass` | 104 | 113 | 10 | inferred_complete_timeline |
| `Action_None` | 114 | 119 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 44 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 35 | 135 | 101 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 136 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 138 | 149 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 129 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 37 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 138 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 24 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 25 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 33 | 38 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 67 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 125 | 98 | inferred_complete_timeline |
| `Action_PassBlock` | 136 | 145 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 110 | 83 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 151 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 148 | 124 | inferred_complete_timeline |
| `Action_None` | 156 | 190 | 35 | inferred_complete_timeline |
| `Action_None` | 194 | 203 | 10 | inferred_complete_timeline |
| `Action_None` | 205 | 269 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 37 | 13 | inferred_complete_timeline |
| `Action_None` | 41 | 57 | 17 | inferred_complete_timeline |
| `Action_None` | 63 | 70 | 8 | inferred_complete_timeline |
| `Action_None` | 80 | 91 | 12 | inferred_complete_timeline |
| `Action_None` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_None` | 107 | 119 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 87 | 63 | inferred_complete_timeline |
| `Action_None` | 94 | 140 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 194 | 170 | inferred_complete_timeline |
| `Action_None` | 196 | 269 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 26 | 103 | 78 | inferred_complete_timeline |
| `Action_None` | 107 | 137 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 125 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 69 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–14
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 14 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 46–152 | 107 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 89–215 | 116 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 91–134 | 42 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 121–232 | 105 | 3 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 127–269 | 138 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 127–164 | 38 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 149–269 | 112 | 3 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 152–269 | 118 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 160–269 | 110 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 220–264 | 44 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 221–238 | 18 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 233–269 | 37 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `16` (C): Annotated start 28 != Inferred start 39
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [25–38], lower_priority='Action_PassBlock' annotated_start=28, effective_Action_PassBlock_start=39.
- ⚠️ Action 'Action_PassBlock' range [28-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [136-145] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-138] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-37] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-57] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-91] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-103] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-69] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-37] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-148] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' range [35-135] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '9' starts at frame 136, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [136-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [138-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-119] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-129] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' for track '16' starts at frame 25, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallSnap' range [25-25] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-152] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-178] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-120] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-189] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-222] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-269] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-204] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-242] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-229] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-264] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-269] for track '29' has 1 frames without a visible bounding box.
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

</details>