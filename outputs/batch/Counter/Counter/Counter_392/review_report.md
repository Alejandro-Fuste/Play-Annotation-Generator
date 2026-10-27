# Play-Annotation-Generator Annotation Review — Counter_392

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_392`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `12` | `11` |
| ✅ EXACT | `Action_DownBlock` | DT2 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 35 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 33 | START | 33 | 47 |
| ✅ EXACT | `Action_DownBlock` | LG | `12` | `11` | 36 | START | 36 | 126 |
| ✅ EXACT | `Action_DownBlock` | DT2 | `15` | `14` | 36 | START | 36 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `8` | `7` | 36 | START | 36 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `11` | `10` | 36 | START | 36 | 65 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 47 | END | 33 | 47 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 57 | START | 57 | 75 |
| ✅ EXACT | `Action_BallCarry` | RB | `2` | `1` | 76 | START | 76 | 81 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 126 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 47 | 15 | inferred_complete_timeline |
| `Action_None` | 48 | 56 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 57 | 75 | 19 | inferred_complete_timeline |
| `Action_None` | 76 | 162 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_BallCarry` | 76 | 81 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 36 | 65 | 30 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 69 | 87 | 19 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 104 | 111 | 8 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 113 | 125 | 13 | inferred_complete_timeline |
| `Action_None` | 128 | 133 | 6 | inferred_complete_timeline |
| `Action_None` | 135 | 210 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 54 | 22 | inferred_complete_timeline |
| `Action_None` | 133 | 187 | 55 | inferred_complete_timeline |
| `Action_None` | 190 | 192 | 3 | inferred_complete_timeline |
| `Action_None` | 196 | 204 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 36 | 126 | 91 | inferred_complete_timeline |
| `Action_None` | 127 | 174 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_BallSnap` | 33 | 47 | 15 | inferred_complete_timeline |
| `Action_None` | 48 | 112 | 65 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PullBlock` | 36 | 71 | 36 | inferred_complete_timeline |
| `Action_PullBlock` | 74 | 126 | 53 | inferred_complete_timeline |
| `Action_None` | 127 | 155 | 29 | inferred_complete_timeline |
| `Action_None` | 157 | 167 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 98 | 66 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 185 | 62 | inferred_complete_timeline |
| `Action_None` | 187 | 193 | 7 | inferred_complete_timeline |
| `Action_None` | 195 | 210 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 82 | 50 | inferred_complete_timeline |
| `Action_None` | 86 | 115 | 30 | inferred_complete_timeline |
| `Action_None` | 124 | 163 | 40 | inferred_complete_timeline |
| `Action_None` | 171 | 176 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 210 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 210 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 36 | 126 | 91 | inferred_complete_timeline |
| `Action_None` | 127 | 210 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 210 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 134 | 102 | inferred_complete_timeline |
| `Action_None` | 143 | 210 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 79 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 11–147 | 123 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 60–210 | 149 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 65–157 | 93 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 109–191 | 72 | 4 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 142–190 | 42 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 142–210 | 59 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 153–210 | 58 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 168–210 | 43 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 171–210 | 40 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 196–210 | 12 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `11` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '7' (RG) duration 91 frames exceeds threshold 90 frames [start=36, end=126].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (LG) duration 91 frames exceeds threshold 90 frames [start=36, end=126].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '14' (DT2) duration 91 frames exceeds threshold 90 frames [start=36, end=126].
- ⚠️ Action 'Action_None' range [33-134] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [76-81] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-54] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-187] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-56] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-185] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [36-71] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-155] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [36-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [69-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [91-92] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [104-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [113-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [36-126] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-82] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-115] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-163] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [33-47] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-112] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-74] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-210] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-176] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-191] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '24' has 1 frames without a visible bounding box.
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

</details>