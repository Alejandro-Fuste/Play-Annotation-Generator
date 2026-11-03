# Play-Annotation-Generator Annotation Review — StopAndGo_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_5`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 120
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `15` | `15` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_VerticalStem` | WR1 | offense | `3` | `3` |
| ✅ EXACT | `Action_SellStop` | WR1 | offense | `3` | `3` |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 11 | START | 11 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `11` | `11` | 14 | START | 14 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `15` | `15` | 14 | START | 14 | 106 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `19` | `19` | 14 | START | 24 | 245 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 14 | START | 14 | 245 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 14 | START | 14 | 164 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 23 | END | 11 | 23 |
| ✅ EXACT | `Action_VerticalStem` | WR1 | `3` | `3` | 23 | START | 23 | 72 |
| ✅ EXACT | `Action_SellStop` | WR1 | `3` | `3` | 73 | START | 73 | 83 |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | `3` | `3` | 84 | START | 84 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | `16` | `16` | 102 | START | 105 | 106 |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 23 | 13 | inferred_complete_timeline |
| `Action_None` | 24 | 100 | 77 | inferred_complete_timeline |
| `Action_ThrowPass` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_ThrowPass` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 239 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 179 | 169 | inferred_complete_timeline |
| `Action_None` | 182 | 192 | 11 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 237 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_VerticalStem` | 23 | 72 | 50 | inferred_complete_timeline |
| `Action_SellStop` | 73 | 83 | 11 | inferred_complete_timeline |
| `Action_RunGoRoute` | 84 | 134 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 245 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 269 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 245 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 106 | 93 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 112 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 117 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 245 | 232 | inferred_complete_timeline |
| `Action_PassBlock` | 249 | 252 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 23 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 245 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 164 | 151 | inferred_complete_timeline |
| `Action_PassBlock` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 174 | 176 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 182 | 198 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 200 | 232 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 100 | 87 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 109 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 66 | 56 | inferred_complete_timeline |
| `Action_None` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_None` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_None` | 97 | 126 | 30 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 210 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_None` | 147 | 177 | 31 | inferred_complete_timeline |
| `Action_None` | 181 | 190 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 216 | 206 | inferred_complete_timeline |
| `Action_None` | 223 | 245 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 245 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 148 | 138 | inferred_complete_timeline |
| `Action_None` | 151 | 183 | 33 | inferred_complete_timeline |
| `Action_None` | 186 | 194 | 9 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 124 | 114 | inferred_complete_timeline |
| `Action_None` | 126 | 269 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 269 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 240 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 39 | 29 | inferred_complete_timeline |
| `Action_None` | 43 | 55 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 132 | 122 | inferred_complete_timeline |
| `Action_None` | 134 | 269 | 136 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–269 | 269 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 54–245 | 192 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 54–55 | 2 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 69–72 | 4 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 105–243 | 139 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 121–233 | 113 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 122–126 | 5 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 138–141 | 4 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 147–151 | 5 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 153–185 | 31 | 2 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 193–269 | 75 | 3 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 229–249 | 7 | 2 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 246–261 | 16 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 246–249 | 4 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 246–249 | 4 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 247–249 | 3 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 247–249 | 3 | 1 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 250–252 | 3 | 1 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 250–252 | 3 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 253–255 | 3 | 1 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 253–255 | 3 | 1 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 256–269 | 14 | 1 | Undefined position; Undefined team |
| `43` | `49` | Position_Unknown | Team_Unknown | 256–269 | 14 | 1 | Undefined position; Undefined team |
| `44` | `50` | Position_Unknown | Team_Unknown | 258–269 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (3 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `19` (C): Annotated start 14 != Inferred start 24
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 10: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [11–23], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=24.
- ⚠️ Action 'Action_None' range [11-245] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-245] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-39] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-55] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [84-134] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-245] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-66] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-92] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-126] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-124] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [108-109] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-148] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-183] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-194] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-216] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-132] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [108-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [105-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-192] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-237] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-240] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-245] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-245] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [249-252] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-164] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [167-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [174-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [182-198] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [200-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-245] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-243] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-185] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-205] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-261] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>