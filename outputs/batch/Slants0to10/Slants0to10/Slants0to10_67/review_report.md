# Play-Annotation-Generator Annotation Review — Slants0to10_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_67`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 61
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `10` | `10` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 6 | START | 6 | 20 |
| ✅ EXACT | `Action_PassBlock` | LT | `10` | `10` | 9 | START | 9 | 132 |
| ✅ EXACT | `Action_PassBlock` | LG | `18` | `18` | 9 | START | 9 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 9 | START | 21 | 44 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 9 | START | 9 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `3` | `3` | 9 | START | 9 | 168 |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | `0` | `0` | 15 | START | 15 | 86 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 20 | END | 6 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | `16` | `16` | 57 | START | 57 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `0` | `0` | 106 | START | 106 | 218 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 6 | 20 | 15 | inferred_complete_timeline |
| `Action_None` | 21 | 56 | 36 | inferred_complete_timeline |
| `Action_ThrowPass` | 57 | 68 | 12 | inferred_complete_timeline |
| `Action_ThrowPass` | 71 | 88 | 18 | inferred_complete_timeline |
| `Action_None` | 89 | 96 | 8 | inferred_complete_timeline |
| `Action_None` | 112 | 118 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 46 | 118 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 269 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 125 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 15 | 86 | 72 | inferred_complete_timeline |
| `Action_None` | 87 | 105 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 218 | 113 | inferred_complete_timeline |
| `Action_BallCarry` | 221 | 225 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 234 | 243 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 132 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 132 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 165 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 6 | 20 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 44 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 64 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 109 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 133 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 66 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 168 | 160 | inferred_complete_timeline |
| `Action_PassBlock` | 170 | 219 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 224 | 242 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 255 | 269 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 269 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 129 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 136 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 47 | 264 | 218 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 211 | 206 | inferred_complete_timeline |
| `Action_None` | 213 | 218 | 6 | inferred_complete_timeline |
| `Action_None` | 226 | 244 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 103 | 98 | inferred_complete_timeline |
| `Action_None` | 107 | 205 | 99 | inferred_complete_timeline |
| `Action_None` | 207 | 211 | 5 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 64 | 59 | inferred_complete_timeline |
| `Action_None` | 68 | 74 | 7 | inferred_complete_timeline |
| `Action_None` | 80 | 115 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 203 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 211 | 206 | inferred_complete_timeline |
| `Action_None` | 228 | 269 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 269 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 269 | 264 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 61–62 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 65–172 | 106 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 136–161 | 9 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 262–269 | 7 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF1` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [6–20], lower_priority='Action_PassBlock' annotated_start=9, effective_Action_PassBlock_start=21.
- ⚠️ Action 'Action_BallCarry' range [106-218] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [221-225] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [229-232] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [234-243] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-205] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [170-219] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [224-242] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [250-251] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-211] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-218] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-203] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-42] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-264] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-64] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [57-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-211] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-109] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-172] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '26' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>