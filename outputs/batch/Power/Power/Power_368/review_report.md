# Play-Annotation-Generator Annotation Review — Power_368

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_368`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 64
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `0` | `Group` | 15 | START | 15 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 15 | START | 15 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 15 | START | 15 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 15 | START | 15 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 15 | START | 15 | 252 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 15 | START | 15 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 15 | START | 15 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 15 | START | 15 | 124 |
| ✅ EXACT | `Action_DownBlock` | C | `13` | `13` | 97 | START | 97 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `5` | `5` | 97 | START | 97 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `1` | `1` | 97 | START | 97 | 120 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 15–166
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 166 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 15–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 124 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 299 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 15–252
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 252 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 15–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 118 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 217 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 239 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 15–229
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 96 | 82 | inferred_complete_timeline |
| `Action_PullBlock` | 97 | 120 | 24 | inferred_complete_timeline |
| `Action_PullBlock` | 123 | 158 | 36 | inferred_complete_timeline |
| `Action_None` | 159 | 163 | 5 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 229 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 15–141
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 96 | 82 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 141 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 15–201
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 96 | 82 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 109 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 158 | 46 | inferred_complete_timeline |
| `Action_None` | 159 | 171 | 13 | inferred_complete_timeline |
| `Action_None` | 183 | 186 | 4 | inferred_complete_timeline |
| `Action_None` | 190 | 201 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 15–190
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 142 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 170 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 190 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 15–147
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 138 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 147 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 15–229
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 157 | 143 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 173 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 229 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 15–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 189 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 299 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 15–264
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 201 | 187 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 255 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 264 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 15–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 299 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 15–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 299 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 15–299
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 138 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 197 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 256 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `19` | Position_Unknown | Team_Unknown | 139–299 | 128 | 7 | Undefined position; Undefined team |
| `16` | `22` | Position_Unknown | Team_Unknown | 157–278 | 107 | 3 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 168–174 | 7 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 178–185 | 8 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 194–284 | 82 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 196–299 | 104 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 227–229 | 3 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 256–299 | 44 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 268–299 | 32 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 284–299 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 52 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [15-166] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [97-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [123-158] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-229] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-201] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-212] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-255] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-264] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [97-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-171] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-138] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-197] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-256] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-147] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-124] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-189] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-118] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-252] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [97-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-157] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-188] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-206] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-278] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-247] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-264] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-284] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-290] for track '24' has 1 frames without a visible bounding box.
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

</details>