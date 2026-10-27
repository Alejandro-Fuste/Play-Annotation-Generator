# Play-Annotation-Generator Annotation Review — Counter_324

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_324`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 35
- **Ball Tracks:** 1
- **Action Segments:** 90
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 72 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 70 | START | 70 | 80 |
| ✅ EXACT | `Action_DownBlock` | RT | `10` | `9` | 73 | START | 73 | 173 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `16` | `15` | 73 | START | 81 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `4` | `3` | 73 | START | 73 | 95 |
| ✅ EXACT | `Action_PullBlock` | LG | `9` | `8` | 73 | START | 73 | 117 |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | `1` | `0` | 73 | START | 73 | 173 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 80 | END | 70 | 80 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 92 | START | 92 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 116 | START | 116 | 241 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 173 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_SnapReceive` | 70 | 80 | 11 | inferred_complete_timeline |
| `Action_None` | 81 | 91 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 92 | 115 | 24 | inferred_complete_timeline |
| `Action_None` | 116 | 193 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 241 | 126 | inferred_complete_timeline |
| `Action_BallCarry` | 276 | 291 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 135 | 66 | inferred_complete_timeline |
| `Action_None` | 137 | 202 | 66 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 73 | 173 | 101 | inferred_complete_timeline |
| `Action_None` | 174 | 299 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 239 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PullBlock` | 73 | 117 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_BallSnap` | 70 | 80 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 81 | 173 | 93 | inferred_complete_timeline |
| `Action_None` | 174 | 299 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_DownBlock` | 73 | 95 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 173 | 77 | inferred_complete_timeline |
| `Action_None` | 174 | 212 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_DownBlock` | 73 | 173 | 101 | inferred_complete_timeline |
| `Action_None` | 174 | 298 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 87 | 18 | inferred_complete_timeline |
| `Action_None` | 132 | 149 | 18 | inferred_complete_timeline |
| `Action_None` | 154 | 166 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 299 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 95 | 26 | inferred_complete_timeline |
| `Action_None` | 103 | 110 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 87 | 18 | inferred_complete_timeline |
| `Action_None` | 95 | 98 | 4 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_None` | 116 | 120 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 258 | 189 | inferred_complete_timeline |
| `Action_None` | 260 | 299 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 109 | 40 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 299 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 130 | 61 | inferred_complete_timeline |
| `Action_None` | 132 | 166 | 35 | inferred_complete_timeline |
| `Action_None` | 169 | 198 | 30 | inferred_complete_timeline |
| `Action_None` | 203 | 299 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 222 | 153 | inferred_complete_timeline |
| `Action_None` | 225 | 299 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 104–299 | 196 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 108–299 | 189 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 113–294 | 181 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 119–299 | 168 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 124–299 | 176 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 126–299 | 173 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 133–297 | 155 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 150–299 | 90 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 160–163 | 4 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 166–299 | 134 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 181–299 | 119 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 221–236 | 16 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 222–223 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 241–242 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 244–278 | 35 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 250–275 | 26 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `27` | 130 | 150 | 11 | 52.4% | 135–143, 145 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `16` (C): Annotated start 73 != Inferred start 81
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (RG) duration 101 frames exceeds threshold 90 frames [start=73, end=173].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '9' (RT) duration 101 frames exceeds threshold 90 frames [start=73, end=173].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (C) duration 101 frames exceeds threshold 90 frames [start=73, end=173].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [70–80], lower_priority='Action_DownBlock' annotated_start=73, effective_Action_DownBlock_start=81.
- ⚠️ Action 'Action_None' range [70-109] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-135] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-202] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [73-95] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-241] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [276-291] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [296-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-222] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [73-117] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [73-173] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-298] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-239] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-258] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-149] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-87] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-177] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-207] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-288] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-294] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-130] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-213] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-207] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-203] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-281] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-297] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-236] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-278] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-275] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '35' has 1 frames without a visible bounding box.
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

</details>