# Play-Annotation-Generator Annotation Review — RPO_240

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_240`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `20` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_RunBlock` | C | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 71 |
| ✅ EXACT | `Action_RunBlock` | LT | `1` | `1` | 73 | START | 73 | 132 |
| ✅ EXACT | `Action_RunBlock` | RG | `10` | `10` | 73 | START | 73 | 132 |
| ✅ EXACT | `Action_RunBlock` | RT | `3` | `3` | 73 | START | 73 | 132 |
| ✅ EXACT | `Action_RunBlock` | C | `5` | `5` | 73 | START | 73 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `6` | `6` | 73 | START | 73 | 126 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `8` | 82 | START | 82 | 96 |
| ✅ EXACT | `Action_PullBall` | QB | `8` | `8` | 97 | START | 97 | 105 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 125 | START | 125 | 132 |

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
- **Visible Frames:** 0–186
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 81 | 10 | inferred_complete_timeline |
| `Action_ReadDefender` | 82 | 96 | 15 | inferred_complete_timeline |
| `Action_PullBall` | 97 | 105 | 9 | inferred_complete_timeline |
| `Action_None` | 106 | 124 | 19 | inferred_complete_timeline |
| `Action_ThrowPass` | 125 | 132 | 8 | inferred_complete_timeline |
| `Action_None` | 133 | 149 | 17 | inferred_complete_timeline |
| `Action_None` | 152 | 186 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 197 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 113 | 42 | inferred_complete_timeline |
| `Action_None` | 118 | 179 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 72 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 73 | 132 | 60 | inferred_complete_timeline |
| `Action_None` | 133 | 171 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 72 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 73 | 126 | 54 | inferred_complete_timeline |
| `Action_RunBlock` | 128 | 132 | 5 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 72 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 73 | 132 | 60 | inferred_complete_timeline |
| `Action_None` | 133 | 188 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 72 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 73 | 132 | 60 | inferred_complete_timeline |
| `Action_None` | 133 | 165 | 33 | inferred_complete_timeline |
| `Action_None` | 169 | 182 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 72 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 73 | 132 | 60 | inferred_complete_timeline |
| `Action_None` | 133 | 206 | 74 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 191 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 100 | 29 | inferred_complete_timeline |
| `Action_None` | 102 | 131 | 30 | inferred_complete_timeline |
| `Action_None` | 140 | 206 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 77 | 6 | inferred_complete_timeline |
| `Action_None` | 81 | 174 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 116 | 45 | inferred_complete_timeline |
| `Action_None` | 118 | 184 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 196 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 187 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 56 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 89–181 | 93 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 107–120 | 11 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 121–299 | 179 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 125–299 | 175 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 130–299 | 169 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 134–218 | 85 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 182–221 | 10 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 186–203 | 8 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 234–299 | 66 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 235–299 | 63 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 237–299 | 63 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 238–299 | 62 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 37 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [72-116] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-184] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-197] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-206] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [73-132] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-188] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [73-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-187] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-191] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-131] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-181] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-218] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-276] for track '24' has 1 frames without a visible bounding box.
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