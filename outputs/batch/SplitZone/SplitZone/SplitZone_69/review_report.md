# Play-Annotation-Generator Annotation Review — SplitZone_69

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_69`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 125
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 104
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_BlockSecondLevel` | DE2 | defense | `5` | `5` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `13` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 4 | START | 5 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 4 | START | 5 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 4 | START | 5 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 4 | START | 5 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 4 | START | 5 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 4 | START | 5 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 4 | START | 5 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `2` | `Group` | 4 | START | 5 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 4 | START | 5 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 4 | START | 5 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 4 | START | 5 | 76 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 77 | START | 77 | 90 |
| ✅ EXACT | `Action_SplitBlock` | HB | `2` | `2` | 79 | START | 79 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `12` | 80 | START | 80 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 80 | START | 91 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `17` | 80 | START | 80 | 105 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 80 | START | 80 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `21` | 80 | START | 80 | 100 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 90 | END | 77 | 90 |
| ✅ EXACT | `Action_BlockSecondLevel` | DE2 | `5` | `5` | 113 | START | 113 | 124 |
| ✅ EXACT | `Action_BallCarry` | QB | `13` | `13` | 115 | START | 115 | 254 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 124 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 5–254
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_SnapReceive` | 77 | 90 | 14 | inferred_complete_timeline |
| `Action_None` | 91 | 114 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 115 | 254 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 5–158
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 103 | 27 | inferred_complete_timeline |
| `Action_None` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 134 | 24 | inferred_complete_timeline |
| `Action_None` | 154 | 158 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 78 | 74 | inferred_complete_timeline |
| `Action_SplitBlock` | 79 | 124 | 46 | inferred_complete_timeline |
| `Action_None` | 125 | 152 | 28 | inferred_complete_timeline |
| `Action_None` | 156 | 269 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 5–118
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 79 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 105 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 118 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 79 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 100 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 124 | 23 | inferred_complete_timeline |
| `Action_None` | 125 | 194 | 70 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 209 | 211 | 3 | inferred_complete_timeline |
| `Action_None` | 216 | 238 | 23 | inferred_complete_timeline |
| `Action_None` | 241 | 269 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 5–157
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_BallSnap` | 77 | 90 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_None` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_None` | 148 | 157 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 79 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 124 | 45 | inferred_complete_timeline |
| `Action_None` | 125 | 137 | 13 | inferred_complete_timeline |
| `Action_None` | 142 | 186 | 45 | inferred_complete_timeline |
| `Action_None` | 191 | 195 | 5 | inferred_complete_timeline |
| `Action_None` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_None` | 209 | 238 | 30 | inferred_complete_timeline |
| `Action_None` | 241 | 269 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 79 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 100 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 109 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 124 | 3 | inferred_complete_timeline |
| `Action_None` | 128 | 140 | 13 | inferred_complete_timeline |
| `Action_None` | 144 | 202 | 59 | inferred_complete_timeline |
| `Action_None` | 208 | 227 | 20 | inferred_complete_timeline |
| `Action_None` | 229 | 238 | 10 | inferred_complete_timeline |
| `Action_None` | 241 | 269 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 195 | 119 | inferred_complete_timeline |
| `Action_None` | 197 | 203 | 7 | inferred_complete_timeline |
| `Action_None` | 205 | 238 | 34 | inferred_complete_timeline |
| `Action_None` | 241 | 269 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 112 | 108 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 113 | 124 | 12 | inferred_complete_timeline |
| `Action_None` | 125 | 205 | 81 | inferred_complete_timeline |
| `Action_None` | 208 | 269 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 133 | 57 | inferred_complete_timeline |
| `Action_None` | 144 | 158 | 15 | inferred_complete_timeline |
| `Action_None` | 176 | 184 | 9 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_None` | 208 | 238 | 31 | inferred_complete_timeline |
| `Action_None` | 241 | 269 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 142 | 66 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 162 | 6 | inferred_complete_timeline |
| `Action_None` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_None` | 170 | 195 | 26 | inferred_complete_timeline |
| `Action_None` | 197 | 269 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–171
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 171 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 152 | 76 | inferred_complete_timeline |
| `Action_None` | 158 | 195 | 38 | inferred_complete_timeline |
| `Action_None` | 197 | 239 | 43 | inferred_complete_timeline |
| `Action_None` | 241 | 269 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 5–176
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 171 | 95 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–259
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 259 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 77 | 163 | 87 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 170 | 195 | 26 | inferred_complete_timeline |
| `Action_None` | 197 | 204 | 8 | inferred_complete_timeline |
| `Action_None` | 206 | 269 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 60–172 | 27 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 64–67 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 167–269 | 95 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 178–269 | 78 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 193–265 | 71 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 193–269 | 65 | 5 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 199–200 | 2 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 210–269 | 60 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 248–268 | 14 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 259–266 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [77–90], lower_priority='Action_ZoneBlock' annotated_start=80, effective_Action_ZoneBlock_start=91.
- ⚠️ Action 'Action_None' range [125-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-133] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-184] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-163] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-205] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-171] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-142] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-195] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-152] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-195] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-239] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-194] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-238] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [115-254] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-157] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-259] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [116-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-195] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-186] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-238] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-202] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-227] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-238] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-72] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-67] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-204] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-269] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-261] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-227] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-266] for track '32' has 3 frames without a visible bounding box.
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

</details>