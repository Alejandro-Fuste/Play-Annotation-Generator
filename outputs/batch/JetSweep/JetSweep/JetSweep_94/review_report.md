# Play-Annotation-Generator Annotation Review — JetSweep_94

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_94`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 125
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `8` | `7` |
| ✅ EXACT | `Action_BallSnap` | LB2 | defense | `9` | `8` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `23` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT2 | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `20` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 0 | START | 39 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `8` | `7` | 41 | START | 41 | 109 |
| ✅ EXACT | `Action_BallSnap` | LB2 | `9` | `8` | 81 | START | 81 | 95 |
| ✅ EXACT | `Action_LeadBlock` | RB | `7` | `6` | 86 | START | 86 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `16` | 86 | START | 86 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `17` | 86 | START | 86 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 86 | START | 86 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `21` | `20` | 86 | START | 86 | 165 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `23` | `21` | 86 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 95 | END | 81 | 95 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 98 | START | 98 | 109 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT2 | `14` | `13` | 103 | START | 103 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `8` | `7` | 110 | START | 110 | 167 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 165 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_SnapReceive` | 81 | 95 | 15 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_Toss` | 98 | 109 | 12 | inferred_complete_timeline |
| `Action_None` | 110 | 140 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_LeadBlock` | 86 | 165 | 80 | inferred_complete_timeline |
| `Action_None` | 166 | 210 | 45 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 359 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_JetMotion` | 41 | 109 | 69 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 167 | 58 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 185 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 189 | 359 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 162 | 82 | inferred_complete_timeline |
| `Action_None` | 164 | 172 | 9 | inferred_complete_timeline |
| `Action_None` | 174 | 179 | 6 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 294 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 138 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 165 | 80 | inferred_complete_timeline |
| `Action_None` | 166 | 304 | 139 | inferred_complete_timeline |
| `Action_None` | 306 | 359 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 98 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 165 | 58 | inferred_complete_timeline |
| `Action_None` | 166 | 359 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 103 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 122 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 137 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 165 | 22 | inferred_complete_timeline |
| `Action_None` | 166 | 183 | 18 | inferred_complete_timeline |
| `Action_None` | 196 | 206 | 11 | inferred_complete_timeline |
| `Action_None` | 214 | 255 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 39–83
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 39 | 52 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 83 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 128 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 165 | 36 | inferred_complete_timeline |
| `Action_None` | 166 | 311 | 146 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 104 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 132 | 52 | inferred_complete_timeline |
| `Action_None` | 134 | 191 | 58 | inferred_complete_timeline |
| `Action_None` | 195 | 245 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 340 | 260 | inferred_complete_timeline |
| `Action_None` | 342 | 359 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 103 | 165 | 63 | inferred_complete_timeline |
| `Action_None` | 166 | 184 | 19 | inferred_complete_timeline |
| `Action_None` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_None` | 209 | 229 | 21 | inferred_complete_timeline |
| `Action_None` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_None` | 239 | 270 | 32 | inferred_complete_timeline |
| `Action_None` | 273 | 296 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 139 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_BallSnap` | 81 | 95 | 15 | inferred_complete_timeline |
| `Action_None` | 96 | 359 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 128 | 48 | inferred_complete_timeline |
| `Action_None` | 141 | 248 | 108 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 126 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 328 | 248 | inferred_complete_timeline |
| `Action_None` | 331 | 333 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 247 | 167 | inferred_complete_timeline |
| `Action_None` | 249 | 274 | 26 | inferred_complete_timeline |
| `Action_None` | 276 | 286 | 11 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 298 | 3 | inferred_complete_timeline |
| `Action_None` | 304 | 307 | 4 | inferred_complete_timeline |
| `Action_None` | 309 | 311 | 3 | inferred_complete_timeline |
| `Action_None` | 320 | 359 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 189 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 106–275 | 164 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 109–359 | 238 | 6 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 145–297 | 153 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 153–359 | 207 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 155–359 | 203 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 155–182 | 24 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 191–359 | 115 | 5 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 240–358 | 113 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 244–250 | 7 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 247–359 | 113 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 261–349 | 82 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 272–359 | 84 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 287–359 | 65 | 3 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 320–321 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `23` (RG)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=86, end=83. Clamping end to start.
- ⚠️ Action 'Action_None' range [81-162] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-132] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-191] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-245] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-126] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-340] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-185] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-247] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-274] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-286] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-307] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-184] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-270] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-296] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-248] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-328] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-137] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-206] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-255] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-128] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-311] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-294] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-304] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-52] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-187] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-259] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-266] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-263] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-272] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-339] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-297] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-359] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-174] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-230] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-296] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-270] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-338] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-358] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-340] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-350] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-311] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '36' has 1 frames without a visible bounding box.
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

</details>