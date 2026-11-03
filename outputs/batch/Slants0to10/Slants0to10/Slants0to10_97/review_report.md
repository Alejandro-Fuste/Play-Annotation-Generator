# Play-Annotation-Generator Annotation Review — Slants0to10_97

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_97`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_RunSlantRoute` | WR4 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_BallCarry` | WR4 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `17` | 3 | START | 3 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 3 | START | 3 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 3 | START | 3 | 34 |
| ✅ EXACT | `Action_PassBlock` | C | `21` | `21` | 3 | START | 3 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `5` | `5` | 3 | START | 3 | 112 |
| ✅ EXACT | `Action_RunSlantRoute` | WR4 | `0` | `0` | 3 | START | 3 | 83 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 5 | END | 5 | 5 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 50 | START | 50 | 58 |
| ✅ EXACT | `Action_BallCarry` | WR4 | `0` | `0` | 85 | START | 85 | 180 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 5 | 1 | inferred_complete_timeline |
| `Action_None` | 6 | 49 | 44 | inferred_complete_timeline |
| `Action_ThrowPass` | 50 | 58 | 9 | inferred_complete_timeline |
| `Action_None` | 59 | 129 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 119 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 131 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 3 | 83 | 81 | inferred_complete_timeline |
| `Action_None` | 84 | 84 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 180 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 32 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 45 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 61 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 75 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 152 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 45 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 78 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 180 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 164 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 34 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 147 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 149 | 180 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 112 | 110 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 133 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 97 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 133 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 149 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 180 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 141 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 149 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 156 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 133 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 143 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 160 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 129 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 133 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 75 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 96 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 180 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 22–176 | 151 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 39–41 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 73–89 | 16 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 90–102 | 6 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 98–118 | 12 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 129–154 | 26 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 140–166 | 27 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 142–168 | 7 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 153–155 | 3 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 156–163 | 8 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 164–172 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (4 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 73 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_BallCarry' range [85-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-112] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [130-133] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-60] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-143] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-131] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-97] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-133] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-75] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-141] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-45] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-45] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-60] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-147] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [149-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-164] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-29] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-35] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-176] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-41] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-76] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-89] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-93] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-104] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-118] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-166] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-155] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-163] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-168] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-172] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>