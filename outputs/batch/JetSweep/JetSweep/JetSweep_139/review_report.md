# Play-Annotation-Generator Annotation Review — JetSweep_139

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_139`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 139
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 112
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR2 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_LeadBlock` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `1` | `0` |
| ✅ EXACT | `Action_Toss` | CB2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB1 | defense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR2 | `2` | `1` | 35 | START | 35 | 233 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 70 | START | 70 | 81 |
| ✅ EXACT | `Action_LeadBlock` | QB | `8` | `7` | 71 | START | 71 | 147 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `9` | 71 | START | 71 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 71 | START | 82 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `16` | 71 | START | 71 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `18` | 71 | START | 71 | 147 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `19` | 71 | START | 71 | 130 |
| ✅ EXACT | `Action_SnapReceive` | RB | `1` | `0` | 81 | END | 70 | 81 |
| ✅ EXACT | `Action_Toss` | CB2 | `11` | `10` | 85 | START | 85 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB1 | `6` | `5` | 94 | START | 94 | 200 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 147 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_LeadBlock` | 71 | 147 | 77 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 163 | 13 | inferred_complete_timeline |
| `Action_None` | 168 | 180 | 13 | inferred_complete_timeline |
| `Action_None` | 185 | 225 | 41 | inferred_complete_timeline |
| `Action_None` | 232 | 359 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_SnapReceive` | 70 | 81 | 12 | inferred_complete_timeline |
| `Action_None` | 82 | 359 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 150 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–335
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_JetMotion` | 35 | 233 | 199 | inferred_complete_timeline |
| `Action_JetMotion` | 236 | 262 | 27 | inferred_complete_timeline |
| `Action_JetMotion` | 265 | 335 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 147 | 78 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 177 | 10 | inferred_complete_timeline |
| `Action_None` | 180 | 200 | 21 | inferred_complete_timeline |
| `Action_None` | 211 | 311 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 147 | 77 | inferred_complete_timeline |
| `Action_None` | 148 | 164 | 17 | inferred_complete_timeline |
| `Action_None` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_None` | 183 | 227 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 130 | 60 | inferred_complete_timeline |
| `Action_None` | 157 | 359 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_BallSnap` | 70 | 81 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 90 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 136 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 146 | 8 | inferred_complete_timeline |
| `Action_None` | 159 | 260 | 102 | inferred_complete_timeline |
| `Action_None` | 266 | 359 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 88 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 117 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 147 | 26 | inferred_complete_timeline |
| `Action_None` | 148 | 359 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 104 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 3–124
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 69 | 67 | inferred_complete_timeline |
| `Action_None` | 70 | 99 | 30 | inferred_complete_timeline |
| `Action_None` | 108 | 124 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 96 | 27 | inferred_complete_timeline |
| `Action_None` | 101 | 117 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 69 | 46 | inferred_complete_timeline |
| `Action_None` | 70 | 359 | 290 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 131 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 131 | 62 | inferred_complete_timeline |
| `Action_None` | 139 | 359 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 156 | 87 | inferred_complete_timeline |
| `Action_None` | 158 | 163 | 6 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 236 | 58 | inferred_complete_timeline |
| `Action_None` | 238 | 262 | 25 | inferred_complete_timeline |
| `Action_None` | 264 | 311 | 48 | inferred_complete_timeline |
| `Action_None` | 313 | 359 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 156 | 87 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 359 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 200 | 107 | inferred_complete_timeline |
| `Action_BallCarry` | 211 | 215 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 220 | 232 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_Toss` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_None` | 94 | 359 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 233 | 164 | inferred_complete_timeline |
| `Action_None` | 250 | 259 | 10 | inferred_complete_timeline |
| `Action_None` | 264 | 359 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 95 | 26 | inferred_complete_timeline |
| `Action_None` | 99 | 177 | 79 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 359 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 2–359 | 322 | 11 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 103–359 | 253 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 124–187 | 64 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 168–359 | 191 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 187–359 | 172 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 241–242 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 244–272 | 29 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 246–359 | 108 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 247–359 | 101 | 6 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 270–276 | 6 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 282–359 | 69 | 3 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 286–343 | 28 | 7 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 331–359 | 29 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 339–340 | 2 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 340–347 | 5 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 344–359 | 13 | 3 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 353–354 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [70–81], lower_priority='Action_ZoneBlock' annotated_start=71, effective_Action_ZoneBlock_start=82.
- ⚠️ Action 'Action_JetMotion' range [35-233] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [236-262] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [265-335] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-96] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-117] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-233] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-259] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [211-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-156] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-359] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [71-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-225] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-177] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-359] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-90] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-146] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-260] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-156] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-236] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-262] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-311] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-117] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-177] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-311] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-164] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-227] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-130] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-153] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-219] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-124] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-349] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-187] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-260] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-262] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-272] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-262] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-304] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-317] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-294] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-324] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-347] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-353] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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