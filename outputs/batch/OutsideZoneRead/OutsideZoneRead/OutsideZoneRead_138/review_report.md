# Play-Annotation-Generator Annotation Review — OutsideZoneRead_138

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_138`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Keep` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 6 | START | 6 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `9` | 8 | START | 8 | 105 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `11` | `10` | 8 | START | 8 | 105 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 8 | START | 8 | 105 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `5` | `4` | 8 | START | 25 | 64 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `6` | 8 | START | 8 | 105 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 24 | END | 6 | 24 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `9` | `8` | 27 | START | 27 | 32 |
| ✅ EXACT | `Action_Keep` | QB | `9` | `8` | 33 | START | 33 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `9` | `8` | 52 | START | 52 | 128 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `5` | `4` | 65 | START | 65 | 105 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 105 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 6 | 24 | 19 | inferred_complete_timeline |
| `Action_None` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 27 | 32 | 6 | inferred_complete_timeline |
| `Action_Keep` | 33 | 51 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 52 | 128 | 77 | inferred_complete_timeline |
| `Action_BallCarry` | 131 | 201 | 71 | inferred_complete_timeline |
| `Action_BallCarry` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 105 | 98 | inferred_complete_timeline |
| `Action_None` | 106 | 121 | 16 | inferred_complete_timeline |
| `Action_None` | 125 | 210 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 105 | 98 | inferred_complete_timeline |
| `Action_None` | 106 | 123 | 18 | inferred_complete_timeline |
| `Action_None` | 125 | 210 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 6 | 24 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 64 | 40 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 65 | 105 | 41 | inferred_complete_timeline |
| `Action_None` | 106 | 210 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 105 | 98 | inferred_complete_timeline |
| `Action_None` | 106 | 210 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 105 | 98 | inferred_complete_timeline |
| `Action_None` | 106 | 190 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 112 | 107 | inferred_complete_timeline |
| `Action_None` | 120 | 210 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 27 | 22 | inferred_complete_timeline |
| `Action_None` | 30 | 36 | 7 | inferred_complete_timeline |
| `Action_None` | 40 | 53 | 14 | inferred_complete_timeline |
| `Action_None` | 111 | 156 | 46 | inferred_complete_timeline |
| `Action_None` | 158 | 210 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 35 | 30 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 115 | 110 | inferred_complete_timeline |
| `Action_None` | 121 | 210 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 205 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | Position_Unknown | Team_Unknown | 53–86 | 25 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 60–92 | 33 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 66–210 | 145 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 83–210 | 122 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 89–91 | 3 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 95–130 | 36 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 123–184 | 20 | 6 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 141–210 | 48 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 143–208 | 52 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 162–210 | 49 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 174–210 | 37 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 188–210 | 23 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 203–209 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `5` (C): Annotated start 8 != Inferred start 25
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RT) duration 98 frames exceeds threshold 90 frames [start=8, end=105].
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [6–24], lower_priority='Action_ZoneBlock' annotated_start=8, effective_Action_ZoneBlock_start=25.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 98 frames exceeds threshold 90 frames [start=8, end=105].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 98 frames exceeds threshold 90 frames [start=8, end=105].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 98 frames exceeds threshold 90 frames [start=8, end=105].
- ⚠️ Action 'Action_None' range [6-210] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-205] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [52-128] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [131-201] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-36] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-53] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-35] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-86] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-130] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-128] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-170] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-183] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-182] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '26' has 3 frames without a visible bounding box.
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

</details>