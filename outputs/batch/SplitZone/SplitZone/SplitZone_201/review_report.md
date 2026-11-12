# Play-Annotation-Generator Annotation Review — SplitZone_201

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_201`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `32` | `28` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 9 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 9 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 9 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 9 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 9 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 9 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 9 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 9 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 9 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 9 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 9 | 103 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `32` | `28` | 101 | START | 218 | 218 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `15` | 104 | START | 104 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 104 | START | 104 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `21` | 104 | START | 104 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `7` | 104 | START | 104 | 135 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `8` | 104 | START | 104 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `2` | `2` | 107 | START | 107 | 148 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 114 | END | 101 | 114 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 120 | START | 120 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `16` | 126 | START | 126 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `18` | `18` | 140 | START | 140 | 157 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 337 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 9–269
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_SnapReceive` | 101 | 114 | 14 | inferred_complete_timeline |
| `Action_None` | 115 | 119 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 120 | 125 | 6 | inferred_complete_timeline |
| `Action_None` | 126 | 152 | 27 | inferred_complete_timeline |
| `Action_None` | 154 | 174 | 21 | inferred_complete_timeline |
| `Action_None` | 176 | 180 | 5 | inferred_complete_timeline |
| `Action_None` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_None` | 217 | 269 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 9–147
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 125 | 117 | inferred_complete_timeline |
| `Action_BallCarry` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 138 | 147 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 9–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 101 | 198 | 98 | inferred_complete_timeline |
| `Action_None` | 201 | 255 | 55 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 9–267
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 101 | 143 | 43 | inferred_complete_timeline |
| `Action_None` | 146 | 152 | 7 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_None` | 190 | 203 | 14 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 241 | 26 | inferred_complete_timeline |
| `Action_None` | 245 | 267 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 9–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 9–269
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 106 | 98 | inferred_complete_timeline |
| `Action_SplitBlock` | 107 | 148 | 42 | inferred_complete_timeline |
| `Action_SplitBlock` | 150 | 162 | 13 | inferred_complete_timeline |
| `Action_SplitBlock` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 214 | 269 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 9–269
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 135 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 147 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 225 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 227 | 269 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 9–147
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 147 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 9–269
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 150 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 164 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 170 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 269 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 9–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 134 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 140 | 157 | 18 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 160 | 269 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 9–269
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 143 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 164 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 173 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 180 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 195 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 269 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 9–162
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 101 | 123 | 23 | inferred_complete_timeline |
| `Action_None` | 127 | 157 | 31 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 9–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 9–150
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 101 | 123 | 23 | inferred_complete_timeline |
| `Action_None` | 129 | 133 | 5 | inferred_complete_timeline |
| `Action_None` | 137 | 145 | 9 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–162
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 101 | 150 | 50 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–269
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 101 | 152 | 52 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 225 | 6 | inferred_complete_timeline |
| `Action_None` | 227 | 261 | 35 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 9–269
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 101 | 173 | 73 | inferred_complete_timeline |
| `Action_None` | 176 | 180 | 5 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_None` | 218 | 269 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 9–245
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 101 | 178 | 78 | inferred_complete_timeline |
| `Action_None` | 243 | 245 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 9–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 101 | 203 | 103 | inferred_complete_timeline |
| `Action_None` | 216 | 269 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 9–269 | 261 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 9–36 | 15 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 92–94 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 183–188 | 6 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 183–207 | 24 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 217–269 | 51 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 218–269 | 52 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 218–269 | 51 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 221–269 | 48 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 226–235 | 7 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 227–269 | 36 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 229–269 | 41 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `32` (Position_Unknown): Annotated start 101 != Inferred start 218
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (8 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (5 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `2` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `22` (actor_track_id `22`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 5 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 166 frames exceeds threshold 90 frames [start=104, end=269].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RT) duration 166 frames exceeds threshold 90 frames [start=104, end=269].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '18' (RG) duration 130 frames exceeds threshold 90 frames [start=140, end=269].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 166 frames exceeds threshold 90 frames [start=104, end=269].
- ⚠️ Segment 'Action_BallSnap' for track '28' has invalid range: start=218, end=114. Clamping end to start.
- ⚠️ Action 'Action_None' range [101-143] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-203] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-241] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-267] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [107-148] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [150-162] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [169-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-198] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-255] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-135] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-147] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [216-225] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-147] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-261] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-150] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-157] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-143] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [160-164] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [126-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [138-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-178] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [140-157] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-174] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-269] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-14] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-20] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-36] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-150] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [160-164] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [192-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-94] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-207] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-225] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-225] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-243] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-269] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Action event 'Action_None' has invalid start frame 337. Video range is [0, 269].

</details>