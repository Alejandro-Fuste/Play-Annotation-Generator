# Play-Annotation-Generator Annotation Review — Counter_183

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_183`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE2 | defense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 10 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 10 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 10 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 10 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 10 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 10 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 10 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 10 | 139 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `22` | `21` | 140 | START | 140 | 144 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `19` | `18` | 145 | START | 145 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `22` | `21` | 145 | START | 145 | 209 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `21` | `20` | 145 | START | 145 | 173 |
| ✅ EXACT | `Action_PullLeadBlock` | LG | `11` | `10` | 145 | START | 145 | 185 |
| ✅ EXACT | `Action_SnapReceive` | C | `15` | `14` | 152 | END | 140 | 152 |
| ✅ EXACT | `Action_Handoff` | C | `15` | `14` | 163 | START | 163 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE2 | `16` | `15` | 180 | START | 180 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 218 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 10–299
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_None` | 140 | 160 | 21 | inferred_complete_timeline |
| `Action_None` | 162 | 199 | 38 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 299 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 10–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_None` | 140 | 299 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 10–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_None` | 140 | 299 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 10–290
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_None` | 140 | 290 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 10–185
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 144 | 135 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 145 | 185 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 10–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_SnapReceive` | 140 | 152 | 13 | inferred_complete_timeline |
| `Action_None` | 153 | 162 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 163 | 179 | 17 | inferred_complete_timeline |
| `Action_None` | 180 | 299 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 10–176
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_None` | 140 | 159 | 20 | inferred_complete_timeline |
| `Action_None` | 162 | 176 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 10–290
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_None` | 140 | 290 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_None` | 140 | 204 | 65 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 299 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 170 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 179 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 180 | 239 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 244 | 299 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_None` | 140 | 206 | 67 | inferred_complete_timeline |
| `Action_None` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_None` | 218 | 225 | 8 | inferred_complete_timeline |
| `Action_None` | 229 | 299 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_None` | 140 | 299 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_None` | 140 | 283 | 144 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_None` | 140 | 299 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 10–299 | 286 | 4 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 10–299 | 280 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 10–299 | 278 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 10–299 | 290 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 10–299 | 274 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 10–216 | 204 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 10–299 | 285 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 10–299 | 282 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 183–188 | 6 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 192–299 | 95 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 225–299 | 75 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 232–299 | 68 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 40 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [140-209] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-283] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-237] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-290] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-160] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-199] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [145-185] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-206] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-299] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-290] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-204] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [180-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [241-242] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [145-207] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [145-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [145-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [214-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-235] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-299] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>