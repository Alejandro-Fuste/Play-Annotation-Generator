# Play-Annotation-Generator Annotation Review — InsideZoneRead_379

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_379`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB1 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | DE1 | defense | `10` | `9` |
| ✅ EXACT | `Action_ReadDefender` | DE1 | defense | `10` | `9` |
| ✅ EXACT | `Action_Keep` | DE1 | defense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | DE1 | defense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `17` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 2 |
| ✅ EXACT | `Action_BallSnap` | LB1 | `15` | `14` | 3 | START | 3 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 6 | START | 6 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `12` | 6 | START | 6 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 6 | START | 6 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 6 | START | 6 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `4` | 6 | START | 6 | 46 |
| ✅ EXACT | `Action_SnapReceive` | DE1 | `10` | `9` | 19 | END | 3 | 19 |
| ✅ EXACT | `Action_ReadDefender` | DE1 | `10` | `9` | 23 | START | 23 | 31 |
| ✅ EXACT | `Action_Keep` | DE1 | `10` | `9` | 32 | START | 32 | 47 |
| ✅ EXACT | `Action_BallCarry` | DE1 | `10` | `9` | 52 | START | 52 | 124 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 81 | BOUNDARY | N/A | N/A |

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
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 266 | 264 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 46 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 216 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 269 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 82 | 80 | inferred_complete_timeline |
| `Action_None` | 84 | 143 | 60 | inferred_complete_timeline |
| `Action_None` | 146 | 153 | 8 | inferred_complete_timeline |
| `Action_None` | 155 | 266 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 146 | 144 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 207 | 16 | inferred_complete_timeline |
| `Action_None` | 209 | 269 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 46 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 81 | 30 | inferred_complete_timeline |
| `Action_None` | 82 | 151 | 70 | inferred_complete_timeline |
| `Action_None` | 155 | 269 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 46 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 81 | 8 | inferred_complete_timeline |
| `Action_None` | 82 | 135 | 54 | inferred_complete_timeline |
| `Action_None` | 138 | 269 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 46 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 81 | 30 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 47 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 81 | 4 | inferred_complete_timeline |
| `Action_None` | 82 | 130 | 49 | inferred_complete_timeline |
| `Action_None` | 143 | 151 | 9 | inferred_complete_timeline |
| `Action_None` | 156 | 249 | 94 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 265 | 12 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 47 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 81 | 30 | inferred_complete_timeline |
| `Action_None` | 82 | 101 | 20 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 19 | 17 | inferred_complete_timeline |
| `Action_None` | 20 | 22 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 23 | 31 | 9 | inferred_complete_timeline |
| `Action_Keep` | 32 | 47 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 52 | 124 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 269 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 47 | 45 | inferred_complete_timeline |
| `Action_None` | 51 | 205 | 155 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 269 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 48 | 46 | inferred_complete_timeline |
| `Action_None` | 51 | 70 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 19 | 17 | inferred_complete_timeline |
| `Action_None` | 20 | 92 | 73 | inferred_complete_timeline |
| `Action_None` | 94 | 171 | 78 | inferred_complete_timeline |
| `Action_None` | 175 | 269 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 148 | 146 | inferred_complete_timeline |
| `Action_None` | 155 | 269 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 269 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 169 | 167 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 227 | 40 | inferred_complete_timeline |
| `Action_None` | 235 | 255 | 21 | inferred_complete_timeline |
| `Action_None` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 195 | 193 | inferred_complete_timeline |
| `Action_None` | 204 | 269 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 241 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 174 | 172 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 205 | 12 | inferred_complete_timeline |
| `Action_None` | 215 | 269 | 55 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 64–269 | 206 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 70–269 | 113 | 3 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 105–134 | 29 | 2 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 108–117 | 5 | 2 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 116–269 | 135 | 9 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 159–269 | 111 | 1 | Undefined position; Undefined team |
| `28` | `45` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `29` | `47` | Position_Unknown | Team_Unknown | 235–269 | 17 | 2 | Undefined position; Undefined team |
| `30` | `51` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |
| `31` | `52` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (9 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 71 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [3-82] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-153] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-46] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-151] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-227] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-255] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-48] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-70] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [32-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [52-124] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-46] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-171] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-269] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-216] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-205] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-266] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-151] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-249] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-265] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-46] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-54] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-135] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-269] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-183] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-130] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-199] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-208] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-227] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-256] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_379'; source metadata written as null.

</details>