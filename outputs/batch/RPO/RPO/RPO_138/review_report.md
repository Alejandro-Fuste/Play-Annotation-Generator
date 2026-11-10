# Play-Annotation-Generator Annotation Review — RPO_138

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_138`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `26` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `0` | `0` | 65 | START | 65 | 90 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `11` | `11` | 65 | START | 65 | 119 |
| ✅ EXACT | `Action_ZoneBlock` | C | `12` | `12` | 65 | START | 65 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `13` | 65 | START | 65 | 96 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `9` | 65 | START | 65 | 119 |
| ✅ EXACT | `Action_ReadDefender` | QB | `4` | `4` | 68 | START | 68 | 86 |
| ✅ EXACT | `Action_PullBall` | QB | `4` | `4` | 87 | START | 87 | 101 |
| ✅ EXACT | `Action_ThrowPass` | QB | `4` | `4` | 112 | START | 112 | 119 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 67 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 68 | 86 | 19 | inferred_complete_timeline |
| `Action_PullBall` | 87 | 101 | 15 | inferred_complete_timeline |
| `Action_None` | 102 | 111 | 10 | inferred_complete_timeline |
| `Action_ThrowPass` | 112 | 119 | 8 | inferred_complete_timeline |
| `Action_None` | 120 | 163 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 170 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 122 | 59 | inferred_complete_timeline |
| `Action_None` | 125 | 165 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 90 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 105 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 116 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 96 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 119 | 21 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 119 | 55 | inferred_complete_timeline |
| `Action_None` | 120 | 167 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 119 | 55 | inferred_complete_timeline |
| `Action_None` | 120 | 130 | 11 | inferred_complete_timeline |
| `Action_None` | 137 | 165 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 119 | 55 | inferred_complete_timeline |
| `Action_None` | 120 | 128 | 9 | inferred_complete_timeline |
| `Action_None` | 146 | 192 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 134 | 71 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 113 | 50 | inferred_complete_timeline |
| `Action_None` | 116 | 157 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 174 | 111 | inferred_complete_timeline |
| `Action_None` | 177 | 183 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 171 | 108 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 209 | 6 | inferred_complete_timeline |
| `Action_None` | 211 | 233 | 23 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 127 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 188 | 125 | inferred_complete_timeline |
| `Action_None` | 209 | 229 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 4–128 | 125 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 64–65 | 2 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 84–239 | 156 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 90–237 | 142 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 118–182 | 54 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 122–239 | 113 | 3 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 124–170 | 45 | 2 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 132–165 | 34 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 141–146 | 6 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 142–155 | 13 | 2 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 149–239 | 91 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 149–162 | 14 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 155–157 | 3 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 157–239 | 81 | 3 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 184–238 | 55 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 199–233 | 35 | 1 | Undefined position; Undefined team |
| `31` | `49` | Position_Unknown | Team_Unknown | 221–227 | 7 | 1 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 222–223 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 57 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_ZoneBlock' range [65-90] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-105] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-116] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-233] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-165] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-163] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-127] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-188] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-229] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-192] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-174] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-183] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-119] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-96] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-157] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-128] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-128] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-182] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-197] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-238] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-233] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-227] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '32' has 1 frames without a visible bounding box.
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