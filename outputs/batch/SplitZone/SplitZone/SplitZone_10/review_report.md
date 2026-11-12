# Play-Annotation-Generator Annotation Review — SplitZone_10

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_10`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `13` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 59 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 57 | START | 57 | 66 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `12` | 60 | START | 60 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `14` | 60 | START | 60 | 75 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `16` | 60 | START | 67 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `4` | 60 | START | 60 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `8` | 60 | START | 60 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `13` | `13` | 65 | START | 65 | 70 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 66 | END | 57 | 66 |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | `17` | `17` | 93 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `6` | 106 | START | 106 | 113 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 128 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 11 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 27 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 56 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 66 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 113 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 115 | 204 | 90 | inferred_complete_timeline |
| `Action_BallCarry` | 206 | 251 | 46 | inferred_complete_timeline |
| `Action_BallCarry` | 253 | 287 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 136 | 80 | inferred_complete_timeline |
| `Action_None` | 144 | 299 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_SplitBlock` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_SplitBlock` | 72 | 103 | 32 | inferred_complete_timeline |
| `Action_SplitBlock` | 106 | 128 | 23 | inferred_complete_timeline |
| `Action_None` | 129 | 195 | 67 | inferred_complete_timeline |
| `Action_None` | 198 | 299 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 75 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 99 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 124 | 5 | inferred_complete_timeline |
| `Action_None` | 130 | 299 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 128 | 69 | inferred_complete_timeline |
| `Action_None` | 129 | 132 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 57 | 66 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 128 | 62 | inferred_complete_timeline |
| `Action_None` | 129 | 299 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 81 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 128 | 21 | inferred_complete_timeline |
| `Action_None` | 129 | 149 | 21 | inferred_complete_timeline |
| `Action_None` | 152 | 299 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 128 | 69 | inferred_complete_timeline |
| `Action_None` | 129 | 299 | 171 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 162 | 106 | inferred_complete_timeline |
| `Action_None` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_None` | 170 | 299 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 215 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 140 | 84 | inferred_complete_timeline |
| `Action_None` | 145 | 152 | 8 | inferred_complete_timeline |
| `Action_None` | 160 | 195 | 36 | inferred_complete_timeline |
| `Action_None` | 197 | 218 | 22 | inferred_complete_timeline |
| `Action_None` | 238 | 299 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 120 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 299 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 97 | 41 | inferred_complete_timeline |
| `Action_None` | 99 | 141 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 299 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 235 | 179 | inferred_complete_timeline |
| `Action_None` | 238 | 290 | 53 | inferred_complete_timeline |
| `Action_None` | 295 | 299 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 150 | 94 | inferred_complete_timeline |
| `Action_None` | 152 | 219 | 68 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 76–299 | 196 | 6 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 82–299 | 218 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 113–257 | 145 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 124–292 | 165 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 159–200 | 32 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 176–299 | 123 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 198–217 | 19 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 205–299 | 95 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 232–299 | 55 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 252–299 | 48 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 255–299 | 45 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 255–299 | 32 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 281–293 | 13 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 288–299 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (5 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 60 != Inferred start 67
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `13` (3 segments found)
- ❌ Missing segment for action `Action_Handoff` on target `17` (QB)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [57–66], lower_priority='Action_ZoneBlock' annotated_start=60, effective_Action_ZoneBlock_start=67.
- ⚠️ Segment 'Action_Handoff' for track '17' has invalid range: start=93, end=66. Clamping end to start.
- ⚠️ Action 'Action_None' range [57-97] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-215] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-136] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-81] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [115-204] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [206-251] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [253-287] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-162] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-152] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-195] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-218] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [65-70] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [72-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-99] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-235] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-290] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [57-66] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-170] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-255] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-292] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-168] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-190] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-211] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-282] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-294] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-293] for track '30' has 1 frames without a visible bounding box.
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

</details>