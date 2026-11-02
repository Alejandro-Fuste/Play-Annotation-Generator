# Play-Annotation-Generator Annotation Review — JetSweep_221

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_221`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `5` | `4` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | WR2 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `20` |
| ❌ MISSING SEGMENT | `Action_Toss` | QB | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 50 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `5` | `4` | 18 | START | 18 | 77 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 49 | START | 49 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | WR2 | `3` | `2` | 51 | START | 51 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `14` | 51 | START | 51 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `15` | 51 | START | 51 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `18` | 51 | START | 51 | 61 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `20` | `19` | 51 | START | 63 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `6` | `5` | 51 | START | 51 | 73 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `20` | 62 | END | 49 | 62 |
| ❌ MISSING SEGMENT | `Action_Toss` | QB | `21` | `20` | 71 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `5` | `4` | 78 | START | 78 | 140 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 137 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 62 | 14 | inferred_complete_timeline |
| `Action_None` | 63 | 70 | 8 | inferred_complete_timeline |
| `Action_None` | 79 | 210 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 30 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_None` | 49 | 49 | 1 | inferred_complete_timeline |
| `Action_None` | 64 | 144 | 81 | inferred_complete_timeline |
| `Action_None` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_JetMotion` | 18 | 77 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 78 | 140 | 63 | inferred_complete_timeline |
| `Action_BallCarry` | 174 | 175 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_LeadBlock` | 51 | 60 | 10 | inferred_complete_timeline |
| `Action_LeadBlock` | 63 | 137 | 75 | inferred_complete_timeline |
| `Action_None` | 138 | 149 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 210 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 73 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 92 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 115 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 137 | 15 | inferred_complete_timeline |
| `Action_None` | 138 | 153 | 16 | inferred_complete_timeline |
| `Action_None` | 155 | 210 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 63 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 137 | 71 | inferred_complete_timeline |
| `Action_None` | 138 | 203 | 66 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_BallSnap` | 49 | 62 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 137 | 75 | inferred_complete_timeline |
| `Action_None` | 138 | 210 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 61 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 67 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 137 | 87 | inferred_complete_timeline |
| `Action_None` | 138 | 186 | 49 | inferred_complete_timeline |
| `Action_None` | 194 | 210 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 77 | 29 | inferred_complete_timeline |
| `Action_None` | 91 | 210 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 130 | 82 | inferred_complete_timeline |
| `Action_None` | 132 | 136 | 5 | inferred_complete_timeline |
| `Action_None` | 139 | 173 | 35 | inferred_complete_timeline |
| `Action_None` | 176 | 178 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 205 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 83 | 35 | inferred_complete_timeline |
| `Action_None` | 85 | 139 | 55 | inferred_complete_timeline |
| `Action_None` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_None` | 162 | 210 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 63 | 15 | inferred_complete_timeline |
| `Action_None` | 67 | 115 | 49 | inferred_complete_timeline |
| `Action_None` | 188 | 210 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 165 | 117 | inferred_complete_timeline |
| `Action_None` | 167 | 210 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 120 | 72 | inferred_complete_timeline |
| `Action_None` | 123 | 144 | 22 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 180 | 16 | inferred_complete_timeline |
| `Action_None` | 184 | 191 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 210 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 137 | 89 | inferred_complete_timeline |
| `Action_None` | 142 | 157 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 145 | 97 | inferred_complete_timeline |
| `Action_None` | 147 | 171 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 200 | 152 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 132 | 84 | inferred_complete_timeline |
| `Action_None` | 135 | 138 | 4 | inferred_complete_timeline |
| `Action_None` | 143 | 145 | 3 | inferred_complete_timeline |
| `Action_None` | 149 | 210 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 80–207 | 127 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 117–210 | 93 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 139–210 | 39 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 145–209 | 59 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 184–210 | 15 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 202–209 | 8 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 204–205 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `20` (C): Annotated start 51 != Inferred start 63
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (4 segments found)
- ❌ Missing segment for action `Action_Toss` on target `21` (QB)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 444: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [49–62], lower_priority='Action_ZoneBlock' annotated_start=51, effective_Action_ZoneBlock_start=63.
- ⚠️ Action 'Action_None' range [49-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-173] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-205] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [51-60] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [63-137] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [78-140] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [174-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-115] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-153] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-200] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-165] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-63] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-115] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-144] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-191] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-145] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-171] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-137] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-157] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-186] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-203] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-67] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-30] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 49, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [49-49] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-139] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-146] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-165] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-178] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-209] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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