# Play-Annotation-Generator Annotation Review — InsideZoneRead_133

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_133`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 124
- **Validation Warnings:** 105
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 3 | START | 3 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 3 | START | 3 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 3 | START | 3 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 3 | START | 3 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 3 | START | 3 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 3 | START | 3 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 3 | START | 3 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 3 | START | 3 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 3 | START | 3 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 3 | START | 3 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 3 | START | 3 | 109 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 107 | START | 107 | 122 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `16` | `15` | 110 | START | 110 | 184 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `19` | `18` | 110 | START | 110 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 110 | START | 123 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 110 | START | 110 | 159 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 110 | START | 110 | 173 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 122 | END | 107 | 122 |
| ✅ EXACT | `Action_ReadDefender` | QB | `14` | `13` | 126 | START | 126 | 137 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `21` | `20` | 130 | START | 130 | 184 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 138 | START | 138 | 145 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `10` | `9` | 146 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 184 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_SnapReceive` | 107 | 122 | 16 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 126 | 137 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 138 | 145 | 8 | inferred_complete_timeline |
| `Action_None` | 146 | 269 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 3–134
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 134 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 269 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 269 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 3–194
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 156 | 50 | inferred_complete_timeline |
| `Action_None` | 162 | 173 | 12 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 194 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–258
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 220 | 114 | inferred_complete_timeline |
| `Action_None` | 222 | 231 | 10 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 247 | 9 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 109 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 184 | 75 | inferred_complete_timeline |
| `Action_None` | 185 | 206 | 22 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 257 | 24 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 3–222
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 109 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 184 | 75 | inferred_complete_timeline |
| `Action_None` | 185 | 218 | 34 | inferred_complete_timeline |
| `Action_None` | 220 | 222 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 3–212
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_BallSnap` | 107 | 122 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 129 | 7 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 130 | 184 | 55 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 212 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 3–204
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 109 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 159 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 165 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 182 | 13 | inferred_complete_timeline |
| `Action_None` | 192 | 197 | 6 | inferred_complete_timeline |
| `Action_None` | 200 | 204 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 3–250
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 109 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 173 | 64 | inferred_complete_timeline |
| `Action_None` | 206 | 209 | 4 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 220 | 6 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 237 | 243 | 7 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 188 | 82 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 215 | 9 | inferred_complete_timeline |
| `Action_None` | 219 | 232 | 14 | inferred_complete_timeline |
| `Action_None` | 234 | 237 | 4 | inferred_complete_timeline |
| `Action_None` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_None` | 244 | 247 | 4 | inferred_complete_timeline |
| `Action_None` | 249 | 266 | 18 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–194
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 188 | 82 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–257
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 176 | 70 | inferred_complete_timeline |
| `Action_None` | 182 | 253 | 72 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 3–260
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 180 | 74 | inferred_complete_timeline |
| `Action_None` | 210 | 220 | 11 | inferred_complete_timeline |
| `Action_None` | 222 | 226 | 5 | inferred_complete_timeline |
| `Action_None` | 244 | 254 | 11 | inferred_complete_timeline |
| `Action_None` | 256 | 260 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 247 | 141 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 162 | 56 | inferred_complete_timeline |
| `Action_None` | 167 | 170 | 4 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 180 | 5 | inferred_complete_timeline |
| `Action_None` | 206 | 215 | 10 | inferred_complete_timeline |
| `Action_None` | 218 | 232 | 15 | inferred_complete_timeline |
| `Action_None` | 234 | 269 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 269 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–220
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 220 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 236 | 130 | inferred_complete_timeline |
| `Action_None` | 239 | 264 | 26 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 269 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 3–243
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 107 | 243 | 137 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 94–95 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 139–264 | 110 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 147–153 | 7 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 211–261 | 19 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 233–269 | 24 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 235–269 | 35 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 244–269 | 10 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 248–269 | 17 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 257–264 | 8 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 262–269 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `10` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '9' has invalid range: start=146, end=134. Clamping end to start.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [107–122], lower_priority='Action_ZoneBlock' annotated_start=110, effective_Action_ZoneBlock_start=123.
- ⚠️ Action 'Action_None' range [107-220] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-247] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-220] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-173] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-243] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-162] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-188] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-264] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-247] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-176] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-253] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-188] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-215] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-232] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-266] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-206] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-257] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-243] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-218] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-180] for track '19' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-220] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-254] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [130-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [170-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-220] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-244] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-264] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-249] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-243] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-263] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-264] for track '30' has 2 frames without a visible bounding box.
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

</details>