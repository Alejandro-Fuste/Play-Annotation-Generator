# Play-Annotation-Generator Annotation Review — SplitZone_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_61`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 170
- **Validation Warnings:** 180
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
- **Inferred Coverage Segments (Action_None):** 148
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `21` | `21` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 1 | START | 2 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 1 | START | 2 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 1 | START | 2 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 1 | START | 2 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 1 | START | 2 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 1 | START | 2 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 1 | START | 2 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 1 | START | 2 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 1 | START | 2 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 1 | START | 2 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 1 | START | 2 | 48 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 41 | START | 41 | 54 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `11` | 44 | START | 44 | 128 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `14` | 44 | START | 44 | 70 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `15` | `15` | 44 | START | 44 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `16` | 44 | START | 44 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `17` | 44 | START | 55 | 59 |
| ✅ EXACT | `Action_SplitBlock` | TE | `5` | `5` | 49 | START | 49 | 128 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 54 | END | 41 | 54 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `18` | 62 | START | 62 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `21` | `21` | 70 | START | 70 | 346 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `14` | `14` | 71 | START | 71 | 124 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 128 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 2–75
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 54 | 14 | inferred_complete_timeline |
| `Action_None` | 55 | 61 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 62 | 69 | 8 | inferred_complete_timeline |
| `Action_None` | 70 | 75 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 69 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 346 | 277 | inferred_complete_timeline |
| `Action_BallCarry` | 353 | 359 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 2–248
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 135 | 95 | inferred_complete_timeline |
| `Action_None` | 141 | 171 | 31 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_None` | 179 | 219 | 41 | inferred_complete_timeline |
| `Action_None` | 223 | 233 | 11 | inferred_complete_timeline |
| `Action_None` | 245 | 248 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 359 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 326 | 286 | inferred_complete_timeline |
| `Action_None` | 335 | 359 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 2–348
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_SplitBlock` | 49 | 128 | 80 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 159 | 28 | inferred_complete_timeline |
| `Action_None` | 163 | 200 | 38 | inferred_complete_timeline |
| `Action_None` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 312 | 96 | inferred_complete_timeline |
| `Action_None` | 314 | 340 | 27 | inferred_complete_timeline |
| `Action_None` | 347 | 348 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 43 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 128 | 85 | inferred_complete_timeline |
| `Action_None` | 129 | 198 | 70 | inferred_complete_timeline |
| `Action_None` | 201 | 206 | 6 | inferred_complete_timeline |
| `Action_None` | 210 | 359 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 2–123
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 43 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 123 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 2–81
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_BallSnap` | 41 | 54 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 59 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 81 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 2–188
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 43 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 64 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 128 | 60 | inferred_complete_timeline |
| `Action_None` | 129 | 135 | 7 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 174 | 9 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 188 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 2–124
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 43 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 70 | 27 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 71 | 124 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 337 | 297 | inferred_complete_timeline |
| `Action_None` | 344 | 359 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 2–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 120 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 2–320
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 182 | 142 | inferred_complete_timeline |
| `Action_None` | 184 | 206 | 23 | inferred_complete_timeline |
| `Action_None` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_None` | 214 | 225 | 12 | inferred_complete_timeline |
| `Action_None` | 228 | 230 | 3 | inferred_complete_timeline |
| `Action_None` | 235 | 240 | 6 | inferred_complete_timeline |
| `Action_None` | 242 | 308 | 67 | inferred_complete_timeline |
| `Action_None` | 310 | 313 | 4 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 105 | 65 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_None` | 117 | 359 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 2–65
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 60 | 20 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 114 | 74 | inferred_complete_timeline |
| `Action_None` | 122 | 160 | 39 | inferred_complete_timeline |
| `Action_None` | 163 | 359 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 2–236
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 186 | 146 | inferred_complete_timeline |
| `Action_None` | 188 | 236 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 156 | 116 | inferred_complete_timeline |
| `Action_None` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_None` | 166 | 174 | 9 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 331 | 151 | inferred_complete_timeline |
| `Action_None` | 334 | 337 | 4 | inferred_complete_timeline |
| `Action_None` | 341 | 344 | 4 | inferred_complete_timeline |
| `Action_None` | 350 | 359 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 359 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 330 | 290 | inferred_complete_timeline |
| `Action_None` | 333 | 339 | 7 | inferred_complete_timeline |
| `Action_None` | 344 | 345 | 2 | inferred_complete_timeline |
| `Action_None` | 349 | 350 | 2 | inferred_complete_timeline |
| `Action_None` | 352 | 359 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 2–272
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 272 | 232 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 72–75 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 77–343 | 223 | 8 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 85–94 | 10 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 107–109 | 3 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 127–359 | 221 | 6 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 147–349 | 191 | 7 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 152–153 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 176–348 | 149 | 10 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 223–359 | 81 | 6 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 247–278 | 32 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 258–359 | 102 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 306–307 | 2 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 308–359 | 27 | 5 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 315–359 | 40 | 3 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 321–326 | 5 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 323–324 | 2 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 334–336 | 3 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 335–336 | 2 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 337–359 | 23 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 341–342 | 2 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 342–343 | 2 | 1 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 349–359 | 9 | 3 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 354–359 | 6 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 357–358 | 2 | 1 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 128 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [41–54], lower_priority='Action_ZoneBlock' annotated_start=44, effective_Action_ZoneBlock_start=55.
- ⚠️ Action 'Action_None' range [41-135] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-171] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-219] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-233] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-120] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-60] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-326] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-337] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-159] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-200] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-312] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-340] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-186] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-156] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-331] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-344] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-160] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-359] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-272] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-198] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [71-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-188] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-59] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-72] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-330] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-339] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-206] for track '20' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-225] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-240] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-308] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-346] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-114] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-257] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-301] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-343] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-94] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-196] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-206] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-234] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-260] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-287] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-349] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-182] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-206] for track '29' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-233] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-254] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-287] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-329] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-294] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-308] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-359] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-278] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-359] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-313] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-322] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-337] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-339] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '45' has 1 frames without a visible bounding box.
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

</details>