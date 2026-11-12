# Play-Annotation-Generator Annotation Review — SplitZone_63

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_63`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 160
- **Validation Warnings:** 189
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 140
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `24` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `20` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 11 | START | 12 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 11 | START | 12 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 11 | START | 12 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 11 | START | 12 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 11 | START | 12 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 11 | START | 12 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 11 | START | 12 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `24` | `Group` | 11 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 11 | START | 12 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 11 | START | 12 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 11 | START | 12 | 37 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `14` | `14` | 38 | START | 38 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `12` | 61 | START | 61 | 135 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `15` | 61 | START | 61 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `18` | 61 | START | 61 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 61 | START | 61 | 160 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `24` | `23` | 61 | START | 122 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `4` | `4` | 64 | START | 64 | 129 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 75 | END | 38 | 75 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 83 | START | 83 | 92 |
| ✅ EXACT | `Action_BallCarry` | RB | `20` | `20` | 93 | START | 93 | 139 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 160 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 12–404
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 75 | 38 | inferred_complete_timeline |
| `Action_None` | 76 | 82 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 83 | 92 | 10 | inferred_complete_timeline |
| `Action_None` | 93 | 395 | 303 | inferred_complete_timeline |
| `Action_None` | 403 | 404 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 12–139
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 85 | 74 | inferred_complete_timeline |
| `Action_BallCarry` | 93 | 139 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 12–419
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 250 | 213 | inferred_complete_timeline |
| `Action_None` | 252 | 387 | 136 | inferred_complete_timeline |
| `Action_None` | 389 | 397 | 9 | inferred_complete_timeline |
| `Action_None` | 404 | 413 | 10 | inferred_complete_timeline |
| `Action_None` | 418 | 419 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 12–360
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 360 | 323 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–401
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 401 | 364 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–413
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 63 | 52 | inferred_complete_timeline |
| `Action_SplitBlock` | 64 | 129 | 66 | inferred_complete_timeline |
| `Action_SplitBlock` | 132 | 160 | 29 | inferred_complete_timeline |
| `Action_None` | 161 | 184 | 24 | inferred_complete_timeline |
| `Action_None` | 187 | 258 | 72 | inferred_complete_timeline |
| `Action_None` | 271 | 278 | 8 | inferred_complete_timeline |
| `Action_None` | 280 | 392 | 113 | inferred_complete_timeline |
| `Action_None` | 404 | 405 | 2 | inferred_complete_timeline |
| `Action_None` | 408 | 413 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 12–387
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 60 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 81 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 160 | 21 | inferred_complete_timeline |
| `Action_None` | 161 | 387 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 12–405
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 60 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 160 | 100 | inferred_complete_timeline |
| `Action_None` | 161 | 397 | 237 | inferred_complete_timeline |
| `Action_None` | 404 | 405 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 122–275
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 122 | 160 | 39 | inferred_complete_timeline |
| `Action_None` | 161 | 192 | 32 | inferred_complete_timeline |
| `Action_None` | 195 | 231 | 37 | inferred_complete_timeline |
| `Action_None` | 233 | 238 | 6 | inferred_complete_timeline |
| `Action_None` | 245 | 250 | 6 | inferred_complete_timeline |
| `Action_None` | 269 | 275 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 12–419
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 60 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 160 | 100 | inferred_complete_timeline |
| `Action_None` | 161 | 419 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 12–148
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 60 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 135 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 144 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 148 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 12–139
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 112 | 75 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_None` | 119 | 139 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 12–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 128 | 91 | inferred_complete_timeline |
| `Action_None` | 132 | 419 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 135 | 98 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 155 | 10 | inferred_complete_timeline |
| `Action_None` | 163 | 182 | 20 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 419 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–419
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 419 | 382 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 12–413
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 209 | 172 | inferred_complete_timeline |
| `Action_None` | 216 | 326 | 111 | inferred_complete_timeline |
| `Action_None` | 328 | 413 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 12–405
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 397 | 360 | inferred_complete_timeline |
| `Action_None` | 404 | 405 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–370
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 227 | 190 | inferred_complete_timeline |
| `Action_None` | 311 | 357 | 47 | inferred_complete_timeline |
| `Action_None` | 363 | 365 | 3 | inferred_complete_timeline |
| `Action_None` | 369 | 370 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–395
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 345 | 308 | inferred_complete_timeline |
| `Action_None` | 357 | 395 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 12–369
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 134 | 97 | inferred_complete_timeline |
| `Action_None` | 136 | 347 | 212 | inferred_complete_timeline |
| `Action_None` | 350 | 369 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 12–419
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 167 | 130 | inferred_complete_timeline |
| `Action_None` | 175 | 370 | 196 | inferred_complete_timeline |
| `Action_None` | 372 | 419 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 12–238
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 219 | 182 | inferred_complete_timeline |
| `Action_None` | 223 | 238 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 12–419 | 386 | 9 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 91–96 | 6 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 142–419 | 278 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 143–225 | 16 | 5 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 150–312 | 156 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 211–216 | 6 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 222–223 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 226–414 | 178 | 5 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 249–267 | 4 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 256–419 | 162 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 258–260 | 3 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 263–291 | 11 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 266–267 | 2 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 268–282 | 7 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 278–419 | 142 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 285–419 | 127 | 5 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 285–315 | 8 | 3 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 287–288 | 2 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 297–298 | 2 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 299–301 | 3 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 325–381 | 36 | 4 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 329–335 | 5 | 2 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 342–343 | 2 | 1 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 348–417 | 21 | 5 | Undefined position; Undefined team |
| `47` | `67` | Position_Unknown | Team_Unknown | 381–415 | 24 | 2 | Undefined position; Undefined team |
| `48` | `68` | Position_Unknown | Team_Unknown | 382–384 | 3 | 1 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 390–392 | 3 | 1 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 404–416 | 13 | 1 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 414–416 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `24` (C): Annotated start 61 != Inferred start 122
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 125 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RG) duration 100 frames exceeds threshold 90 frames [start=61, end=160].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 100 frames exceeds threshold 90 frames [start=61, end=160].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 100 frames exceeds threshold 90 frames [start=61, end=160].
- ⚠️ Action 'Action_None' range [38-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-401] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-345] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-395] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [64-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [132-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-184] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-258] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-278] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-392] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-413] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-134] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-347] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-369] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-360] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-227] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-357] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-365] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-135] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-182] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-419] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-250] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-387] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-397] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-413] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-219] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-397] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 76, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [76-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-247] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-419] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-167] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-370] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-209] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-326] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-413] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-387] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-395] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [93-139] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-397] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-275] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-419] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-250] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-312] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-374] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-384] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-397] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-414] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-416] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-282] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-419] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-296] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-300] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-317] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-343] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-330] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-346] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-370] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-357] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-387] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-417] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-398] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-415] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-416] for track '50' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-416] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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