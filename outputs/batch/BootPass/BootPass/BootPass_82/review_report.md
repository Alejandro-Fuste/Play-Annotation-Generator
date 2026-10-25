# Play-Annotation-Generator Annotation Review — BootPass_82

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_82`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 1
- **Action Segments:** 81
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `36` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `13` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 50 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 44 | START | 44 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `10` | `10` | 51 | START | 51 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `15` | `15` | 51 | START | 62 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `2` | `2` | 51 | START | 51 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `8` | `8` | 51 | START | 51 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `9` | `9` | 51 | START | 51 | 102 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 61 | END | 44 | 61 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `6` | `6` | 62 | START | 62 | 78 |
| ✅ EXACT | `Action_BootAway` | QB | `6` | `6` | 79 | START | 79 | 118 |
| ✅ EXACT | `Action_ThrowPass` | QB | `6` | `6` | 125 | START | 125 | 138 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `36` | `31` | 174 | START | 174 | 185 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 61 | 18 | inferred_complete_timeline |
| `Action_FakeHandoff` | 62 | 78 | 17 | inferred_complete_timeline |
| `Action_BootAway` | 79 | 118 | 40 | inferred_complete_timeline |
| `Action_None` | 119 | 124 | 6 | inferred_complete_timeline |
| `Action_ThrowPass` | 125 | 138 | 14 | inferred_complete_timeline |
| `Action_None` | 139 | 210 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 138 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 83 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_RunBlock` | 51 | 79 | 29 | inferred_complete_timeline |
| `Action_RunBlock` | 81 | 139 | 59 | inferred_complete_timeline |
| `Action_RunBlock` | 141 | 155 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_RunBlock` | 51 | 75 | 25 | inferred_complete_timeline |
| `Action_RunBlock` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 132 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_BallSnap` | 44 | 61 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 62 | 71 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 73 | 91 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_RunBlock` | 51 | 64 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 66 | 86 | 21 | inferred_complete_timeline |
| `Action_RunBlock` | 91 | 145 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_RunBlock` | 51 | 102 | 52 | inferred_complete_timeline |
| `Action_RunBlock` | 108 | 167 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 56 | 13 | inferred_complete_timeline |
| `Action_None` | 63 | 65 | 3 | inferred_complete_timeline |
| `Action_None` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_None` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_None` | 83 | 110 | 28 | inferred_complete_timeline |
| `Action_None` | 115 | 142 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 62 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 92 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 143 | 100 | inferred_complete_timeline |
| `Action_None` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 85 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 58 | 15 | inferred_complete_timeline |
| `Action_None` | 60 | 139 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 77–107 | 6 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 80–86 | 6 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 89–119 | 31 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 89–210 | 120 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 90–210 | 121 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 96–210 | 115 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 102–168 | 67 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 106–107 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 109–110 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 120–167 | 48 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 125–210 | 86 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 127–175 | 11 | 3 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 132–208 | 77 | 3 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 193–210 | 18 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 196–210 | 15 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 201–206 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | 67 | 67 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [44–61], lower_priority='Action_RunBlock' annotated_start=51, effective_Action_RunBlock_start=62.
- ⚠️ Action 'Action_None' range [44-92] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-85] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [51-79] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [81-139] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [141-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-138] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-143] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [51-64] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [66-86] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [91-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [51-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [108-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [51-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [80-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [88-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [62-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [73-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-62] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-58] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-139] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-119] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-168] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-167] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-208] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '34' has 1 frames without a visible bounding box.
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

</details>