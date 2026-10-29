# Play-Annotation-Generator Annotation Review — DeepCross_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_51`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 76
- **Ball Tracks:** 0
- **Action Segments:** 216
- **Validation Warnings:** 308
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 191
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 311 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 10 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 3 | START | 3 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `17` | 3 | START | 3 | 7 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 3 | START | 3 | 28 |
| ✅ EXACT | `Action_PassBlock` | RT | `19` | `19` | 3 | START | 3 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 3 | START | 3 | 16 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | `3` | `3` | 11 | START | 11 | 191 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 11 | END | 11 | 11 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `10` | `10` | 110 | START | N/A | N/A |
| ✅ EXACT | `Action_BallCarry` | WR2 | `3` | `3` | 200 | START | 200 | 229 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 11 | 1 | inferred_complete_timeline |
| `Action_None` | 12 | 68 | 57 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 125 | 359 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 311 | 312 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 352 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 359 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 11 | 191 | 181 | inferred_complete_timeline |
| `Action_None` | 192 | 199 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 200 | 229 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 21 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 40 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 63 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 78 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 28 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 46 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 51 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 7 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 27 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 53 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 142 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 27 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 53 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 64 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 82 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 16 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 27 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 52 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 62 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–18
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 18 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 27 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 51 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 67 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 81 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 26 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 125 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 17 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 53 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 274 | 232 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 330 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 359 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 213 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 221 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 235 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 246 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 299 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 306 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 359 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 223 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 226 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–66 | 57 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 17–18 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 61–341 | 185 | 7 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 73–74 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 95–123 | 23 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 99–359 | 244 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 99–108 | 5 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 104–113 | 10 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 107–117 | 10 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 122–123 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 137–359 | 219 | 3 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 143–159 | 8 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 148–152 | 5 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 148–149 | 2 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 161–258 | 35 | 6 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 170–359 | 175 | 4 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 170–221 | 52 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 170–359 | 190 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 174–177 | 4 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 174–359 | 176 | 4 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 176–178 | 3 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 179–359 | 170 | 3 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 181–355 | 135 | 13 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 181–359 | 177 | 2 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 188–240 | 52 | 2 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 188–359 | 160 | 7 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 193–359 | 166 | 2 | Undefined position; Undefined team |
| `50` | `71` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 219–349 | 94 | 5 | Undefined position; Undefined team |
| `52` | `78` | Position_Unknown | Team_Unknown | 224–295 | 72 | 1 | Undefined position; Undefined team |
| `53` | `79` | Position_Unknown | Team_Unknown | 225–359 | 129 | 4 | Undefined position; Undefined team |
| `54` | `81` | Position_Unknown | Team_Unknown | 232–264 | 27 | 3 | Undefined position; Undefined team |
| `55` | `82` | Position_Unknown | Team_Unknown | 233–359 | 121 | 4 | Undefined position; Undefined team |
| `56` | `84` | Position_Unknown | Team_Unknown | 236–359 | 95 | 6 | Undefined position; Undefined team |
| `57` | `85` | Position_Unknown | Team_Unknown | 247–277 | 31 | 1 | Undefined position; Undefined team |
| `58` | `86` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `59` | `90` | Position_Unknown | Team_Unknown | 253–258 | 6 | 1 | Undefined position; Undefined team |
| `60` | `91` | Position_Unknown | Team_Unknown | 257–258 | 2 | 1 | Undefined position; Undefined team |
| `61` | `92` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |
| `62` | `93` | Position_Unknown | Team_Unknown | 265–359 | 67 | 3 | Undefined position; Undefined team |
| `63` | `94` | Position_Unknown | Team_Unknown | 266–359 | 90 | 2 | Undefined position; Undefined team |
| `64` | `95` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |
| `65` | `96` | Position_Unknown | Team_Unknown | 268–359 | 50 | 13 | Undefined position; Undefined team |
| `66` | `97` | Position_Unknown | Team_Unknown | 271–352 | 60 | 4 | Undefined position; Undefined team |
| `67` | `99` | Position_Unknown | Team_Unknown | 277–279 | 3 | 1 | Undefined position; Undefined team |
| `68` | `102` | Position_Unknown | Team_Unknown | 290–295 | 6 | 1 | Undefined position; Undefined team |
| `69` | `103` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `70` | `105` | Position_Unknown | Team_Unknown | 309–311 | 3 | 1 | Undefined position; Undefined team |
| `71` | `109` | Position_Unknown | Team_Unknown | 322–359 | 24 | 2 | Undefined position; Undefined team |
| `72` | `111` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |
| `73` | `112` | Position_Unknown | Team_Unknown | 329–331 | 3 | 1 | Undefined position; Undefined team |
| `74` | `113` | Position_Unknown | Team_Unknown | 330–359 | 10 | 2 | Undefined position; Undefined team |
| `75` | `114` | Position_Unknown | Team_Unknown | 340–344 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (5 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `10` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 55 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 55 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 110 |
| Missing visible bounding boxes during action | 195 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 54: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-233] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-299] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-306] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-311] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-352] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [200-229] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-359] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-51] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-66] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-213] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-221] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-246] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-274] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-330] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-68] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-21] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-40] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-78] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-64] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-51] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-67] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-7] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-53] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-28] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-51] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-18] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-16] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-27] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-52] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-67] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-79] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-155] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-329] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-341] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-110] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-130] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-143] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-108] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-113] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-117] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-181] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-351] for track '32' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-148] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-152] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-170] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-186] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-199] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-216] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-261] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-271] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-300] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-221] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-359] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-177] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-178] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-329] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-335] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-359] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-178] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-179] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-251] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-261] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-188] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-206] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-224] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-231] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-241] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-259] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-278] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-285] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-295] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-323] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-340] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-355] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-188] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-359] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-226] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-240] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-189] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-201] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-279] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-291] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-298] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-307] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-194] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-201] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-259] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-270] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-301] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-331] for track '51' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-349] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-295] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-251] for track '53' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-278] for track '53' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-288] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-359] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-239] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-258] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-236] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-252] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-273] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-288] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-296] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-312] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-322] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-330] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-359] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-277] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-258] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-269] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-279] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-319] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-359] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-277] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-289] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-296] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-302] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-314] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-320] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-338] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-343] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-349] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-355] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-359] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-291] for track '66' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-297] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-328] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-352] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-279] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-295] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-311] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-342] for track '71' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-329] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-331] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-336] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-359] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-344] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.

</details>