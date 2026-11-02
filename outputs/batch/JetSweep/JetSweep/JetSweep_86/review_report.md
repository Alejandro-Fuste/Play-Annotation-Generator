# Play-Annotation-Generator Annotation Review — JetSweep_86

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_86`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 138
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 111
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 82 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `3` | `2` | 44 | START | 44 | 112 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 83 | START | 83 | 95 |
| ✅ EXACT | `Action_LeadBlock` | RB | `6` | `5` | 89 | START | 89 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE | `14` | `13` | 89 | START | 89 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `11` | 89 | START | 89 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `18` | 89 | START | 89 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 89 | START | 89 | 102 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `21` | `20` | 89 | START | 96 | 104 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 95 | END | 83 | 95 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 103 | START | 103 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `21` | `20` | 105 | START | 105 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `3` | `2` | 113 | START | 113 | 164 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 145 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_SnapReceive` | 83 | 95 | 13 | inferred_complete_timeline |
| `Action_None` | 96 | 102 | 7 | inferred_complete_timeline |
| `Action_Toss` | 103 | 112 | 10 | inferred_complete_timeline |
| `Action_None` | 113 | 120 | 8 | inferred_complete_timeline |
| `Action_None` | 122 | 230 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_LeadBlock` | 89 | 145 | 57 | inferred_complete_timeline |
| `Action_None` | 146 | 153 | 8 | inferred_complete_timeline |
| `Action_None` | 156 | 164 | 9 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 329 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_JetMotion` | 44 | 112 | 69 | inferred_complete_timeline |
| `Action_BallCarry` | 113 | 164 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 261 | 87 | inferred_complete_timeline |
| `Action_BallCarry` | 265 | 297 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 308 | 311 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 154 | 72 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 173 | 179 | 7 | inferred_complete_timeline |
| `Action_None` | 183 | 188 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_SealBlock` | 89 | 136 | 48 | inferred_complete_timeline |
| `Action_SealBlock` | 145 | 164 | 20 | inferred_complete_timeline |
| `Action_SealBlock` | 168 | 267 | 100 | inferred_complete_timeline |
| `Action_SealBlock` | 274 | 284 | 11 | inferred_complete_timeline |
| `Action_SealBlock` | 292 | 293 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 102 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 134 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 141 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 145 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 179 | 34 | inferred_complete_timeline |
| `Action_None` | 183 | 227 | 45 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 249 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_BallSnap` | 83 | 95 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 104 | 9 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 105 | 110 | 6 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 112 | 145 | 34 | inferred_complete_timeline |
| `Action_None` | 146 | 223 | 78 | inferred_complete_timeline |
| `Action_None` | 233 | 247 | 15 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 265 | 3 | inferred_complete_timeline |
| `Action_None` | 273 | 274 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 288 | 10 | inferred_complete_timeline |
| `Action_None` | 295 | 300 | 6 | inferred_complete_timeline |
| `Action_None` | 302 | 310 | 9 | inferred_complete_timeline |
| `Action_None` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 94 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 114 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 145 | 25 | inferred_complete_timeline |
| `Action_None` | 146 | 166 | 21 | inferred_complete_timeline |
| `Action_None` | 169 | 252 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 134 | 52 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 268 | 130 | inferred_complete_timeline |
| `Action_None` | 277 | 329 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 174 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 118 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 112 | 30 | inferred_complete_timeline |
| `Action_None` | 127 | 134 | 8 | inferred_complete_timeline |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 175 | 93 | inferred_complete_timeline |
| `Action_None` | 185 | 329 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 145 | 63 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 289 | 207 | inferred_complete_timeline |
| `Action_None` | 292 | 329 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 158 | 76 | inferred_complete_timeline |
| `Action_None` | 167 | 175 | 9 | inferred_complete_timeline |
| `Action_None` | 179 | 286 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 210 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 231 | 149 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 196 | 114 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 87–329 | 219 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 110–329 | 217 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 145–329 | 177 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 164–245 | 71 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 172–203 | 20 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 184–279 | 93 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 206–328 | 114 | 5 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 223–287 | 57 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 249–251 | 3 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 250–317 | 68 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 293–310 | 18 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 294–298 | 5 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 295–302 | 6 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 315–316 | 2 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 320–329 | 9 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 322–329 | 7 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 323–329 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SealBlock` and target `14` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (5 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `21` (C): Annotated start 89 != Inferred start 96
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 102 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [83–95], lower_priority='Action_ZoneBlock' annotated_start=89, effective_Action_ZoneBlock_start=96.
- ⚠️ Action 'Action_None' range [83-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [175-261] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [265-297] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [308-311] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-153] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-164] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-239] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-231] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-268] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-289] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-166] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-252] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-286] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [89-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [145-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [168-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [274-284] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [292-293] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-196] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-94] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-249] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [105-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-223] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-247] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-288] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-300] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-310] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-269] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-329] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-251] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-325] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-215] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-245] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-203] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-268] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-275] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-256] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-294] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-321] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-262] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-279] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-287] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-317] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-310] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-298] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-325] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '36' has 1 frames without a visible bounding box.
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