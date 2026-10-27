# Play-Annotation-Generator Annotation Review — Counter_46

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_46`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `15` | `14` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 25 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 51 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 182 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 183 | START | 183 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 186 | START | 198 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `14` | `13` | 186 | START | 186 | 228 |
| ✅ EXACT | `Action_DownBlock` | LT | `5` | `4` | 186 | START | 186 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `15` | `14` | 186 | START | 186 | 198 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `11` | `10` | 186 | START | 186 | 216 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 197 | END | 183 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `12` | `11` | 205 | START | 205 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `18` | `17` | 223 | START | 223 | 280 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 264 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_SnapReceive` | 183 | 197 | 15 | inferred_complete_timeline |
| `Action_None` | 198 | 204 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_None` | 228 | 290 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 212 | 30 | inferred_complete_timeline |
| `Action_None` | 219 | 226 | 8 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 259 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_DownBlock` | 186 | 219 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 25–246
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 43 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 185 | 133 | inferred_complete_timeline |
| `Action_DownBlock` | 186 | 228 | 43 | inferred_complete_timeline |
| `Action_DownBlock` | 245 | 246 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_BallSnap` | 183 | 197 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 198 | 201 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 204 | 213 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 51–299
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 68 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 117 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 127 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 185 | 51 | inferred_complete_timeline |
| `Action_PullBlock` | 186 | 198 | 13 | inferred_complete_timeline |
| `Action_PullBlock` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_None` | 271 | 283 | 13 | inferred_complete_timeline |
| `Action_None` | 285 | 288 | 4 | inferred_complete_timeline |
| `Action_None` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 186 | 216 | 31 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 221 | 39 | inferred_complete_timeline |
| `Action_None` | 224 | 228 | 5 | inferred_complete_timeline |
| `Action_None` | 237 | 296 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 299 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 208 | 26 | inferred_complete_timeline |
| `Action_None` | 222 | 299 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 253 | 71 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 299 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 299 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 299 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 60–224
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 60 | 182 | 123 | inferred_complete_timeline |
| `Action_None` | 183 | 224 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 204 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–248 | 249 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 188–212 | 24 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 199–299 | 89 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 247–299 | 45 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 267–299 | 33 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 268–299 | 32 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 275–299 | 25 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 297–299 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [183–197], lower_priority='Action_DownBlock' annotated_start=186, effective_Action_DownBlock_start=198.
- ⚠️ Action 'Action_None' range [183-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-248] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-221] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-296] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [186-219] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-212] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-259] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-208] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [186-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [183-197] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [205-206] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [211-219] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-290] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [198-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [204-213] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [186-228] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [245-246] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-185] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [186-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [237-238] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-283] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-224] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-212] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-280] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>