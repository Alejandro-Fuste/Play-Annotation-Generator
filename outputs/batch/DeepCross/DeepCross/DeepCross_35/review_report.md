# Play-Annotation-Generator Annotation Review — DeepCross_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_35`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 138
- **Validation Warnings:** 144
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 117
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | Position_Unknown | Team_Unknown | `25` | `25` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `25` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 12 | START | 12 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `16` | `16` | 15 | START | 15 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 15 | START | 17 | 89 |
| ✅ EXACT | `Action_PassBlock` | LG | `19` | `19` | 15 | START | 15 | 135 |
| ✅ EXACT | `Action_PassBlock` | RT | `20` | `20` | 15 | START | 15 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 15 | START | 15 | 23 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 16 | END | 12 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | Position_Unknown | `25` | `25` | 28 | START | 88 | 146 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 134 | START | 134 | 147 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `25` | `25` | 204 | START | 204 | 269 |

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
- **Visible Frames:** 0–147
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 12 | 16 | 5 | inferred_complete_timeline |
| `Action_None` | 17 | 114 | 98 | inferred_complete_timeline |
| `Action_None` | 120 | 133 | 14 | inferred_complete_timeline |
| `Action_ThrowPass` | 134 | 147 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 51 | 40 | inferred_complete_timeline |
| `Action_None` | 53 | 193 | 141 | inferred_complete_timeline |
| `Action_None` | 201 | 255 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 39 | 52 | 14 | inferred_complete_timeline |
| `Action_None` | 54 | 98 | 45 | inferred_complete_timeline |
| `Action_None` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_None` | 114 | 138 | 25 | inferred_complete_timeline |
| `Action_None` | 140 | 165 | 26 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 269 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 32 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 81 | 70 | inferred_complete_timeline |
| `Action_None` | 83 | 88 | 6 | inferred_complete_timeline |
| `Action_None` | 126 | 146 | 21 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 111 | 97 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 120 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 135 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 12 | 16 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 89 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 98 | 129 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 148 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 163 | 172 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 189 | 193 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 195 | 196 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 23 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 45 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 72 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 103 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 125 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 149 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 246 | 249 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 253 | 254 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 59 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 66 | 55 | inferred_complete_timeline |
| `Action_None` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_None` | 108 | 118 | 11 | inferred_complete_timeline |
| `Action_None` | 120 | 170 | 51 | inferred_complete_timeline |
| `Action_None` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 221 | 10 | inferred_complete_timeline |
| `Action_None` | 229 | 264 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 175 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 58 | 47 | inferred_complete_timeline |
| `Action_None` | 62 | 85 | 24 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_None` | 91 | 93 | 3 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 198 | 187 | inferred_complete_timeline |
| `Action_None` | 209 | 269 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 222 | 211 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 248 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 97 | 86 | inferred_complete_timeline |
| `Action_None` | 99 | 210 | 112 | inferred_complete_timeline |
| `Action_None` | 217 | 220 | 4 | inferred_complete_timeline |
| `Action_None` | 224 | 269 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 102 | 91 | inferred_complete_timeline |
| `Action_None` | 104 | 108 | 5 | inferred_complete_timeline |
| `Action_None` | 110 | 115 | 6 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 65 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 269 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 269 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 269 | 258 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 45–255 | 69 | 7 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 56–68 | 8 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 67–84 | 18 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 88–269 | 177 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 127–256 | 130 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 133–171 | 39 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 186–201 | 16 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 206–210 | 5 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 230–256 | 9 | 3 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 231–256 | 24 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 231–255 | 19 | 4 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 242–250 | 9 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 244–260 | 17 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (10 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (15 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `25` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 110 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [12–16], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=17.
- ⚠️ Action 'Action_None' range [12-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-37] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-52] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-138] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-165] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-269] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-51] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-193] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-255] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-65] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-222] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-248] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-269] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-114] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [134-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-198] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-85] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-89] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [98-129] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [157-158] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [163-172] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [174-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [189-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [195-196] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-170] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-264] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-135] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-59] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-23] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-72] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-125] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [130-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [134-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [153-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [167-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [170-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [246-249] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [253-254] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-171] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-255] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [88-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [149-195] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [204-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-256] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-201] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-256] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-252] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-250] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-260] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '37' has 1 frames without a visible bounding box.
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

</details>