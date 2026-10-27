# Play-Annotation-Generator Annotation Review — Counter_377

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_377`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 236
- **Validation Warnings:** 280
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 212
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB2 | defense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `27` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB2 | defense | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 102 |
| ✅ EXACT | `Action_BallSnap` | CB2 | `7` | `6` | 103 | START | 103 | 105 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | LT | `14` | `13` | 106 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `27` | `23` | 106 | START | 106 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB2 | `7` | `6` | 106 | START | 106 | 118 |
| ✅ EXACT | `Action_PullBlock` | RG | `6` | `5` | 106 | START | 106 | 140 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `11` | `10` | 106 | START | 106 | 186 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 119 | END | 103 | 119 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 134 | START | 134 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `11` | 156 | START | 156 | 165 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 186 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_SnapReceive` | 103 | 119 | 17 | inferred_complete_timeline |
| `Action_None` | 120 | 133 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 134 | 146 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 155 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 156 | 165 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 167 | 186 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 195 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 232 | 35 | inferred_complete_timeline |
| `Action_BallCarry` | 239 | 255 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 258 | 259 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 147 | 45 | inferred_complete_timeline |
| `Action_None` | 157 | 205 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 150 | 48 | inferred_complete_timeline |
| `Action_None` | 156 | 166 | 11 | inferred_complete_timeline |
| `Action_None` | 178 | 189 | 12 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |
| `Action_None` | 214 | 216 | 3 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 115 | 13 | inferred_complete_timeline |
| `Action_None` | 119 | 158 | 40 | inferred_complete_timeline |
| `Action_None` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_None` | 186 | 225 | 40 | inferred_complete_timeline |
| `Action_None` | 229 | 231 | 3 | inferred_complete_timeline |
| `Action_None` | 235 | 268 | 34 | inferred_complete_timeline |
| `Action_None` | 270 | 281 | 12 | inferred_complete_timeline |
| `Action_None` | 283 | 298 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 106 | 186 | 81 | inferred_complete_timeline |
| `Action_None` | 187 | 229 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 111 | 9 | inferred_complete_timeline |
| `Action_None` | 116 | 125 | 10 | inferred_complete_timeline |
| `Action_None` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_None` | 140 | 147 | 8 | inferred_complete_timeline |
| `Action_None` | 149 | 157 | 9 | inferred_complete_timeline |
| `Action_None` | 175 | 184 | 10 | inferred_complete_timeline |
| `Action_None` | 186 | 194 | 9 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_None` | 227 | 231 | 5 | inferred_complete_timeline |
| `Action_None` | 233 | 265 | 33 | inferred_complete_timeline |
| `Action_None` | 273 | 286 | 14 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PullBlock` | 106 | 140 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 138 | 36 | inferred_complete_timeline |
| `Action_None` | 140 | 147 | 8 | inferred_complete_timeline |
| `Action_None` | 157 | 188 | 32 | inferred_complete_timeline |
| `Action_None` | 192 | 213 | 22 | inferred_complete_timeline |
| `Action_None` | 218 | 295 | 78 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 38 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 102 | 59 | inferred_complete_timeline |
| `Action_None` | 103 | 108 | 6 | inferred_complete_timeline |
| `Action_None` | 151 | 203 | 53 | inferred_complete_timeline |
| `Action_None` | 205 | 214 | 10 | inferred_complete_timeline |
| `Action_None` | 217 | 268 | 52 | inferred_complete_timeline |
| `Action_None` | 271 | 279 | 9 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 35 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 81 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 101 | 19 | inferred_complete_timeline |
| `Action_None` | 110 | 195 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 166 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 72 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 102 | 8 | inferred_complete_timeline |
| `Action_None` | 103 | 109 | 7 | inferred_complete_timeline |
| `Action_None` | 113 | 144 | 32 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 161 | 9 | inferred_complete_timeline |
| `Action_None` | 165 | 177 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 148 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 152 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 149 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_BallSnap` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 106 | 118 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 141 | 146 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 102 | 86 | inferred_complete_timeline |
| `Action_None` | 103 | 115 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `22` | Position_Unknown | Team_Unknown | 8–298 | 274 | 9 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 9–116 | 100 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 17–23 | 7 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 19–104 | 59 | 5 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 85–174 | 69 | 6 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 117–119 | 3 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 121–296 | 134 | 8 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 124–298 | 110 | 11 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 129–244 | 28 | 4 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 130–198 | 42 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 134–252 | 78 | 8 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 135–299 | 157 | 4 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 136–275 | 105 | 10 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 156–299 | 139 | 4 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 159–193 | 20 | 3 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 182–299 | 90 | 4 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 183–192 | 9 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 190–203 | 12 | 2 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 212–293 | 81 | 2 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 219–233 | 11 | 4 | Undefined position; Undefined team |
| `39` | `65` | Position_Unknown | Team_Unknown | 227–298 | 65 | 6 | Undefined position; Undefined team |
| `40` | `67` | Position_Unknown | Team_Unknown | 234–299 | 36 | 6 | Undefined position; Undefined team |
| `41` | `68` | Position_Unknown | Team_Unknown | 239–240 | 2 | 1 | Undefined position; Undefined team |
| `42` | `71` | Position_Unknown | Team_Unknown | 246–249 | 4 | 1 | Undefined position; Undefined team |
| `43` | `73` | Position_Unknown | Team_Unknown | 246–298 | 43 | 7 | Undefined position; Undefined team |
| `44` | `75` | Position_Unknown | Team_Unknown | 258–299 | 36 | 4 | Undefined position; Undefined team |
| `45` | `76` | Position_Unknown | Team_Unknown | 259–299 | 25 | 3 | Undefined position; Undefined team |
| `46` | `77` | Position_Unknown | Team_Unknown | 262–264 | 3 | 1 | Undefined position; Undefined team |
| `47` | `78` | Position_Unknown | Team_Unknown | 263–281 | 16 | 2 | Undefined position; Undefined team |
| `48` | `79` | Position_Unknown | Team_Unknown | 270–299 | 17 | 5 | Undefined position; Undefined team |
| `49` | `80` | Position_Unknown | Team_Unknown | 271–299 | 29 | 1 | Undefined position; Undefined team |
| `50` | `81` | Position_Unknown | Team_Unknown | 273–275 | 3 | 1 | Undefined position; Undefined team |
| `51` | `82` | Position_Unknown | Team_Unknown | 291–292 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `14` (LT)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `27` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 211 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 756: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '13' has invalid range: start=106, end=105. Clamping end to start.
- ⚠️ Action 'Action_None' range [103-138] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-213] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-295] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-148] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-150] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-166] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-189] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-152] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-149] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [106-140] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [106-118] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [121-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [141-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-166] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-115] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-158] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-225] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-268] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-281] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-298] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [134-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [106-186] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-229] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [156-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [167-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-232] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [239-255] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-259] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-147] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-205] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-157] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-184] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-194] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-265] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-286] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-115] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-35] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-81] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-101] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-195] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-108] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-214] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-268] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-279] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-109] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-177] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-116] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-194] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-221] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-234] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-255] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-268] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-298] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-116] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-23] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-23] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-89] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [106-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [125-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [128-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [132-174] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-175] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-252] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-264] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-278] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-296] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-192] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-219] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-264] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-272] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-298] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-142] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-158] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-178] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-202] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-248] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-145] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-264] for track '30' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-188] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-218] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-231] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-245] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-194] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-207] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-299] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-171] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-199] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-222] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-293] for track '37' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-263] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-276] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-288] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-243] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-288] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-263] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-298] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-268] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-281] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-299] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-284] for track '45' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-281] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-299] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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