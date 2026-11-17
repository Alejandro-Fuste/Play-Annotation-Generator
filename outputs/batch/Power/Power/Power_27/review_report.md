# Play-Annotation-Generator Annotation Review — Power_27

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_27`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `0` | `Group` | 25 | START | 25 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 25 | START | 25 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 25 | START | 25 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 25 | START | 25 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 25 | START | 25 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 25 | START | 25 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 25 | START | 25 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `3` | `Group` | 25 | START | 25 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `4` | `Group` | 25 | START | 25 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 25 | START | 25 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 25 | START | 25 | 270 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `16` | `16` | 128 | START | 128 | 133 |
| ✅ EXACT | `Action_DownBlock` | LG | `17` | `17` | 128 | START | 128 | 185 |
| ✅ EXACT | `Action_PullBlock` | RG | `21` | `21` | 128 | START | 128 | 181 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 25–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 299 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 25–299
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 270 | 246 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 275 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 286 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 299 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 25–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 163 | 139 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 169 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 299 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 25–297
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 147 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 201 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 241 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 259 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 264 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 275 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 297 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 25–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 299 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 25–207
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 142 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 207 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 25–299
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 140 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 168 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 188 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 299 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 25–227
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 127 | 103 | inferred_complete_timeline |
| `Action_DownBlock` | 128 | 185 | 58 | inferred_complete_timeline |
| `Action_None` | 186 | 196 | 11 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 222 | 227 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 25–141
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 127 | 103 | inferred_complete_timeline |
| `Action_DownBlock` | 128 | 133 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 137 | 141 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 25–299
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 127 | 103 | inferred_complete_timeline |
| `Action_PullBlock` | 128 | 181 | 54 | inferred_complete_timeline |
| `Action_None` | 198 | 299 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 25–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 299 | 275 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 25–168
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 157 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 168 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 25–299
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 139 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 163 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 206 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 219 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 241 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 299 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 25–299
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 192 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 206 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 299 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 25–299
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 219 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 238 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 281 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 295 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 25–299
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 191 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 204 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 224 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 286 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 25–282
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 219 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 282 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 25–299
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 219 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 241 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 281 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 299 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 25–299
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 250 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 257 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 299 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 25–256
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 256 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 25–292
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 292 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 25–299
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 231 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 281 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 292 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 299 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 152–195 | 44 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 203–239 | 35 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 224–299 | 61 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 237–240 | 4 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 258–299 | 38 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 286–288 | 3 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 286–299 | 14 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 78 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [25-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-282] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-201] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-241] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-259] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-264] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-275] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-163] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-169] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-299] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-250] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-257] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-191] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-204] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-286] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-270] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-275] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-256] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-139] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-206] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-219] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-299] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-219] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-241] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-281] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-231] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-281] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-292] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-292] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-206] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-214] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-238] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-281] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-295] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [128-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [137-141] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-196] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-140] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-168] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-188] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-201] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [128-181] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-207] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-221] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-239] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-241] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-299] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-240] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-276] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-288] for track '27' has 1 frames without a visible bounding box.
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

</details>