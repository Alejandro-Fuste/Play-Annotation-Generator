# Play-Annotation-Generator Annotation Review — JetSweep_239

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_239`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | DT1 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | WR2 | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 162 |
| ✅ EXACT | `Action_JetMotion` | WR3 | `3` | `2` | 51 | START | 51 | 188 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | DT1 | `13` | `12` | 163 | START | 167 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | WR2 | `10` | `9` | 164 | START | 164 | 207 |
| ✅ EXACT | `Action_ZoneBlock` | C | `15` | `14` | 164 | START | 164 | 186 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `16` | 164 | START | 164 | 327 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 164 | START | 164 | 327 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 164 | START | 164 | 171 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `21` | `20` | 164 | START | 164 | 234 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 177 | END | 163 | 177 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 184 | START | 184 | 188 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `3` | `2` | 189 | START | 189 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 327 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_SnapReceive` | 163 | 177 | 15 | inferred_complete_timeline |
| `Action_None` | 178 | 183 | 6 | inferred_complete_timeline |
| `Action_Toss` | 184 | 188 | 5 | inferred_complete_timeline |
| `Action_None` | 189 | 244 | 56 | inferred_complete_timeline |
| `Action_None` | 246 | 359 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 359 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 359 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_LeadBlock` | 164 | 207 | 44 | inferred_complete_timeline |
| `Action_LeadBlock` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_LeadBlock` | 217 | 327 | 111 | inferred_complete_timeline |
| `Action_None` | 328 | 359 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_JetMotion` | 51 | 188 | 138 | inferred_complete_timeline |
| `Action_BallCarry` | 189 | 359 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 348 | 186 | inferred_complete_timeline |
| `Action_None` | 352 | 355 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 327 | 164 | inferred_complete_timeline |
| `Action_None` | 328 | 359 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 171 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 266 | 94 | inferred_complete_timeline |
| `Action_ZoneBlock` | 271 | 273 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 276 | 280 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 292 | 327 | 36 | inferred_complete_timeline |
| `Action_None` | 328 | 359 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 186 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 327 | 164 | inferred_complete_timeline |
| `Action_None` | 328 | 359 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 234 | 71 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 196 | 34 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 239 | 33 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 359 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 230 | 68 | inferred_complete_timeline |
| `Action_None` | 233 | 292 | 60 | inferred_complete_timeline |
| `Action_None` | 294 | 313 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 161 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 172 | 177 | 6 | inferred_complete_timeline |
| `Action_None` | 178 | 237 | 60 | inferred_complete_timeline |
| `Action_None` | 240 | 244 | 5 | inferred_complete_timeline |
| `Action_None` | 246 | 359 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 162 | 45 | inferred_complete_timeline |
| `Action_None` | 163 | 189 | 27 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 197 | 359 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 244 | 82 | inferred_complete_timeline |
| `Action_None` | 246 | 269 | 24 | inferred_complete_timeline |
| `Action_None` | 271 | 359 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 359 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 359 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 359 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 325 | 163 | inferred_complete_timeline |
| `Action_None` | 330 | 332 | 3 | inferred_complete_timeline |
| `Action_None` | 336 | 340 | 5 | inferred_complete_timeline |
| `Action_None` | 350 | 355 | 6 | inferred_complete_timeline |
| `Action_None` | 357 | 359 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 359 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 181 | 19 | inferred_complete_timeline |
| `Action_None` | 184 | 196 | 13 | inferred_complete_timeline |
| `Action_None` | 200 | 251 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 166–205 | 15 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 179–187 | 5 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 212–359 | 146 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 220–253 | 20 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 232–240 | 9 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 239–359 | 121 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 260–359 | 100 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 311–359 | 49 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 314–315 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 329–354 | 13 | 3 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 341–342 | 2 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 357–359 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 164 frames exceeds threshold 90 frames [start=164, end=327].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '9' (WR2) duration 164 frames exceeds threshold 90 frames [start=164, end=327].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (RG) duration 164 frames exceeds threshold 90 frames [start=164, end=327].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 164 frames exceeds threshold 90 frames [start=164, end=327].
- ⚠️ Action 'Action_JetMotion' range [51-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-244] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-348] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-239] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [164-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [209-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-244] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-325] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-355] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-161] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [167-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-237] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-181] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-196] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-251] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-186] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-230] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-292] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-313] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-266] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [271-273] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [276-280] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-234] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-189] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-238] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-359] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-240] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-359] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-354] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '33' has 1 frames without a visible bounding box.
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

</details>