# Play-Annotation-Generator Annotation Review — JetSweep_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_15`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 27
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | CB | defense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `5` | `4` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `18` | `17` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `19` | `18` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `22` | `21` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `7` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_JetMotion` | WR | `5` | `4` | 0 | START | 0 | 70 |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | CB | `5` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 37 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 38 | START | 38 | 54 |
| ✅ EXACT | `Action_LeadBlock` | TE | `2` | `1` | 40 | START | 40 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `17` | 40 | START | 40 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `18` | 40 | START | 40 | 56 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `19` | 40 | START | 40 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 40 | START | 40 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `7` | `6` | 40 | START | 55 | 59 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 54 | END | 38 | 54 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 61 | START | 61 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `5` | `4` | 71 | START | 71 | 196 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `18` | `17` | 102 | BOUNDARY | N/A | 102 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `19` | `18` | 102 | BOUNDARY | N/A | 102 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `20` | `19` | 102 | BOUNDARY | N/A | 102 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `22` | `21` | 102 | BOUNDARY | N/A | 102 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `7` | `6` | 102 | BOUNDARY | 101 | 102 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 54 | 17 | inferred_complete_timeline |
| `Action_None` | 55 | 60 | 6 | inferred_complete_timeline |
| `Action_Toss` | 61 | 70 | 10 | inferred_complete_timeline |
| `Action_None` | 71 | 210 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 155 | 118 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 170 | 4 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_None` | 179 | 184 | 6 | inferred_complete_timeline |
| `Action_None` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 210 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 196 | 126 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 205 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_LeadBlock` | 40 | 102 | 63 | inferred_complete_timeline |
| `Action_None` | 103 | 176 | 74 | inferred_complete_timeline |
| `Action_None` | 179 | 185 | 7 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 56 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 99 | 19 | inferred_complete_timeline |
| `Action_None` | 103 | 188 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 57 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 57 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_BallSnap` | 38 | 54 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 59 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 99 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 210 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 53 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 99 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 57 | 20 | inferred_complete_timeline |
| `Action_None` | 69 | 71 | 3 | inferred_complete_timeline |
| `Action_None` | 73 | 100 | 28 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 165 | 60 | inferred_complete_timeline |
| `Action_None` | 167 | 187 | 21 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 59 | 22 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 95 | 15 | inferred_complete_timeline |
| `Action_None` | 112 | 115 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 57 | 20 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 78 | 87 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 57 | 20 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 100 | 22 | inferred_complete_timeline |
| `Action_None` | 136 | 162 | 27 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 177 | 140 | inferred_complete_timeline |
| `Action_None` | 179 | 201 | 23 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 177 | 140 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_None` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_None` | 200 | 210 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 190 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 171 | 134 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_None` | 189 | 191 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 210 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 210 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 210 | 173 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–210 | 180 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 79–210 | 101 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 90–99 | 8 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 132–210 | 79 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 135–210 | 76 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 137–162 | 26 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 137–208 | 51 | 6 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 32: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [38–54], lower_priority='Action_ZoneBlock' annotated_start=40, effective_Action_ZoneBlock_start=55.
- ⚠️ Action 'Action_None' range [38-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [40-102] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-176] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-57] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-100] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-196] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-205] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-59] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-99] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-210] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-171] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-190] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-177] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-201] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-177] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-99] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-59] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-57] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-70] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-56] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-99] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-57] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-100] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-99] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-100] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-99] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '29' has 1 frames without a visible bounding box.
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

</details>