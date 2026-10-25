# Play-Annotation-Generator Annotation Review — BootPass_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_51`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 129
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 103
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_RunFlatRoute` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 59 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 29 | START | 29 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `12` | `12` | 35 | START | 57 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `15` | `15` | 35 | START | 35 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `17` | `17` | 35 | START | 35 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `19` | `19` | 35 | START | 35 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `20` | `20` | 35 | START | 35 | 46 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 42 | END | 29 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | `16` | `16` | 65 | START | 65 | 65 |
| ✅ EXACT | `Action_BootAway` | QB | `16` | `16` | 66 | START | 66 | 78 |
| ✅ EXACT | `Action_RunFlatRoute` | QB | `16` | `16` | 107 | START | 107 | 122 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 123 | START | 123 | 152 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `7` | `7` | 197 | START | 197 | 205 |

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
- **Visible Frames:** 0–183
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 42 | 14 | inferred_complete_timeline |
| `Action_None` | 43 | 64 | 22 | inferred_complete_timeline |
| `Action_FakeHandoff` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_BootAway` | 66 | 78 | 13 | inferred_complete_timeline |
| `Action_FakeHandoff` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 106 | 25 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 107 | 122 | 16 | inferred_complete_timeline |
| `Action_ThrowPass` | 123 | 152 | 30 | inferred_complete_timeline |
| `Action_None` | 153 | 162 | 10 | inferred_complete_timeline |
| `Action_None` | 176 | 183 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 94 | 66 | inferred_complete_timeline |
| `Action_None` | 98 | 244 | 147 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 137 | 109 | inferred_complete_timeline |
| `Action_None` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_None` | 144 | 149 | 6 | inferred_complete_timeline |
| `Action_None` | 151 | 269 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 79 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 90 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 196 | 105 | inferred_complete_timeline |
| `Action_SecureCatch` | 197 | 205 | 9 | inferred_complete_timeline |
| `Action_None` | 206 | 250 | 45 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 110 | 82 | inferred_complete_timeline |
| `Action_None` | 116 | 162 | 47 | inferred_complete_timeline |
| `Action_None` | 164 | 195 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 67 | 39 | inferred_complete_timeline |
| `Action_None` | 92 | 100 | 9 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 122 | 16 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 138 | 144 | 7 | inferred_complete_timeline |
| `Action_None` | 147 | 205 | 59 | inferred_complete_timeline |
| `Action_None` | 212 | 243 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 42 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 44 | 52 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 107 | 116 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 143 | 150 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 152 | 259 | 108 | inferred_complete_timeline |
| `Action_RunBlock` | 265 | 268 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 46 | 12 | inferred_complete_timeline |
| `Action_RunBlock` | 49 | 53 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 55 | 104 | 50 | inferred_complete_timeline |
| `Action_RunBlock` | 107 | 121 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 135 | 170 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_BallSnap` | 29 | 40 | 12 | inferred_complete_timeline |
| `Action_RunBlock` | 57 | 63 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 80 | 86 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 94 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 97 | 100 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 109 | 110 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 48 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 89 | 102 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 136 | 172 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 179 | 188 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 192 | 252 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 81 | 47 | inferred_complete_timeline |
| `Action_RunBlock` | 89 | 94 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 97 | 172 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 67 | 39 | inferred_complete_timeline |
| `Action_None` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_None` | 79 | 94 | 16 | inferred_complete_timeline |
| `Action_None` | 99 | 104 | 6 | inferred_complete_timeline |
| `Action_None` | 106 | 269 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 104 | 76 | inferred_complete_timeline |
| `Action_None` | 107 | 126 | 20 | inferred_complete_timeline |
| `Action_None` | 137 | 166 | 30 | inferred_complete_timeline |
| `Action_None` | 168 | 174 | 7 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 198 | 201 | 4 | inferred_complete_timeline |
| `Action_None` | 215 | 250 | 36 | inferred_complete_timeline |
| `Action_None` | 252 | 261 | 10 | inferred_complete_timeline |
| `Action_None` | 263 | 268 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 71 | 43 | inferred_complete_timeline |
| `Action_None` | 73 | 124 | 52 | inferred_complete_timeline |
| `Action_None` | 135 | 144 | 10 | inferred_complete_timeline |
| `Action_None` | 148 | 170 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 191 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 262 | 234 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 63 | 35 | inferred_complete_timeline |
| `Action_None` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 77 | 7 | inferred_complete_timeline |
| `Action_None` | 79 | 121 | 43 | inferred_complete_timeline |
| `Action_None` | 128 | 177 | 50 | inferred_complete_timeline |
| `Action_None` | 179 | 269 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 56–68 | 11 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 140–172 | 27 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 213–247 | 29 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 222–269 | 48 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `12` (7 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (9 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [29–42], lower_priority='Action_RunBlock' annotated_start=35, effective_Action_RunBlock_start=43.
- ⚠️ Action 'Action_None' range [29-137] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-110] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-162] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-191] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-67] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-100] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-122] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-205] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-243] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-196] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-250] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-67] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-77] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-94] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-77] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-121] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-177] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-94] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-244] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [29-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [57-63] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [65-67] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [69-77] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [80-86] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [88-94] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [97-100] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [109-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [44-52] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [69-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [85-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [107-116] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [136-138] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [143-150] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [152-259] for track '15' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [265-268] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-81] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [89-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [97-172] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-104] for track '18' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-126] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-166] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-250] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-261] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-48] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [89-102] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [136-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [179-188] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [192-252] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-46] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [49-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [55-104] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [107-121] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [135-170] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-71] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-124] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-170] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-172] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-218] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-247] for track '25' has 1 frames without a visible bounding box.
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

</details>