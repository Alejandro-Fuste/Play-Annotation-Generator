# Play-Annotation-Generator Annotation Review — SplitZone_212

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_212`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 101 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `17` | `17` | 99 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | `14` | `14` | 101 | START | 101 | 107 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `1` | `1` | 102 | START | 102 | 148 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `10` | `10` | 102 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `3` | 102 | START | 102 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `5` | 102 | START | 102 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `8` | 102 | START | 102 | 135 |
| ✅ EXACT | `Action_SnapReceive` | C | `10` | `10` | 113 | END | 99 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | `13` | `13` | 121 | START | 121 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | `10` | `10` | 134 | START | 134 | 141 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 168 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 145 | 47 | inferred_complete_timeline |
| `Action_None` | 147 | 205 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 269 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–14
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 14 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 125 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 168 | 40 | inferred_complete_timeline |
| `Action_None` | 169 | 269 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 155 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 168 | 5 | inferred_complete_timeline |
| `Action_None` | 169 | 269 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_SnapReceive` | 99 | 113 | 15 | inferred_complete_timeline |
| `Action_None` | 114 | 129 | 16 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 134 | 141 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 174 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 184 | 269 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 148 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 135 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 162 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 151 | 53 | inferred_complete_timeline |
| `Action_None` | 153 | 269 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 171 | 73 | inferred_complete_timeline |
| `Action_None` | 174 | 180 | 7 | inferred_complete_timeline |
| `Action_None` | 215 | 217 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 137 | 39 | inferred_complete_timeline |
| `Action_None` | 141 | 173 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 204 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 269 | 171 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–269 | 268 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–269 | 258 | 4 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–150 | 145 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–180 | 110 | 6 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 12–42 | 20 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 90–269 | 154 | 5 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 100–269 | 142 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 108–167 | 60 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 143–202 | 60 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 160–269 | 110 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 165–167 | 3 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 175–269 | 95 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 177–184 | 8 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 191–245 | 52 | 3 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 192–269 | 78 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 194–207 | 12 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 201–269 | 69 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 204–269 | 66 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 223–240 | 18 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 243–252 | 10 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 260–269 | 10 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 269–269 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `17` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `14` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `10` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '10' has invalid range: start=102, end=98. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=99, end=7. Clamping end to start.
- ⚠️ Action 'Action_None' range [99-171] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-151] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-155] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-145] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-205] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-125] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-135] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [134-141] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-137] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [121-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [101-107] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-269] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-129] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-63] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-18] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-33] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-42] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-236] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-184] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-222] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-245] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-200] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-240] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-252] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>