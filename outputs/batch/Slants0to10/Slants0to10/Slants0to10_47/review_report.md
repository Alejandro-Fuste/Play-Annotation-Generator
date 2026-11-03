# Play-Annotation-Generator Annotation Review — Slants0to10_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_47`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `22` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `18` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 1 | START | 1 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `10` | `10` | 4 | START | 16 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `16` | `16` | 4 | START | 4 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `22` | `22` | 4 | START | 4 | 9 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `3` | `3` | 4 | START | 4 | 65 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `0` | `0` | 15 | START | 15 | 66 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 15 | END | 1 | 15 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 51 | START | 51 | 60 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `0` | `0` | 93 | START | 93 | 329 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 15 | 15 | inferred_complete_timeline |
| `Action_None` | 16 | 50 | 35 | inferred_complete_timeline |
| `Action_ThrowPass` | 51 | 60 | 10 | inferred_complete_timeline |
| `Action_None` | 61 | 81 | 21 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 132 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 104 | 104 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 279 | 141 | inferred_complete_timeline |
| `Action_None` | 282 | 329 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 15 | 66 | 52 | inferred_complete_timeline |
| `Action_None` | 67 | 92 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 93 | 329 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 92 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 48 | 48 | inferred_complete_timeline |
| `Action_None` | 58 | 190 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 9 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 128 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 15 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 28 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 31 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 130 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 65 | 62 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 127 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 35 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 138 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 83 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 120 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 286 | 286 | inferred_complete_timeline |
| `Action_None` | 289 | 329 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 316 | 316 | inferred_complete_timeline |
| `Action_None` | 318 | 329 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–126 | 127 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–128 | 119 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–3 | 4 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 7–133 | 116 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 27–73 | 46 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 60–61 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 82–329 | 247 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 91–138 | 48 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 95–124 | 30 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 137–180 | 44 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 138–140 | 3 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 174–275 | 51 | 8 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 176–329 | 153 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 277–288 | 12 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 281–282 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 48: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Track ID '23' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [1–15], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=16.
- ⚠️ Action 'Action_None' range [1-35] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-126] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-65] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-127] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-104] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-279] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-329] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-28] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-31] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-286] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-120] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-316] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-130] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-48] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-190] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-92] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-43] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-63] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-128] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-3] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-9] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-12] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-17] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-23] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-63] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-320] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-138] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-124] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-188] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-204] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-231] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-254] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-308] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-329] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-288] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>