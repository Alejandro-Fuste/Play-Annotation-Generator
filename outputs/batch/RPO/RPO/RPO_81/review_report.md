# Play-Annotation-Generator Annotation Review — RPO_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_81`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 65
- **Ball Tracks:** 0
- **Action Segments:** 156
- **Validation Warnings:** 214
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `1` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 138
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBall` | RB | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 77 | START | 77 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `14` | 77 | START | 77 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `15` | 77 | START | 77 | 143 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `16` | `16` | 77 | START | 77 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 77 | START | 79 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `9` | `9` | 84 | START | 84 | 135 |
| ✅ EXACT | `Action_PullBall` | RB | `4` | `4` | 98 | START | 98 | 114 |
| ✅ EXACT | `Action_ThrowPass` | RB | `4` | `4` | 133 | START | 133 | 143 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 83 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 84 | 135 | 52 | inferred_complete_timeline |
| `Action_ReadDefender` | 137 | 173 | 37 | inferred_complete_timeline |
| `Action_ReadDefender` | 178 | 185 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 187 | 214 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 97 | 22 | inferred_complete_timeline |
| `Action_PullBall` | 98 | 114 | 17 | inferred_complete_timeline |
| `Action_None` | 115 | 132 | 18 | inferred_complete_timeline |
| `Action_ThrowPass` | 133 | 143 | 11 | inferred_complete_timeline |
| `Action_None` | 144 | 161 | 18 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 137 | 62 | inferred_complete_timeline |
| `Action_None` | 139 | 148 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 141 | 66 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 114 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 143 | 67 | inferred_complete_timeline |
| `Action_None` | 144 | 173 | 30 | inferred_complete_timeline |
| `Action_None` | 179 | 199 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 113 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 163 | 19 | inferred_complete_timeline |
| `Action_None` | 165 | 207 | 43 | inferred_complete_timeline |
| `Action_None` | 215 | 220 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 114 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 143 | 27 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 143 | 49 | inferred_complete_timeline |
| `Action_None` | 144 | 213 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 143 | 67 | inferred_complete_timeline |
| `Action_None` | 144 | 181 | 38 | inferred_complete_timeline |
| `Action_None` | 187 | 202 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 117 | 42 | inferred_complete_timeline |
| `Action_None` | 120 | 182 | 63 | inferred_complete_timeline |
| `Action_None` | 195 | 199 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 89 | 14 | inferred_complete_timeline |
| `Action_None` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_None` | 117 | 123 | 7 | inferred_complete_timeline |
| `Action_None` | 137 | 199 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 78 | 150 | 73 | inferred_complete_timeline |
| `Action_None` | 155 | 173 | 19 | inferred_complete_timeline |
| `Action_None` | 181 | 185 | 5 | inferred_complete_timeline |
| `Action_None` | 187 | 207 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 153 | 78 | inferred_complete_timeline |
| `Action_None` | 157 | 174 | 18 | inferred_complete_timeline |
| `Action_None` | 177 | 199 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 133 | 58 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 150 | 8 | inferred_complete_timeline |
| `Action_None` | 152 | 199 | 48 | inferred_complete_timeline |
| `Action_None` | 207 | 209 | 3 | inferred_complete_timeline |
| `Action_None` | 212 | 215 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 176 | 101 | inferred_complete_timeline |
| `Action_None` | 183 | 248 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 199 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 199 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 135 | 60 | inferred_complete_timeline |
| `Action_None` | 138 | 148 | 11 | inferred_complete_timeline |
| `Action_None` | 153 | 359 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 213 | 138 | inferred_complete_timeline |
| `Action_None` | 220 | 226 | 7 | inferred_complete_timeline |
| `Action_None` | 231 | 246 | 16 | inferred_complete_timeline |
| `Action_None` | 252 | 359 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 260 | 185 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–199 | 200 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 48–65 | 10 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 131–173 | 43 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 159–199 | 41 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 162–359 | 197 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 168–199 | 26 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 180–204 | 21 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 188–198 | 11 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 191–199 | 9 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 200–213 | 14 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 200–231 | 20 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 200–207 | 8 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 200–207 | 5 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 200–207 | 8 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 200–237 | 38 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 200–207 | 7 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 200–209 | 10 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 200–202 | 3 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 205–211 | 6 | 2 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 208–243 | 26 | 2 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 208–211 | 4 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 208–220 | 13 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 208–220 | 13 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 208–220 | 13 | 1 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 210–279 | 29 | 7 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 210–248 | 39 | 1 | Undefined position; Undefined team |
| `47` | `56` | Position_Unknown | Team_Unknown | 217–229 | 10 | 2 | Undefined position; Undefined team |
| `48` | `57` | Position_Unknown | Team_Unknown | 221–231 | 11 | 1 | Undefined position; Undefined team |
| `49` | `58` | Position_Unknown | Team_Unknown | 221–231 | 11 | 1 | Undefined position; Undefined team |
| `50` | `61` | Position_Unknown | Team_Unknown | 221–223 | 3 | 1 | Undefined position; Undefined team |
| `51` | `62` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `52` | `63` | Position_Unknown | Team_Unknown | 232–242 | 11 | 1 | Undefined position; Undefined team |
| `53` | `64` | Position_Unknown | Team_Unknown | 232–235 | 4 | 1 | Undefined position; Undefined team |
| `54` | `66` | Position_Unknown | Team_Unknown | 247–248 | 2 | 1 | Undefined position; Undefined team |
| `55` | `67` | Position_Unknown | Team_Unknown | 247–248 | 2 | 1 | Undefined position; Undefined team |
| `56` | `69` | Position_Unknown | Team_Unknown | 250–252 | 3 | 1 | Undefined position; Undefined team |
| `57` | `71` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `58` | `73` | Position_Unknown | Team_Unknown | 277–278 | 2 | 1 | Undefined position; Undefined team |
| `59` | `75` | Position_Unknown | Team_Unknown | 290–297 | 8 | 1 | Undefined position; Undefined team |
| `60` | `76` | Position_Unknown | Team_Unknown | 298–303 | 6 | 1 | Undefined position; Undefined team |
| `61` | `77` | Position_Unknown | Team_Unknown | 313–330 | 18 | 1 | Undefined position; Undefined team |
| `62` | `79` | Position_Unknown | Team_Unknown | 318–334 | 15 | 2 | Undefined position; Undefined team |
| `63` | `80` | Position_Unknown | Team_Unknown | 322–327 | 6 | 1 | Undefined position; Undefined team |
| `64` | `81` | Position_Unknown | Team_Unknown | 340–341 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 44 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 44 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 88 |
| Missing visible bounding boxes during action | 124 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 148: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [76-137] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-141] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-135] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-199] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-117] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-182] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-199] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-260] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-246] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [84-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [137-173] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [178-185] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [187-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-114] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-123] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-207] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-213] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-181] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-199] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-153] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-248] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-121] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-141] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-163] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-207] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-339] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-199] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-199] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-213] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-231] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-237] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-209] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-220] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-243] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-220] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-220] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-220] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-217] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-248] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-231] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-231] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-242] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-297] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-303] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-330] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-329] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-334] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-327] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '64' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.

</details>