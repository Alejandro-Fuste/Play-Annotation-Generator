# Play-Annotation-Generator Annotation Review — Draw_84

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_84`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 102
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
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `16` | `15` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 3 | START | 3 | 16 |
| ✅ EXACT | `Action_PassBlock` | RT | `16` | `15` | 6 | START | 6 | 132 |
| ✅ EXACT | `Action_PassBlock` | RG | `19` | `18` | 6 | START | 6 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `20` | 6 | START | 17 | 132 |
| ✅ EXACT | `Action_PassBlock` | LG | `22` | `21` | 6 | START | 6 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `8` | 6 | START | 6 | 118 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 16 | END | 3 | 16 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `20` | `19` | 23 | START | 23 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `20` | `19` | 54 | START | 54 | 74 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 132 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 16 | 14 | inferred_complete_timeline |
| `Action_None` | 17 | 22 | 6 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 23 | 53 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 54 | 74 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 79 | 111 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 189 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 111 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 118 | 113 | inferred_complete_timeline |
| `Action_PassBlock` | 120 | 124 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_None` | 133 | 210 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 132 | 127 | inferred_complete_timeline |
| `Action_None` | 133 | 210 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 16 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 132 | 116 | inferred_complete_timeline |
| `Action_None` | 134 | 210 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 132 | 127 | inferred_complete_timeline |
| `Action_None` | 133 | 171 | 39 | inferred_complete_timeline |
| `Action_None` | 173 | 210 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 132 | 127 | inferred_complete_timeline |
| `Action_None` | 133 | 210 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 178 | 176 | inferred_complete_timeline |
| `Action_None` | 183 | 196 | 14 | inferred_complete_timeline |
| `Action_None` | 201 | 210 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 31 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 99 | 97 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 210 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 111 | 210 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 184 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 210 | 208 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–199 | 198 | 3 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–210 | 191 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–126 | 119 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 0–123 | 89 | 7 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 32–210 | 179 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 32–210 | 178 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 32–131 | 42 | 9 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 112–210 | 99 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 124–126 | 3 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 129–130 | 2 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 137–146 | 10 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 175–183 | 9 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 190–210 | 14 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 167: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [3–16], lower_priority='Action_PassBlock' annotated_start=6, effective_Action_PassBlock_start=17.
- ⚠️ Action 'Action_None' range [3-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-31] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-178] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-189] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-99] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [120-124] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-184] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-25] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-79] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-171] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [54-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [79-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-74] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-126] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-39] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-64] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-83] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-123] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-50] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-33] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-72] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-80] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-113] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-146] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-183] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>