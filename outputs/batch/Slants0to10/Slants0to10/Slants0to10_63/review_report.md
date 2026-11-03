# Play-Annotation-Generator Annotation Review — Slants0to10_63

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_63`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `17` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 12 | START | 12 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 15 | START | 27 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 15 | START | 15 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 15 | START | 15 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 15 | START | 15 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 15 | START | 15 | 40 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 26 | END | 12 | 26 |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | `2` | `2` | 29 | START | 29 | 80 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 66 | START | 66 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `2` | `2` | 108 | START | 108 | 167 |

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
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 12 | 26 | 15 | inferred_complete_timeline |
| `Action_None` | 27 | 65 | 39 | inferred_complete_timeline |
| `Action_ThrowPass` | 66 | 76 | 11 | inferred_complete_timeline |
| `Action_None` | 77 | 151 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 103 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 29 | 80 | 52 | inferred_complete_timeline |
| `Action_None` | 81 | 107 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 108 | 167 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 178 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 190 | 210 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 210 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 48 | 37 | inferred_complete_timeline |
| `Action_None` | 51 | 210 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 210 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 47 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 69 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 114 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 120 | 153 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 69 | 55 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 104 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 154 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–39
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 12 | 26 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 36 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 39 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 40 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 47 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 68 | 54 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 107 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 109 | 118 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 159 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 48 | 37 | inferred_complete_timeline |
| `Action_None` | 58 | 69 | 12 | inferred_complete_timeline |
| `Action_None` | 75 | 106 | 32 | inferred_complete_timeline |
| `Action_None` | 110 | 146 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 69 | 58 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 104 | 13 | inferred_complete_timeline |
| `Action_None` | 112 | 185 | 74 | inferred_complete_timeline |
| `Action_None` | 187 | 206 | 20 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 45 | 34 | inferred_complete_timeline |
| `Action_None` | 47 | 55 | 9 | inferred_complete_timeline |
| `Action_None` | 58 | 69 | 12 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_None` | 89 | 110 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 181 | 170 | inferred_complete_timeline |
| `Action_None` | 188 | 210 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 171 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 87 | 76 | inferred_complete_timeline |
| `Action_None` | 92 | 120 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 179 | 168 | inferred_complete_timeline |
| `Action_None` | 181 | 201 | 21 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 169 | 158 | inferred_complete_timeline |
| `Action_None` | 171 | 210 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 168 | 157 | inferred_complete_timeline |
| `Action_None` | 170 | 210 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 210 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 159 | 148 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 31–32 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 54–124 | 44 | 7 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 59–69 | 11 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 65–68 | 4 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 97–141 | 45 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 131–132 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 177–210 | 34 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 198–210 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [12–26], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=27.
- ⚠️ Action 'Action_None' range [12-171] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-103] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [108-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-178] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-181] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-201] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-69] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-206] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-48] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-69] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-106] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-45] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-55] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-69] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-110] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-87] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [66-76] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 77, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [77-151] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-169] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-36] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-69] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-154] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-48] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-68] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-107] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [109-118] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-159] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-51] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-69] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-114] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [120-153] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-32] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-69] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-124] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-69] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '29' has 5 frames without a visible bounding box.
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