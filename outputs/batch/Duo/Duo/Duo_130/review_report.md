# Play-Annotation-Generator Annotation Review — Duo_130

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_130`
- **Frame Range:** 0 to 298 (299 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 298
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `16` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 90 |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | `17` | `17` | 154 | START | 154 | 218 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | `4` | `4` | 154 | START | 154 | 208 |
| ✅ EXACT | `Action_ComboBlock` | LG | `7` | `7` | 154 | START | 154 | 218 |
| ✅ EXACT | `Action_ComboBlock` | RG | `9` | `9` | 154 | START | 154 | 218 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 218 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 298 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 151 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 181 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 298 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 186 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 298 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_ComboBlock` | 154 | 218 | 65 | inferred_complete_timeline |
| `Action_None` | 219 | 298 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 153 | 62 | inferred_complete_timeline |
| `Action_ComboBlock` | 154 | 218 | 65 | inferred_complete_timeline |
| `Action_None` | 219 | 253 | 35 | inferred_complete_timeline |
| `Action_None` | 269 | 283 | 15 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 153 | 53 | inferred_complete_timeline |
| `Action_ComboBlock` | 154 | 208 | 55 | inferred_complete_timeline |
| `Action_ComboBlock` | 210 | 218 | 9 | inferred_complete_timeline |
| `Action_None` | 223 | 298 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 298 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 142 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 21 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 90 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 108 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 127 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 150 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 210 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 230 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 255 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 284 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 290 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 229 | 230 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 269 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 298 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 144–298 | 136 | 8 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 180–298 | 112 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 184–298 | 97 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 191–298 | 87 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 195–196 | 2 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 201–297 | 91 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 219–266 | 48 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 226–254 | 29 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 230–298 | 53 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 232–298 | 67 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 239–298 | 60 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 244–278 | 25 | 3 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 248–298 | 48 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 272–298 | 18 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 68 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-255] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [154-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [210-218] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-249] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-298] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-271] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-284] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-290] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [154-218] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-283] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-269] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-90] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-138] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-230] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-151] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-246] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-283] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-248] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-261] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-226] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-264] for track '20' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-275] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-298] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-196] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-219] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-297] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-266] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-254] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-291] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-294] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-298] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-249] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-261] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-278] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-298] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-278] for track '30' has 1 frames without a visible bounding box.
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

</details>