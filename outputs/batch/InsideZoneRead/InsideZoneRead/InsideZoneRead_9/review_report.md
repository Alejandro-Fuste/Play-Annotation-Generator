# Play-Annotation-Generator Annotation Review — InsideZoneRead_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_9`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | WR1 | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `23` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 2 | START | 2 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 2 | START | 2 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 2 | START | 2 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 2 | START | 2 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 2 | START | 2 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 2 | START | 2 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 2 | START | 2 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 2 | START | 2 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 2 | START | 2 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 2 | START | 2 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 2 | START | 2 | 116 |
| ✅ EXACT | `Action_BallSnap` | WR1 | `5` | `4` | 115 | START | 115 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `16` | `15` | 117 | START | 117 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `16` | 117 | START | 117 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 117 | START | 117 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 117 | START | 117 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `8` | 117 | START | 117 | 140 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 126 | END | 115 | 126 |
| ✅ EXACT | `Action_ReadDefender` | QB | `19` | `18` | 130 | START | 130 | 133 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `18` | 134 | START | 134 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | `23` | `22` | 144 | START | 150 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `22` | `21` | 158 | START | 200 | 204 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 200 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 2–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_SnapReceive` | 115 | 126 | 12 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 134 | 157 | 24 | inferred_complete_timeline |
| `Action_None` | 158 | 180 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 2–212
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 134 | 133 | inferred_complete_timeline |
| `Action_BallCarry` | 200 | 204 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 209 | 212 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 2–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_BallSnap` | 115 | 126 | 12 | inferred_complete_timeline |
| `Action_None` | 127 | 246 | 120 | inferred_complete_timeline |
| `Action_None` | 248 | 269 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 2–234
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 216 | 102 | inferred_complete_timeline |
| `Action_None` | 218 | 234 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 2–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 243 | 129 | inferred_complete_timeline |
| `Action_None` | 248 | 269 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 2–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 269 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 2–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 116 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 200 | 84 | inferred_complete_timeline |
| `Action_None` | 201 | 213 | 13 | inferred_complete_timeline |
| `Action_None` | 216 | 269 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 2–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 116 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 145 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 166 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 200 | 15 | inferred_complete_timeline |
| `Action_None` | 201 | 269 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 2–269
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 116 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 140 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 162 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 176 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 200 | 18 | inferred_complete_timeline |
| `Action_None` | 201 | 269 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 2–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 116 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 146 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 170 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 200 | 15 | inferred_complete_timeline |
| `Action_None` | 201 | 213 | 13 | inferred_complete_timeline |
| `Action_None` | 215 | 226 | 12 | inferred_complete_timeline |
| `Action_None` | 228 | 269 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 2–269
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 116 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 140 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 155 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 162 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 200 | 25 | inferred_complete_timeline |
| `Action_None` | 201 | 233 | 33 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 269 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 2–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 177 | 63 | inferred_complete_timeline |
| `Action_None` | 180 | 269 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 2–162
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 146 | 32 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 162 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 2–143
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 143 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 2–269
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 170 | 56 | inferred_complete_timeline |
| `Action_None` | 172 | 202 | 31 | inferred_complete_timeline |
| `Action_None` | 205 | 213 | 9 | inferred_complete_timeline |
| `Action_None` | 234 | 269 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 2–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 240 | 126 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 258 | 9 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 2–240
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 221 | 107 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 235 | 7 | inferred_complete_timeline |
| `Action_None` | 238 | 240 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 2–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 242 | 128 | inferred_complete_timeline |
| `Action_None` | 245 | 263 | 19 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 2–243
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 243 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 269 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 2–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 269 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 114 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 269 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 150–269 | 83 | 10 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 160–269 | 109 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 191–214 | 24 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 204–212 | 8 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 227–269 | 43 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 248–269 | 22 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 253–269 | 11 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (8 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (6 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `23` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 63 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [115-243] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-234] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-243] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-213] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-140] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [152-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-181] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-242] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-263] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-177] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-240] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-258] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-213] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-140] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-162] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-233] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-145] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [171-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-170] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-213] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-226] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [200-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [209-212] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [150-166] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [171-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-215] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-171] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-269] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-214] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '28' has 1 frames without a visible bounding box.
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