# Play-Annotation-Generator Annotation Review — RPO_121

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_121`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 167
- **Validation Warnings:** 198
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunHitchRoute` | actor_track_id `0` | source `Route` | no temporal frame

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
- **Inferred Coverage Segments (Action_None):** 148
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `3` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 68 | START | 68 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | C | `19` | `19` | 68 | START | 68 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `21` | 68 | START | 68 | 116 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 68 | START | 68 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `9` | 68 | START | 68 | 78 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `12` | 71 | START | 71 | 86 |
| ✅ EXACT | `Action_PullBall` | QB | `12` | `12` | 87 | START | 87 | 94 |
| ✅ EXACT | `Action_ThrowPass` | RB | `8` | `8` | 123 | START | 123 | 130 |

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
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 70 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 71 | 86 | 16 | inferred_complete_timeline |
| `Action_PullBall` | 87 | 94 | 8 | inferred_complete_timeline |
| `Action_None` | 95 | 263 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 122 | 56 | inferred_complete_timeline |
| `Action_ThrowPass` | 123 | 130 | 8 | inferred_complete_timeline |
| `Action_None` | 131 | 177 | 47 | inferred_complete_timeline |
| `Action_None` | 263 | 269 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 172 | 106 | inferred_complete_timeline |
| `Action_None` | 249 | 252 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 206 | 140 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 269 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 107 | 41 | inferred_complete_timeline |
| `Action_None` | 112 | 154 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 116 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 127 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 78 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 128 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 130 | 1 | inferred_complete_timeline |
| `Action_None` | 131 | 131 | 1 | inferred_complete_timeline |
| `Action_None` | 134 | 140 | 7 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 154 | 8 | inferred_complete_timeline |
| `Action_None` | 162 | 183 | 22 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 217 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 130 | 63 | inferred_complete_timeline |
| `Action_None` | 131 | 173 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 121 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 130 | 8 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 142 | 6 | inferred_complete_timeline |
| `Action_None` | 148 | 171 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 130 | 63 | inferred_complete_timeline |
| `Action_None` | 131 | 223 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 113 | 47 | inferred_complete_timeline |
| `Action_None` | 122 | 155 | 34 | inferred_complete_timeline |
| `Action_None` | 157 | 179 | 23 | inferred_complete_timeline |
| `Action_None` | 190 | 192 | 3 | inferred_complete_timeline |
| `Action_None` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |
| `Action_None` | 249 | 269 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 102 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 81 | 15 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 93 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 115 | 49 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 160 | 41 | inferred_complete_timeline |
| `Action_None` | 162 | 165 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 114 | 48 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 125 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 242 | 176 | inferred_complete_timeline |
| `Action_None` | 252 | 258 | 7 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 269 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 227 | 161 | inferred_complete_timeline |
| `Action_None` | 232 | 269 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 149 | 83 | inferred_complete_timeline |
| `Action_None` | 151 | 167 | 17 | inferred_complete_timeline |
| `Action_None` | 169 | 177 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–210 | 117 | 13 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 95–97 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 113–117 | 5 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 124–127 | 4 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 131–257 | 92 | 4 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 148–269 | 52 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 150–153 | 4 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 154–155 | 2 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 156–269 | 114 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 156–269 | 110 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 159–262 | 79 | 6 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 160–165 | 6 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 180–202 | 18 | 4 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 183–236 | 50 | 3 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 194–269 | 76 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 196–198 | 3 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 197–263 | 39 | 4 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 200–210 | 7 | 2 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 200–269 | 70 | 1 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 204–269 | 66 | 1 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 205–269 | 65 | 1 | Undefined position; Undefined team |
| `43` | `50` | Position_Unknown | Team_Unknown | 205–207 | 3 | 1 | Undefined position; Undefined team |
| `44` | `51` | Position_Unknown | Team_Unknown | 205–269 | 18 | 3 | Undefined position; Undefined team |
| `45` | `52` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |
| `46` | `53` | Position_Unknown | Team_Unknown | 208–253 | 41 | 3 | Undefined position; Undefined team |
| `47` | `54` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `48` | `55` | Position_Unknown | Team_Unknown | 241–263 | 23 | 1 | Undefined position; Undefined team |
| `49` | `56` | Position_Unknown | Team_Unknown | 246–263 | 17 | 2 | Undefined position; Undefined team |
| `50` | `57` | Position_Unknown | Team_Unknown | 254–268 | 14 | 2 | Undefined position; Undefined team |
| `51` | `58` | Position_Unknown | Team_Unknown | 256–268 | 11 | 2 | Undefined position; Undefined team |
| `52` | `60` | Position_Unknown | Team_Unknown | 259–269 | 9 | 2 | Undefined position; Undefined team |
| `53` | `62` | Position_Unknown | Team_Unknown | 264–268 | 5 | 1 | Undefined position; Undefined team |
| `54` | `63` | Position_Unknown | Team_Unknown | 264–269 | 6 | 1 | Undefined position; Undefined team |
| `55` | `64` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `56` | `66` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 35 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 35 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 70 |
| Missing visible bounding boxes during action | 127 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [67-206] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-125] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-102] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-172] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-179] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-93] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-223] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-177] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-128] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 131, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [131-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-140] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-183] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-217] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-242] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-258] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [71-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-263] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-227] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-115] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-160] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-167] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-171] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-130] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-15] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-93] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-122] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-150] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-171] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-202] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-116] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-114] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-117] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-233] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-217] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-269] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-242] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-269] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-167] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-187] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-200] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-241] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-262] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-227] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-212] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-245] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-263] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-269] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-269] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-212] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-235] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-248] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-263] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-263] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-259] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-268] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>