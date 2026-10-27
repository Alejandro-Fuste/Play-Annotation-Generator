# Play-Annotation-Generator Annotation Review — Counter_267

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_267`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 146
- **Validation Warnings:** 148
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 120
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF2 | defense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | WR1 | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 132 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 130 | START | 130 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF2 | `16` | `15` | 133 | START | 133 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `19` | `18` | 133 | START | 144 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `20` | `19` | 133 | START | 133 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `14` | `13` | 133 | START | 133 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | WR1 | `7` | `6` | 133 | START | 133 | 203 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 143 | END | 130 | 143 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 157 | START | 157 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 171 | START | 171 | 201 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 235 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_SnapReceive` | 130 | 143 | 14 | inferred_complete_timeline |
| `Action_None` | 144 | 156 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 157 | 170 | 14 | inferred_complete_timeline |
| `Action_None` | 171 | 359 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_BallCarry` | 171 | 201 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 209 | 212 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 214 | 216 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 219 | 230 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 133 | 203 | 71 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 206 | 235 | 30 | inferred_complete_timeline |
| `Action_None` | 236 | 359 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 347 | 218 | inferred_complete_timeline |
| `Action_None` | 349 | 358 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 359 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 193 | 64 | inferred_complete_timeline |
| `Action_None` | 195 | 208 | 14 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 242 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 168 | 39 | inferred_complete_timeline |
| `Action_None` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_None` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_None` | 228 | 254 | 27 | inferred_complete_timeline |
| `Action_None` | 263 | 285 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 147 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 209 | 49 | inferred_complete_timeline |
| `Action_DownBlock` | 231 | 235 | 5 | inferred_complete_timeline |
| `Action_None` | 236 | 359 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_BallSnap` | 130 | 143 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 235 | 92 | inferred_complete_timeline |
| `Action_None` | 236 | 286 | 51 | inferred_complete_timeline |
| `Action_None` | 288 | 295 | 8 | inferred_complete_timeline |
| `Action_None` | 299 | 359 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PullBlock` | 133 | 190 | 58 | inferred_complete_timeline |
| `Action_PullBlock` | 199 | 235 | 37 | inferred_complete_timeline |
| `Action_None` | 236 | 296 | 61 | inferred_complete_timeline |
| `Action_None` | 300 | 342 | 43 | inferred_complete_timeline |
| `Action_None` | 345 | 359 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 322 | 193 | inferred_complete_timeline |
| `Action_None` | 324 | 359 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 155 | 26 | inferred_complete_timeline |
| `Action_None` | 163 | 175 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 151 | 22 | inferred_complete_timeline |
| `Action_None` | 153 | 161 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 186 | 57 | inferred_complete_timeline |
| `Action_None` | 188 | 193 | 6 | inferred_complete_timeline |
| `Action_None` | 195 | 197 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 227 | 98 | inferred_complete_timeline |
| `Action_None` | 230 | 348 | 119 | inferred_complete_timeline |
| `Action_None` | 352 | 357 | 6 | inferred_complete_timeline |
| `Action_None` | 359 | 359 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 177 | 48 | inferred_complete_timeline |
| `Action_None` | 182 | 189 | 8 | inferred_complete_timeline |
| `Action_None` | 201 | 359 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 305 | 176 | inferred_complete_timeline |
| `Action_None` | 308 | 314 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 228 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 146 | 17 | inferred_complete_timeline |
| `Action_None` | 149 | 305 | 157 | inferred_complete_timeline |
| `Action_None` | 308 | 345 | 38 | inferred_complete_timeline |
| `Action_None` | 348 | 352 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_None` | 130 | 188 | 59 | inferred_complete_timeline |
| `Action_None` | 190 | 202 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 158 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 235 | 75 | inferred_complete_timeline |
| `Action_None` | 236 | 249 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–197 | 195 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 44–45 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 167–359 | 188 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 198–354 | 135 | 6 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 234–269 | 34 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 239–358 | 112 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 251–359 | 103 | 5 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 252–254 | 3 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 259–284 | 4 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 266–358 | 88 | 5 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 271–352 | 59 | 6 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 275–359 | 65 | 6 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 282–322 | 14 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 283–354 | 52 | 6 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 302–354 | 36 | 4 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 309–359 | 40 | 3 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 356–357 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 107 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 536: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '13' (RG) duration 103 frames exceeds threshold 90 frames [start=133, end=235].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (SAF2) duration 103 frames exceeds threshold 90 frames [start=133, end=235].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (C) duration 103 frames exceeds threshold 90 frames [start=133, end=235].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [130–143], lower_priority='Action_DownBlock' annotated_start=133, effective_Action_DownBlock_start=144.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 103 frames exceeds threshold 90 frames [start=133, end=235].
- ⚠️ Action 'Action_None' range [130-347] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-358] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-206] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [209-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [214-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [219-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-193] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-242] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-305] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-345] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-352] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [133-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-305] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-314] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-186] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-254] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-285] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-322] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-202] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [133-190] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-296] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-342] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-177] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-228] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-286] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-295] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-359] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-359] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-227] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-348] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-357] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-291] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-304] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-335] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-354] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-255] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-341] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-358] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-286] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-298] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-341] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-286] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-298] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-311] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-335] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-358] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-286] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-333] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-279] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-352] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-322] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-296] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-335] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-354] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-304] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-333] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-354] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-338] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-345] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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