# Play-Annotation-Generator Annotation Review — BootPass_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_25`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 93
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
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunFlatRoute` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_SecureCatch` | TE | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 38 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 39 | START | 39 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `15` | `15` | 49 | START | 65 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `16` | `16` | 49 | START | 49 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `18` | `18` | 49 | START | 49 | 51 |
| ✅ EXACT | `Action_RunBlock` | RG | `20` | `20` | 49 | START | 49 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `21` | `21` | 49 | START | 49 | 51 |
| ✅ EXACT | `Action_RunFlatRoute` | WR2 | `0` | `0` | 55 | START | 55 | 126 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 55 | END | 39 | 55 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `14` | `14` | 64 | START | 64 | 79 |
| ✅ EXACT | `Action_BootAway` | QB | `14` | `14` | 80 | START | 80 | 115 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 127 | START | 127 | 139 |
| ✅ EXACT | `Action_SecureCatch` | TE | `19` | `19` | 151 | START | 151 | 156 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_SnapReceive` | 39 | 55 | 17 | inferred_complete_timeline |
| `Action_None` | 56 | 63 | 8 | inferred_complete_timeline |
| `Action_FakeHandoff` | 64 | 79 | 16 | inferred_complete_timeline |
| `Action_BootAway` | 80 | 115 | 36 | inferred_complete_timeline |
| `Action_None` | 116 | 126 | 11 | inferred_complete_timeline |
| `Action_ThrowPass` | 127 | 139 | 13 | inferred_complete_timeline |
| `Action_None` | 140 | 329 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 61 | 23 | inferred_complete_timeline |
| `Action_None` | 66 | 329 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 327 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 55 | 126 | 72 | inferred_complete_timeline |
| `Action_None` | 127 | 329 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 329 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 101 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 150 | 45 | inferred_complete_timeline |
| `Action_SecureCatch` | 151 | 156 | 6 | inferred_complete_timeline |
| `Action_None` | 157 | 287 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_RunBlock` | 49 | 57 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 64 | 101 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 109 | 329 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_RunBlock` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 64 | 100 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_BallSnap` | 39 | 53 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 65 | 101 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 108 | 160 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_RunBlock` | 49 | 51 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_RunBlock` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 66 | 85 | 20 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 99 | 12 | inferred_complete_timeline |
| `Action_RunBlock` | 144 | 329 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 100 | 62 | inferred_complete_timeline |
| `Action_None` | 110 | 142 | 33 | inferred_complete_timeline |
| `Action_None` | 145 | 148 | 4 | inferred_complete_timeline |
| `Action_None` | 154 | 316 | 163 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_None` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 51 | 13 | inferred_complete_timeline |
| `Action_None` | 65 | 101 | 37 | inferred_complete_timeline |
| `Action_None` | 109 | 226 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 57 | 19 | inferred_complete_timeline |
| `Action_None` | 66 | 101 | 36 | inferred_complete_timeline |
| `Action_None` | 109 | 329 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 51 | 13 | inferred_complete_timeline |
| `Action_None` | 65 | 100 | 36 | inferred_complete_timeline |
| `Action_None` | 106 | 138 | 33 | inferred_complete_timeline |
| `Action_None` | 140 | 159 | 20 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 301 | 123 | inferred_complete_timeline |
| `Action_None` | 305 | 329 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 222 | 184 | inferred_complete_timeline |
| `Action_None` | 225 | 309 | 85 | inferred_complete_timeline |
| `Action_None` | 312 | 316 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 297 | 259 | inferred_complete_timeline |
| `Action_None` | 300 | 302 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 302 | 264 | inferred_complete_timeline |
| `Action_None` | 312 | 313 | 2 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_None` | 326 | 327 | 2 | inferred_complete_timeline |
| `Action_None` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 193 | 155 | inferred_complete_timeline |
| `Action_None` | 205 | 216 | 12 | inferred_complete_timeline |
| `Action_None` | 219 | 224 | 6 | inferred_complete_timeline |
| `Action_None` | 226 | 308 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 120 | 82 | inferred_complete_timeline |
| `Action_None` | 131 | 259 | 129 | inferred_complete_timeline |
| `Action_None` | 271 | 328 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 327 | 289 | inferred_complete_timeline |
| `Action_None` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 329 | 291 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 111–114 | 4 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 114–123 | 10 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 128–326 | 196 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 161–329 | 160 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 167–329 | 163 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 228–327 | 97 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 232–297 | 36 | 5 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 281–282 | 2 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 308–313 | 6 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [39–55], lower_priority='Action_RunBlock' annotated_start=49, effective_Action_RunBlock_start=56.
- ⚠️ Action 'Action_None' range [39-193] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-308] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-302] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-327] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-327] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-297] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-259] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-328] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-222] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-309] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-316] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-159] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-301] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-51] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-57] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-101] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-316] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-329] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [39-53] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [65-101] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [108-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [49-57] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [64-101] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [106-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [109-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-61] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [49-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [64-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-101] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-287] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [49-51] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [49-51] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [54-55] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [66-85] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [88-99] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-299] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-326] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-277] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-283] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-301] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-327] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-248] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-279] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-313] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '31' has 1 frames without a visible bounding box.
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

</details>