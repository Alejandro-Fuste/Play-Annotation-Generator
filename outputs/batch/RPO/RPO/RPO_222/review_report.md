# Play-Annotation-Generator Annotation Review — RPO_222

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_222`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `19` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `10` | 44 | START | 44 | 104 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `15` | 44 | START | 44 | 104 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 44 | START | 44 | 104 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 44 | START | 44 | 104 |
| ✅ EXACT | `Action_ZoneBlock` | C | `9` | `9` | 44 | START | 44 | 104 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `8` | 48 | START | 48 | 65 |
| ✅ EXACT | `Action_PullBall` | QB | `8` | `8` | 66 | START | 66 | 75 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 97 | START | 97 | 104 |

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
- **Visible Frames:** 0–165
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 47 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 48 | 65 | 18 | inferred_complete_timeline |
| `Action_PullBall` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_None` | 76 | 96 | 21 | inferred_complete_timeline |
| `Action_ThrowPass` | 97 | 104 | 8 | inferred_complete_timeline |
| `Action_None` | 105 | 154 | 50 | inferred_complete_timeline |
| `Action_None` | 157 | 165 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 75 | 33 | inferred_complete_timeline |
| `Action_None` | 87 | 155 | 69 | inferred_complete_timeline |
| `Action_None` | 162 | 299 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 150 | 108 | inferred_complete_timeline |
| `Action_None` | 154 | 171 | 18 | inferred_complete_timeline |
| `Action_None` | 173 | 186 | 14 | inferred_complete_timeline |
| `Action_None` | 206 | 299 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 104 | 61 | inferred_complete_timeline |
| `Action_None` | 105 | 122 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 104 | 61 | inferred_complete_timeline |
| `Action_None` | 105 | 214 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 104 | 61 | inferred_complete_timeline |
| `Action_None` | 105 | 245 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 104 | 61 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 108 | 299 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 104 | 61 | inferred_complete_timeline |
| `Action_None` | 105 | 184 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 88 | 46 | inferred_complete_timeline |
| `Action_None` | 90 | 177 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 184 | 142 | inferred_complete_timeline |
| `Action_None` | 187 | 296 | 110 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 126 | 13 | inferred_complete_timeline |
| `Action_None` | 130 | 179 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 293 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 93 | 51 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 264 | 164 | inferred_complete_timeline |
| `Action_None` | 266 | 274 | 9 | inferred_complete_timeline |
| `Action_None` | 276 | 299 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 212 | 170 | inferred_complete_timeline |
| `Action_None` | 221 | 290 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 107 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 25–118 | 28 | 8 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 95–140 | 46 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 95–151 | 55 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 106–299 | 187 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 117–169 | 53 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 127–128 | 2 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 140–299 | 160 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 144–299 | 148 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 156–212 | 52 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 161–299 | 139 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 175–220 | 45 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 234–299 | 66 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 242–299 | 58 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 242–279 | 38 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 247–299 | 40 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 254–299 | 46 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 257–285 | 29 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 275–278 | 4 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 286–293 | 4 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 56 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [43-212] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-290] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-293] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-93] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-274] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-214] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-186] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-184] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-296] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-126] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-179] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-26] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-101] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-140] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-177] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-280] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-183] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-220] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-279] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-252] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-285] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '34' has 1 frames without a visible bounding box.
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

</details>