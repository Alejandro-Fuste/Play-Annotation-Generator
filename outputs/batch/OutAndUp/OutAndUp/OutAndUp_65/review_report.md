# Play-Annotation-Generator Annotation Review — OutAndUp_65

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_65`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 299
- **Player Tracks:** 55
- **Ball Tracks:** 0
- **Action Segments:** 168
- **Validation Warnings:** 200
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 146
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_SellOut` | TE1 | offense | `18` | `18` |
| ✅ EXACT | `Action_RunGoRoute` | TE1 | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `0` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `13` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `20` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 64 |
| ✅ EXACT | `Action_BallSnap` | C | `4` | `4` | 65 | START | 65 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `11` | `11` | 68 | START | 68 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `16` | `16` | 68 | START | 68 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `17` | `17` | 68 | START | 68 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 68 | START | 68 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `4` | `4` | 68 | START | 71 | 79 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 70 | END | 65 | 70 |
| ✅ EXACT | `Action_SellOut` | TE1 | `18` | `18` | 129 | START | 129 | 157 |
| ✅ EXACT | `Action_RunGoRoute` | TE1 | `18` | `18` | 158 | START | 158 | 240 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 165 | START | 165 | 174 |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_SnapReceive` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_None` | 71 | 164 | 94 | inferred_complete_timeline |
| `Action_ThrowPass` | 165 | 174 | 10 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 299 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 220 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 128 | 17 | inferred_complete_timeline |
| `Action_SellOut` | 129 | 157 | 29 | inferred_complete_timeline |
| `Action_RunGoRoute` | 158 | 240 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 80 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 139 | 75 | inferred_complete_timeline |
| `Action_None` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_None` | 164 | 177 | 14 | inferred_complete_timeline |
| `Action_None` | 181 | 189 | 9 | inferred_complete_timeline |
| `Action_None` | 192 | 199 | 8 | inferred_complete_timeline |
| `Action_None` | 206 | 218 | 13 | inferred_complete_timeline |
| `Action_None` | 224 | 238 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 89 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 96 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 92 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 107 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_BallSnap` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 79 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 110 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 92 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 110 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 128 | 161 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 74 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 84 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 91 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 124 | 60 | inferred_complete_timeline |
| `Action_None` | 126 | 151 | 26 | inferred_complete_timeline |
| `Action_None` | 154 | 161 | 8 | inferred_complete_timeline |
| `Action_None` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_None` | 172 | 183 | 12 | inferred_complete_timeline |
| `Action_None` | 187 | 203 | 17 | inferred_complete_timeline |
| `Action_None` | 207 | 211 | 5 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 107 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 110 | 46 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 137 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 187 | 123 | inferred_complete_timeline |
| `Action_None` | 190 | 193 | 4 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 287 | 223 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 131 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 138 | 74 | inferred_complete_timeline |
| `Action_None` | 141 | 149 | 9 | inferred_complete_timeline |
| `Action_None` | 155 | 215 | 61 | inferred_complete_timeline |
| `Action_None` | 222 | 254 | 33 | inferred_complete_timeline |
| `Action_None` | 256 | 299 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 225 | 161 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 100 | 36 | inferred_complete_timeline |
| `Action_None` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_None` | 143 | 186 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 170 | 106 | inferred_complete_timeline |
| `Action_None` | 173 | 202 | 30 | inferred_complete_timeline |
| `Action_None` | 204 | 215 | 12 | inferred_complete_timeline |
| `Action_None` | 218 | 299 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 104–297 | 121 | 7 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 129–196 | 64 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 131–206 | 62 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 137–297 | 123 | 6 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 147–192 | 46 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 181–207 | 27 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 185–297 | 90 | 8 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 219–278 | 47 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 223–267 | 33 | 4 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 224–299 | 72 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 228–299 | 72 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 232–243 | 12 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 233–299 | 66 | 2 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 233–243 | 6 | 3 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 238–292 | 52 | 3 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 242–299 | 45 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 244–299 | 53 | 3 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 248–267 | 19 | 2 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 250–260 | 6 | 2 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 252–299 | 43 | 4 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 253–299 | 42 | 2 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 253–254 | 2 | 1 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 257–299 | 38 | 4 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 271–296 | 26 | 1 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 275–295 | 21 | 1 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 278–283 | 6 | 1 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 285–299 | 15 | 1 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 285–286 | 2 | 1 | Undefined position; Undefined team |
| `52` | `77` | Position_Unknown | Team_Unknown | 288–299 | 12 | 1 | Undefined position; Undefined team |
| `53` | `80` | Position_Unknown | Team_Unknown | 291–295 | 5 | 1 | Undefined position; Undefined team |
| `54` | `81` | Position_Unknown | Team_Unknown | 297–299 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 132 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [65–70], lower_priority='Action_PassBlock' annotated_start=68, effective_Action_PassBlock_start=71.
- ⚠️ Action 'Action_None' range [65-220] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-287] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-110] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-137] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-110] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-100] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-186] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-124] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-183] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-215] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-138] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-215] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-254] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-107] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-225] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-107] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-89] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [158-240] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-139] for track '20' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-218] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-238] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-92] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-110] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [128-161] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-204] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-268] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-297] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-196] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-151] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-224] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-293] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-192] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-207] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-195] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-257] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-297] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-248] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-299] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-243] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-277] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-260] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-292] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-260] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-263] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-273] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-283] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-296] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-271] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-299] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-275] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-299] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-296] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-295] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-283] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-299] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-295] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '54' has 1 frames without a visible bounding box.
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

</details>