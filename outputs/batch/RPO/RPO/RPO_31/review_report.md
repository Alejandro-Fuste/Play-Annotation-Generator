# Play-Annotation-Generator Annotation Review — RPO_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_31`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_ZoneBlock` | C | `10` | `10` | 44 | START | 44 | 135 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `4` | 44 | START | 44 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 44 | START | 44 | 135 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 44 | START | 44 | 135 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 44 | START | 44 | 135 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `8` | 57 | START | 57 | 65 |
| ✅ EXACT | `Action_PullBall` | QB | `8` | `8` | 66 | START | 66 | 83 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 126 | START | 126 | 135 |

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
- **Visible Frames:** 0–308
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 56 | 14 | inferred_complete_timeline |
| `Action_ReadDefender` | 57 | 65 | 9 | inferred_complete_timeline |
| `Action_PullBall` | 66 | 83 | 18 | inferred_complete_timeline |
| `Action_None` | 84 | 125 | 42 | inferred_complete_timeline |
| `Action_ThrowPass` | 126 | 135 | 10 | inferred_complete_timeline |
| `Action_None` | 136 | 308 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 119 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 135 | 92 | inferred_complete_timeline |
| `Action_None` | 136 | 329 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 135 | 92 | inferred_complete_timeline |
| `Action_None` | 136 | 181 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 135 | 92 | inferred_complete_timeline |
| `Action_None` | 136 | 151 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 111 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 135 | 92 | inferred_complete_timeline |
| `Action_None` | 136 | 170 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 53 | 11 | inferred_complete_timeline |
| `Action_None` | 61 | 65 | 5 | inferred_complete_timeline |
| `Action_None` | 70 | 83 | 14 | inferred_complete_timeline |
| `Action_None` | 102 | 329 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 67 | 25 | inferred_complete_timeline |
| `Action_None` | 71 | 98 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 63 | 21 | inferred_complete_timeline |
| `Action_None` | 66 | 71 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 319 | 277 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 86 | 44 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 181 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 265 | 223 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `15` | Position_Unknown | Team_Unknown | 70–246 | 177 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 72–140 | 69 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 89–313 | 225 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 100–156 | 57 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 112–131 | 7 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 123–144 | 22 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 136–137 | 2 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 154–187 | 34 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 155–329 | 175 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 161–305 | 145 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 164–171 | 8 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 168–329 | 161 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 176–325 | 150 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 184–329 | 146 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 189–329 | 141 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 263–327 | 65 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 284–285 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 326–328 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LG) duration 92 frames exceeds threshold 90 frames [start=44, end=135].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 92 frames exceeds threshold 90 frames [start=44, end=135].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 92 frames exceeds threshold 90 frames [start=44, end=135].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 92 frames exceeds threshold 90 frames [start=44, end=135].
- ⚠️ Action 'Action_None' range [43-319] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-119] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-67] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-98] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-86] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-181] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-308] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-329] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-151] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-53] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-65] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-83] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-63] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-246] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-140] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-313] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-305] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-325] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-327] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '32' has 1 frames without a visible bounding box.
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

</details>