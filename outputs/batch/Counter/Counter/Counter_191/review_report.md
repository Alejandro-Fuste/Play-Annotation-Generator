# Play-Annotation-Generator Annotation Review — Counter_191

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_191`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 49
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | DE2 | defense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 94 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `20` | `19` | 95 | START | 95 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `18` | `17` | 98 | START | 98 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `19` | `18` | 98 | START | 98 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `20` | `19` | 98 | START | 98 | 142 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `21` | `20` | 98 | START | 98 | 177 |
| ✅ EXACT | `Action_PullLeadBlock` | DE2 | `4` | `3` | 98 | START | 98 | 150 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `22` | `21` | 105 | END | 95 | 105 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `22` | `21` | 114 | START | 114 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | `14` | `13` | 130 | START | 130 | 142 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 177 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 127 | 33 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 176 | 43 | inferred_complete_timeline |
| `Action_None` | 201 | 247 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 169 | 75 | inferred_complete_timeline |
| `Action_None` | 174 | 269 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 142 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 171 | 258 | 88 | inferred_complete_timeline |
| `Action_BallCarry` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 122 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 98 | 150 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–269 | 260 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–269 | 265 | 7 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–116 | 117 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–269 | 263 | 6 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–269 | 270 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–269 | 270 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 129–269 | 141 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 143–146 | 4 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 162–269 | 108 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 166–269 | 104 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 191–194 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 24 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_PullLeadBlock' range [98-150] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-176] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-247] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [147-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-258] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-269] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [98-120] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [122-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [138-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [98-116] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [98-142] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [148-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '26' has 1 frames without a visible bounding box.
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

</details>