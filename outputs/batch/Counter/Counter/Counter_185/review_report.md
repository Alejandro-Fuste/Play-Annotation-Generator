# Play-Annotation-Generator Annotation Review — Counter_185

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_185`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 57
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `23` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_PlaySideFakeStep` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | DT1 | defense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | DT1 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 168 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `16` | `15` | 169 | START | 169 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `16` | `15` | 173 | START | 173 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `17` | `16` | 173 | START | 173 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `21` | `20` | 173 | START | 173 | 198 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `23` | `21` | 177 | START | 177 | 258 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `5` | `4` | 177 | START | 177 | 258 |
| ✅ EXACT | `Action_PlaySideFakeStep` | Position_Unknown | `20` | `19` | 178 | START | 178 | 210 |
| ✅ EXACT | `Action_SnapReceive` | DT1 | `15` | `14` | 184 | END | 169 | 184 |
| ✅ EXACT | `Action_Handoff` | DT1 | `15` | `14` | 194 | START | 194 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `20` | `19` | 211 | START | 211 | 243 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 258 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 282 | 114 | inferred_complete_timeline |
| `Action_None` | 285 | 299 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 299 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 177 | 258 | 82 | inferred_complete_timeline |
| `Action_None` | 259 | 299 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 299 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 299 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 267 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 251 | 83 | inferred_complete_timeline |
| `Action_None` | 253 | 299 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 299 | 131 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 299 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 299 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_SnapReceive` | 169 | 184 | 16 | inferred_complete_timeline |
| `Action_None` | 185 | 193 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 194 | 210 | 17 | inferred_complete_timeline |
| `Action_None` | 211 | 299 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 292 | 124 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 299 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 209 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 237 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–299 | 287 | 7 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–230 | 211 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–299 | 298 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–247 | 241 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 13–299 | 287 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 196–299 | 98 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 238–299 | 62 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 261–276 | 14 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 269–299 | 31 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 271–299 | 29 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 276–299 | 23 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 291–298 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 26 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [169-209] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [177-258] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-282] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-237] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-292] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [173-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [194-217] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [224-225] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [173-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [227-230] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [211-243] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [173-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [206-247] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-299] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-283] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-298] for track '29' has 2 frames without a visible bounding box.
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