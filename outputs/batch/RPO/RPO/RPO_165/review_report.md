# Play-Annotation-Generator Annotation Review — RPO_165

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_165`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 171
- **Validation Warnings:** 178
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantGoRoute` | actor_track_id `6` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 152
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `22` | `22` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 64 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `19` | 66 | START | 66 | 138 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 66 | START | 66 | 124 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 66 | START | 66 | 138 |
| ✅ EXACT | `Action_ZoneBlock` | C | `22` | `22` | 66 | START | 66 | 138 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 66 | START | 66 | 137 |
| ✅ EXACT | `Action_ReadDefender` | QB | `14` | `14` | 77 | START | 77 | 95 |
| ✅ EXACT | `Action_PullBall` | QB | `14` | `14` | 96 | START | 96 | 103 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 129 | START | 129 | 138 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 76 | 12 | inferred_complete_timeline |
| `Action_ReadDefender` | 77 | 95 | 19 | inferred_complete_timeline |
| `Action_PullBall` | 96 | 103 | 8 | inferred_complete_timeline |
| `Action_None` | 104 | 128 | 25 | inferred_complete_timeline |
| `Action_ThrowPass` | 129 | 138 | 10 | inferred_complete_timeline |
| `Action_None` | 139 | 158 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 79 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 112 | 48 | inferred_complete_timeline |
| `Action_None` | 115 | 284 | 170 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 167 | 103 | inferred_complete_timeline |
| `Action_None` | 170 | 299 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 141 | 77 | inferred_complete_timeline |
| `Action_None` | 143 | 165 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 299 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 137 | 72 | inferred_complete_timeline |
| `Action_None` | 143 | 299 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 138 | 73 | inferred_complete_timeline |
| `Action_None` | 139 | 154 | 16 | inferred_complete_timeline |
| `Action_None` | 160 | 167 | 8 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_None` | 177 | 179 | 3 | inferred_complete_timeline |
| `Action_None` | 182 | 208 | 27 | inferred_complete_timeline |
| `Action_None` | 210 | 245 | 36 | inferred_complete_timeline |
| `Action_None` | 248 | 262 | 15 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |
| `Action_None` | 284 | 286 | 3 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 138 | 73 | inferred_complete_timeline |
| `Action_None` | 139 | 146 | 8 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 165 | 4 | inferred_complete_timeline |
| `Action_None` | 170 | 282 | 113 | inferred_complete_timeline |
| `Action_None` | 284 | 288 | 5 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 124 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 138 | 73 | inferred_complete_timeline |
| `Action_None` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 192 | 50 | inferred_complete_timeline |
| `Action_None` | 194 | 198 | 5 | inferred_complete_timeline |
| `Action_None` | 200 | 206 | 7 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |
| `Action_None` | 212 | 216 | 5 | inferred_complete_timeline |
| `Action_None` | 220 | 224 | 5 | inferred_complete_timeline |
| `Action_None` | 227 | 234 | 8 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 100 | 36 | inferred_complete_timeline |
| `Action_None` | 102 | 126 | 25 | inferred_complete_timeline |
| `Action_None` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 83 | 19 | inferred_complete_timeline |
| `Action_None` | 111 | 114 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 94 | 30 | inferred_complete_timeline |
| `Action_None` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_None` | 102 | 126 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 116 | 52 | inferred_complete_timeline |
| `Action_None` | 118 | 123 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 118 | 54 | inferred_complete_timeline |
| `Action_None` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_None` | 146 | 148 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 148 | 84 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 159 | 165 | 7 | inferred_complete_timeline |
| `Action_None` | 170 | 299 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 220 | 156 | inferred_complete_timeline |
| `Action_None` | 226 | 233 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 299 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 299 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 116 | 52 | inferred_complete_timeline |
| `Action_None` | 126 | 259 | 134 | inferred_complete_timeline |
| `Action_None` | 261 | 263 | 3 | inferred_complete_timeline |
| `Action_None` | 267 | 299 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 197 | 133 | inferred_complete_timeline |
| `Action_None` | 200 | 299 | 100 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–218 | 199 | 9 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 26–79 | 8 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 95–102 | 7 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 97–299 | 201 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 104–205 | 71 | 7 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 117–119 | 3 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 132–299 | 156 | 5 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 138–139 | 2 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 144–160 | 14 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 154–185 | 19 | 4 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 163–165 | 3 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 163–209 | 37 | 4 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 165–185 | 8 | 3 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 171–198 | 8 | 3 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 173–299 | 126 | 2 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 178–225 | 40 | 4 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 185–299 | 115 | 1 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 189–197 | 9 | 1 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 202–206 | 4 | 2 | Undefined position; Undefined team |
| `43` | `51` | Position_Unknown | Team_Unknown | 213–298 | 85 | 2 | Undefined position; Undefined team |
| `44` | `52` | Position_Unknown | Team_Unknown | 214–299 | 84 | 2 | Undefined position; Undefined team |
| `45` | `53` | Position_Unknown | Team_Unknown | 222–227 | 6 | 1 | Undefined position; Undefined team |
| `46` | `54` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `47` | `55` | Position_Unknown | Team_Unknown | 228–233 | 4 | 2 | Undefined position; Undefined team |
| `48` | `56` | Position_Unknown | Team_Unknown | 231–234 | 4 | 1 | Undefined position; Undefined team |
| `49` | `57` | Position_Unknown | Team_Unknown | 247–299 | 51 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 121 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [65-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-284] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-220] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-197] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-299] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-137] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-126] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-126] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-299] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-259] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-208] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-245] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-262] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-282] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-29] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-145] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-141] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-167] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-227] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-160] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-170] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-184] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-205] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-265] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-216] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-225] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-197] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-298] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-259] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>