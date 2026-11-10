# Play-Annotation-Generator Annotation Review — RPO_131

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_131`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 64
- **Ball Tracks:** 0
- **Action Segments:** 141
- **Validation Warnings:** 178
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `2` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `0` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 74 | START | 74 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `15` | 74 | START | 74 | 74 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `17` | 74 | START | 74 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `18` | 74 | START | 74 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `20` | 74 | START | 74 | 94 |
| ✅ EXACT | `Action_ReadDefender` | QB | `19` | `19` | 76 | START | 76 | 87 |
| ✅ EXACT | `Action_PullBall` | QB | `19` | `19` | 88 | START | 88 | 95 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 120 | START | 120 | 127 |

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
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 76 | 87 | 12 | inferred_complete_timeline |
| `Action_PullBall` | 88 | 95 | 8 | inferred_complete_timeline |
| `Action_None` | 96 | 119 | 24 | inferred_complete_timeline |
| `Action_ThrowPass` | 120 | 127 | 8 | inferred_complete_timeline |
| `Action_None` | 128 | 156 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 72 | 34 | inferred_complete_timeline |
| `Action_None` | 73 | 84 | 12 | inferred_complete_timeline |
| `Action_None` | 88 | 221 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–345
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 345 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 214 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 200 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 96 | 24 | inferred_complete_timeline |
| `Action_None` | 112 | 121 | 10 | inferred_complete_timeline |
| `Action_None` | 124 | 179 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 91 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 118 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 137 | 9 | inferred_complete_timeline |
| `Action_None` | 144 | 189 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 93 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 92 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 127 | 34 | inferred_complete_timeline |
| `Action_None` | 128 | 161 | 34 | inferred_complete_timeline |
| `Action_None` | 163 | 166 | 4 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 74 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 81 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 94 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 158 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 88 | 16 | inferred_complete_timeline |
| `Action_None` | 96 | 178 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 98 | 26 | inferred_complete_timeline |
| `Action_None` | 103 | 136 | 34 | inferred_complete_timeline |
| `Action_None` | 142 | 196 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 93 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 208 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 117 | 45 | inferred_complete_timeline |
| `Action_None` | 124 | 129 | 6 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 163 | 29 | inferred_complete_timeline |
| `Action_None` | 171 | 179 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 218 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 77 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 126 | 54 | inferred_complete_timeline |
| `Action_None` | 129 | 182 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 185 | 113 | inferred_complete_timeline |
| `Action_None` | 191 | 389 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 302 | 230 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 32–43 | 12 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 75–389 | 313 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 106–205 | 73 | 7 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 136–230 | 87 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 150–173 | 24 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 154–181 | 9 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 165–179 | 5 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 168–193 | 26 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 171–173 | 3 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 213–219 | 7 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 220–223 | 4 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 247–249 | 3 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 258–262 | 5 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 271–389 | 119 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 279–280 | 2 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 281–389 | 109 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 284–288 | 5 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 288–389 | 102 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 298–317 | 20 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 300–389 | 88 | 3 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 310–317 | 8 | 1 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 312–317 | 6 | 1 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 312–317 | 6 | 1 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 318–389 | 72 | 1 | Undefined position; Undefined team |
| `46` | `58` | Position_Unknown | Team_Unknown | 318–389 | 72 | 1 | Undefined position; Undefined team |
| `47` | `59` | Position_Unknown | Team_Unknown | 318–389 | 72 | 1 | Undefined position; Undefined team |
| `48` | `60` | Position_Unknown | Team_Unknown | 318–389 | 72 | 1 | Undefined position; Undefined team |
| `49` | `62` | Position_Unknown | Team_Unknown | 322–389 | 68 | 1 | Undefined position; Undefined team |
| `50` | `63` | Position_Unknown | Team_Unknown | 324–389 | 66 | 1 | Undefined position; Undefined team |
| `51` | `64` | Position_Unknown | Team_Unknown | 326–389 | 61 | 2 | Undefined position; Undefined team |
| `52` | `65` | Position_Unknown | Team_Unknown | 326–331 | 6 | 1 | Undefined position; Undefined team |
| `53` | `66` | Position_Unknown | Team_Unknown | 329–385 | 50 | 5 | Undefined position; Undefined team |
| `54` | `67` | Position_Unknown | Team_Unknown | 329–389 | 61 | 1 | Undefined position; Undefined team |
| `55` | `68` | Position_Unknown | Team_Unknown | 330–389 | 60 | 1 | Undefined position; Undefined team |
| `56` | `69` | Position_Unknown | Team_Unknown | 332–389 | 58 | 1 | Undefined position; Undefined team |
| `57` | `72` | Position_Unknown | Team_Unknown | 340–389 | 50 | 1 | Undefined position; Undefined team |
| `58` | `73` | Position_Unknown | Team_Unknown | 341–389 | 36 | 4 | Undefined position; Undefined team |
| `59` | `75` | Position_Unknown | Team_Unknown | 353–372 | 19 | 2 | Undefined position; Undefined team |
| `60` | `76` | Position_Unknown | Team_Unknown | 363–380 | 4 | 2 | Undefined position; Undefined team |
| `61` | `77` | Position_Unknown | Team_Unknown | 363–365 | 3 | 1 | Undefined position; Undefined team |
| `62` | `78` | Position_Unknown | Team_Unknown | 385–387 | 3 | 1 | Undefined position; Undefined team |
| `63` | `79` | Position_Unknown | Team_Unknown | 387–389 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 42 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 42 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 84 |
| Missing visible bounding boxes during action | 93 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_None' range [73-96] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-179] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-158] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-345] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-98] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-136] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-208] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-218] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-179] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-178] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-126] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-182] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-161] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '15' starts at frame 74, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [74-74] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-137] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-189] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-156] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-84] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-43] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-320] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-146] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-186] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-220] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-317] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-374] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-389] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-317] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-389] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-355] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-389] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-331] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-366] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-374] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-385] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-357] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-367] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-360] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-372] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-365] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-387] for track '62' has 1 frames without a visible bounding box.
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

</details>