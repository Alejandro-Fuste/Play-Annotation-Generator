# Play-Annotation-Generator Annotation Review — Counter_205

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_205`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 107
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | DE2 | defense | `5` | `4` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `15` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 84 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 83 | START | 83 | 100 |
| ✅ EXACT | `Action_DownBlock` | LG | `16` | `15` | 85 | START | 85 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `20` | `19` | 85 | START | 101 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `9` | `8` | 85 | START | 85 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `22` | `21` | 85 | START | 85 | 141 |
| ✅ EXACT | `Action_PullLeadBlock` | DE2 | `5` | `4` | 85 | START | 85 | 170 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `8` | `7` | 95 | START | 95 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `20` | 100 | END | 83 | 100 |
| ✅ EXACT | `Action_Handoff` | QB | `21` | `20` | 117 | START | 117 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `7` | 128 | START | 128 | 211 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 170 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_SnapReceive` | 83 | 100 | 18 | inferred_complete_timeline |
| `Action_None` | 101 | 116 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 117 | 127 | 11 | inferred_complete_timeline |
| `Action_None` | 128 | 299 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 95 | 127 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 128 | 211 | 84 | inferred_complete_timeline |
| `Action_BallCarry` | 214 | 268 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 193 | 111 | inferred_complete_timeline |
| `Action_None` | 196 | 209 | 14 | inferred_complete_timeline |
| `Action_None` | 218 | 222 | 5 | inferred_complete_timeline |
| `Action_None` | 226 | 242 | 17 | inferred_complete_timeline |
| `Action_None` | 248 | 271 | 24 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 291 | 13 | inferred_complete_timeline |
| `Action_None` | 293 | 297 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 241 | 159 | inferred_complete_timeline |
| `Action_None` | 245 | 248 | 4 | inferred_complete_timeline |
| `Action_None` | 255 | 299 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 299 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 259 | 177 | inferred_complete_timeline |
| `Action_None` | 269 | 299 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_DownBlock` | 85 | 131 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 138 | 152 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 167 | 170 | 4 | inferred_complete_timeline |
| `Action_None` | 174 | 181 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_DownBlock` | 85 | 170 | 86 | inferred_complete_timeline |
| `Action_None` | 171 | 242 | 72 | inferred_complete_timeline |
| `Action_None` | 245 | 247 | 3 | inferred_complete_timeline |
| `Action_None` | 253 | 256 | 4 | inferred_complete_timeline |
| `Action_None` | 262 | 299 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_BallSnap` | 83 | 100 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 101 | 101 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 114 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PullBlock` | 85 | 141 | 57 | inferred_complete_timeline |
| `Action_PullBlock` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 160 | 165 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 167 | 169 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 135 | 53 | inferred_complete_timeline |
| `Action_None` | 137 | 145 | 9 | inferred_complete_timeline |
| `Action_None` | 147 | 156 | 10 | inferred_complete_timeline |
| `Action_None` | 158 | 260 | 103 | inferred_complete_timeline |
| `Action_None` | 262 | 265 | 4 | inferred_complete_timeline |
| `Action_None` | 270 | 299 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 156 | 74 | inferred_complete_timeline |
| `Action_None` | 160 | 211 | 52 | inferred_complete_timeline |
| `Action_None` | 214 | 218 | 5 | inferred_complete_timeline |
| `Action_None` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 85 | 170 | 86 | inferred_complete_timeline |
| `Action_None` | 171 | 299 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 129 | 47 | inferred_complete_timeline |
| `Action_None` | 131 | 152 | 22 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 178 | 20 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 260 | 76 | inferred_complete_timeline |
| `Action_None` | 262 | 266 | 5 | inferred_complete_timeline |
| `Action_None` | 270 | 299 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 156 | 74 | inferred_complete_timeline |
| `Action_None` | 160 | 207 | 48 | inferred_complete_timeline |
| `Action_None` | 212 | 265 | 54 | inferred_complete_timeline |
| `Action_None` | 271 | 299 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 148 | 66 | inferred_complete_timeline |
| `Action_None` | 150 | 260 | 111 | inferred_complete_timeline |
| `Action_None` | 262 | 299 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 299 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 154 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 193 | 111 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |
| `Action_None` | 228 | 263 | 36 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_None` | 276 | 281 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 218 | 136 | inferred_complete_timeline |
| `Action_None` | 223 | 273 | 51 | inferred_complete_timeline |
| `Action_None` | 275 | 289 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 221 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 299 | 217 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 64–176 | 74 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 66–67 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 123–142 | 9 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 141–142 | 2 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 167–299 | 133 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 175–177 | 3 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 179–299 | 121 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 180–299 | 117 | 3 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 186–299 | 85 | 5 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 202–299 | 15 | 4 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 202–278 | 71 | 2 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 245–248 | 4 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 255–299 | 33 | 4 | Undefined position; Undefined team |
| `38` | `61` | Position_Unknown | Team_Unknown | 275–276 | 2 | 1 | Undefined position; Undefined team |
| `39` | `64` | Position_Unknown | Team_Unknown | 297–299 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [83–100], lower_priority='Action_DownBlock' annotated_start=85, effective_Action_DownBlock_start=101.
- ⚠️ Action 'Action_None' range [83-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-211] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-259] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-193] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-209] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-242] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-271] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-291] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-299] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-260] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-211] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [214-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [85-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [138-152] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [167-170] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-181] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-218] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-273] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-289] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-156] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-207] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-265] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-129] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-260] for track '11' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-135] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-156] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-260] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-193] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-263] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-281] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-241] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [85-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-242] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-154] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-299] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '19' starts at frame 101, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [101-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [85-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [148-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [160-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [167-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-299] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-256] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-266] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-214] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-240] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-255] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-299] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-208] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-208] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-278] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-276] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-293] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '39' has 1 frames without a visible bounding box.
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