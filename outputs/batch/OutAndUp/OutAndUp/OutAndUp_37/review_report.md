# Play-Annotation-Generator Annotation Review — OutAndUp_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_37`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 168
- **Validation Warnings:** 195
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 147
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_SellOut` | WR2 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 2 | START | 2 | 8 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `16` | `16` | 5 | START | 5 | 40 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `17` | `17` | 5 | START | 9 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 5 | START | 5 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 5 | START | 5 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 5 | START | 5 | 37 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 8 | END | 2 | 8 |
| ⚠️ AMBIGUOUS MATCH | `Action_SellOut` | WR2 | `0` | `0` | 68 | START | 68 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR2 | `0` | `0` | 93 | START | 93 | 201 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 107 | START | 107 | 117 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 8 | 7 | inferred_complete_timeline |
| `Action_None` | 9 | 57 | 49 | inferred_complete_timeline |
| `Action_None` | 59 | 106 | 48 | inferred_complete_timeline |
| `Action_ThrowPass` | 107 | 117 | 11 | inferred_complete_timeline |
| `Action_None` | 118 | 136 | 19 | inferred_complete_timeline |
| `Action_None` | 145 | 198 | 54 | inferred_complete_timeline |
| `Action_None` | 206 | 258 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 213 | 212 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 99 | 98 | inferred_complete_timeline |
| `Action_None` | 103 | 177 | 75 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 84 | 83 | inferred_complete_timeline |
| `Action_None` | 87 | 155 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_SellOut` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_SellOut` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_SellOut` | 78 | 92 | 15 | inferred_complete_timeline |
| `Action_RunGoRoute` | 93 | 201 | 109 | inferred_complete_timeline |
| `Action_RunGoRoute` | 255 | 257 | 3 | inferred_complete_timeline |
| `Action_RunGoRoute` | 259 | 269 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 63 | 62 | inferred_complete_timeline |
| `Action_None` | 76 | 269 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 40 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 57 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 250 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 29 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 60 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 146 | 85 | inferred_complete_timeline |
| `Action_PassBlock` | 155 | 197 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 199 | 266 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 8 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 24 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 60 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 111 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 123 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 128 | 136 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 145 | 152 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 221 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 40 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 60 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 121 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 123 | 218 | 96 | inferred_complete_timeline |
| `Action_PassBlock` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 225 | 241 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 246 | 268 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 46 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 60 | 59 | inferred_complete_timeline |
| `Action_None` | 62 | 236 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 27 | 26 | inferred_complete_timeline |
| `Action_None` | 42 | 44 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 60 | 59 | inferred_complete_timeline |
| `Action_None` | 67 | 76 | 10 | inferred_complete_timeline |
| `Action_None` | 78 | 133 | 56 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 154 | 6 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 173 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 240 | 239 | inferred_complete_timeline |
| `Action_None` | 244 | 269 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 73 | 72 | inferred_complete_timeline |
| `Action_None` | 75 | 85 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 269 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |
| `Action_None` | 152 | 184 | 33 | inferred_complete_timeline |
| `Action_None` | 186 | 269 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 75 | 74 | inferred_complete_timeline |
| `Action_None` | 80 | 87 | 8 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 103 | 11 | inferred_complete_timeline |
| `Action_None` | 107 | 199 | 93 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_None` | 208 | 213 | 6 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 269 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 227 | 226 | inferred_complete_timeline |
| `Action_None` | 230 | 269 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 41–44 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 43–60 | 18 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 88–269 | 181 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 91–112 | 10 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 98–100 | 3 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 113–269 | 157 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 125–197 | 66 | 4 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 138–139 | 2 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 142–265 | 124 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 166–191 | 9 | 3 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 178–216 | 25 | 6 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 180–269 | 42 | 6 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 186–197 | 11 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 187–269 | 81 | 2 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 191–194 | 4 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 192–194 | 3 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 193–195 | 3 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 196–255 | 52 | 2 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 196–258 | 51 | 4 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 213–215 | 3 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 216–242 | 4 | 2 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 233–258 | 22 | 2 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 243–269 | 17 | 3 | Undefined position; Undefined team |
| `46` | `69` | Position_Unknown | Team_Unknown | 243–251 | 9 | 1 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 243–268 | 25 | 2 | Undefined position; Undefined team |
| `48` | `72` | Position_Unknown | Team_Unknown | 246–269 | 19 | 4 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 246–269 | 21 | 2 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 246–269 | 24 | 1 | Undefined position; Undefined team |
| `51` | `82` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (4 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `17` (C): Annotated start 5 != Inferred start 9
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (10 segments found)
- ⚠️ Ambiguous match for action `Action_SellOut` and target `0` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `0` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 133 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [2–8], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=9.
- ⚠️ Action 'Action_SellOut' range [68-69] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellOut' range [73-75] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [93-201] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [255-257] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-87] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-199] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-63] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-99] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-177] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-60] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-236] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-84] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-155] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-213] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-184] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-73] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-85] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-227] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-269] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-46] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-27] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-240] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-57] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-250] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-24] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-45] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-60] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-146] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [155-197] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [199-266] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-121] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [123-218] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [220-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [225-241] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [246-268] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-57] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-198] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-258] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-37] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-60] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-123] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [128-136] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [145-152] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [155-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [161-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [166-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-221] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-44] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-60] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-262] for track '24' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-153] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-265] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-188] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-241] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-215] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-255] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-206] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-215] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-258] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-250] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-251] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-263] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-251] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-268] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '48' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-269] for track '49' has 3 frames without a visible bounding box.
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

</details>