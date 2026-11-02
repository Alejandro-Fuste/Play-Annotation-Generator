# Play-Annotation-Generator Annotation Review — JetSweep_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_70`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Toss` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 73 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `2` | `1` | 22 | START | 22 | 105 |
| ✅ EXACT | `Action_BallSnap` | C | `6` | `5` | 74 | START | 74 | 89 |
| ✅ EXACT | `Action_LeadBlock` | RB | `14` | `13` | 80 | START | 80 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `14` | 80 | START | 80 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `15` | 80 | START | 80 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `16` | 80 | START | 80 | 131 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 80 | START | 80 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `6` | `5` | 80 | START | 90 | 131 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 89 | END | 74 | 89 |
| ✅ EXACT | `Action_Toss` | QB | `19` | `18` | 92 | START | 92 | 105 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `2` | `1` | 106 | START | 106 | 228 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 174 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 89 | 16 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_Toss` | 92 | 105 | 14 | inferred_complete_timeline |
| `Action_None` | 106 | 299 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_LeadBlock` | 80 | 174 | 95 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_JetMotion` | 22 | 105 | 84 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 228 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 299 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 299 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 151 | 78 | inferred_complete_timeline |
| `Action_None` | 164 | 167 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 174 | 95 | inferred_complete_timeline |
| `Action_None` | 175 | 196 | 22 | inferred_complete_timeline |
| `Action_None` | 198 | 243 | 46 | inferred_complete_timeline |
| `Action_None` | 245 | 248 | 4 | inferred_complete_timeline |
| `Action_None` | 259 | 263 | 5 | inferred_complete_timeline |
| `Action_None` | 270 | 276 | 7 | inferred_complete_timeline |
| `Action_None` | 287 | 299 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 174 | 80 | inferred_complete_timeline |
| `Action_None` | 175 | 191 | 17 | inferred_complete_timeline |
| `Action_None` | 199 | 248 | 50 | inferred_complete_timeline |
| `Action_None` | 250 | 273 | 24 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 89 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 131 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 174 | 32 | inferred_complete_timeline |
| `Action_None` | 175 | 272 | 98 | inferred_complete_timeline |
| `Action_None` | 277 | 279 | 3 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 118 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 174 | 50 | inferred_complete_timeline |
| `Action_None` | 175 | 275 | 101 | inferred_complete_timeline |
| `Action_None` | 277 | 281 | 5 | inferred_complete_timeline |
| `Action_None` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_None` | 290 | 298 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 131 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 142 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 150 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 174 | 21 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 266 | 193 | inferred_complete_timeline |
| `Action_None` | 269 | 271 | 3 | inferred_complete_timeline |
| `Action_None` | 288 | 289 | 2 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 299 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 240 | 167 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 257 | 6 | inferred_complete_timeline |
| `Action_None` | 259 | 263 | 5 | inferred_complete_timeline |
| `Action_None` | 265 | 299 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 132 | 59 | inferred_complete_timeline |
| `Action_None` | 135 | 143 | 9 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 152 | 5 | inferred_complete_timeline |
| `Action_None` | 167 | 172 | 6 | inferred_complete_timeline |
| `Action_None` | 175 | 193 | 19 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 299 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 219 | 146 | inferred_complete_timeline |
| `Action_None` | 221 | 258 | 38 | inferred_complete_timeline |
| `Action_None` | 264 | 281 | 18 | inferred_complete_timeline |
| `Action_None` | 288 | 293 | 6 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 191 | 118 | inferred_complete_timeline |
| `Action_None` | 198 | 201 | 4 | inferred_complete_timeline |
| `Action_None` | 207 | 299 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 299 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 299 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 278 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 299 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 292 | 219 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 83–133 | 44 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 216–219 | 4 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 218–222 | 5 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 234–299 | 65 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 271–286 | 9 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 276–279 | 4 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 95 frames exceeds threshold 90 frames [start=80, end=174].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (C) duration 95 frames exceeds threshold 90 frames [start=80, end=174].
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [74–89], lower_priority='Action_ZoneBlock' annotated_start=80, effective_Action_ZoneBlock_start=90.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '13' (RB) duration 95 frames exceeds threshold 90 frames [start=80, end=174].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 95 frames exceeds threshold 90 frames [start=80, end=174].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LG) duration 95 frames exceeds threshold 90 frames [start=80, end=174].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (RT) duration 95 frames exceeds threshold 90 frames [start=80, end=174].
- ⚠️ Action 'Action_BallCarry' range [106-228] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-151] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-243] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-276] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-266] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-131] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-272] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-132] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-143] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-193] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-292] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-118] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-275] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-298] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-85] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-248] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-273] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-131] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-142] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-278] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-240] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-257] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-219] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-258] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-281] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-293] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-191] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-104] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-219] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-291] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-277] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '28' has 1 frames without a visible bounding box.
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

</details>