# Play-Annotation-Generator Annotation Review — OutAndUp_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_1`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 76
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB1 | offense | `14` | `14` |
| ✅ EXACT | `Action_SellOut` | WR1 | offense | `11` | `11` |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | QB1 | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `14` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | `17` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `21` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `6` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 21 | START | 21 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 26 | START | 35 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `13` | `13` | 26 | START | 26 | 73 |
| ✅ EXACT | `Action_PassBlock` | LT | `16` | `16` | 26 | START | 26 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 26 | START | 26 | 61 |
| ✅ EXACT | `Action_PassBlock` | RT | `20` | `20` | 26 | START | 26 | 210 |
| ✅ EXACT | `Action_SnapReceive` | QB1 | `14` | `14` | 34 | END | 21 | 34 |
| ✅ EXACT | `Action_SellOut` | WR1 | `11` | `11` | 82 | START | 82 | 102 |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | `11` | `11` | 103 | START | 103 | 180 |
| ✅ EXACT | `Action_ThrowPass` | QB1 | `14` | `14` | 113 | START | 113 | 124 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_None` | 35 | 112 | 78 | inferred_complete_timeline |
| `Action_ThrowPass` | 113 | 124 | 12 | inferred_complete_timeline |
| `Action_None` | 125 | 210 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>QB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 94 | 74 | inferred_complete_timeline |
| `Action_None` | 99 | 163 | 65 | inferred_complete_timeline |
| `Action_None` | 165 | 169 | 5 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_SellOut` | 82 | 102 | 21 | inferred_complete_timeline |
| `Action_RunGoRoute` | 103 | 180 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 207 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 73 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 88 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 125 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 127 | 130 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 210 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 41 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 191 | 195 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 61 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 189 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 210 | 185 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 114 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 51 | 31 | inferred_complete_timeline |
| `Action_None` | 53 | 61 | 9 | inferred_complete_timeline |
| `Action_None` | 87 | 112 | 26 | inferred_complete_timeline |
| `Action_None` | 116 | 123 | 8 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_None` | 134 | 174 | 41 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 210 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 169 | 149 | inferred_complete_timeline |
| `Action_None` | 171 | 210 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 191 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 112–143 | 32 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 167–182 | 9 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 167–210 | 43 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 169–210 | 42 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 180–185 | 5 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 184–192 | 9 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 195–199 | 5 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 203–205 | 3 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [21–34], lower_priority='Action_PassBlock' annotated_start=26, effective_Action_PassBlock_start=35.
- ⚠️ Action 'Action_None' range [21-114] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-169] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-51] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-61] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-174] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-191] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [103-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-41] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-89] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [182-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [191-195] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [198-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-73] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-88] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-125] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [127-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-207] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-94] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-163] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-61] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-143] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-182] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-192] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
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