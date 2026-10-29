# Play-Annotation-Generator Annotation Review — Duo_196

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_196`
- **Frame Range:** 0 to 274 (275 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 274
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 274 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 2 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 272 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 157 |
| ✅ EXACT | `Action_ComboBlock` | RG | `10` | `10` | 152 | START | 152 | 189 |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | `21` | `21` | 152 | START | 152 | 189 |
| ✅ EXACT | `Action_ComboBlock` | LG | `4` | `4` | 152 | START | 152 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | `6` | `6` | 152 | START | 152 | 162 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 189 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 272 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 223 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 254 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 274 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 232 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 189 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 197 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_ComboBlock` | 152 | 189 | 38 | inferred_complete_timeline |
| `Action_None` | 190 | 207 | 18 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 274 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_ComboBlock` | 152 | 162 | 11 | inferred_complete_timeline |
| `Action_ComboBlock` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 170 | 189 | 20 | inferred_complete_timeline |
| `Action_None` | 190 | 274 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_ComboBlock` | 152 | 189 | 38 | inferred_complete_timeline |
| `Action_None` | 190 | 274 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 2–245
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 127 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 147 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 236 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 245 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 136 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 274 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 69 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 94 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 131 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 153 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 172 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 186 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 141 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 237 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 244 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 260 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 274 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 266 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 209 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 274 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 77–90 | 14 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 92–274 | 183 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 94–214 | 87 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 104–106 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 120–135 | 16 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 148–172 | 21 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 148–274 | 118 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 180–274 | 95 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 182–232 | 51 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 182–274 | 82 | 6 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 203–274 | 61 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 208–233 | 26 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 222–274 | 44 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 223–254 | 15 | 3 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 232–274 | 43 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 243–274 | 19 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 80 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 274 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-183] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-237] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-260] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-274] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-207] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-274] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [152-162] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [164-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [170-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-136] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-272] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-232] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [152-189] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-69] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-131] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-137] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-153] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-172] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-266] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-274] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-207] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-223] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-254] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-127] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-147] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-236] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-245] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-274] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-135] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-164] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-172] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-151] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-154] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-232] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-207] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-229] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-246] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-251] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-257] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-240] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-253] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-274] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-233] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-227] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-225] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-254] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-244] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-249] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-274] for track '34' has 1 frames without a visible bounding box.
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