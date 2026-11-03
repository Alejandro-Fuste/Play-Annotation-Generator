# Play-Annotation-Generator Annotation Review — Slants0to10_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_43`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | DT1 | defense | `18` | `18` |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | DT1 | defense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 1 | START | 1 | 13 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 4 | START | 4 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 4 | START | 14 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 4 | START | 4 | 8 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 4 | START | 7 | 9 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `8` | `8` | 4 | START | 4 | 47 |
| ✅ EXACT | `Action_SnapReceive` | DT1 | `18` | `18` | 13 | END | 1 | 13 |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | `0` | `0` | 18 | START | 18 | 81 |
| ✅ EXACT | `Action_ThrowPass` | DT1 | `18` | `18` | 46 | START | 46 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `0` | `0` | 83 | START | 83 | 102 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 56 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 18 | 81 | 64 | inferred_complete_timeline |
| `Action_None` | 82 | 82 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 83 | 102 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 182 | 73 | inferred_complete_timeline |
| `Action_BallCarry` | 185 | 195 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 199 | 217 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 239 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 226 | 226 | inferred_complete_timeline |
| `Action_None` | 229 | 234 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 107 | 107 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 158 | 46 | inferred_complete_timeline |
| `Action_None` | 167 | 239 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 150 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 47 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 55 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 36 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 54 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 13 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 57 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 97 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 8 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 26 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 9 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 57 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 163 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 56 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 13 | 13 | inferred_complete_timeline |
| `Action_None` | 14 | 21 | 8 | inferred_complete_timeline |
| `Action_None` | 24 | 45 | 22 | inferred_complete_timeline |
| `Action_ThrowPass` | 46 | 52 | 7 | inferred_complete_timeline |
| `Action_None` | 53 | 55 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 57 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 220 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 75 | 75 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_None` | 82 | 153 | 72 | inferred_complete_timeline |
| `Action_None` | 155 | 239 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 143 | 143 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 151 | 151 | inferred_complete_timeline |
| `Action_None` | 153 | 187 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–55 | 56 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 52–54 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 82–239 | 141 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 82–239 | 151 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 117–239 | 122 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 119–147 | 26 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 119–173 | 55 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 119–221 | 103 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 119–130 | 8 | 3 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 124–132 | 9 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 127–139 | 13 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 173–189 | 13 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 181–185 | 5 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 199–239 | 41 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 218–239 | 22 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 226–239 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 44: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [1–13], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=14.
- ⚠️ Action 'Action_BallCarry' range [83-102] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-107] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-182] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [185-195] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [199-217] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [219-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-226] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-57] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-153] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-56] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-55] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-158] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-56] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-187] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-54] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-57] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-97] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-21] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-8] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-26] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-9] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-163] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-99] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-236] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-215] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-219] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-130] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-221] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-132] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-139] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-189] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>