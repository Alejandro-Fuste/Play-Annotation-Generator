# Play-Annotation-Generator Annotation Review — SplitZone_253

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_253`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 146
- **Validation Warnings:** 155
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 129
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 22 | START | 23 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 22 | START | 23 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 22 | START | 23 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 22 | START | 23 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 22 | START | 23 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 22 | START | 23 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 22 | START | 23 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 22 | START | 23 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 22 | START | 23 | 102 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 103 | START | 103 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `14` | 106 | START | 106 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 106 | START | 115 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `20` | 106 | START | 106 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 106 | START | 106 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `3` | `3` | 108 | START | 108 | 134 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 114 | END | 103 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `11` | `11` | 143 | START | 143 | 268 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 232 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 23–352
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_SnapReceive` | 103 | 114 | 12 | inferred_complete_timeline |
| `Action_None` | 115 | 142 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 143 | 268 | 126 | inferred_complete_timeline |
| `Action_BallCarry` | 272 | 301 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 307 | 336 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 338 | 343 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 350 | 352 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 23–124
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 124 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 23–230
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 226 | 124 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 23–146
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 138 | 36 | inferred_complete_timeline |
| `Action_None` | 141 | 146 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 23–138
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 107 | 85 | inferred_complete_timeline |
| `Action_SplitBlock` | 108 | 134 | 27 | inferred_complete_timeline |
| `Action_SplitBlock` | 137 | 138 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 23–204
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 105 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 119 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 124 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 152 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 163 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 177 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 194 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 204 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 23–143
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 105 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 118 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 143 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 23–359
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_BallSnap` | 103 | 114 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 134 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 216 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 221 | 232 | 12 | inferred_complete_timeline |
| `Action_None` | 233 | 359 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 23–127
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 105 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 117 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 127 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 23–143
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 134 | 32 | inferred_complete_timeline |
| `Action_None` | 137 | 143 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 23–209
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 177 | 75 | inferred_complete_timeline |
| `Action_None` | 180 | 197 | 18 | inferred_complete_timeline |
| `Action_None` | 199 | 209 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 23–151
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 134 | 32 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 23–143
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 134 | 32 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 23–206
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 166 | 64 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_None` | 181 | 193 | 13 | inferred_complete_timeline |
| `Action_None` | 203 | 206 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 23–359
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 134 | 32 | inferred_complete_timeline |
| `Action_None` | 181 | 193 | 13 | inferred_complete_timeline |
| `Action_None` | 201 | 328 | 128 | inferred_complete_timeline |
| `Action_None` | 332 | 359 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 23–323
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 291 | 189 | inferred_complete_timeline |
| `Action_None` | 298 | 304 | 7 | inferred_complete_timeline |
| `Action_None` | 311 | 323 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 23–359
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 164 | 62 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 195 | 12 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_None` | 201 | 206 | 6 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 222 | 359 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 23–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 209 | 107 | inferred_complete_timeline |
| `Action_None` | 213 | 217 | 5 | inferred_complete_timeline |
| `Action_None` | 219 | 359 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 23–308
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 191 | 89 | inferred_complete_timeline |
| `Action_None` | 195 | 271 | 77 | inferred_complete_timeline |
| `Action_None` | 273 | 289 | 17 | inferred_complete_timeline |
| `Action_None` | 298 | 301 | 4 | inferred_complete_timeline |
| `Action_None` | 306 | 308 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 23–134
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 134 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 23–315 | 267 | 5 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 23–155 | 128 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 141–152 | 12 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 181–296 | 79 | 5 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 182–359 | 173 | 4 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 182–271 | 87 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 182–317 | 125 | 5 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 194–359 | 158 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 220–359 | 138 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 222–354 | 124 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 224–297 | 74 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 225–284 | 53 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 226–359 | 134 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 226–274 | 46 | 3 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 227–301 | 75 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 237–345 | 95 | 2 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 249–316 | 68 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 269–359 | 80 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (9 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 113 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 508: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 508: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 127 frames exceeds threshold 90 frames [start=106, end=232].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [103–114], lower_priority='Action_ZoneBlock' annotated_start=106, effective_Action_ZoneBlock_start=115.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 99 frames exceeds threshold 90 frames [start=106, end=204].
- ⚠️ Action 'Action_None' range [103-138] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-209] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-126] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-315] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [108-134] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [137-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-226] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-291] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-323] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-164] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-134] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-193] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-328] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [143-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [272-301] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [307-336] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [338-343] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [350-352] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-191] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-271] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-289] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-166] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-193] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [126-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-216] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-209] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [126-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-163] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-204] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-193] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-296] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-199] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-311] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-350] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-194] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-195] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-215] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-309] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-213] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-277] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-323] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-354] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-297] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-231] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-284] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-359] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-235] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-274] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-301] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-329] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-316] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-289] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>