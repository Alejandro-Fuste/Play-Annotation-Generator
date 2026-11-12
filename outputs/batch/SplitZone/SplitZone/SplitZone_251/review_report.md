# Play-Annotation-Generator Annotation Review — SplitZone_251

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_251`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 136
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 118
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | SAF2 | defense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 91 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 92 | START | 92 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 95 | START | 101 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `20` | 95 | START | 95 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 95 | START | 95 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `5` | 95 | START | 95 | 115 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 100 | END | 92 | 100 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `16` | 113 | START | 113 | 131 |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | SAF2 | `18` | `18` | 129 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `10` | 132 | START | 132 | 135 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 199 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_SnapReceive` | 92 | 100 | 9 | inferred_complete_timeline |
| `Action_None` | 101 | 112 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 113 | 131 | 19 | inferred_complete_timeline |
| `Action_None` | 132 | 155 | 24 | inferred_complete_timeline |
| `Action_None` | 157 | 172 | 16 | inferred_complete_timeline |
| `Action_None` | 211 | 299 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_BallCarry` | 132 | 135 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 138 | 299 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 208 | 117 | inferred_complete_timeline |
| `Action_None` | 210 | 262 | 53 | inferred_complete_timeline |
| `Action_None` | 264 | 299 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 137 | 46 | inferred_complete_timeline |
| `Action_None` | 140 | 161 | 22 | inferred_complete_timeline |
| `Action_None` | 168 | 174 | 7 | inferred_complete_timeline |
| `Action_None` | 182 | 193 | 12 | inferred_complete_timeline |
| `Action_None` | 199 | 231 | 33 | inferred_complete_timeline |
| `Action_None` | 234 | 299 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 162 | 71 | inferred_complete_timeline |
| `Action_None` | 165 | 176 | 12 | inferred_complete_timeline |
| `Action_None` | 186 | 299 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 121 | 30 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_None` | 258 | 281 | 24 | inferred_complete_timeline |
| `Action_None` | 284 | 293 | 10 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 115 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 162 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_BallSnap` | 92 | 100 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 107 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 119 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 124 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 114 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 171 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 115 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 124 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 121 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 127 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 115 | 24 | inferred_complete_timeline |
| `Action_None` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 243 | 37 | inferred_complete_timeline |
| `Action_None` | 258 | 273 | 16 | inferred_complete_timeline |
| `Action_None` | 275 | 299 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 115 | 24 | inferred_complete_timeline |
| `Action_None` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 269 | 93 | inferred_complete_timeline |
| `Action_None` | 272 | 287 | 16 | inferred_complete_timeline |
| `Action_None` | 293 | 297 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 134 | 43 | inferred_complete_timeline |
| `Action_None` | 147 | 150 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 152 | 61 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 201 | 110 | inferred_complete_timeline |
| `Action_None` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 299 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 299 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 299 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 172 | 81 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 293 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–299 | 240 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–138 | 43 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 170–299 | 44 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 202–299 | 98 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 214–299 | 67 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 215–299 | 71 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 252–299 | 43 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 259–269 | 9 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 259–293 | 34 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 261–299 | 35 | 5 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 276–299 | 17 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 285–299 | 14 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 290–299 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `18` (SAF2)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 104 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 504: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '18' has invalid range: start=129, end=114. Clamping end to start.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [92–100], lower_priority='Action_ZoneBlock' annotated_start=95, effective_Action_ZoneBlock_start=101.
- ⚠️ Action 'Action_None' range [92-162] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-176] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-121] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-121] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-281] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-293] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-161] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-193] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-299] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-127] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-121] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-162] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-208] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-262] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-287] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-198] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-229] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-272] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-299] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-243] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-273] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [132-135] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-293] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-152] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-201] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [116-119] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-121] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-114] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [116-121] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [170-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-29] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-273] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-293] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-223] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-289] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-293] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-273] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-293] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-273] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-281] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-299] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-286] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-292] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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