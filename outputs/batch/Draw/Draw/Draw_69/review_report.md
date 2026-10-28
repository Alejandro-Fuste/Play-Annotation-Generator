# Play-Annotation-Generator Annotation Review — Draw_69

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_69`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 50
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 38 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 36 | START | 36 | 54 |
| ✅ EXACT | `Action_PassBlock` | RT | `2` | `1` | 39 | START | 39 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `19` | 39 | START | 55 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `20` | 39 | START | 39 | 87 |
| ✅ EXACT | `Action_PassBlock` | RG | `22` | `21` | 39 | START | 39 | 77 |
| ✅ EXACT | `Action_PassBlock` | LT | `7` | `6` | 39 | START | 39 | 130 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 54 | END | 36 | 54 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `15` | `14` | 58 | START | 58 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `15` | `14` | 77 | START | 77 | 130 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 130 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 36 | 54 | 19 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 58 | 76 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 130 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 132 | 239 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 239 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 112 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 239 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 239 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 130 | 92 | inferred_complete_timeline |
| `Action_None` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 87 | 49 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 130 | 41 | inferred_complete_timeline |
| `Action_None` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_BallSnap` | 36 | 54 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 130 | 76 | inferred_complete_timeline |
| `Action_None` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 77 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 130 | 92 | inferred_complete_timeline |
| `Action_None` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 69 | 34 | inferred_complete_timeline |
| `Action_None` | 75 | 239 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 83 | 48 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_None` | 94 | 168 | 75 | inferred_complete_timeline |
| `Action_None` | 170 | 218 | 49 | inferred_complete_timeline |
| `Action_None` | 220 | 234 | 15 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 69 | 34 | inferred_complete_timeline |
| `Action_None` | 76 | 112 | 37 | inferred_complete_timeline |
| `Action_None` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_None` | 125 | 129 | 5 | inferred_complete_timeline |
| `Action_None` | 134 | 219 | 86 | inferred_complete_timeline |
| `Action_None` | 222 | 231 | 10 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 63 | 28 | inferred_complete_timeline |
| `Action_None` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_None` | 76 | 105 | 30 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 239 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 239 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 129 | 94 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 236 | 201 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 127 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 239 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 239 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 224 | 189 | inferred_complete_timeline |
| `Action_None` | 230 | 235 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 61–71 | 6 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 96–239 | 137 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 161–213 | 52 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 137: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [36–54], lower_priority='Action_PassBlock' annotated_start=39, effective_Action_PassBlock_start=55.
- ⚠️ Action 'Action_None' range [36-236] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-112] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-219] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-231] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-127] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-218] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-234] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [77-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-224] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-87] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-77] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>