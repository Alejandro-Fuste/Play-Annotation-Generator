# Play-Annotation-Generator Annotation Review — RPO_32

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_32`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 184
- **Validation Warnings:** 177
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunHitchGoRoute` | actor_track_id `3` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 165
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 4 | START | 4 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 4 | START | 4 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 4 | START | 4 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 4 | START | 4 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 4 | START | 4 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 4 | START | 4 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 4 | START | 4 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 4 | START | 4 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 4 | START | 4 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 4 | START | 4 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 4 | START | 4 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 40 | START | 40 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `16` | `16` | 40 | START | 40 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 40 | START | 40 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `19` | 40 | START | 40 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `20` | 40 | START | 40 | 47 |
| ✅ EXACT | `Action_ReadDefender` | QB | `17` | `17` | 47 | START | 47 | 68 |
| ✅ EXACT | `Action_PullBall` | QB | `17` | `17` | 69 | START | 69 | 95 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 100 | START | 100 | 128 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 46 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 47 | 68 | 22 | inferred_complete_timeline |
| `Action_PullBall` | 69 | 95 | 27 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_ThrowPass` | 100 | 128 | 29 | inferred_complete_timeline |
| `Action_None` | 129 | 139 | 11 | inferred_complete_timeline |
| `Action_None` | 152 | 174 | 23 | inferred_complete_timeline |
| `Action_None` | 180 | 183 | 4 | inferred_complete_timeline |
| `Action_None` | 187 | 207 | 21 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 231 | 235 | 5 | inferred_complete_timeline |
| `Action_None` | 249 | 273 | 25 | inferred_complete_timeline |
| `Action_None` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 4–56
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 56 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 4–296
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 207 | 169 | inferred_complete_timeline |
| `Action_None` | 219 | 233 | 15 | inferred_complete_timeline |
| `Action_None` | 246 | 257 | 12 | inferred_complete_timeline |
| `Action_None` | 259 | 265 | 7 | inferred_complete_timeline |
| `Action_None` | 267 | 276 | 10 | inferred_complete_timeline |
| `Action_None` | 278 | 281 | 4 | inferred_complete_timeline |
| `Action_None` | 285 | 296 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–235
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 235 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 4–259
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 259 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 4–259
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 73 | 35 | inferred_complete_timeline |
| `Action_None` | 75 | 86 | 12 | inferred_complete_timeline |
| `Action_None` | 89 | 133 | 45 | inferred_complete_timeline |
| `Action_None` | 151 | 238 | 88 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 259 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 4–198
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 120 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 128 | 4 | inferred_complete_timeline |
| `Action_None` | 129 | 136 | 8 | inferred_complete_timeline |
| `Action_None` | 160 | 198 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 56 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 113 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 122 | 6 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 202 | 40 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 221 | 4 | inferred_complete_timeline |
| `Action_None` | 224 | 274 | 51 | inferred_complete_timeline |
| `Action_None` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 4–158
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 36 | 33 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 42 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 109 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 118 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 128 | 1 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 152 | 21 | inferred_complete_timeline |
| `Action_None` | 155 | 158 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 4–108
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 83 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 99 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 108 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 4–73
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 47 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 73 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 4–260
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 112 | 74 | inferred_complete_timeline |
| `Action_None` | 114 | 135 | 22 | inferred_complete_timeline |
| `Action_None` | 152 | 198 | 47 | inferred_complete_timeline |
| `Action_None` | 205 | 229 | 25 | inferred_complete_timeline |
| `Action_None` | 231 | 233 | 3 | inferred_complete_timeline |
| `Action_None` | 238 | 243 | 6 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 260 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 4–54
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 54 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–80
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 80 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 4–87
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 87 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 4–171
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 95 | 57 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 83 | 45 | inferred_complete_timeline |
| `Action_None` | 85 | 90 | 6 | inferred_complete_timeline |
| `Action_None` | 92 | 95 | 4 | inferred_complete_timeline |
| `Action_None` | 98 | 103 | 6 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 160 | 262 | 103 | inferred_complete_timeline |
| `Action_None` | 268 | 299 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 186 | 148 | inferred_complete_timeline |
| `Action_None` | 190 | 216 | 27 | inferred_complete_timeline |
| `Action_None` | 220 | 258 | 39 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 299 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 201 | 163 | inferred_complete_timeline |
| `Action_None` | 205 | 230 | 26 | inferred_complete_timeline |
| `Action_None` | 232 | 299 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 299 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 272 | 234 | inferred_complete_timeline |
| `Action_None` | 288 | 294 | 7 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 4–260
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 39 | 155 | 117 | inferred_complete_timeline |
| `Action_None` | 159 | 222 | 64 | inferred_complete_timeline |
| `Action_None` | 226 | 246 | 21 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 82–118 | 37 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 114–115 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 122–299 | 159 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 128–154 | 27 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 150–299 | 150 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 151–299 | 117 | 11 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 169–279 | 65 | 9 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 184–299 | 87 | 8 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 193–299 | 98 | 4 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 198–199 | 2 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 201–299 | 94 | 3 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 244–295 | 36 | 5 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 246–269 | 24 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 248–289 | 39 | 3 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 253–299 | 28 | 6 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 268–272 | 5 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 282–299 | 18 | 1 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 286–299 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 140 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [39-207] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-233] for track '0' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-257] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-265] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-276] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-296] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-87] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-95] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-235] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-83] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-90] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-262] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-229] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-243] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-259] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-155] for track '7' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-222] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-246] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-54] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-186] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-216] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-201] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-230] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-86] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-133] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-238] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-272] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-294] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-118] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-152] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-120] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-136] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-198] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-207] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-273] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-99] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [105-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-56] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-274] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-73] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-118] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-231] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-154] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-299] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-184] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-218] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-234] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-257] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-279] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-211] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-237] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-279] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-227] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-258] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-274] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-289] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-273] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-223] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-236] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-271] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-295] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-269] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-280] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-279] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-272] for track '37' has 2 frames without a visible bounding box.
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

</details>