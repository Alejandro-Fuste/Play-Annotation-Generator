# Play-Annotation-Generator Annotation Review — Power_236

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_236`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 131
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | defense | `6` | `6` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `18` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 9 | START | 9 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `13` | `Group` | 9 | START | 23 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 9 | START | 93 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 9 | START | 102 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 9 | START | 9 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 9 | START | 9 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 9 | START | 9 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 9 | START | 9 | 135 |
| ✅ EXACT | `Action_DownBlock` | C | `4` | `4` | 116 | START | 116 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | `6` | `6` | 116 | START | 116 | 129 |
| ✅ EXACT | `Action_DownBlock` | LT | `7` | `7` | 116 | START | 116 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `18` | `17` | 116 | START | 116 | 118 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 9–216
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 135 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 196 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 216 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 23–229
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 24 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 33 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 113 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 132 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 182 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 223 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 229 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 93–171
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 93 | 122 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 171 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 9–273
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 115 | 107 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 184 | 69 | inferred_complete_timeline |
| `Action_None` | 209 | 211 | 3 | inferred_complete_timeline |
| `Action_None` | 224 | 273 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 59 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 113 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 299 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–144
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 115 | 107 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 144 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 102–217
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 102 | 105 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 115 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 145 | 188 | 44 | inferred_complete_timeline |
| `Action_None` | 189 | 217 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 9–166
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 122 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 159 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 166 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–176
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 176 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–139
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 22 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 115 | 92 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 129 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 138 | 139 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 27–186
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 137 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 186 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 49–299
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 49 | 214 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 223 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 299 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 15 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 24 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 194 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 204 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 214 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 299 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 9–295
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 157 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 210 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 295 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 9–237
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 237 | 229 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 9–99 | 91 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 9–26 | 18 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 12–18 | 7 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 117–256 | 111 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 128–299 | 119 | 8 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 144–162 | 19 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 149–232 | 80 | 3 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 180–203 | 24 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 191–270 | 34 | 3 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 194–268 | 49 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 200–299 | 92 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 205–273 | 68 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 221–228 | 8 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 225–240 | 16 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 234–299 | 59 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 240–284 | 45 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 245–299 | 55 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 249–254 | 6 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 260–289 | 30 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 262–283 | 17 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 265–279 | 15 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 283–295 | 13 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 84 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [9-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-26] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-144] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-295] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-22] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [138-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-273] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-122] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-196] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-216] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-59] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-113] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-299] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-15] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-24] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-194] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-204] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-214] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-18] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-33] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-113] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-182] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-223] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-214] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-223] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-171] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [116-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-217] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-212] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-256] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-158] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-178] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-238] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-250] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-259] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-162] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-219] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-270] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-219] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-252] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-268] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-272] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-273] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-228] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-240] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-294] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-284] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-254] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-289] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-283] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-279] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-295] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.

</details>