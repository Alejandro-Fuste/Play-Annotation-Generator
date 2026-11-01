# Play-Annotation-Generator Annotation Review — InsideZoneRead_68

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_68`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 38 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 36 | START | 36 | 47 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `9` | 39 | START | 87 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `2` | 39 | START | 39 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 39 | START | 39 | 57 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `6` | 39 | START | 39 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 39 | START | 39 | 92 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 49 | END | 36 | 49 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `7` | 52 | START | 52 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `7` | `6` | 68 | START | 68 | 78 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 69 | START | 69 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 82 | START | 84 | 86 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 119 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 36 | 49 | 14 | inferred_complete_timeline |
| `Action_None` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 52 | 68 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 69 | 75 | 7 | inferred_complete_timeline |
| `Action_None` | 82 | 126 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_BallCarry` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 98 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 130 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 66 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 94 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 119 | 18 | inferred_complete_timeline |
| `Action_None` | 120 | 133 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 67 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 68 | 78 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 85 | 92 | 8 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 102 | 119 | 18 | inferred_complete_timeline |
| `Action_None` | 120 | 178 | 59 | inferred_complete_timeline |
| `Action_None` | 183 | 269 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_BallSnap` | 36 | 47 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 119 | 33 | inferred_complete_timeline |
| `Action_None` | 120 | 137 | 18 | inferred_complete_timeline |
| `Action_None` | 140 | 184 | 45 | inferred_complete_timeline |
| `Action_None` | 186 | 269 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 92 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 105 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 119 | 12 | inferred_complete_timeline |
| `Action_None` | 120 | 147 | 28 | inferred_complete_timeline |
| `Action_None` | 149 | 158 | 10 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 57 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 68 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 248 | 128 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 77 | 42 | inferred_complete_timeline |
| `Action_None` | 80 | 85 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 61 | 26 | inferred_complete_timeline |
| `Action_None` | 69 | 108 | 40 | inferred_complete_timeline |
| `Action_None` | 112 | 228 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 90 | 55 | inferred_complete_timeline |
| `Action_None` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_None` | 157 | 183 | 27 | inferred_complete_timeline |
| `Action_None` | 186 | 269 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 209 | 174 | inferred_complete_timeline |
| `Action_None` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_None` | 222 | 269 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 110 | 75 | inferred_complete_timeline |
| `Action_None` | 114 | 191 | 78 | inferred_complete_timeline |
| `Action_None` | 194 | 237 | 44 | inferred_complete_timeline |
| `Action_None` | 240 | 251 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `14` | Position_Unknown | Team_Unknown | 98–99 | 2 | 1 | Undefined position; Undefined team |
| `13` | `17` | Position_Unknown | Team_Unknown | 110–269 | 147 | 3 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 115–120 | 6 | 1 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 117–269 | 153 | 1 | Undefined position; Undefined team |
| `16` | `22` | Position_Unknown | Team_Unknown | 120–246 | 126 | 2 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 123–269 | 142 | 3 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 126–269 | 142 | 3 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 135–269 | 111 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 141–269 | 86 | 4 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 144–185 | 32 | 4 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 148–269 | 115 | 3 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 161–216 | 56 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 172–269 | 93 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 186–190 | 5 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 195–269 | 74 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 200–206 | 7 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 200–269 | 61 | 4 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 203–209 | 7 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 204–207 | 4 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 215–217 | 3 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 224–269 | 32 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 39 != Inferred start 87
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [36–49], lower_priority='Action_ZoneBlock' annotated_start=39, effective_Action_ZoneBlock_start=50.
- ⚠️ Action 'Action_None' range [36-77] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-191] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-237] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-251] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-66] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-94] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-209] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-219] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-57] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-68] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-119] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-248] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-86] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-130] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [68-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [85-92] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [98-99] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-269] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [69-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-92] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-105] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-119] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [36-47] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-184] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-90] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-183] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-108] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-152] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-246] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-269] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-178] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-212] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-242] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-178] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-225] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-216] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-222] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-252] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '34' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>