# Play-Annotation-Generator Annotation Review — BootPass_74

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_74`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Comp.`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 9
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_RunFlatRoute` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `33` | `24` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 20 | START | 20 | 35 |
| ✅ EXACT | `Action_RunBlock` | LT | `0` | `0` | 26 | START | 26 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `12` | `12` | 26 | START | 36 | 42 |
| ✅ EXACT | `Action_RunBlock` | RT | `14` | `14` | 26 | START | 26 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `3` | `3` | 26 | START | 26 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `6` | `6` | 26 | START | 26 | 34 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 35 | END | 20 | 35 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `11` | `11` | 41 | START | 41 | 57 |
| ✅ EXACT | `Action_BootAway` | QB | `11` | `11` | 58 | START | 58 | 96 |
| ✅ EXACT | `Action_RunFlatRoute` | LT | `0` | `0` | 65 | START | 65 | 96 |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 107 | START | 107 | 117 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `33` | `24` | 166 | START | 166 | 185 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_None` | 36 | 40 | 5 | inferred_complete_timeline |
| `Action_FakeHandoff` | 41 | 57 | 17 | inferred_complete_timeline |
| `Action_BootAway` | 58 | 96 | 39 | inferred_complete_timeline |
| `Action_None` | 97 | 106 | 10 | inferred_complete_timeline |
| `Action_ThrowPass` | 107 | 117 | 11 | inferred_complete_timeline |
| `Action_None` | 118 | 177 | 60 | inferred_complete_timeline |
| `Action_None` | 179 | 185 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 92 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 48 | 29 | inferred_complete_timeline |
| `Action_None` | 57 | 63 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_RunBlock` | 26 | 64 | 39 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 65 | 96 | 32 | inferred_complete_timeline |
| `Action_None` | 97 | 201 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_RunBlock` | 26 | 40 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 44 | 99 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 36 | 42 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 44 | 89 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_RunBlock` | 26 | 34 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 36 | 63 | 28 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 81 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 25 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 26 | 69 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 22 | 3 | inferred_complete_timeline |
| `Action_None` | 25 | 62 | 38 | inferred_complete_timeline |
| `Action_None` | 65 | 100 | 36 | inferred_complete_timeline |
| `Action_None` | 104 | 188 | 85 | inferred_complete_timeline |
| `Action_None` | 191 | 210 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 32 | 13 | inferred_complete_timeline |
| `Action_None` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_None` | 48 | 65 | 18 | inferred_complete_timeline |
| `Action_None` | 67 | 73 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 26 | 7 | inferred_complete_timeline |
| `Action_None` | 32 | 40 | 9 | inferred_complete_timeline |
| `Action_None` | 69 | 210 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 29 | 35 | 7 | inferred_complete_timeline |
| `Action_None` | 38 | 68 | 31 | inferred_complete_timeline |
| `Action_None` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_None` | 82 | 86 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 39 | 20 | inferred_complete_timeline |
| `Action_None` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_None` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_None` | 63 | 125 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 39 | 20 | inferred_complete_timeline |
| `Action_None` | 43 | 68 | 26 | inferred_complete_timeline |
| `Action_None` | 70 | 210 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 36 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 19–44 | 26 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 20–96 | 61 | 4 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 24–76 | 53 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 53–87 | 33 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 60–65 | 6 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 67–210 | 143 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 77–210 | 131 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 81–119 | 39 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 91–210 | 119 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 92–198 | 104 | 5 | Undefined position; Undefined team |
| `25` | `42` | Position_Unknown | Team_Unknown | 178–210 | 11 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [20–35], lower_priority='Action_RunBlock' annotated_start=26, effective_Action_RunBlock_start=36.
- ⚠️ Action 'Action_RunBlock' range [26-64] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-201] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-36] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-92] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [26-40] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [44-99] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-39] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-56] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-22] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-100] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-188] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [26-34] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [36-63] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-81] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-48] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-63] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-39] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-32] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-26] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-40] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-177] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-18] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [36-42] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [44-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-35] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-68] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [26-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-44] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-42] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-82] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-65] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-119] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-113] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-139] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [166-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '25' has 1 frames without a visible bounding box.
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

</details>