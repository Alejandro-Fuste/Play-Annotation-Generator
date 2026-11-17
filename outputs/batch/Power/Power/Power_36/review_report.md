# Play-Annotation-Generator Annotation Review — Power_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_36`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 138
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_PullBlock` | DT2 | defense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `0` | `Group` | 34 | START | 14 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 34 | START | 14 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 34 | START | 14 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 34 | START | 14 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 34 | START | 14 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 34 | START | 14 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 34 | START | 14 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 34 | START | 14 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | QB | `16` | `16` | 156 | START | 156 | 174 |
| ✅ EXACT | `Action_PullBlock` | DT2 | `11` | `11` | 156 | START | 156 | 176 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 14–243
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 75 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 152 | 41 | inferred_complete_timeline |
| `Action_DownBlock` | 156 | 174 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 176 | 193 | 18 | inferred_complete_timeline |
| `Action_None` | 194 | 243 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 14–329
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 211 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 225 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 306 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 319 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 14–81
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 70 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 81 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 14–329
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 50 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 172 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 319 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 14–274
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 61 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 170 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 274 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 14–72
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 72 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 14–329
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 158 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 265 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 294 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 329 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 14–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 329 | 316 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 14–272
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 174 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 199 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 269 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 272 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 14–329
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 65 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 149 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 207 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 329 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 14–176
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 90 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 155 | 54 | inferred_complete_timeline |
| `Action_PullBlock` | 156 | 176 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 14–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 197 | 184 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 329 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 14–249
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 167 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 249 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 14–329
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 169 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 183 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 203 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 220 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 329 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 14–235
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 235 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 14–232
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 24 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 232 | 204 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 14–34 | 21 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 51–329 | 218 | 8 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 75–222 | 63 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 121–315 | 195 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 147–205 | 57 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 161–329 | 125 | 8 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 217–329 | 100 | 4 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 239–329 | 86 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 242–329 | 88 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 244–246 | 3 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 252–256 | 5 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 253–263 | 11 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 257–329 | 62 | 3 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 259–273 | 15 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 262–329 | 68 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 268–329 | 62 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 269–329 | 55 | 3 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 278–321 | 44 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 281–303 | 23 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 289–329 | 41 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 302–308 | 7 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 309–318 | 8 | 2 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 316–329 | 14 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 317–321 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 87 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [14-72] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-61] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-274] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-183] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-203] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-220] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-70] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-81] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-265] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-294] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-211] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-225] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-306] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-319] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-50] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-319] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-65] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-24] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-232] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-197] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-329] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-90] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [156-176] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-235] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-174] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-249] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-75] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [156-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-243] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-98] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-246] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-266] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-127] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-315] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-200] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-253] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-295] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-305] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-234] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-244] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-254] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-261] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-280] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-329] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-246] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-263] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-284] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-273] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-329] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-280] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-322] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-321] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-303] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-308] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-314] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>