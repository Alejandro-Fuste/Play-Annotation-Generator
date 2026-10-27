# Play-Annotation-Generator Annotation Review — CrackToss_74

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_74`
- **Frame Range:** 0 to 249 (250 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 249
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 142
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 118
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | WR4 | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | offense | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_Toss` | QB | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 139 |
| ✅ EXACT | `Action_BallSnap` | WR4 | `4` | `3` | 106 | START | 106 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | `3` | `2` | 109 | START | 109 | 156 |
| ✅ EXACT | `Action_PullBlock` | RT | `10` | `9` | 109 | START | 109 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `20` | `19` | 109 | START | 109 | 156 |
| ✅ EXACT | `Action_SnapReceive` | QB | `22` | `21` | 117 | END | 106 | 117 |
| ✅ EXACT | `Action_Toss` | QB | `22` | `21` | 123 | START | 123 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `5` | `4` | 140 | START | 140 | 237 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 167 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_SnapReceive` | 106 | 117 | 12 | inferred_complete_timeline |
| `Action_None` | 118 | 122 | 5 | inferred_complete_timeline |
| `Action_Toss` | 123 | 139 | 17 | inferred_complete_timeline |
| `Action_None` | 140 | 156 | 17 | inferred_complete_timeline |
| `Action_None` | 158 | 226 | 69 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 161 | 56 | inferred_complete_timeline |
| `Action_None` | 163 | 227 | 65 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_BallCarry` | 140 | 237 | 98 | inferred_complete_timeline |
| `Action_BallCarry` | 239 | 249 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_CrackBlock` | 109 | 156 | 48 | inferred_complete_timeline |
| `Action_CrackBlock` | 158 | 163 | 6 | inferred_complete_timeline |
| `Action_CrackBlock` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 168 | 1 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_None` | 181 | 184 | 4 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 192 | 3 | inferred_complete_timeline |
| `Action_None` | 194 | 207 | 14 | inferred_complete_timeline |
| `Action_None` | 210 | 233 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 156 | 51 | inferred_complete_timeline |
| `Action_None` | 158 | 163 | 6 | inferred_complete_timeline |
| `Action_None` | 166 | 183 | 18 | inferred_complete_timeline |
| `Action_None` | 185 | 238 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_BallSnap` | 106 | 117 | 12 | inferred_complete_timeline |
| `Action_None` | 118 | 191 | 74 | inferred_complete_timeline |
| `Action_None` | 195 | 249 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 142 | 37 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 175 | 5 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 249 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 156 | 51 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 200 | 249 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 123 | 18 | inferred_complete_timeline |
| `Action_None` | 126 | 163 | 38 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 192 | 3 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_None` | 214 | 249 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PullBlock` | 109 | 156 | 48 | inferred_complete_timeline |
| `Action_PullBlock` | 158 | 163 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 168 | 1 | inferred_complete_timeline |
| `Action_None` | 170 | 176 | 7 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 192 | 3 | inferred_complete_timeline |
| `Action_None` | 194 | 203 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PullBlock` | 109 | 167 | 59 | inferred_complete_timeline |
| `Action_None` | 168 | 175 | 8 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 249 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 236 | 131 | inferred_complete_timeline |
| `Action_None` | 241 | 249 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 156 | 51 | inferred_complete_timeline |
| `Action_None` | 158 | 168 | 11 | inferred_complete_timeline |
| `Action_None` | 170 | 179 | 10 | inferred_complete_timeline |
| `Action_None` | 185 | 191 | 7 | inferred_complete_timeline |
| `Action_None` | 194 | 229 | 36 | inferred_complete_timeline |
| `Action_None` | 231 | 236 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 175 | 70 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 207 | 4 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 249 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 156 | 51 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 204 | 11 | inferred_complete_timeline |
| `Action_None` | 206 | 211 | 6 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 222 | 5 | inferred_complete_timeline |
| `Action_None` | 225 | 227 | 3 | inferred_complete_timeline |
| `Action_None` | 231 | 249 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 156 | 51 | inferred_complete_timeline |
| `Action_None` | 158 | 175 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 249 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 249 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 249 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 156 | 51 | inferred_complete_timeline |
| `Action_None` | 158 | 169 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 249 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 239 | 134 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 30–31 | 2 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 191–249 | 58 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 193–249 | 47 | 5 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 213–236 | 24 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 224–236 | 11 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 242–249 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 106 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 249 as fallback play end.
- ⚠️ Action 'Action_None' range [106-156] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-183] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-238] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [109-156] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [158-163] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '2' starts at frame 168, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [168-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-233] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [140-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [239-249] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-249] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-156] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-168] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-179] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-229] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-175] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [109-167] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-249] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-249] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-169] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-163] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-161] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-227] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-239] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-175] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [109-156] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [158-163] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 168, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [168-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-203] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-156] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-226] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-207] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-220] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-249] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-236] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-249] for track '27' has 3 frames without a visible bounding box.
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

</details>