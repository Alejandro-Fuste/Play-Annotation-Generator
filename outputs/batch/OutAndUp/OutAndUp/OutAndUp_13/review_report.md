# Play-Annotation-Generator Annotation Review — OutAndUp_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_13`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_SellOut` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_PumpFake` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_RunGoRoute` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `5` | 8 | START | 8 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 11 | START | 11 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 11 | START | 11 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `5` | `5` | 11 | START | 24 | 33 |
| ✅ EXACT | `Action_PassBlock` | RT | `7` | `7` | 11 | START | 11 | 152 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 23 | END | 8 | 23 |
| ✅ EXACT | `Action_SellOut` | WR2 | `1` | `1` | 60 | START | 60 | 101 |
| ✅ EXACT | `Action_PumpFake` | QB | `13` | `13` | 74 | START | 74 | 97 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 98 | START | 98 | 107 |
| ✅ EXACT | `Action_RunGoRoute` | WR2 | `1` | `1` | 102 | START | 102 | 180 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 23 | 16 | inferred_complete_timeline |
| `Action_None` | 24 | 73 | 50 | inferred_complete_timeline |
| `Action_PumpFake` | 74 | 97 | 24 | inferred_complete_timeline |
| `Action_ThrowPass` | 98 | 107 | 10 | inferred_complete_timeline |
| `Action_None` | 108 | 125 | 18 | inferred_complete_timeline |
| `Action_None` | 127 | 151 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 64 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 64 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_SellOut` | 60 | 101 | 42 | inferred_complete_timeline |
| `Action_RunGoRoute` | 102 | 180 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 54 | 47 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 180 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 34 | 27 | inferred_complete_timeline |
| `Action_None` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 180 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 90 | 80 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 180 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 164 | 154 | inferred_complete_timeline |
| `Action_PassBlock` | 167 | 180 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 23 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 33 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 158 | 123 | inferred_complete_timeline |
| `Action_PassBlock` | 170 | 180 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 152 | 142 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 127 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 171 | 43 | inferred_complete_timeline |
| `Action_None` | 174 | 180 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 83 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 180 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 164 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 104 | 97 | inferred_complete_timeline |
| `Action_None` | 108 | 122 | 15 | inferred_complete_timeline |
| `Action_None` | 124 | 175 | 52 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 180 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 60 | 53 | inferred_complete_timeline |
| `Action_None` | 63 | 158 | 96 | inferred_complete_timeline |
| `Action_None` | 168 | 180 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 180 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 92 | 85 | inferred_complete_timeline |
| `Action_None` | 96 | 163 | 68 | inferred_complete_timeline |
| `Action_None` | 167 | 171 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 154 | 147 | inferred_complete_timeline |
| `Action_None` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_None` | 166 | 172 | 7 | inferred_complete_timeline |
| `Action_None` | 174 | 178 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 92 | 85 | inferred_complete_timeline |
| `Action_None` | 95 | 98 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–159 | 154 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–27 | 15 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 22–29 | 4 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 36–37 | 2 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 84–175 | 76 | 3 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 86–180 | 95 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 88–180 | 93 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 113–177 | 60 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 16: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [8–23], lower_priority='Action_PassBlock' annotated_start=11, effective_Action_PassBlock_start=24.
- ⚠️ Action 'Action_None' range [8-54] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [102-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-92] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-64] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-33] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [170-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-122] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-34] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-164] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-127] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-171] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-164] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [167-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-90] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-180] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-10] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-27] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-23] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-29] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-87] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-158] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-162] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-177] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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