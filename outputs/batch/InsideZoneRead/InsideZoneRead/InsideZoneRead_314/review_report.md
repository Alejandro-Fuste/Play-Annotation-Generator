# Play-Annotation-Generator Annotation Review — InsideZoneRead_314

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_314`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 127
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
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Keep` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `2` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 5 | START | 5 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `0` | 8 | START | 8 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 8 | START | 8 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `2` | 8 | START | 8 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `7` | 8 | START | 8 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `8` | 8 | START | 20 | 75 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 19 | END | 5 | 19 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `5` | 26 | START | 26 | 35 |
| ✅ EXACT | `Action_Keep` | QB | `6` | `5` | 36 | START | 36 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `6` | `5` | 59 | START | 59 | 138 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 96 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 19 | 15 | inferred_complete_timeline |
| `Action_None` | 20 | 25 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 26 | 35 | 10 | inferred_complete_timeline |
| `Action_Keep` | 36 | 58 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 59 | 138 | 80 | inferred_complete_timeline |
| `Action_BallCarry` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 157 | 161 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 51 | 47 | inferred_complete_timeline |
| `Action_None` | 59 | 75 | 17 | inferred_complete_timeline |
| `Action_None` | 77 | 122 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 75 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 144 | 52 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_None` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 75 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 83 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 62 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 5 | 19 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 75 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 86 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 33 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 96 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 40 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 75 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 96 | 14 | inferred_complete_timeline |
| `Action_None` | 97 | 119 | 23 | inferred_complete_timeline |
| `Action_None` | 121 | 146 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_None` | 55 | 75 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 48 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 73 | 23 | inferred_complete_timeline |
| `Action_None` | 79 | 99 | 21 | inferred_complete_timeline |
| `Action_None` | 109 | 160 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 12 | 8 | inferred_complete_timeline |
| `Action_None` | 16 | 28 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_None` | 38 | 55 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 29 | 25 | inferred_complete_timeline |
| `Action_None` | 42 | 44 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 10 | 6 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 27–74 | 29 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 37–65 | 29 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 43–180 | 114 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 46–88 | 43 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 60–109 | 45 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 80–180 | 91 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 98–180 | 83 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 99–109 | 11 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 108–159 | 36 | 4 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 118–162 | 33 | 3 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 128–167 | 23 | 3 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 131–143 | 13 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 132–174 | 35 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 133–153 | 21 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 137–162 | 26 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 144–170 | 18 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 149–180 | 32 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 152–180 | 29 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 153–180 | 28 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 155–174 | 20 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 161–166 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [5–19], lower_priority='Action_ZoneBlock' annotated_start=8, effective_Action_ZoneBlock_start=20.
- ⚠️ Action 'Action_ZoneBlock' range [8-75] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-83] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-75] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-144] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-33] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-96] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-37] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-75] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-51] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [59-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [145-147] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [157-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-48] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-73] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-99] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-40] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-75] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-86] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-29] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-62] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-10] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-12] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-28] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-36] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-46] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-48] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-69] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-180] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-88] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-75] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-109] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-131] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-143] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-143] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-161] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-174] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-153] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-162] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-174] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '33' has 1 frames without a visible bounding box.
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

</details>