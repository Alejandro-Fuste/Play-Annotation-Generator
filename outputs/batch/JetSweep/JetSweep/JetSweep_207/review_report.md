# Play-Annotation-Generator Annotation Review — JetSweep_207

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_207`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `10` | `9` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Toss` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 64 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `10` | `9` | 31 | START | 31 | 93 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 65 | START | 65 | 75 |
| ✅ EXACT | `Action_LeadBlock` | TE | `4` | `3` | 66 | START | 66 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `14` | 66 | START | 66 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `16` | 66 | START | 66 | 105 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `19` | 66 | START | 66 | 111 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `22` | `21` | 66 | START | 76 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 66 | START | 66 | 111 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 75 | END | 65 | 75 |
| ✅ EXACT | `Action_Toss` | QB | `5` | `4` | 85 | START | 85 | 93 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `10` | `9` | 94 | START | 94 | 170 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 111 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_SnapReceive` | 65 | 75 | 11 | inferred_complete_timeline |
| `Action_None` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_Toss` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_None` | 94 | 269 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 154 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 163 | 99 | inferred_complete_timeline |
| `Action_None` | 166 | 235 | 70 | inferred_complete_timeline |
| `Action_None` | 238 | 252 | 15 | inferred_complete_timeline |
| `Action_None` | 259 | 267 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_JetMotion` | 31 | 93 | 63 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 170 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 150 | 86 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_None` | 160 | 269 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_LeadBlock` | 66 | 111 | 46 | inferred_complete_timeline |
| `Action_None` | 112 | 204 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 111 | 43 | inferred_complete_timeline |
| `Action_None` | 112 | 120 | 9 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 111 | 46 | inferred_complete_timeline |
| `Action_None` | 112 | 178 | 67 | inferred_complete_timeline |
| `Action_None` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_BallSnap` | 65 | 75 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 111 | 36 | inferred_complete_timeline |
| `Action_None` | 112 | 148 | 37 | inferred_complete_timeline |
| `Action_None` | 152 | 269 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 111 | 46 | inferred_complete_timeline |
| `Action_None` | 112 | 269 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 105 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 111 | 1 | inferred_complete_timeline |
| `Action_None` | 112 | 154 | 43 | inferred_complete_timeline |
| `Action_None` | 170 | 269 | 100 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 91 | 27 | inferred_complete_timeline |
| `Action_None` | 93 | 187 | 95 | inferred_complete_timeline |
| `Action_None` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 269 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 84 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 90 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 112 | 48 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 187 | 66 | inferred_complete_timeline |
| `Action_None` | 191 | 207 | 17 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 217 | 6 | inferred_complete_timeline |
| `Action_None` | 220 | 259 | 40 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 184 | 120 | inferred_complete_timeline |
| `Action_None` | 203 | 231 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 126 | 62 | inferred_complete_timeline |
| `Action_None` | 134 | 157 | 24 | inferred_complete_timeline |
| `Action_None` | 164 | 169 | 6 | inferred_complete_timeline |
| `Action_None` | 178 | 225 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 215 | 151 | inferred_complete_timeline |
| `Action_None` | 221 | 269 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 150 | 86 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 171 | 107 | inferred_complete_timeline |
| `Action_None` | 176 | 183 | 8 | inferred_complete_timeline |
| `Action_None` | 193 | 196 | 4 | inferred_complete_timeline |
| `Action_None` | 203 | 231 | 29 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 171 | 107 | inferred_complete_timeline |
| `Action_None` | 173 | 180 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 126–269 | 127 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 128–132 | 5 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 141–269 | 122 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 176–234 | 58 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 187–269 | 83 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 199–201 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 200–269 | 57 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 204–264 | 52 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 226–228 | 3 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 239–241 | 3 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 249–269 | 21 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `22` (C): Annotated start 66 != Inferred start 76

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [65–75], lower_priority='Action_ZoneBlock' annotated_start=66, effective_Action_ZoneBlock_start=76.
- ⚠️ Action 'Action_None' range [65-154] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-150] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-204] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-269] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-163] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-235] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-252] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-267] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-184] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-231] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-170] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-90] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-259] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-105] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-154] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-171] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-231] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-269] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-234] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-204] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-234] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-246] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-249] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '31' has 1 frames without a visible bounding box.
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