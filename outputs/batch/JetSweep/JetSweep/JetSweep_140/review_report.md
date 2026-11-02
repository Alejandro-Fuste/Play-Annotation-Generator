# Play-Annotation-Generator Annotation Review — JetSweep_140

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_140`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 9
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `21` | `19` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `8` | `7` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `14` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 58 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `21` | `19` | 50 | START | 50 | 88 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 58 | START | 58 | 70 |
| ✅ EXACT | `Action_LeadBlock` | RB | `8` | `7` | 59 | START | 59 | 137 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `12` | 59 | START | 71 | 100 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 59 | START | 59 | 137 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `4` | 59 | START | 59 | 137 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `6` | 59 | START | 59 | 137 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 70 | END | 58 | 70 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 72 | START | 72 | 88 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `21` | `19` | 89 | START | 89 | 206 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 137 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 70 | 13 | inferred_complete_timeline |
| `Action_None` | 71 | 71 | 1 | inferred_complete_timeline |
| `Action_Toss` | 72 | 88 | 17 | inferred_complete_timeline |
| `Action_None` | 89 | 174 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_LeadBlock` | 59 | 137 | 79 | inferred_complete_timeline |
| `Action_None` | 138 | 204 | 67 | inferred_complete_timeline |
| `Action_None` | 206 | 292 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 101 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 65 | 8 | inferred_complete_timeline |
| `Action_None` | 69 | 156 | 88 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 228 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 137 | 79 | inferred_complete_timeline |
| `Action_None` | 138 | 250 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_BallSnap` | 58 | 70 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 100 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 137 | 79 | inferred_complete_timeline |
| `Action_None` | 138 | 165 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 137 | 79 | inferred_complete_timeline |
| `Action_None` | 138 | 162 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 2–6
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 6 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 71 | 14 | inferred_complete_timeline |
| `Action_None` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_None` | 97 | 108 | 12 | inferred_complete_timeline |
| `Action_None` | 112 | 124 | 13 | inferred_complete_timeline |
| `Action_None` | 132 | 149 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 74 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 7–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 57 | 51 | inferred_complete_timeline |
| `Action_None` | 58 | 210 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 100 | 43 | inferred_complete_timeline |
| `Action_None` | 124 | 148 | 25 | inferred_complete_timeline |
| `Action_None` | 150 | 152 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 68 | 11 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_None` | 75 | 124 | 50 | inferred_complete_timeline |
| `Action_None` | 126 | 329 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 129 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 165 | 108 | inferred_complete_timeline |
| `Action_None` | 170 | 217 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 207 | 150 | inferred_complete_timeline |
| `Action_None` | 226 | 229 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 42 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–329 | 280 | 7 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 50–206 | 157 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 58–197 | 139 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 85–317 | 228 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 94–329 | 234 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 139–170 | 21 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 141–329 | 185 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 141–159 | 19 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 148–160 | 13 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 167–329 | 154 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 192–329 | 133 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 208–329 | 120 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 211–329 | 119 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 215–329 | 115 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 254–329 | 70 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 264–329 | 66 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 271–329 | 56 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 273–329 | 56 | 2 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 274–309 | 36 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 277–329 | 45 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 280–287 | 7 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 304–310 | 7 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 321–329 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 59 != Inferred start 71

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 282: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [58–70], lower_priority='Action_ZoneBlock' annotated_start=59, effective_Action_ZoneBlock_start=71.
- ⚠️ Action 'Action_None' range [58-68] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-124] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-165] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-217] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-101] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-129] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-162] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-204] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-292] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-255] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-272] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-309] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-148] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-42] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-156] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-228] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-250] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-6] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [50-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [89-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-112] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-310] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-224] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-159] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-160] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-261] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-329] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-286] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-309] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-302] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-310] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-329] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>