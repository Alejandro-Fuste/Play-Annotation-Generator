# Play-Annotation-Generator Annotation Review — SplitZone_252

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_252`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 124
- **Validation Warnings:** 158
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `8` | `8` |
| ⚠️ START CHANGED | `Action_Handoff` | C | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | C | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `5` | `5` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 89 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `12` | `11` | 90 | START | 103 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `4` | 93 | START | 93 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 93 | START | 93 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `7` | 93 | START | 93 | 130 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `8` | `8` | 93 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_Handoff` | C | `8` | `8` | 100 | START | 105 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | C | `8` | `8` | 104 | END | 94 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `5` | `5` | 114 | START | 114 | 133 |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `21` | `17` | 130 | START | 150 | 152 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 235 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–2
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 139 | 50 | inferred_complete_timeline |
| `Action_None` | 141 | 151 | 11 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 188 | 19 | inferred_complete_timeline |
| `Action_None` | 190 | 193 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 71 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 92 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 113 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 114 | 133 | 20 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 150 | 159 | 10 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 162 | 163 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 105 | 129 | 25 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 121 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 214 | 217 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 130 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 157 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 169 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 211 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 224 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 14 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 18 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 26 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 102 | 13 | inferred_complete_timeline |
| `Action_None` | 104 | 108 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 174 | 85 | inferred_complete_timeline |
| `Action_None` | 177 | 209 | 33 | inferred_complete_timeline |
| `Action_None` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 109 | 20 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 141 | 52 | inferred_complete_timeline |
| `Action_None` | 144 | 151 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 156 | 67 | inferred_complete_timeline |
| `Action_None` | 161 | 186 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 4–217 | 128 | 13 | Undefined position; Undefined team |
| `12` | `15` | Position_Unknown | Team_Unknown | 27–192 | 73 | 8 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 46–51 | 6 | 1 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 92–217 | 79 | 9 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 95–98 | 4 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 102–129 | 23 | 4 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 105–152 | 19 | 4 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 109–256 | 113 | 4 | Undefined position; Undefined team |
| `19` | `29` | Position_Unknown | Team_Unknown | 147–170 | 5 | 2 | Undefined position; Undefined team |
| `20` | `35` | Position_Unknown | Team_Unknown | 159–167 | 7 | 3 | Undefined position; Undefined team |
| `21` | `36` | Position_Unknown | Team_Unknown | 161–210 | 45 | 2 | Undefined position; Undefined team |
| `22` | `37` | Position_Unknown | Team_Unknown | 162–202 | 41 | 1 | Undefined position; Undefined team |
| `23` | `38` | Position_Unknown | Team_Unknown | 162–178 | 11 | 3 | Undefined position; Undefined team |
| `24` | `40` | Position_Unknown | Team_Unknown | 175–206 | 31 | 2 | Undefined position; Undefined team |
| `25` | `43` | Position_Unknown | Team_Unknown | 185–186 | 2 | 1 | Undefined position; Undefined team |
| `26` | `44` | Position_Unknown | Team_Unknown | 191–293 | 94 | 5 | Undefined position; Undefined team |
| `27` | `46` | Position_Unknown | Team_Unknown | 204–208 | 5 | 1 | Undefined position; Undefined team |
| `28` | `47` | Position_Unknown | Team_Unknown | 206–296 | 88 | 3 | Undefined position; Undefined team |
| `29` | `52` | Position_Unknown | Team_Unknown | 223–295 | 57 | 2 | Undefined position; Undefined team |
| `30` | `53` | Position_Unknown | Team_Unknown | 223–227 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `12` (Position_Unknown): Annotated start 90 != Inferred start 103
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (6 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `8` (C)
- ⚠️ `Action_Handoff` for actor_track_id `8` (C): Annotated start 100 != Inferred start 105
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `5` (4 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `21` (Position_Unknown): Annotated start 130 != Inferred start 150

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 114 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 506: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 125 frames exceeds threshold 90 frames [start=93, end=217].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 132 frames exceeds threshold 90 frames [start=93, end=224].
- ⚠️ Action 'Action_None' range [90-156] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-186] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-141] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-151] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-174] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-209] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-299] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-144] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [201-204] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [206-207] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [214-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-71] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-92] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [114-133] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [137-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [150-159] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [162-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-18] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-26] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-130] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-157] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [165-169] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [178-211] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [216-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [94-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [105-129] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-139] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-19] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-33] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-71] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-211] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-36] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 90, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [90-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-181] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-51] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-153] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-190] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-113] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-119] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-123] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-173] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-184] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-186] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-206] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-293] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-225] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-296] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-262] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>