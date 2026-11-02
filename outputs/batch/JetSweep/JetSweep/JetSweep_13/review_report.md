# Play-Annotation-Generator Annotation Review — JetSweep_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_13`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 29
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `5` | `4` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Toss` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `5` | `4` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `15` | `14` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `15` | `14` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `21` | `20` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `22` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `4` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 50 |
| ✅ EXACT | `Action_JetMotion` | WR | `5` | `4` | 51 | START | 51 | 101 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 78 | START | 78 | 94 |
| ✅ EXACT | `Action_LeadBlock` | TE | `2` | `1` | 83 | START | 83 | 147 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `14` | 83 | START | 83 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 83 | START | 95 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 83 | START | 83 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 83 | START | 83 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 83 | START | 83 | 103 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 94 | END | 78 | 94 |
| ✅ EXACT | `Action_Toss` | QB | `17` | `16` | 97 | START | 97 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `5` | `4` | 102 | START | 102 | 228 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `15` | `14` | 107 | START | 107 | 147 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `15` | `14` | 147 | BOUNDARY | 107 | 147 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `20` | `19` | 147 | BOUNDARY | 83 | 147 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `20` | `19` | 147 | BOUNDARY | 83 | 147 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `21` | `20` | 147 | BOUNDARY | N/A | 147 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `22` | `21` | 147 | BOUNDARY | N/A | 147 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_SnapReceive` | 78 | 94 | 17 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_Toss` | 97 | 101 | 5 | inferred_complete_timeline |
| `Action_None` | 102 | 122 | 21 | inferred_complete_timeline |
| `Action_None` | 124 | 148 | 25 | inferred_complete_timeline |
| `Action_None` | 157 | 169 | 13 | inferred_complete_timeline |
| `Action_None` | 172 | 196 | 25 | inferred_complete_timeline |
| `Action_None` | 198 | 240 | 43 | inferred_complete_timeline |
| `Action_None` | 242 | 260 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 116 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 127 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 252 | 175 | inferred_complete_timeline |
| `Action_None` | 254 | 269 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_JetMotion` | 51 | 101 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 102 | 228 | 127 | inferred_complete_timeline |
| `Action_BallCarry` | 230 | 233 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_LeadBlock` | 83 | 147 | 65 | inferred_complete_timeline |
| `Action_None` | 148 | 173 | 26 | inferred_complete_timeline |
| `Action_None` | 179 | 269 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 147 | 65 | inferred_complete_timeline |
| `Action_None` | 148 | 165 | 18 | inferred_complete_timeline |
| `Action_None` | 170 | 173 | 4 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 94 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_BallSnap` | 78 | 94 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 105 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 82 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 103 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 106 | 24 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 107 | 147 | 41 | inferred_complete_timeline |
| `Action_None` | 148 | 156 | 9 | inferred_complete_timeline |
| `Action_None` | 161 | 198 | 38 | inferred_complete_timeline |
| `Action_None` | 214 | 216 | 3 | inferred_complete_timeline |
| `Action_None` | 219 | 259 | 41 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 218 | 141 | inferred_complete_timeline |
| `Action_None` | 222 | 234 | 13 | inferred_complete_timeline |
| `Action_None` | 237 | 265 | 29 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 190 | 113 | inferred_complete_timeline |
| `Action_None` | 192 | 198 | 7 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_None` | 208 | 233 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 181 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 126 | 49 | inferred_complete_timeline |
| `Action_None` | 128 | 269 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 145 | 68 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 229 | 76 | inferred_complete_timeline |
| `Action_None` | 244 | 262 | 19 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 269 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 264 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 269 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 227 | 150 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 235 | 158 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 219 | 142 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |
| `Action_None` | 225 | 269 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 57–65 | 9 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 102–256 | 92 | 6 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 120–170 | 49 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 125–138 | 13 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 131–146 | 16 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 152–269 | 95 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 172–269 | 39 | 4 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 193–255 | 38 | 6 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 197–269 | 68 | 2 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 217–246 | 15 | 3 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 253–269 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [78–94], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=95.
- ⚠️ Action 'Action_None' range [78-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-173] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-227] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-252] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-228] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-233] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-229] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-262] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-218] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-265] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-264] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-235] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-259] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-190] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-233] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-122] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-148] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-240] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-260] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-219] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-105] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-165] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-94] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-166] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-249] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-139] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-138] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-166] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-269] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-219] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-246] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-269] for track '33' has 2 frames without a visible bounding box.
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

</details>