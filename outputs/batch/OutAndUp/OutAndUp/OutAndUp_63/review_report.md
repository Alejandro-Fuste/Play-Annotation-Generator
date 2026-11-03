# Play-Annotation-Generator Annotation Review — OutAndUp_63

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_63`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_SellOut` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB1 | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `20` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `21` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | `5` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 26 | START | 26 | 30 |
| ✅ EXACT | `Action_SnapReceive` | LT | `16` | `16` | 30 | END | 26 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 34 | START | 34 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `16` | `16` | 34 | START | 34 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 34 | START | 34 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 34 | START | 34 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 34 | START | 34 | 48 |
| ✅ EXACT | `Action_SellOut` | WR1 | `1` | `1` | 67 | START | 67 | 94 |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | `1` | `1` | 95 | START | 95 | 213 |
| ✅ EXACT | `Action_ThrowPass` | QB1 | `20` | `20` | 127 | START | 127 | 137 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_ThrowPass` | 127 | 137 | 11 | inferred_complete_timeline |
| `Action_None` | 138 | 149 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>QB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 107 | 82 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_SellOut` | 67 | 94 | 28 | inferred_complete_timeline |
| `Action_RunGoRoute` | 95 | 213 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 198 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 79 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 73 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 30 | 5 | inferred_complete_timeline |
| `Action_None` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 101 | 68 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 115 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 126 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 142 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 153 | 157 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 45 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 99 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 106 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 109 | 152 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 30 | 5 | inferred_complete_timeline |
| `Action_None` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 45 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 24 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 33 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 139 | 106 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 144 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 146 | 149 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 48 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 112 | 62 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 147 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 165 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 139 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 126 | 101 | inferred_complete_timeline |
| `Action_None` | 131 | 148 | 18 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 113 | 269 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 182 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 192 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 144 | 119 | inferred_complete_timeline |
| `Action_None` | 146 | 149 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 227 | 202 | inferred_complete_timeline |
| `Action_None` | 232 | 242 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 98 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 55–71 | 9 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 57–154 | 71 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 71–175 | 105 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 102–114 | 5 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 125–154 | 26 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 133–159 | 23 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 151–269 | 119 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 210–269 | 60 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 58 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [26-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [95-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-98] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-227] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-242] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-192] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-107] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-144] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-126] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-148] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-73] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-35] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-45] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-165] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-101] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [117-126] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-142] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [153-157] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-24] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-139] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [146-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-45] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-99] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [109-152] for track '18' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-112] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-147] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-149] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-92] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-154] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-154] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-150] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-269] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '30' has 1 frames without a visible bounding box.
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