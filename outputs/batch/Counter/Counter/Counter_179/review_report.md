# Play-Annotation-Generator Annotation Review — Counter_179

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_179`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_PullLeadBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | TE | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | TE | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 32 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `20` | `19` | 33 | START | 33 | 35 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `15` | `14` | 36 | START | 36 | 119 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `20` | `19` | 36 | START | 36 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `22` | `21` | 36 | START | 36 | 50 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `18` | `17` | 36 | START | 36 | 77 |
| ✅ EXACT | `Action_PullLeadBlock` | RG | `8` | `7` | 36 | START | 36 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | Position_Unknown | `21` | `20` | 40 | START | 40 | 63 |
| ✅ EXACT | `Action_SnapReceive` | TE | `9` | `8` | 46 | END | 33 | 46 |
| ✅ EXACT | `Action_Handoff` | TE | `9` | `8` | 52 | START | 52 | 73 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `21` | `20` | 74 | START | 74 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 119 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 239 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 227 | 195 | inferred_complete_timeline |
| `Action_None` | 229 | 239 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 46 | 14 | inferred_complete_timeline |
| `Action_None` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 52 | 73 | 22 | inferred_complete_timeline |
| `Action_None` | 74 | 222 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 230 | 198 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 76 | 44 | inferred_complete_timeline |
| `Action_None` | 109 | 114 | 6 | inferred_complete_timeline |
| `Action_None` | 117 | 239 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 36 | 119 | 84 | inferred_complete_timeline |
| `Action_None` | 120 | 234 | 115 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 239 | 207 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 149 | 117 | inferred_complete_timeline |
| `Action_None` | 152 | 157 | 6 | inferred_complete_timeline |
| `Action_None` | 161 | 218 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 186 | 154 | inferred_complete_timeline |
| `Action_None` | 188 | 212 | 25 | inferred_complete_timeline |
| `Action_None` | 222 | 227 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 226 | 194 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 239 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 133 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 239 | 207 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–221 | 221 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–239 | 240 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–239 | 234 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–77 | 78 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–239 | 237 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–235 | 228 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–239 | 238 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–102 | 89 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 9–14 | 5 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 83–233 | 144 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 92–95 | 4 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 114–229 | 115 | 2 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 144–162 | 19 | 1 | Undefined position; Undefined team |
| `28` | `44` | Position_Unknown | Team_Unknown | 157–239 | 82 | 2 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 197–207 | 7 | 2 | Undefined position; Undefined team |
| `30` | `48` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 43 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [33-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-218] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-212] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-227] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-222] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-226] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-114] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-230] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-214] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [36-77] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-106] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-235] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [40-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [36-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [65-102] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-10] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-14] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-233] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-229] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-162] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-177] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.

</details>