# Play-Annotation-Generator Annotation Review — BootPass_109

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_109`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 160
- **Validation Warnings:** 158
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 141
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `13` | `13` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | DT2 | defense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `22` | `21` |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | Team_Unknown | `34` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunFlatRoute` | CB2 | defense | `3` | `3` |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `34` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `39` | `28` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 37 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | `11` | `11` | 37 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `13` | `13` | 37 | START | 37 | 76 |
| ✅ EXACT | `Action_RunBlock` | LG | `17` | `17` | 37 | START | 37 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `18` | `18` | 37 | START | 37 | 52 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 38 | START | 38 | 45 |
| ✅ EXACT | `Action_SnapReceive` | DT2 | `14` | `14` | 45 | END | 38 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | `22` | `21` | 53 | START | 53 | 59 |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | `34` | `27` | 75 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunFlatRoute` | CB2 | `3` | `3` | 82 | START | 82 | 96 |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | `34` | `27` | 133 | START | 138 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | Position_Unknown | `39` | `28` | 175 | START | 197 | 200 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 78 | 41 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_None` | 94 | 153 | 60 | inferred_complete_timeline |
| `Action_None` | 155 | 168 | 14 | inferred_complete_timeline |
| `Action_None` | 182 | 219 | 38 | inferred_complete_timeline |
| `Action_None` | 224 | 229 | 6 | inferred_complete_timeline |
| `Action_None` | 233 | 269 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 262 | 225 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 100 | 63 | inferred_complete_timeline |
| `Action_None` | 105 | 221 | 117 | inferred_complete_timeline |
| `Action_None` | 245 | 247 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 106 | 69 | inferred_complete_timeline |
| `Action_None` | 109 | 121 | 13 | inferred_complete_timeline |
| `Action_None` | 123 | 172 | 50 | inferred_complete_timeline |
| `Action_None` | 174 | 264 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 79 | 42 | inferred_complete_timeline |
| `Action_None` | 82 | 92 | 11 | inferred_complete_timeline |
| `Action_None` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 240 | 131 | inferred_complete_timeline |
| `Action_None` | 244 | 249 | 6 | inferred_complete_timeline |
| `Action_None` | 251 | 269 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 226 | 189 | inferred_complete_timeline |
| `Action_None` | 235 | 247 | 13 | inferred_complete_timeline |
| `Action_None` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 37 | 76 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 78 | 142 | 65 | inferred_complete_timeline |
| `Action_RunBlock` | 148 | 182 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 37 | 73 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 38 | 45 | 8 | inferred_complete_timeline |
| `Action_None` | 46 | 60 | 15 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 37 | 52 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 57 | 151 | 95 | inferred_complete_timeline |
| `Action_RunBlock` | 169 | 176 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 194 | 232 | 39 | inferred_complete_timeline |
| `Action_RunBlock` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 237 | 251 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 253 | 255 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 262 | 269 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 78 | 41 | inferred_complete_timeline |
| `Action_None` | 83 | 167 | 85 | inferred_complete_timeline |
| `Action_None` | 170 | 177 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 87 | 50 | inferred_complete_timeline |
| `Action_None` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_None` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 113 | 10 | inferred_complete_timeline |
| `Action_None` | 121 | 124 | 4 | inferred_complete_timeline |
| `Action_None` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_None` | 139 | 154 | 16 | inferred_complete_timeline |
| `Action_None` | 160 | 167 | 8 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_None` | 178 | 185 | 8 | inferred_complete_timeline |
| `Action_None` | 188 | 196 | 9 | inferred_complete_timeline |
| `Action_None` | 198 | 201 | 4 | inferred_complete_timeline |
| `Action_None` | 204 | 224 | 21 | inferred_complete_timeline |
| `Action_None` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 246 | 5 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 264 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 45 | 8 | inferred_complete_timeline |
| `Action_None` | 46 | 121 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 144 | 107 | inferred_complete_timeline |
| `Action_None` | 146 | 177 | 32 | inferred_complete_timeline |
| `Action_None` | 182 | 187 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 115 | 78 | inferred_complete_timeline |
| `Action_None` | 121 | 151 | 31 | inferred_complete_timeline |
| `Action_None` | 153 | 191 | 39 | inferred_complete_timeline |
| `Action_None` | 193 | 201 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 211 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 82 | 96 | 15 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 101 | 114 | 14 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 119 | 125 | 7 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 168 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 219 | 182 | inferred_complete_timeline |
| `Action_None` | 224 | 237 | 14 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 265 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 131 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 102 | 65 | inferred_complete_timeline |
| `Action_None` | 104 | 250 | 147 | inferred_complete_timeline |
| `Action_None` | 253 | 267 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–64 | 65 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 6–269 | 235 | 9 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 70–264 | 101 | 9 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 71–135 | 29 | 5 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 105–269 | 165 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 112–269 | 158 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 117–217 | 65 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 138–265 | 127 | 3 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 197–269 | 70 | 5 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 202–260 | 46 | 3 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 225–263 | 38 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 226–269 | 31 | 3 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 238–260 | 21 | 2 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 254–269 | 15 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_RunBlock` on target `11` (C)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (8 segments found)
- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `22` (2 segments found)
- ❌ Missing segment for action `Action_BootAway` on target `27` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_RunFlatRoute` and target `3` (4 segments found)
- ⚠️ `Action_ThrowPass` for actor_track_id `34` (Position_Unknown): Annotated start 133 != Inferred start 138
- ⚠️ Ambiguous match for action `Action_SecureCatch` and target `28` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 126 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 198: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [38–45], lower_priority='Action_RunBlock' annotated_start=37, effective_Action_RunBlock_start=46.
- ⚠️ Segment 'Action_BootAway' for track '27' has invalid range: start=138, end=126. Clamping end to start.
- ⚠️ Action 'Action_None' range [38-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-121] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-264] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-226] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-247] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunFlatRoute' range [82-96] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunFlatRoute' range [101-114] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunFlatRoute' range [116-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunFlatRoute' range [119-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-240] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-219] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-237] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-265] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-177] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-262] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-115] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-191] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-250] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-267] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-60] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-153] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-219] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [37-76] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [78-142] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [148-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-211] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-167] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [37-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [37-52] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [57-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [169-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [194-232] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [234-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [237-251] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [253-255] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-154] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-224] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-43] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-49] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [53-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-106] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-177] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-231] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-251] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-269] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-269] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-265] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [197-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-243] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-240] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-263] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-260] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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