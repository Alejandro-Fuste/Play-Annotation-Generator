# Play-Annotation-Generator Annotation Review — JetSweep_157

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_157`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Position_Unknown | Team_Unknown | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Toss` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `17` | `16` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_JetMotion` | WR3 | `17` | `16` | 0 | START | 0 | 80 |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Position_Unknown | `17` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 56 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 57 | START | 57 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `2` | `1` | 59 | START | 59 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `9` | 59 | START | 59 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `14` | 59 | START | 59 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 59 | START | 59 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 59 | START | 59 | 120 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `22` | `21` | 59 | START | 72 | 83 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 71 | END | 57 | 71 |
| ✅ EXACT | `Action_Toss` | QB | `20` | `19` | 74 | START | 74 | 80 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `17` | `16` | 81 | START | 81 | 155 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `22` | `21` | 84 | START | 84 | 164 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 164 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 71 | 15 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_Toss` | 74 | 80 | 7 | inferred_complete_timeline |
| `Action_None` | 81 | 269 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_LeadBlock` | 59 | 118 | 60 | inferred_complete_timeline |
| `Action_LeadBlock` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_LeadBlock` | 143 | 164 | 22 | inferred_complete_timeline |
| `Action_None` | 165 | 269 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 161 | 105 | inferred_complete_timeline |
| `Action_None` | 163 | 208 | 46 | inferred_complete_timeline |
| `Action_None` | 231 | 269 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_BallCarry` | 81 | 155 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 156 | 100 | inferred_complete_timeline |
| `Action_None` | 160 | 269 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 86 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 120 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 127 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 139 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 164 | 24 | inferred_complete_timeline |
| `Action_None` | 165 | 269 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 120 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 164 | 21 | inferred_complete_timeline |
| `Action_None` | 165 | 269 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 57 | 71 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 83 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 84 | 164 | 81 | inferred_complete_timeline |
| `Action_None` | 165 | 178 | 14 | inferred_complete_timeline |
| `Action_None` | 180 | 191 | 12 | inferred_complete_timeline |
| `Action_None` | 194 | 204 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 95 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 101 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 99 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 134 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 164 | 26 | inferred_complete_timeline |
| `Action_None` | 165 | 269 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 91 | 35 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 115 | 11 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 120 | 64 | inferred_complete_timeline |
| `Action_None` | 123 | 134 | 12 | inferred_complete_timeline |
| `Action_None` | 141 | 151 | 11 | inferred_complete_timeline |
| `Action_None` | 153 | 269 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 120 | 64 | inferred_complete_timeline |
| `Action_None` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_None` | 135 | 158 | 24 | inferred_complete_timeline |
| `Action_None` | 160 | 206 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 146 | 90 | inferred_complete_timeline |
| `Action_None` | 149 | 156 | 8 | inferred_complete_timeline |
| `Action_None` | 160 | 204 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 177 | 121 | inferred_complete_timeline |
| `Action_None` | 180 | 191 | 12 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 211 | 216 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 191 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 205 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 239 | 183 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 258 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 269 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 269 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 204 | 148 | inferred_complete_timeline |
| `Action_None` | 239 | 269 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–239 | 236 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 90–201 | 44 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 97–101 | 5 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 112–269 | 130 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 130–132 | 3 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 144–269 | 75 | 6 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 243–248 | 6 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 252–269 | 12 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `22` (C): Annotated start 59 != Inferred start 72

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 316: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '1' (RB) duration 106 frames exceeds threshold 90 frames [start=59, end=164].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 106 frames exceeds threshold 90 frames [start=59, end=164].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 106 frames exceeds threshold 90 frames [start=59, end=164].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 106 frames exceeds threshold 90 frames [start=59, end=164].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [57–71], lower_priority='Action_ZoneBlock' annotated_start=59, effective_Action_ZoneBlock_start=72.
- ⚠️ Action 'Action_None' range [57-204] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-269] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [59-118] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [127-128] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-146] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-156] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-204] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-177] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-91] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-115] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-205] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-156] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-239] for track '8' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-258] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-86] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-133] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-139] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-269] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-161] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-208] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-151] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-133] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-158] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-206] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-269] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [81-155] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-233] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-99] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-178] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-191] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-204] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-192] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-191] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>