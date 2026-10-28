# Play-Annotation-Generator Annotation Review — Draw_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_81`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 56
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `6` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 35 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 33 | START | 33 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `12` | 36 | START | 36 | 71 |
| ✅ EXACT | `Action_PassBlock` | RG | `18` | `17` | 36 | START | 36 | 134 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `19` | 36 | START | 36 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `7` | `6` | 36 | START | 47 | 55 |
| ✅ EXACT | `Action_PassBlock` | LT | `9` | `8` | 36 | START | 36 | 134 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 46 | END | 33 | 46 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `15` | `14` | 50 | START | 50 | 67 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 68 | START | 68 | 81 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `22` | `21` | 82 | START | 82 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 134 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 46 | 14 | inferred_complete_timeline |
| `Action_None` | 47 | 49 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 50 | 67 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 68 | 81 | 14 | inferred_complete_timeline |
| `Action_None` | 82 | 215 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 239 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 239 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 238 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 157 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 134 | 99 | inferred_complete_timeline |
| `Action_None` | 135 | 239 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 134 | 99 | inferred_complete_timeline |
| `Action_None` | 135 | 239 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_BallSnap` | 33 | 46 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 55 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 82 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 108 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 125 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 239 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 134 | 99 | inferred_complete_timeline |
| `Action_None` | 135 | 237 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 71 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 95 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 134 | 35 | inferred_complete_timeline |
| `Action_None` | 135 | 155 | 21 | inferred_complete_timeline |
| `Action_None` | 157 | 239 | 83 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 74 | 42 | inferred_complete_timeline |
| `Action_None` | 76 | 239 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 239 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 121 | 89 | inferred_complete_timeline |
| `Action_None` | 131 | 135 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 239 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 239 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 234 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 146 | 114 | inferred_complete_timeline |
| `Action_None` | 156 | 159 | 4 | inferred_complete_timeline |
| `Action_None` | 163 | 166 | 4 | inferred_complete_timeline |
| `Action_None` | 170 | 239 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 239 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 239 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 239 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 32 | 18 | inferred_complete_timeline |
| `Action_None` | 33 | 229 | 197 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 20–239 | 216 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 32–89 | 58 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 88–95 | 4 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 138–235 | 27 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 138–141 | 4 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 235–239 | 4 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 162: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [33–46], lower_priority='Action_PassBlock' annotated_start=36, effective_Action_PassBlock_start=47.
- ⚠️ Action 'Action_None' range [33-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-238] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-55] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-61] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-82] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-108] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-125] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [129-130] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-215] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-239] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-74] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-237] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-32] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-229] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-52] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [82-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-89] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-235] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '27' has 1 frames without a visible bounding box.
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