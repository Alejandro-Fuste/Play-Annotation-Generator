# Play-Annotation-Generator Annotation Review — Slants0to10_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_83`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 10 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `13` | 2 | START | 2 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `15` | `15` | 2 | START | 2 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 2 | START | 2 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 2 | START | 2 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 2 | START | 2 | 7 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `5` | `5` | 4 | START | 4 | 66 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 11 | END | 11 | 11 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 38 | START | 38 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `5` | `5` | 81 | START | 81 | 102 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 11 | 1 | inferred_complete_timeline |
| `Action_None` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_ThrowPass` | 38 | 46 | 9 | inferred_complete_timeline |
| `Action_None` | 47 | 64 | 18 | inferred_complete_timeline |
| `Action_None` | 68 | 70 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 4 | 66 | 63 | inferred_complete_timeline |
| `Action_None` | 67 | 80 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 81 | 102 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 208 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 225 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 269 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 181 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 190 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 224 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 238 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 251 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 261 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 269 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 16 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 32 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 63 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 82 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–28
- **Visible Samples:** 15

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 7 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 28 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 15 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 63 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 78 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 84 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 27 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 48 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 38 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 61 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 75 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 95 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 157 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 61 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 157 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 179 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 269 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 140 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 165 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 228 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 123 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB6 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 135 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 178 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 269 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–61 | 59 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 27–35 | 9 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 47–98 | 16 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 59–85 | 4 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 82–90 | 9 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 84–95 | 12 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 87–105 | 14 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 94–165 | 11 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 124–201 | 61 | 4 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 135–138 | 4 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 139–141 | 3 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 159–269 | 109 | 3 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 160–244 | 62 | 9 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 164–167 | 4 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 166–269 | 65 | 2 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 215–216 | 2 | 1 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 217–269 | 53 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 92 |
| Track-related warning | 2 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 84: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 84: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-181] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-190] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-224] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-238] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-251] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-193] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-208] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-225] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-269] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-95] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-179] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunSlantRoute' range [4-66] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [81-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-228] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-64] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-38] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-123] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-27] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-48] for track '15' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-118] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-178] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-269] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-140] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-16] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-32] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-15] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-63] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-7] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-35] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-98] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-90] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-95] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-95] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-105] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-131] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-176] for track '29' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-201] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-138] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-141] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-179] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-184] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-163] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-171] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-181] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-196] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-209] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-230] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-244] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-167] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-211] for track '36' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-216] for track '38' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>