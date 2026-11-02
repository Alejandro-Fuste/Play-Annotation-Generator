# Play-Annotation-Generator Annotation Review — JetSweep_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_73`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 15 | START | 15 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 15 | START | 15 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 15 | START | 15 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 15 | START | 15 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 15 | START | 15 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 15 | START | 15 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 15 | START | 15 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 15 | START | 15 | 46 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `16` | `15` | 45 | START | 45 | 77 |
| ✅ EXACT | `Action_BallSnap` | LG | `13` | `12` | 46 | START | 46 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 47 | START | 47 | 149 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `13` | `12` | 47 | START | 47 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `3` | `2` | 47 | START | 47 | 153 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `3` | 47 | START | 47 | 116 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `7` | 47 | START | 47 | 153 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 57 | END | 46 | 57 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 63 | START | 63 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `16` | `15` | 78 | START | 78 | 157 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `13` | `12` | 85 | START | 85 | 153 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 153 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 15–159
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 57 | 12 | inferred_complete_timeline |
| `Action_None` | 58 | 62 | 5 | inferred_complete_timeline |
| `Action_Toss` | 63 | 77 | 15 | inferred_complete_timeline |
| `Action_None` | 78 | 159 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 15–350
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_None` | 46 | 350 | 305 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 15–411
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_None` | 46 | 197 | 152 | inferred_complete_timeline |
| `Action_None` | 201 | 312 | 112 | inferred_complete_timeline |
| `Action_None` | 314 | 320 | 7 | inferred_complete_timeline |
| `Action_None` | 325 | 411 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 15–336
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 46 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 153 | 107 | inferred_complete_timeline |
| `Action_None` | 155 | 336 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 46 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 84 | 38 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 85 | 153 | 69 | inferred_complete_timeline |
| `Action_None` | 154 | 176 | 23 | inferred_complete_timeline |
| `Action_None` | 178 | 202 | 25 | inferred_complete_timeline |
| `Action_None` | 205 | 403 | 199 | inferred_complete_timeline |
| `Action_None` | 409 | 419 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 46 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 149 | 103 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 161 | 8 | inferred_complete_timeline |
| `Action_None` | 164 | 216 | 53 | inferred_complete_timeline |
| `Action_None` | 221 | 229 | 9 | inferred_complete_timeline |
| `Action_None` | 235 | 419 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 15–116
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 46 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 116 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 15–385
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 46 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 153 | 107 | inferred_complete_timeline |
| `Action_None` | 154 | 385 | 232 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 15–149
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_None` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_None` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_None` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_None` | 96 | 104 | 9 | inferred_complete_timeline |
| `Action_None` | 112 | 116 | 5 | inferred_complete_timeline |
| `Action_None` | 121 | 149 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 15–354
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_None` | 46 | 164 | 119 | inferred_complete_timeline |
| `Action_None` | 167 | 354 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 15–53
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_None` | 46 | 53 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 15–164
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_None` | 46 | 75 | 30 | inferred_complete_timeline |
| `Action_None` | 79 | 123 | 45 | inferred_complete_timeline |
| `Action_None` | 125 | 127 | 3 | inferred_complete_timeline |
| `Action_None` | 129 | 164 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 15–350
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_None` | 46 | 350 | 305 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 15–385
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_None` | 46 | 144 | 99 | inferred_complete_timeline |
| `Action_None` | 146 | 385 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 15–149
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_None` | 46 | 149 | 104 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 45–419 | 374 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 49–364 | 309 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 58–401 | 332 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 97–388 | 275 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 105–347 | 243 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 107–411 | 302 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 124–186 | 63 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 150–151 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 155–157 | 3 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 157–358 | 202 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 160–165 | 5 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 171–419 | 249 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 176–178 | 3 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 184–360 | 177 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 187–419 | 230 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 219–395 | 177 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 222–225 | 4 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 223–408 | 179 | 4 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 275–419 | 145 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 389–395 | 7 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 411–415 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 107 frames exceeds threshold 90 frames [start=47, end=153].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 107 frames exceeds threshold 90 frames [start=47, end=153].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (C) duration 107 frames exceeds threshold 90 frames [start=47, end=153].
- ⚠️ Action 'Action_None' range [46-144] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-385] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-312] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-320] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-411] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-385] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-116] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-350] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-350] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-336] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-56] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-93] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-149] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-216] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-123] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-202] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-403] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-354] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [78-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-223] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-364] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-401] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-388] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-347] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-200] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-411] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-358] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-360] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-395] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-256] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-345] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-408] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-395] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-415] for track '36' has 1 frames without a visible bounding box.
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