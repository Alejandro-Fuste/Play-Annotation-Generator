# Play-Annotation-Generator Annotation Review — Power_354

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_354`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 62
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 39
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 22 | START | 22 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 22 | START | 22 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 22 | START | 22 | 255 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 22 | START | 22 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 22 | START | 60 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 22 | START | 22 | 295 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 22 | START | 22 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `7` | `Group` | 22 | START | 22 | 243 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `10` | `10` | 175 | START | 175 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `15` | `15` | 175 | START | 175 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `12` | `12` | 175 | START | 175 | 199 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 22–277
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 255 | 234 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 269 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 277 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 22–295
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 295 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 22–289
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 243 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 252 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 286 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 289 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 22–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 215 | 194 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 299 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 22–202
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 174 | 153 | inferred_complete_timeline |
| `Action_PullBlock` | 175 | 199 | 25 | inferred_complete_timeline |
| `Action_PullBlock` | 201 | 202 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 60–299
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 60 | 165 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 174 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 185 | 219 | 35 | inferred_complete_timeline |
| `Action_None` | 220 | 278 | 59 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 22–299
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 189 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 207 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 240 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 299 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 22–265
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 174 | 153 | inferred_complete_timeline |
| `Action_DownBlock` | 175 | 194 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 196 | 219 | 24 | inferred_complete_timeline |
| `Action_None` | 220 | 256 | 37 | inferred_complete_timeline |
| `Action_None` | 262 | 265 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 22–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 299 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 22–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 275 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 299 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 22–299
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 44 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 170 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 213 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 299 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 22–175
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 175 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 22–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 299 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 22–78
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 78 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 22–292
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 238 | 217 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 278 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 292 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 22–60 | 39 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 88–299 | 208 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 97–169 | 48 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 184–265 | 82 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 194–269 | 57 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 207–299 | 87 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 254–299 | 31 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 275–299 | 25 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 287–299 | 13 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 48 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [22-275] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-215] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-60] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-78] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-295] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-240] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-247] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-243] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-247] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-252] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-286] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-289] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-299] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [175-194] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-256] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-255] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-277] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [175-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [201-202] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-238] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-278] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-292] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-174] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [175-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-278] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-279] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-133] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-140] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-158] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-265] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-197] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-269] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-270] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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