# Play-Annotation-Generator Annotation Review — SlantAndGo_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_47`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `15` | `15` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_SellRoute` | WR1 | offense | `9` | `9` |
| ✅ EXACT | `Action_VerticalStem` | WR1 | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 36 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 10 | START | 10 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `15` | `15` | 20 | START | 20 | 31 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `16` | `16` | 20 | START | 28 | 126 |
| ✅ EXACT | `Action_PassBlock` | LT | `18` | `18` | 20 | START | 20 | 134 |
| ✅ EXACT | `Action_PassBlock` | RT | `20` | `20` | 20 | START | 20 | 143 |
| ✅ EXACT | `Action_PassBlock` | LG | `21` | `21` | 20 | START | 20 | 21 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 27 | END | 10 | 27 |
| ✅ EXACT | `Action_SellRoute` | WR1 | `9` | `9` | 37 | START | 37 | 86 |
| ✅ EXACT | `Action_VerticalStem` | WR1 | `9` | `9` | 87 | START | 87 | 210 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 115 | START | 115 | 127 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 27 | 18 | inferred_complete_timeline |
| `Action_None` | 28 | 114 | 87 | inferred_complete_timeline |
| `Action_ThrowPass` | 115 | 127 | 13 | inferred_complete_timeline |
| `Action_None` | 128 | 160 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 152 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_SellRoute` | 37 | 86 | 50 | inferred_complete_timeline |
| `Action_VerticalStem` | 87 | 210 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 209 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 134 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–21
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 12 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 19 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 21 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 27 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 126 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 31 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 132 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 143 | 124 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 170 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 120 | 111 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 164 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 195 | 186 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 94 | 85 | inferred_complete_timeline |
| `Action_None` | 96 | 105 | 10 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 71 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 45 | 36 | inferred_complete_timeline |
| `Action_None` | 47 | 49 | 3 | inferred_complete_timeline |
| `Action_None` | 51 | 156 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 176 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 140 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 179 | 170 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 28–153 | 107 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 31–48 | 11 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 69–73 | 5 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 75–150 | 76 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 117–210 | 91 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 148–150 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 154–201 | 34 | 6 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `16` (C): Annotated start 20 != Inferred start 28

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [10–27], lower_priority='Action_PassBlock' annotated_start=20, effective_Action_PassBlock_start=28.
- ⚠️ Action 'Action_None' range [10-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-179] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-170] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-176] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-71] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [87-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-209] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-152] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-45] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-49] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-160] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-143] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-12] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-19] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-21] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-33] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-37] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-150] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '28' has 1 frames without a visible bounding box.
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