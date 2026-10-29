# Play-Annotation-Generator Annotation Review — Duo_44

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_44`
- **Frame Range:** 0 to 298 (299 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 298
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 121
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `24` | `22` |
| ✅ EXACT | `Action_ComboBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 272 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | `24` | `22` | 154 | START | 154 | 186 |
| ✅ EXACT | `Action_ComboBlock` | RT | `3` | `3` | 154 | START | 154 | 218 |
| ✅ EXACT | `Action_ComboBlock` | LG | `5` | `5` | 154 | START | 154 | 212 |
| ✅ EXACT | `Action_ComboBlock` | RG | `7` | `7` | 154 | START | 154 | 217 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 218 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 272 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 287 | 288 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 291 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 298 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 205 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 246 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 264 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_ComboBlock` | 154 | 212 | 59 | inferred_complete_timeline |
| `Action_None` | 221 | 253 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_ComboBlock` | 154 | 217 | 64 | inferred_complete_timeline |
| `Action_None` | 219 | 267 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_ComboBlock` | 154 | 218 | 65 | inferred_complete_timeline |
| `Action_None` | 219 | 274 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 225 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 83 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 179 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 201 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 226 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 235 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 240 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 296 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 298 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 192 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 240 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 273 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 80 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 106 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 241 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 298 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 84 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 98 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 179 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 192 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 241 | 242 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 278 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 287 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 298 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 187 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 260 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 298 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 62–65 | 4 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 81–298 | 131 | 6 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 97–254 | 158 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 118–129 | 11 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 140–186 | 47 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 159–295 | 134 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 161–298 | 133 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 205–266 | 31 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 218–266 | 46 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 232–257 | 26 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 233–240 | 6 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 236–298 | 63 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 238–259 | 18 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 269–271 | 3 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 269–271 | 3 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 278–296 | 18 | 2 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 288–294 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 84 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-241] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-278] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-287] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-298] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-246] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-264] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-274] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-287] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-291] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [154-212] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-187] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-260] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [154-217] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-267] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-298] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-201] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-231] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-235] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-240] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-296] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-272] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-240] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-273] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-241] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-298] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-143] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-252] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-263] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-282] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-254] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-129] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [154-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-269] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-295] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-215] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-298] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-208] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-266] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-230] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-263] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-257] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-240] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-298] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-251] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-271] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-271] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-293] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-296] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-294] for track '35' has 1 frames without a visible bounding box.
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