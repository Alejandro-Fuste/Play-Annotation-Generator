# Play-Annotation-Generator Annotation Review — Slants0to10_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_11`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 57
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `16` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `7` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 15 | START | 15 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `11` | `11` | 18 | START | 18 | 71 |
| ✅ EXACT | `Action_PassBlock` | RG | `14` | `14` | 18 | START | 18 | 165 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `17` | `17` | 18 | START | 29 | 176 |
| ✅ EXACT | `Action_PassBlock` | LG | `21` | `21` | 18 | START | 18 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `4` | `4` | 18 | START | 18 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 28 | END | 15 | 28 |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | `1` | `1` | 29 | START | 29 | 87 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 80 | START | 80 | 89 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `1` | `1` | 118 | START | 118 | 269 |

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
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 28 | 14 | inferred_complete_timeline |
| `Action_None` | 29 | 79 | 51 | inferred_complete_timeline |
| `Action_ThrowPass` | 80 | 89 | 10 | inferred_complete_timeline |
| `Action_None` | 90 | 93 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 118 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 29 | 87 | 59 | inferred_complete_timeline |
| `Action_None` | 88 | 117 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 186 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 179 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 269 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 71 | 54 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 146 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 80 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 15 | 28 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 176 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 165 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 88 | 71 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 145 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 81 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 58 | 44 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_None` | 96 | 147 | 52 | inferred_complete_timeline |
| `Action_None` | 149 | 154 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 60 | 46 | inferred_complete_timeline |
| `Action_None` | 66 | 72 | 7 | inferred_complete_timeline |
| `Action_None` | 76 | 205 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 170 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 243 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 59 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 269 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 133 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 69 | 55 | inferred_complete_timeline |
| `Action_None` | 72 | 155 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 202 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 225 | 211 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 76–148 | 70 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 87–131 | 45 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 94–178 | 85 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 109–168 | 60 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 119–123 | 5 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 124–125 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 132–269 | 136 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 235–269 | 35 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `17` (C): Annotated start 18 != Inferred start 29
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [15–28], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=29.
- ⚠️ Action 'Action_None' range [15-58] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-147] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-243] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-88] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-145] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-118] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-59] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-170] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-202] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-71] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-165] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-155] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-60] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-72] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-205] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-168] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '28' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>