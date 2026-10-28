# Play-Annotation-Generator Annotation Review — Draw_62

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_62`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 51 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 49 | START | 49 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `1` | `0` | 52 | START | 52 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `11` | 52 | START | 66 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `7` | `6` | 52 | START | 52 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `8` | `7` | 52 | START | 52 | 91 |
| ✅ EXACT | `Action_PassBlock` | LT | `9` | `8` | 52 | START | 52 | 113 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 65 | END | 49 | 65 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `11` | `10` | 70 | START | 70 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `11` | `10` | 90 | START | 90 | 160 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 113 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 65 | 17 | inferred_complete_timeline |
| `Action_None` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 70 | 89 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 160 | 71 | inferred_complete_timeline |
| `Action_BallCarry` | 162 | 186 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 192 | 234 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 70 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 196 | 148 | inferred_complete_timeline |
| `Action_None` | 208 | 239 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 113 | 62 | inferred_complete_timeline |
| `Action_None` | 114 | 145 | 32 | inferred_complete_timeline |
| `Action_None` | 149 | 239 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 91 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 113 | 13 | inferred_complete_timeline |
| `Action_None` | 114 | 239 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_BallSnap` | 49 | 65 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 113 | 37 | inferred_complete_timeline |
| `Action_None` | 114 | 239 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 97 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 113 | 9 | inferred_complete_timeline |
| `Action_None` | 114 | 239 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 113 | 62 | inferred_complete_timeline |
| `Action_None` | 114 | 239 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 77 | 29 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_None` | 52 | 55 | 4 | inferred_complete_timeline |
| `Action_None` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_None` | 69 | 239 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 96 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 239 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 51 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 13–239 | 222 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 60–106 | 47 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 65–99 | 12 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 65–239 | 175 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 74–239 | 162 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 86–239 | 153 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 103–239 | 137 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 105–239 | 107 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 113–116 | 4 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 117–239 | 116 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 140–209 | 69 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 157–239 | 77 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 166–239 | 74 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 178–239 | 62 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 234–236 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [49–65], lower_priority='Action_PassBlock' annotated_start=52, effective_Action_PassBlock_start=66.
- ⚠️ Action 'Action_PassBlock' range [52-97] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-96] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-51] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-160] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [162-186] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [192-234] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-52] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-182] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-167] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-156] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-239] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '28' has 1 frames without a visible bounding box.
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

</details>