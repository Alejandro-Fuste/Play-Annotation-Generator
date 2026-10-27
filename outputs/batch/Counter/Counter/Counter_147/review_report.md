# Play-Annotation-Generator Annotation Review — Counter_147

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_147`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 166
- **Validation Warnings:** 173
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 133
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | TE2 | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 6 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 15 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 0 | START | 0 | 132 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `10` | `9` | 122 | START | 122 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 127 | END | 122 | 127 |
| ✅ EXACT | `Action_DownBlock` | RT | `16` | `15` | 133 | START | 133 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 133 | START | 133 | 133 |
| ✅ EXACT | `Action_DownBlock` | TE2 | `9` | `8` | 133 | START | 133 | 182 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | `20` | `19` | 133 | START | 138 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LG | `15` | `14` | 133 | START | 133 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `17` | `16` | 152 | START | 152 | 162 |
| ✅ EXACT | `Action_BallCarry` | RB | `1` | `0` | 166 | START | 166 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 210 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 18 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 26 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 121 | 90 | inferred_complete_timeline |
| `Action_SnapReceive` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_None` | 128 | 151 | 24 | inferred_complete_timeline |
| `Action_Handoff` | 152 | 162 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 189 | 24 | inferred_complete_timeline |
| `Action_None` | 195 | 200 | 6 | inferred_complete_timeline |
| `Action_None` | 231 | 233 | 3 | inferred_complete_timeline |
| `Action_None` | 235 | 276 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 299 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 149 | 28 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 182 | 50 | inferred_complete_timeline |
| `Action_None` | 212 | 215 | 4 | inferred_complete_timeline |
| `Action_None` | 217 | 264 | 48 | inferred_complete_timeline |
| `Action_None` | 268 | 274 | 7 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 289 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 36 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 108 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 138 | 171 | 34 | inferred_complete_timeline |
| `Action_PullBlock` | 186 | 210 | 25 | inferred_complete_timeline |
| `Action_None` | 211 | 225 | 15 | inferred_complete_timeline |
| `Action_None` | 228 | 264 | 37 | inferred_complete_timeline |
| `Action_None` | 266 | 290 | 25 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 34 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 132 | 97 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 141 | 153 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 15–299
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 132 | 118 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 133 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 160 | 210 | 51 | inferred_complete_timeline |
| `Action_None` | 211 | 299 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 170 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 135 | 14 | inferred_complete_timeline |
| `Action_None` | 137 | 149 | 13 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 193 | 39 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 209 | 3 | inferred_complete_timeline |
| `Action_None` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_None` | 220 | 225 | 6 | inferred_complete_timeline |
| `Action_None` | 228 | 234 | 7 | inferred_complete_timeline |
| `Action_None` | 236 | 252 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 135 | 14 | inferred_complete_timeline |
| `Action_None` | 139 | 178 | 40 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 223 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 3–195
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 65 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 121 | 52 | inferred_complete_timeline |
| `Action_None` | 122 | 134 | 13 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 168 | 47 | inferred_complete_timeline |
| `Action_None` | 170 | 252 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 219 | 98 | inferred_complete_timeline |
| `Action_None` | 223 | 227 | 5 | inferred_complete_timeline |
| `Action_None` | 235 | 246 | 12 | inferred_complete_timeline |
| `Action_None` | 249 | 262 | 14 | inferred_complete_timeline |
| `Action_None` | 268 | 274 | 7 | inferred_complete_timeline |
| `Action_None` | 281 | 284 | 4 | inferred_complete_timeline |
| `Action_None` | 286 | 292 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 171 | 50 | inferred_complete_timeline |
| `Action_None` | 173 | 203 | 31 | inferred_complete_timeline |
| `Action_None` | 206 | 214 | 9 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 250 | 25 | inferred_complete_timeline |
| `Action_None` | 252 | 258 | 7 | inferred_complete_timeline |
| `Action_None` | 269 | 274 | 6 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 291 | 293 | 3 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 174 | 53 | inferred_complete_timeline |
| `Action_None` | 186 | 192 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 121 | 43 | inferred_complete_timeline |
| `Action_None` | 122 | 244 | 123 | inferred_complete_timeline |
| `Action_None` | 246 | 253 | 8 | inferred_complete_timeline |
| `Action_None` | 255 | 264 | 10 | inferred_complete_timeline |
| `Action_None` | 266 | 276 | 11 | inferred_complete_timeline |
| `Action_None` | 285 | 286 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 274 | 153 | inferred_complete_timeline |
| `Action_None` | 278 | 281 | 4 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 2–277
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 5 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 121 | 114 | inferred_complete_timeline |
| `Action_None` | 122 | 277 | 156 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–136 | 137 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 22–71 | 15 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 67–78 | 12 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 75–235 | 150 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 140–273 | 81 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 152–162 | 11 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 170–293 | 93 | 5 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 181–299 | 116 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 182–183 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 188–299 | 32 | 8 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 208–211 | 4 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 231–244 | 14 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 234–273 | 31 | 4 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 236–299 | 35 | 6 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 241–273 | 27 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 261–299 | 36 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 261–296 | 16 | 3 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 262–299 | 37 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 135 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 295: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [122-274] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-171] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-203] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-250] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-258] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-274] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-252] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-219] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-246] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-262] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-292] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-264] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-244] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-264] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-276] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-223] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-193] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-252] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-34] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [133-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [138-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [141-153] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-26] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [152-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-276] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-5] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-277] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-36] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [138-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [186-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-225] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-264] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-290] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '20' starts at frame 133, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [133-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [160-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-78] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-170] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-239] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-259] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-162] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-230] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-247] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-274] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-293] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-299] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-270] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-244] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-257] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-273] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-285] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-297] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-265] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-270] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-271] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-294] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>