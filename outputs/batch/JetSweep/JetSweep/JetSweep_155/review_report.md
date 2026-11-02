# Play-Annotation-Generator Annotation Review — JetSweep_155

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_155`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 91
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `2` | `1` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 22 | START | 22 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 22 | START | 22 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 22 | START | 22 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 22 | START | 22 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 22 | START | 22 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 22 | START | 22 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 22 | START | 22 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 22 | START | 22 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 22 | START | 22 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 22 | START | 22 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 22 | START | 22 | 60 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `2` | `1` | 34 | START | 34 | 84 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 61 | START | 61 | 73 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `12` | 63 | START | 63 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `17` | 63 | START | 63 | 92 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `19` | `18` | 63 | START | 63 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 63 | START | 74 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 63 | START | 63 | 115 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 73 | END | 61 | 73 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 77 | START | 77 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `2` | `1` | 85 | START | 85 | 198 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `21` | `20` | 90 | START | 90 | 115 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 115 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 22–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_SnapReceive` | 61 | 73 | 13 | inferred_complete_timeline |
| `Action_None` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_Toss` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_None` | 85 | 239 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 22–239
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 95 | 35 | inferred_complete_timeline |
| `Action_None` | 102 | 164 | 63 | inferred_complete_timeline |
| `Action_None` | 167 | 174 | 8 | inferred_complete_timeline |
| `Action_None` | 177 | 239 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 22–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 239 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 22–217
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 33 | 12 | inferred_complete_timeline |
| `Action_JetMotion` | 34 | 84 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 198 | 114 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 209 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 211 | 217 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 22–239
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 154 | 94 | inferred_complete_timeline |
| `Action_None` | 163 | 209 | 47 | inferred_complete_timeline |
| `Action_None` | 211 | 239 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 22–168
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 150 | 90 | inferred_complete_timeline |
| `Action_None` | 152 | 157 | 6 | inferred_complete_timeline |
| `Action_None` | 161 | 168 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 22–239
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 62 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 107 | 45 | inferred_complete_timeline |
| `Action_None` | 120 | 159 | 40 | inferred_complete_timeline |
| `Action_None` | 170 | 239 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 22–239
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 62 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 112 | 50 | inferred_complete_timeline |
| `Action_None` | 116 | 164 | 49 | inferred_complete_timeline |
| `Action_None` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_None` | 175 | 178 | 4 | inferred_complete_timeline |
| `Action_None` | 189 | 205 | 17 | inferred_complete_timeline |
| `Action_None` | 207 | 239 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 22–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_BallSnap` | 61 | 73 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 86 | 13 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 90 | 115 | 26 | inferred_complete_timeline |
| `Action_None` | 116 | 205 | 90 | inferred_complete_timeline |
| `Action_None` | 207 | 239 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 22–239
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 62 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 115 | 53 | inferred_complete_timeline |
| `Action_None` | 116 | 129 | 14 | inferred_complete_timeline |
| `Action_None` | 132 | 145 | 14 | inferred_complete_timeline |
| `Action_None` | 147 | 172 | 26 | inferred_complete_timeline |
| `Action_None` | 176 | 183 | 8 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 193 | 202 | 10 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 239 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 22–239
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 62 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 92 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 115 | 17 | inferred_complete_timeline |
| `Action_None` | 116 | 156 | 41 | inferred_complete_timeline |
| `Action_None` | 170 | 191 | 22 | inferred_complete_timeline |
| `Action_None` | 193 | 202 | 10 | inferred_complete_timeline |
| `Action_None` | 206 | 239 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 22–160
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 131 | 71 | inferred_complete_timeline |
| `Action_None` | 133 | 160 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 22–154
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 154 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 22–154
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 125 | 65 | inferred_complete_timeline |
| `Action_None` | 129 | 154 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 22–239
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 86 | 26 | inferred_complete_timeline |
| `Action_None` | 88 | 140 | 53 | inferred_complete_timeline |
| `Action_None` | 143 | 156 | 14 | inferred_complete_timeline |
| `Action_None` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_None` | 169 | 182 | 14 | inferred_complete_timeline |
| `Action_None` | 185 | 239 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 22–239
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 209 | 149 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 233 | 19 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 22–238
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 230 | 170 | inferred_complete_timeline |
| `Action_None` | 236 | 238 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 22–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 239 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 22–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 161 | 101 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_None` | 171 | 239 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 22–228
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 222 | 162 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 22–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 239 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 22–238
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 209 | 149 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 232 | 18 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 174–239 | 61 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 186–234 | 45 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 193–239 | 44 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 199–239 | 41 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 221–239 | 17 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 230–237 | 8 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [61–73], lower_priority='Action_ZoneBlock' annotated_start=63, effective_Action_ZoneBlock_start=74.
- ⚠️ Action 'Action_None' range [61-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-209] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-198] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-209] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [211-217] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-168] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-131] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-125] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-222] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-230] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-209] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-233] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-209] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-232] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-239] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-156] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-202] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-164] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-205] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-154] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-86] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-205] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-227] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-239] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-237] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '29' has 1 frames without a visible bounding box.
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