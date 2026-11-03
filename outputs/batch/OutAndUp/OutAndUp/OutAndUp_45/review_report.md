# Play-Annotation-Generator Annotation Review — OutAndUp_45

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_45`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 113
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB1 | offense | `20` | `20` |
| ✅ EXACT | `Action_SellOut` | WR2 | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR2 | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB1 | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | `13` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `20` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 26 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 27 | START | 27 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `11` | `11` | 31 | START | 32 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `12` | `12` | 31 | START | 31 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `17` | `17` | 31 | START | 31 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 31 | START | 31 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 31 | START | 31 | 31 |
| ✅ EXACT | `Action_SnapReceive` | QB1 | `20` | `20` | 31 | END | 27 | 31 |
| ✅ EXACT | `Action_SellOut` | WR2 | `14` | `14` | 81 | START | 81 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR2 | `14` | `14` | 102 | START | 102 | 156 |
| ✅ EXACT | `Action_ThrowPass` | QB1 | `20` | `20` | 123 | START | 123 | 134 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 31 | 5 | inferred_complete_timeline |
| `Action_None` | 32 | 122 | 91 | inferred_complete_timeline |
| `Action_ThrowPass` | 123 | 134 | 12 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>QB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 64 | 38 | inferred_complete_timeline |
| `Action_None` | 66 | 133 | 68 | inferred_complete_timeline |
| `Action_None` | 141 | 202 | 62 | inferred_complete_timeline |
| `Action_None` | 206 | 221 | 16 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 256 | 13 | inferred_complete_timeline |
| `Action_None` | 259 | 269 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 269 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_SellOut` | 81 | 101 | 21 | inferred_complete_timeline |
| `Action_RunGoRoute` | 102 | 156 | 55 | inferred_complete_timeline |
| `Action_RunGoRoute` | 158 | 159 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 119 | 93 | inferred_complete_timeline |
| `Action_None` | 123 | 133 | 11 | inferred_complete_timeline |
| `Action_None` | 135 | 160 | 26 | inferred_complete_timeline |
| `Action_None` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_None` | 217 | 221 | 5 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 250 | 3 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 133 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 77 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 108 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 31 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 102 | 70 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 127 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 129 | 134 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 146 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 159 | 218 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 223 | 228 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 230 | 269 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 27 | 31 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 47 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 125 | 77 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 145 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 208 | 269 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 39 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 104 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 122 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 129 | 269 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 70 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 125 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 136 | 139 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 153 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 135 | 109 | inferred_complete_timeline |
| `Action_None` | 139 | 145 | 7 | inferred_complete_timeline |
| `Action_None` | 149 | 159 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 156 | 130 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 210 | 45 | inferred_complete_timeline |
| `Action_None` | 250 | 258 | 9 | inferred_complete_timeline |
| `Action_None` | 262 | 267 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 102 | 76 | inferred_complete_timeline |
| `Action_None` | 118 | 158 | 41 | inferred_complete_timeline |
| `Action_None` | 166 | 187 | 22 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 209 | 233 | 25 | inferred_complete_timeline |
| `Action_None` | 235 | 238 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 44 | 18 | inferred_complete_timeline |
| `Action_None` | 50 | 125 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 269 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 156 | 130 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 241 | 73 | inferred_complete_timeline |
| `Action_None` | 251 | 256 | 6 | inferred_complete_timeline |
| `Action_None` | 259 | 269 | 11 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 269 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 208 | 182 | inferred_complete_timeline |
| `Action_None` | 210 | 269 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 180 | 154 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 269 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 158 | 132 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 120–269 | 115 | 10 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 144–223 | 17 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 144–153 | 10 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 185–205 | 19 | 3 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 188–260 | 38 | 2 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 193–215 | 23 | 1 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 200–269 | 46 | 2 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 232–269 | 19 | 4 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 245–267 | 21 | 2 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 250–265 | 11 | 2 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (10 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 103 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [27–31], lower_priority='Action_PassBlock' annotated_start=31, effective_Action_PassBlock_start=32.
- ⚠️ Action 'Action_None' range [27-135] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-145] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-44] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-125] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-269] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-180] for track '5' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-156] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-258] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-102] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-158] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-233] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-158] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-47] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-125] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [208-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-202] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-221] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-256] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [102-156] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [158-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-241] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-70] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [117-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [130-133] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [136-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-153] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-133] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-160] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-104] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [129-269] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [123-134] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '21' starts at frame 31, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [31-31] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-102] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [108-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [129-134] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [153-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [159-218] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [223-228] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-145] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-170] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-190] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-269] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-153] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-197] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-215] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-222] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-255] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '31' has 1 frames without a visible bounding box.
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

</details>