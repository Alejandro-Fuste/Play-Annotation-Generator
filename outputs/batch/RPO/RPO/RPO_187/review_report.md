# Play-Annotation-Generator Annotation Review — RPO_187

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_187`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 150
- **Validation Warnings:** 139
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunHitchRoute` | actor_track_id `0` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 131
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 53 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `16` | `16` | 55 | START | 55 | 89 |
| ✅ EXACT | `Action_ZoneBlock` | C | `17` | `17` | 55 | START | 55 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `20` | 55 | START | 55 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 55 | START | 55 | 74 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 55 | START | 55 | 91 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `8` | 62 | START | 62 | 77 |
| ✅ EXACT | `Action_PullBall` | QB | `8` | `8` | 78 | START | 78 | 84 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 85 | START | 85 | 91 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 61 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 62 | 77 | 16 | inferred_complete_timeline |
| `Action_PullBall` | 78 | 84 | 7 | inferred_complete_timeline |
| `Action_ThrowPass` | 85 | 91 | 7 | inferred_complete_timeline |
| `Action_None` | 92 | 119 | 28 | inferred_complete_timeline |
| `Action_None` | 123 | 129 | 7 | inferred_complete_timeline |
| `Action_None` | 131 | 136 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 72 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 269 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 269 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 128 | 75 | inferred_complete_timeline |
| `Action_None` | 134 | 146 | 13 | inferred_complete_timeline |
| `Action_None` | 153 | 269 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 91 | 38 | inferred_complete_timeline |
| `Action_None` | 93 | 103 | 11 | inferred_complete_timeline |
| `Action_None` | 113 | 119 | 7 | inferred_complete_timeline |
| `Action_None` | 122 | 231 | 110 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 269 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 54 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 91 | 37 | inferred_complete_timeline |
| `Action_None` | 92 | 269 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 54 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 74 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 91 | 14 | inferred_complete_timeline |
| `Action_None` | 92 | 99 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 54 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 68 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 54 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 89 | 35 | inferred_complete_timeline |
| `Action_None` | 108 | 155 | 48 | inferred_complete_timeline |
| `Action_None` | 162 | 205 | 44 | inferred_complete_timeline |
| `Action_None` | 209 | 220 | 12 | inferred_complete_timeline |
| `Action_None` | 222 | 254 | 33 | inferred_complete_timeline |
| `Action_None` | 256 | 261 | 6 | inferred_complete_timeline |
| `Action_None` | 263 | 265 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 54 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 83 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 91 | 1 | inferred_complete_timeline |
| `Action_None` | 92 | 92 | 1 | inferred_complete_timeline |
| `Action_None` | 161 | 165 | 5 | inferred_complete_timeline |
| `Action_None` | 168 | 188 | 21 | inferred_complete_timeline |
| `Action_None` | 193 | 201 | 9 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 220 | 6 | inferred_complete_timeline |
| `Action_None` | 222 | 233 | 12 | inferred_complete_timeline |
| `Action_None` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 75 | 22 | inferred_complete_timeline |
| `Action_None` | 77 | 122 | 46 | inferred_complete_timeline |
| `Action_None` | 124 | 211 | 88 | inferred_complete_timeline |
| `Action_None` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_None` | 219 | 269 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 83 | 30 | inferred_complete_timeline |
| `Action_None` | 97 | 102 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 118 | 65 | inferred_complete_timeline |
| `Action_None` | 126 | 171 | 46 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 178 | 3 | inferred_complete_timeline |
| `Action_None` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 104 | 51 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 145 | 5 | inferred_complete_timeline |
| `Action_None` | 147 | 151 | 5 | inferred_complete_timeline |
| `Action_None` | 162 | 189 | 28 | inferred_complete_timeline |
| `Action_None` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_None` | 226 | 235 | 10 | inferred_complete_timeline |
| `Action_None` | 248 | 269 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 269 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 129 | 76 | inferred_complete_timeline |
| `Action_None` | 139 | 249 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 128 | 75 | inferred_complete_timeline |
| `Action_None` | 138 | 159 | 22 | inferred_complete_timeline |
| `Action_None` | 161 | 172 | 12 | inferred_complete_timeline |
| `Action_None` | 176 | 197 | 22 | inferred_complete_timeline |
| `Action_None` | 199 | 269 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 105 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 130 | 77 | inferred_complete_timeline |
| `Action_None` | 134 | 143 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 220 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 269 | 216 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 4–60 | 38 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 79–269 | 154 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 135–269 | 114 | 8 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 141–228 | 72 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 154–269 | 104 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 156–269 | 114 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 202–269 | 37 | 6 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 211–219 | 9 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 218–269 | 38 | 3 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 230–269 | 40 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 231–233 | 3 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 232–242 | 9 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 234–269 | 36 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 235–245 | 11 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 237–269 | 25 | 3 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 262–267 | 4 | 2 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 264–267 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 102 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [54-83] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-75] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-211] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-269] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-128] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-159] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-172] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-197] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-220] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-128] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-119] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-129] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-130] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-104] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-189] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-235] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-91] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-231] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-129] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-249] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-171] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-269] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-205] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-220] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-254] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-72] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 92, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [92-92] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-188] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-74] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-7] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-46] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-52] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-104] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-212] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-195] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-216] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-148] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-219] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-212] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-259] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-219] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-233] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-269] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-245] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-242] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '39' has 2 frames without a visible bounding box.
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