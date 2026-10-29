# Play-Annotation-Generator Annotation Review — Duo_235

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_235`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `21` | `17` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `0` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 0 | START | 0 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | `2` | `2` | 132 | START | 132 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | `21` | `17` | 132 | START | 132 | 180 |
| ✅ EXACT | `Action_ComboBlock` | LG | `4` | `4` | 132 | START | 132 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RB | `5` | `5` | 132 | START | 132 | 192 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `4` | `4` | 148 | START | 148 | 209 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 209 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 132 | 192 | 61 | inferred_complete_timeline |
| `Action_ComboBlock` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 198 | 201 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 220 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 223 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_ComboBlock` | 132 | 147 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 148 | 209 | 62 | inferred_complete_timeline |
| `Action_None` | 210 | 221 | 12 | inferred_complete_timeline |
| `Action_None` | 223 | 227 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_ComboBlock` | 132 | 164 | 33 | inferred_complete_timeline |
| `Action_ComboBlock` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 219 | 5 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |
| `Action_None` | 225 | 239 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 239 | 87 | inferred_complete_timeline |

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
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 220 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 117 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 158 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 194 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 216 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 233 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 31 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 121 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 156 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 151 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 179 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 185 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 200 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–239 | 229 | 4 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 20–115 | 71 | 10 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 48–127 | 80 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 111–239 | 124 | 6 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 120–176 | 26 | 6 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 136–161 | 26 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 136–155 | 6 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 164–239 | 27 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 187–200 | 14 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 200–213 | 9 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 200–239 | 39 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 208–239 | 32 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 211–226 | 10 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 212–239 | 28 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 220–234 | 15 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 220–224 | 5 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 224–226 | 3 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 232–233 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 90 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-223] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [132-164] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [180-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-234] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [132-192] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [194-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [198-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-239] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-239] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-220] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-64] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-158] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-194] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-216] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-233] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-151] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-179] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-146] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-31] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-121] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-156] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-200] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-219] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-24] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-82] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-115] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [132-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [182-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-131] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-139] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-200] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-213] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-239] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-218] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-239] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-234] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-224] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '31' has 1 frames without a visible bounding box.
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

</details>