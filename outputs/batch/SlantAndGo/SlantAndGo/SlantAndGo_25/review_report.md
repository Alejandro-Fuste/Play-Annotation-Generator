# Play-Annotation-Generator Annotation Review — SlantAndGo_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_25`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 92
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
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_SellRoute` | WR1 | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR1 | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 2 | START | 2 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 5 | START | 18 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `16` | `16` | 5 | START | 5 | 37 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 5 | START | 5 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 5 | START | 5 | 14 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 17 | END | 2 | 17 |
| ✅ EXACT | `Action_SellRoute` | WR1 | `10` | `10` | 37 | START | 37 | 70 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 57 | START | 57 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR1 | `10` | `10` | 71 | START | 71 | 247 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 17 | 16 | inferred_complete_timeline |
| `Action_None` | 18 | 56 | 39 | inferred_complete_timeline |
| `Action_ThrowPass` | 57 | 79 | 23 | inferred_complete_timeline |
| `Action_None` | 80 | 118 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 134 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_SellRoute` | 37 | 70 | 34 | inferred_complete_timeline |
| `Action_VerticalStem` | 71 | 247 | 177 | inferred_complete_timeline |
| `Action_VerticalStem` | 250 | 278 | 29 | inferred_complete_timeline |
| `Action_VerticalStem` | 280 | 329 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 81 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 118 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 46 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 22 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 17 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 24 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 111 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 124 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 136 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 14 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 131 | 116 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 43 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 139 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 125 | 124 | inferred_complete_timeline |
| `Action_None` | 127 | 133 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 189 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 175 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 187 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 152 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 105 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 129 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 301 | 300 | inferred_complete_timeline |
| `Action_None` | 303 | 307 | 5 | inferred_complete_timeline |
| `Action_None` | 309 | 313 | 5 | inferred_complete_timeline |
| `Action_None` | 315 | 328 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 74 | 73 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_None` | 80 | 312 | 233 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–202 | 200 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–257 | 258 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–113 | 111 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 57–129 | 67 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 60–105 | 14 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 71–134 | 64 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 103–106 | 4 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 117–205 | 89 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 155–253 | 88 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 169–329 | 152 | 4 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 285–295 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (10 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 38: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 38: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 38: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [2–17], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=18.
- ⚠️ Action 'Action_None' range [2-118] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-187] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-312] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-43] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-139] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-133] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-301] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-307] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-313] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-328] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-193] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-202] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [71-247] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [250-278] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-81] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-111] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-124] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [131-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-189] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-257] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-37] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-91] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-105] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-22] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-14] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-131] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-70] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-129] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-253] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-295] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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