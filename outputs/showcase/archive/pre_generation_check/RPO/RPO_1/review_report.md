# Play-Annotation-Generator Annotation Review — RPO_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_1`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `7` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `18` | `18` |
| ⚠️ START CHANGED | `Action_PullBall` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 86 |
| ✅ EXACT | `Action_RunBlock` | RG | `16` | `16` | 88 | START | 88 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `17` | `17` | 88 | START | 88 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `20` | `20` | 88 | START | 88 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `21` | `21` | 88 | START | 88 | 150 |
| ✅ EXACT | `Action_RunBlock` | RT | `4` | `4` | 88 | START | 88 | 239 |
| ✅ EXACT | `Action_ReadDefender` | QB | `18` | `18` | 100 | START | 100 | 118 |
| ⚠️ START CHANGED | `Action_PullBall` | QB | `18` | `18` | 121 | START | 122 | 133 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 134 | START | 134 | 145 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 99 | 13 | inferred_complete_timeline |
| `Action_ReadDefender` | 100 | 118 | 19 | inferred_complete_timeline |
| `Action_PullBall` | 122 | 133 | 12 | inferred_complete_timeline |
| `Action_ThrowPass` | 134 | 145 | 12 | inferred_complete_timeline |
| `Action_None` | 146 | 166 | 21 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 173 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 87 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 150 | 63 | inferred_complete_timeline |
| `Action_RunBlock` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 159 | 239 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 87 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 94 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 98 | 103 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 113 | 144 | 32 | inferred_complete_timeline |
| `Action_RunBlock` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 156 | 239 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 87 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 99 | 12 | inferred_complete_timeline |
| `Action_RunBlock` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 108 | 114 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 87 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 239 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 87 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 239 | 152 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 200 | 114 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 209 | 3 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 103 | 17 | inferred_complete_timeline |
| `Action_None` | 105 | 185 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 159 | 73 | inferred_complete_timeline |
| `Action_None` | 171 | 198 | 28 | inferred_complete_timeline |
| `Action_None` | 212 | 239 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 165 | 79 | inferred_complete_timeline |
| `Action_None` | 176 | 239 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 137 | 51 | inferred_complete_timeline |
| `Action_None` | 140 | 234 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 132 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–239 | 221 | 7 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 121–239 | 113 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 158–239 | 82 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 159–161 | 3 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 185–239 | 55 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 194–239 | 45 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 206–208 | 3 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 209–239 | 31 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (3 segments found)
- ⚠️ `Action_PullBall` for actor_track_id `18` (QB): Annotated start 121 != Inferred start 122

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 4: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 4: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [87-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-185] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-234] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-173] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-198] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-165] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [88-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [103-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [108-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [100-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [88-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [98-103] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [113-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [151-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [156-239] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [88-150] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [152-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>