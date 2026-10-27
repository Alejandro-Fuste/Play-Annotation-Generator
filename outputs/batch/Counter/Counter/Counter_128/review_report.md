# Play-Annotation-Generator Annotation Review — Counter_128

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_128`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `17` | `16` |
| ✅ EXACT | `Action_PullBlock` | SAF | defense | `6` | `5` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 76 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 28 | START | 28 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `9` | 30 | START | 43 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `17` | `16` | 30 | START | 30 | 107 |
| ✅ EXACT | `Action_PullBlock` | SAF | `6` | `5` | 30 | START | 30 | 110 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `1` | `0` | 30 | START | 30 | 110 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 42 | END | 28 | 42 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 51 | START | 51 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `8` | 77 | START | 77 | 168 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 110 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 28 | 42 | 15 | inferred_complete_timeline |
| `Action_None` | 43 | 50 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 51 | 76 | 26 | inferred_complete_timeline |
| `Action_None` | 77 | 130 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 168 | 92 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 192 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 209 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 57 | 30 | inferred_complete_timeline |
| `Action_None` | 62 | 168 | 107 | inferred_complete_timeline |
| `Action_None` | 173 | 210 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 142 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 152 | 125 | inferred_complete_timeline |
| `Action_None` | 154 | 206 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 30 | 107 | 78 | inferred_complete_timeline |
| `Action_DownBlock` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 132 | 22 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_BallSnap` | 28 | 42 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 43 | 65 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 110 | 32 | inferred_complete_timeline |
| `Action_None` | 111 | 136 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 80 | 53 | inferred_complete_timeline |
| `Action_None` | 82 | 103 | 22 | inferred_complete_timeline |
| `Action_None` | 109 | 210 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 30 | 110 | 81 | inferred_complete_timeline |
| `Action_None` | 111 | 210 | 100 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 123 | 96 | inferred_complete_timeline |
| `Action_None` | 127 | 137 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 173 | 146 | inferred_complete_timeline |
| `Action_None` | 176 | 193 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 210 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 98 | 71 | inferred_complete_timeline |
| `Action_None` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_None` | 105 | 156 | 52 | inferred_complete_timeline |
| `Action_None` | 158 | 173 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 210 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 107 | 80 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 159 | 37 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 161 | 134 | inferred_complete_timeline |
| `Action_None` | 167 | 210 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PullBlock` | 30 | 110 | 81 | inferred_complete_timeline |
| `Action_None` | 111 | 154 | 44 | inferred_complete_timeline |
| `Action_None` | 159 | 210 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `20` | Position_Unknown | Team_Unknown | 75–132 | 27 | 5 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 80–83 | 4 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 94–196 | 94 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 129–130 | 2 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 134–210 | 68 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 137–176 | 40 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 139–210 | 72 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 141–210 | 70 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 153–168 | 6 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 160–210 | 46 | 5 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 184–210 | 27 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 198–210 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [28–42], lower_priority='Action_DownBlock' annotated_start=30, effective_Action_DownBlock_start=43.
- ⚠️ Action 'Action_PullLeadBlock' range [30-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-206] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-161] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-107] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-159] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [77-168] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [199-201] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [43-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [68-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-57] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-168] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [51-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [30-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-121] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-154] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-181] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-176] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-177] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '28' has 1 frames without a visible bounding box.
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