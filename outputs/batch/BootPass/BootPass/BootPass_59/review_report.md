# Play-Annotation-Generator Annotation Review — BootPass_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_59`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 157
- **Validation Warnings:** 173
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 136
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_RunFlatRoute` | TE2 | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `19` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 26 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 27 | START | 27 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `10` | `10` | 35 | START | 42 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `12` | `12` | 35 | START | 35 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `15` | `15` | 35 | START | 35 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `21` | `21` | 35 | START | 35 | 234 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 41 | END | 27 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | `17` | `17` | 48 | START | 48 | 52 |
| ✅ EXACT | `Action_BootAway` | QB | `17` | `17` | 64 | START | 64 | 111 |
| ✅ EXACT | `Action_RunFlatRoute` | TE2 | `16` | `16` | 80 | START | 80 | 119 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 115 | START | 115 | 126 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `0` | `0` | 154 | START | 154 | 161 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 41 | 15 | inferred_complete_timeline |
| `Action_None` | 42 | 47 | 6 | inferred_complete_timeline |
| `Action_FakeHandoff` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_FakeHandoff` | 54 | 63 | 10 | inferred_complete_timeline |
| `Action_BootAway` | 64 | 111 | 48 | inferred_complete_timeline |
| `Action_None` | 112 | 114 | 3 | inferred_complete_timeline |
| `Action_ThrowPass` | 115 | 126 | 12 | inferred_complete_timeline |
| `Action_None` | 127 | 359 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 247 | 221 | inferred_complete_timeline |
| `Action_None` | 251 | 359 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 287 | 261 | inferred_complete_timeline |
| `Action_None` | 297 | 301 | 5 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 316 | 319 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_SecureCatch` | 154 | 161 | 8 | inferred_complete_timeline |
| `Action_None` | 162 | 274 | 113 | inferred_complete_timeline |
| `Action_None` | 347 | 358 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 328 | 302 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 80 | 119 | 40 | inferred_complete_timeline |
| `Action_None` | 120 | 287 | 168 | inferred_complete_timeline |
| `Action_None` | 289 | 322 | 34 | inferred_complete_timeline |
| `Action_None` | 325 | 328 | 4 | inferred_complete_timeline |
| `Action_None` | 330 | 334 | 5 | inferred_complete_timeline |
| `Action_None` | 356 | 357 | 2 | inferred_complete_timeline |
| `Action_None` | 359 | 359 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 61 | 27 | inferred_complete_timeline |
| `Action_RunBlock` | 63 | 355 | 293 | inferred_complete_timeline |
| `Action_RunBlock` | 357 | 359 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 52 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 57 | 64 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 27 | 40 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 42 | 45 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 49 | 336 | 288 | inferred_complete_timeline |
| `Action_RunBlock` | 340 | 359 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 234 | 200 | inferred_complete_timeline |
| `Action_RunBlock` | 246 | 359 | 114 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 203 | 177 | inferred_complete_timeline |
| `Action_None` | 205 | 359 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 72 | 46 | inferred_complete_timeline |
| `Action_None` | 77 | 359 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 61 | 35 | inferred_complete_timeline |
| `Action_None` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_None` | 94 | 119 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 69 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 359 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 333 | 307 | inferred_complete_timeline |
| `Action_None` | 335 | 336 | 2 | inferred_complete_timeline |
| `Action_None` | 338 | 359 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 81 | 55 | inferred_complete_timeline |
| `Action_None` | 85 | 181 | 97 | inferred_complete_timeline |
| `Action_None` | 184 | 321 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 218 | 192 | inferred_complete_timeline |
| `Action_None` | 221 | 359 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 207 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 133 | 107 | inferred_complete_timeline |
| `Action_None` | 135 | 266 | 132 | inferred_complete_timeline |
| `Action_None` | 270 | 314 | 45 | inferred_complete_timeline |
| `Action_None` | 326 | 327 | 2 | inferred_complete_timeline |
| `Action_None` | 349 | 359 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–253 | 250 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–359 | 346 | 8 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 100–359 | 259 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 117–287 | 149 | 6 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 128–159 | 21 | 2 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 183–201 | 13 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 213–215 | 3 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 224–286 | 63 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 226–359 | 131 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 228–359 | 89 | 8 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 234–359 | 126 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 234–353 | 32 | 6 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 235–237 | 3 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 265–285 | 20 | 2 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 267–359 | 93 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 269–359 | 59 | 8 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 281–359 | 78 | 2 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 295–342 | 16 | 4 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 310–340 | 26 | 4 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 311–312 | 2 | 1 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 325–359 | 10 | 4 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 325–357 | 5 | 2 | Undefined position; Undefined team |
| `44` | `69` | Position_Unknown | Team_Unknown | 331–334 | 4 | 1 | Undefined position; Undefined team |
| `45` | `76` | Position_Unknown | Team_Unknown | 352–356 | 5 | 1 | Undefined position; Undefined team |
| `46` | `78` | Position_Unknown | Team_Unknown | 357–359 | 3 | 1 | Undefined position; Undefined team |
| `47` | `79` | Position_Unknown | Team_Unknown | 357–358 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 114 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 98: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [27–41], lower_priority='Action_RunBlock' annotated_start=35, effective_Action_RunBlock_start=42.
- ⚠️ Action 'Action_None' range [162-274] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-358] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-203] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-333] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-287] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-301] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-92] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-119] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-133] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-266] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-314] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-218] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [27-40] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [42-45] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [49-336] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-181] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-321] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-52] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [54-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [57-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-247] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-359] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [63-355] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [357-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-287] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-322] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-334] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [48-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [64-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-328] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-51] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-254] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-304] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-344] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-234] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-167] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-165] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-287] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-146] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-191] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-286] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-248] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-359] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-359] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-262] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-305] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-353] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-272] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-285] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-287] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-312] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-340] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-345] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-359] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-322] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-340] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-334] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-356] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>