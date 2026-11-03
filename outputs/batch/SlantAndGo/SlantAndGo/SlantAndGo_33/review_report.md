# Play-Annotation-Generator Annotation Review — SlantAndGo_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_33`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 61
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `22` | `22` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_SellRoute` | WR3 | offense | `6` | `6` |
| ✅ EXACT | `Action_VerticalStem` | WR3 | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 29 | START | 29 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `13` | 38 | START | 38 | 41 |
| ✅ EXACT | `Action_PassBlock` | RG | `14` | `14` | 38 | START | 38 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 38 | START | 42 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 38 | START | 38 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `22` | `22` | 38 | START | 38 | 132 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `2` | 41 | END | 29 | 41 |
| ✅ EXACT | `Action_SellRoute` | WR3 | `6` | `6` | 61 | START | 61 | 86 |
| ✅ EXACT | `Action_VerticalStem` | WR3 | `6` | `6` | 87 | START | 87 | 180 |
| ✅ EXACT | `Action_ThrowPass` | QB | `2` | `2` | 100 | START | 100 | 109 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 41 | 13 | inferred_complete_timeline |
| `Action_None` | 42 | 52 | 11 | inferred_complete_timeline |
| `Action_None` | 70 | 99 | 30 | inferred_complete_timeline |
| `Action_ThrowPass` | 100 | 109 | 10 | inferred_complete_timeline |
| `Action_None` | 110 | 180 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 166 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 162 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_SellRoute` | 61 | 86 | 26 | inferred_complete_timeline |
| `Action_VerticalStem` | 87 | 180 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 92 | 64 | inferred_complete_timeline |
| `Action_None` | 95 | 173 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 106 | 69 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 180 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 15 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 37 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 132 | 95 | inferred_complete_timeline |
| `Action_PassBlock` | 134 | 144 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_BallSnap` | 29 | 41 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 45 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 180 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 180 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 37 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 180 | 136 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 37 | 9 | inferred_complete_timeline |
| `Action_None` | 44 | 174 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 178 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 159 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 145 | 117 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 177 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 162 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 174 | 146 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–35 | 36 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 38–41 | 4 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 42–52 | 11 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 42–174 | 122 | 6 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [29–41], lower_priority='Action_PassBlock' annotated_start=38, effective_Action_PassBlock_start=42.
- ⚠️ Action 'Action_None' range [29-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-52] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-37] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-174] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SellRoute' range [61-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [87-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-145] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-37] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-159] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-35] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [29-41] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-45] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-180] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-178] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-15] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [134-144] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-41] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-52] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-45] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-77] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-106] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.

</details>