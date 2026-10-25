# Play-Annotation-Generator Annotation Review — BootPass_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_21`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 150
- **Validation Warnings:** 148
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 129
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 73 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 63 | START | 63 | 78 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `15` | `15` | 74 | START | 80 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `16` | `16` | 74 | START | 74 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `20` | `20` | 74 | START | 74 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `21` | `21` | 74 | START | 74 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `7` | `7` | 74 | START | 74 | 84 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 78 | END | 63 | 78 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `19` | `19` | 80 | START | 80 | 95 |
| ✅ EXACT | `Action_BootAway` | QB | `19` | `19` | 96 | START | 96 | 139 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 168 | START | 168 | 178 |

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
- **Visible Frames:** 0–230
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_SnapReceive` | 63 | 78 | 16 | inferred_complete_timeline |
| `Action_None` | 79 | 79 | 1 | inferred_complete_timeline |
| `Action_FakeHandoff` | 80 | 95 | 16 | inferred_complete_timeline |
| `Action_BootAway` | 96 | 139 | 44 | inferred_complete_timeline |
| `Action_None` | 140 | 167 | 28 | inferred_complete_timeline |
| `Action_ThrowPass` | 168 | 178 | 11 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_None` | 190 | 198 | 9 | inferred_complete_timeline |
| `Action_None` | 201 | 230 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 120 | 58 | inferred_complete_timeline |
| `Action_None` | 130 | 269 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 269 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 210 | 148 | inferred_complete_timeline |
| `Action_None` | 212 | 215 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 233 | 14 | inferred_complete_timeline |
| `Action_None` | 236 | 248 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 242 | 180 | inferred_complete_timeline |
| `Action_None` | 245 | 269 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 89 | 27 | inferred_complete_timeline |
| `Action_None` | 92 | 96 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_RunBlock` | 74 | 84 | 11 | inferred_complete_timeline |
| `Action_RunBlock` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 102 | 195 | 94 | inferred_complete_timeline |
| `Action_RunBlock` | 201 | 262 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_RunBlock` | 74 | 111 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 119 | 239 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_BallSnap` | 63 | 78 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 80 | 84 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_RunBlock` | 74 | 93 | 20 | inferred_complete_timeline |
| `Action_RunBlock` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 130 | 186 | 57 | inferred_complete_timeline |
| `Action_RunBlock` | 199 | 235 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 237 | 257 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_RunBlock` | 74 | 87 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 102 | 115 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 130 | 138 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 143 | 146 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 149 | 156 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 163 | 188 | 26 | inferred_complete_timeline |
| `Action_RunBlock` | 191 | 213 | 23 | inferred_complete_timeline |
| `Action_RunBlock` | 215 | 221 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 228 | 231 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 233 | 235 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 241 | 245 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 247 | 252 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 96 | 34 | inferred_complete_timeline |
| `Action_None` | 103 | 111 | 9 | inferred_complete_timeline |
| `Action_None` | 127 | 193 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 96 | 34 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 89 | 27 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_None` | 102 | 110 | 9 | inferred_complete_timeline |
| `Action_None` | 130 | 156 | 27 | inferred_complete_timeline |
| `Action_None` | 159 | 184 | 26 | inferred_complete_timeline |
| `Action_None` | 186 | 229 | 44 | inferred_complete_timeline |
| `Action_None` | 232 | 267 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 269 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 190 | 128 | inferred_complete_timeline |
| `Action_None` | 194 | 218 | 25 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 99 | 37 | inferred_complete_timeline |
| `Action_None` | 102 | 110 | 9 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 114 | 52 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 126 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 226 | 164 | inferred_complete_timeline |
| `Action_None` | 228 | 269 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 252 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 160 | 98 | inferred_complete_timeline |
| `Action_None` | 163 | 269 | 107 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–106 | 100 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 0–196 | 181 | 9 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 0–183 | 117 | 8 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 4–79 | 63 | 5 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 38–41 | 4 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 123–269 | 147 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 131–269 | 139 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 133–269 | 132 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 133–248 | 98 | 6 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 142–219 | 19 | 4 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 152–177 | 21 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 204–258 | 34 | 4 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 244–245 | 2 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 248–264 | 17 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 248–261 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_RunBlock` for actor_track_id `15` (C): Annotated start 74 != Inferred start 80
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `16` (13 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (8 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 116 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [63–78], lower_priority='Action_RunBlock' annotated_start=74, effective_Action_RunBlock_start=79.
- ⚠️ Action 'Action_None' range [63-242] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-126] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-233] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-248] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-190] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-218] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-89] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-269] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-114] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [74-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [95-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [102-195] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [201-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-226] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-96] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-99] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-96] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-111] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-193] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [63-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [80-84] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [74-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [102-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [118-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [130-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [143-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [149-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [163-188] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [191-213] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [215-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [228-231] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [233-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [241-245] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [247-252] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-89] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-156] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-267] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-252] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-230] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [74-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [119-239] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [74-93] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [95-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [102-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [106-107] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [118-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [130-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [199-235] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [237-257] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-89] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-18] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-62] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-185] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-62] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-87] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-140] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-183] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-6] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-62] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-79] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-41] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-143] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-156] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-231] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-245] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-177] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-258] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-264] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-261] for track '36' has 1 frames without a visible bounding box.
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

</details>