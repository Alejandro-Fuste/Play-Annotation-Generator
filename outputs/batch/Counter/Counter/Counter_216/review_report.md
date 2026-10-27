# Play-Annotation-Generator Annotation Review — Counter_216

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_216`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 130
- **Validation Warnings:** 163
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 0 | START | 0 | 74 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 74 | START | 74 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 75 | START | 90 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `6` | `5` | 75 | START | 75 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `8` | `7` | 75 | START | 75 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `20` | `19` | 75 | START | 75 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | `9` | `8` | 75 | START | 75 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 89 | END | 74 | 89 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 102 | START | 102 | 107 |
| ⚠️ START CHANGED | `Action_BallCarry` | QB | `11` | `10` | 126 | START | 134 | 150 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 159 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–150
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 89 | 16 | inferred_complete_timeline |
| `Action_None` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 95 | 99 | 5 | inferred_complete_timeline |
| `Action_None` | 101 | 101 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 134 | 150 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 75 | 88 | 14 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 92 | 107 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 84 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_DownBlock` | 75 | 135 | 61 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 159 | 16 | inferred_complete_timeline |
| `Action_None` | 160 | 180 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 89 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 90 | 108 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 129 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 145 | 149 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 30 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 43 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 73 | 28 | inferred_complete_timeline |
| `Action_None` | 74 | 87 | 14 | inferred_complete_timeline |
| `Action_None` | 95 | 124 | 30 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_DownBlock` | 75 | 106 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 159 | 50 | inferred_complete_timeline |
| `Action_None` | 160 | 189 | 30 | inferred_complete_timeline |
| `Action_None` | 198 | 201 | 4 | inferred_complete_timeline |
| `Action_None` | 205 | 232 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 127 | 54 | inferred_complete_timeline |
| `Action_None` | 135 | 177 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 161 | 88 | inferred_complete_timeline |
| `Action_None` | 165 | 178 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 127 | 54 | inferred_complete_timeline |
| `Action_None` | 135 | 156 | 22 | inferred_complete_timeline |
| `Action_None` | 178 | 209 | 32 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 171 | 98 | inferred_complete_timeline |
| `Action_None` | 175 | 178 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 153 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 132 | 59 | inferred_complete_timeline |
| `Action_None` | 134 | 162 | 29 | inferred_complete_timeline |
| `Action_None` | 168 | 183 | 16 | inferred_complete_timeline |
| `Action_None` | 185 | 211 | 27 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 95 | 22 | inferred_complete_timeline |
| `Action_None` | 98 | 146 | 49 | inferred_complete_timeline |
| `Action_None` | 149 | 178 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 253 | 180 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–17 | 16 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 3–33 | 31 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 7–94 | 88 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 19–67 | 7 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 36–119 | 57 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 66–126 | 9 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 86–212 | 116 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 89–198 | 103 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 101–102 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 102–122 | 20 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 112–151 | 37 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 114–238 | 72 | 7 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 119–124 | 4 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 120–133 | 14 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 149–269 | 106 | 5 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 156–214 | 50 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 160–250 | 85 | 5 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 163–268 | 106 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 165–173 | 9 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 173–262 | 86 | 2 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 178–211 | 10 | 2 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 187–269 | 74 | 3 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 189–217 | 29 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 197–229 | 30 | 2 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 202–227 | 10 | 2 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 204–232 | 29 | 1 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 213–214 | 2 | 1 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 236–242 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `9` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `11` (QB): Annotated start 126 != Inferred start 134

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 105 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [74–89], lower_priority='Action_DownBlock' annotated_start=75, effective_Action_DownBlock_start=90.
- ⚠️ Action 'Action_None' range [74-253] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-95] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-146] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-178] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-161] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-178] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-127] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-177] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [75-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-84] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [75-106] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-232] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [75-88] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [92-107] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-153] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [102-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [134-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-183] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-211] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-30] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-87] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-124] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [90-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [145-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-17] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-21] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-67] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [75-90] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [118-119] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-212] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-132] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-190] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-125] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-145] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-128] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-183] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-229] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-238] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-165] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-220] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-252] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-179] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-205] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-182] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-199] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-216] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-241] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-268] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-173] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-262] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-217] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-217] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-232] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-242] for track '42' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>