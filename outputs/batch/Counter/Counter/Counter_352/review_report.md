# Play-Annotation-Generator Annotation Review — Counter_352

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_352`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `7` | `6` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `7` | `6` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 63 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `7` | `6` | 64 | START | 64 | 66 |
| ✅ EXACT | `Action_DownBlock` | LT | `14` | `13` | 67 | START | 67 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `7` | `6` | 67 | START | 67 | 115 |
| ✅ EXACT | `Action_DownBlock` | RT | `8` | `7` | 67 | START | 67 | 147 |
| ✅ EXACT | `Action_PullBlock` | LG | `6` | `5` | 67 | START | 67 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `3` | `2` | 67 | START | 67 | 140 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 76 | END | 64 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `9` | `8` | 86 | START | 86 | 104 |
| ✅ EXACT | `Action_BallCarry` | RB | `1` | `0` | 110 | START | 110 | 158 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 147 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 64 | 76 | 13 | inferred_complete_timeline |
| `Action_None` | 77 | 85 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 86 | 104 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 196 | 87 | inferred_complete_timeline |
| `Action_None` | 205 | 208 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 158 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 67 | 140 | 74 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 161 | 9 | inferred_complete_timeline |
| `Action_None` | 167 | 175 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_DownBlock` | 67 | 147 | 81 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PullBlock` | 67 | 147 | 81 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 63–120
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 63 | 63 | 1 | inferred_complete_timeline |
| `Action_None` | 64 | 91 | 28 | inferred_complete_timeline |
| `Action_None` | 95 | 104 | 10 | inferred_complete_timeline |
| `Action_None` | 106 | 120 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 104 | 41 | inferred_complete_timeline |
| `Action_None` | 106 | 210 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_DownBlock` | 67 | 147 | 81 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 210 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 128 | 65 | inferred_complete_timeline |
| `Action_None` | 131 | 210 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 93 | 30 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 95 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 92 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 161 | 98 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 210 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 210 | 147 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–210 | 201 | 6 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 61–127 | 67 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 96–174 | 32 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 111–128 | 18 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 124–167 | 44 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 135–210 | 76 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 152–210 | 59 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 159–193 | 35 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 168–210 | 43 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 41 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_BallCarry' range [110-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [67-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [143-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [67-115] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-197] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [86-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-196] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-95] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-92] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-128] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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