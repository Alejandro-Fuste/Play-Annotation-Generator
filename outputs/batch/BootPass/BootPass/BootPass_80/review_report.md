# Play-Annotation-Generator Annotation Review — BootPass_80

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_80`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_SecureCatch` | TE2 | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 14 | START | 14 | 33 |
| ✅ EXACT | `Action_RunBlock` | LG | `10` | `10` | 24 | START | 24 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `11` | `11` | 24 | START | 34 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `13` | `13` | 24 | START | 24 | 121 |
| ✅ EXACT | `Action_RunBlock` | RT | `7` | `7` | 24 | START | 24 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `9` | `9` | 24 | START | 24 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 33 | END | 14 | 33 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `8` | `8` | 39 | START | 39 | 66 |
| ✅ EXACT | `Action_BootAway` | QB | `8` | `8` | 67 | START | 67 | 104 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 105 | START | 105 | 116 |
| ✅ EXACT | `Action_SecureCatch` | TE2 | `6` | `6` | 134 | START | 134 | 146 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 14 | 33 | 20 | inferred_complete_timeline |
| `Action_None` | 34 | 38 | 5 | inferred_complete_timeline |
| `Action_FakeHandoff` | 39 | 66 | 28 | inferred_complete_timeline |
| `Action_BootAway` | 67 | 104 | 38 | inferred_complete_timeline |
| `Action_ThrowPass` | 105 | 116 | 12 | inferred_complete_timeline |
| `Action_None` | 117 | 175 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 59 | 46 | inferred_complete_timeline |
| `Action_None` | 61 | 210 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_SecureCatch` | 134 | 146 | 13 | inferred_complete_timeline |
| `Action_None` | 147 | 156 | 10 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_RunBlock` | 24 | 88 | 65 | inferred_complete_timeline |
| `Action_RunBlock` | 92 | 210 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_RunBlock` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_BallSnap` | 14 | 33 | 20 | inferred_complete_timeline |
| `Action_RunBlock` | 34 | 55 | 22 | inferred_complete_timeline |
| `Action_RunBlock` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 85 | 94 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 97 | 210 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_RunBlock` | 24 | 121 | 98 | inferred_complete_timeline |
| `Action_RunBlock` | 124 | 138 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_RunBlock` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 66 | 53 | inferred_complete_timeline |
| `Action_None` | 68 | 210 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 84 | 71 | inferred_complete_timeline |
| `Action_None` | 100 | 205 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 68 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 75 | 62 | inferred_complete_timeline |
| `Action_None` | 78 | 210 | 133 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 73–76 | 4 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 75–210 | 134 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 99–206 | 108 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 102–185 | 83 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 102–210 | 109 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 120–153 | 17 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 146–210 | 65 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 150–210 | 59 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 164–210 | 44 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 173–210 | 38 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 182–210 | 29 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 193–196 | 4 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 200–202 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [14–33], lower_priority='Action_RunBlock' annotated_start=24, effective_Action_RunBlock_start=34.
- ⚠️ Action 'Action_None' range [14-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-84] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-205] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-59] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-68] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-156] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [24-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [24-88] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [92-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [24-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [34-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [65-66] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [85-94] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [97-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [24-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [124-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-206] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-196] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '27' has 1 frames without a visible bounding box.
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

</details>