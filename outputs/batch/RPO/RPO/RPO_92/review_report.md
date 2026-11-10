# Play-Annotation-Generator Annotation Review — RPO_92

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_92`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 81
- **Ball Tracks:** 0
- **Action Segments:** 245
- **Validation Warnings:** 341
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `8` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 4
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 229
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ⚠️ START CHANGED | `Action_PullBall` | QB | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `19` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_ReadDefender` | QB | `1` | `1` | 49 | START | 49 | 64 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `14` | `14` | 49 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `17` | 49 | START | 94 | 96 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `18` | `18` | 49 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `20` | `20` | 49 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `21` | `21` | 49 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_PullBall` | QB | `1` | `1` | 66 | START | 68 | 69 |
| ✅ EXACT | `Action_ThrowPass` | QB | `1` | `1` | 93 | START | 93 | 102 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 49 | 64 | 16 | inferred_complete_timeline |
| `Action_PullBall` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_None` | 75 | 92 | 18 | inferred_complete_timeline |
| `Action_ThrowPass` | 93 | 102 | 10 | inferred_complete_timeline |
| `Action_None` | 103 | 123 | 21 | inferred_complete_timeline |
| `Action_None` | 125 | 150 | 26 | inferred_complete_timeline |
| `Action_None` | 152 | 329 | 178 | inferred_complete_timeline |
| `Action_None` | 331 | 359 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 54 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 113 | 66 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_None` | 121 | 264 | 144 | inferred_complete_timeline |
| `Action_None` | 268 | 287 | 20 | inferred_complete_timeline |
| `Action_None` | 292 | 353 | 62 | inferred_complete_timeline |
| `Action_None` | 355 | 359 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 53 | 6 | inferred_complete_timeline |
| `Action_None` | 56 | 359 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 123 | 76 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 64 | 17 | inferred_complete_timeline |
| `Action_None` | 105 | 117 | 13 | inferred_complete_timeline |
| `Action_None` | 119 | 125 | 7 | inferred_complete_timeline |
| `Action_None` | 127 | 133 | 7 | inferred_complete_timeline |
| `Action_None` | 137 | 292 | 156 | inferred_complete_timeline |
| `Action_None` | 297 | 330 | 34 | inferred_complete_timeline |
| `Action_None` | 342 | 359 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 63 | 16 | inferred_complete_timeline |
| `Action_None` | 65 | 69 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 53 | 6 | inferred_complete_timeline |
| `Action_None` | 56 | 62 | 7 | inferred_complete_timeline |
| `Action_None` | 65 | 67 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 359 | 312 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 171 | 124 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 359 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 249 | 202 | inferred_complete_timeline |
| `Action_None` | 260 | 262 | 3 | inferred_complete_timeline |
| `Action_None` | 269 | 270 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 107 | 60 | inferred_complete_timeline |
| `Action_None` | 130 | 132 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 57–100 | 29 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 95–99 | 5 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 95–97 | 3 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 102–110 | 7 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 106–236 | 16 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 113–121 | 9 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 113–230 | 104 | 3 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 118–119 | 2 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 124–359 | 231 | 4 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 126–357 | 156 | 7 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 129–149 | 21 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 132–343 | 185 | 9 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 137–142 | 6 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 142–143 | 2 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 144–292 | 120 | 8 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 148–186 | 35 | 2 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 156–284 | 129 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 160–163 | 4 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 165–358 | 154 | 11 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 170–359 | 189 | 2 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 170–172 | 3 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `44` | `54` | Position_Unknown | Team_Unknown | 177–178 | 2 | 1 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `46` | `56` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `47` | `57` | Position_Unknown | Team_Unknown | 185–359 | 146 | 5 | Undefined position; Undefined team |
| `48` | `60` | Position_Unknown | Team_Unknown | 189–359 | 133 | 14 | Undefined position; Undefined team |
| `49` | `61` | Position_Unknown | Team_Unknown | 191–230 | 40 | 1 | Undefined position; Undefined team |
| `50` | `62` | Position_Unknown | Team_Unknown | 191–193 | 3 | 1 | Undefined position; Undefined team |
| `51` | `64` | Position_Unknown | Team_Unknown | 207–212 | 6 | 1 | Undefined position; Undefined team |
| `52` | `65` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `53` | `67` | Position_Unknown | Team_Unknown | 210–217 | 8 | 1 | Undefined position; Undefined team |
| `54` | `68` | Position_Unknown | Team_Unknown | 211–238 | 26 | 2 | Undefined position; Undefined team |
| `55` | `69` | Position_Unknown | Team_Unknown | 213–338 | 40 | 6 | Undefined position; Undefined team |
| `56` | `71` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `57` | `72` | Position_Unknown | Team_Unknown | 222–225 | 4 | 1 | Undefined position; Undefined team |
| `58` | `74` | Position_Unknown | Team_Unknown | 227–359 | 97 | 7 | Undefined position; Undefined team |
| `59` | `77` | Position_Unknown | Team_Unknown | 231–327 | 66 | 7 | Undefined position; Undefined team |
| `60` | `78` | Position_Unknown | Team_Unknown | 231–232 | 2 | 1 | Undefined position; Undefined team |
| `61` | `79` | Position_Unknown | Team_Unknown | 233–359 | 100 | 6 | Undefined position; Undefined team |
| `62` | `86` | Position_Unknown | Team_Unknown | 246–281 | 26 | 2 | Undefined position; Undefined team |
| `63` | `100` | Position_Unknown | Team_Unknown | 257–359 | 79 | 6 | Undefined position; Undefined team |
| `64` | `114` | Position_Unknown | Team_Unknown | 276–327 | 33 | 4 | Undefined position; Undefined team |
| `65` | `115` | Position_Unknown | Team_Unknown | 278–359 | 79 | 3 | Undefined position; Undefined team |
| `66` | `116` | Position_Unknown | Team_Unknown | 283–285 | 3 | 1 | Undefined position; Undefined team |
| `67` | `123` | Position_Unknown | Team_Unknown | 294–319 | 11 | 4 | Undefined position; Undefined team |
| `68` | `125` | Position_Unknown | Team_Unknown | 296–334 | 34 | 3 | Undefined position; Undefined team |
| `69` | `126` | Position_Unknown | Team_Unknown | 303–359 | 30 | 5 | Undefined position; Undefined team |
| `70` | `128` | Position_Unknown | Team_Unknown | 305–346 | 11 | 3 | Undefined position; Undefined team |
| `71` | `130` | Position_Unknown | Team_Unknown | 309–310 | 2 | 1 | Undefined position; Undefined team |
| `72` | `131` | Position_Unknown | Team_Unknown | 310–321 | 6 | 2 | Undefined position; Undefined team |
| `73` | `132` | Position_Unknown | Team_Unknown | 313–359 | 47 | 1 | Undefined position; Undefined team |
| `74` | `136` | Position_Unknown | Team_Unknown | 319–335 | 9 | 4 | Undefined position; Undefined team |
| `75` | `139` | Position_Unknown | Team_Unknown | 323–350 | 6 | 3 | Undefined position; Undefined team |
| `76` | `142` | Position_Unknown | Team_Unknown | 327–359 | 28 | 4 | Undefined position; Undefined team |
| `77` | `143` | Position_Unknown | Team_Unknown | 332–359 | 21 | 2 | Undefined position; Undefined team |
| `78` | `146` | Position_Unknown | Team_Unknown | 345–359 | 14 | 2 | Undefined position; Undefined team |
| `79` | `147` | Position_Unknown | Team_Unknown | 347–359 | 11 | 2 | Undefined position; Undefined team |
| `80` | `148` | Position_Unknown | Team_Unknown | 348–359 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `14` (RT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `18` (C)
- ❌ Missing segment for action `Action_ZoneBlock` on target `20` (LG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (LT)
- ⚠️ `Action_PullBall` for actor_track_id `1` (QB): Annotated start 66 != Inferred start 68

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 59 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 59 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 118 |
| Missing visible bounding boxes during action | 218 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '14' has invalid range: start=49, end=42. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '18' has invalid range: start=49, end=35. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '20' has invalid range: start=49, end=41. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=49, end=41. Clamping end to start.
- ⚠️ Action 'Action_None' range [48-64] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-117] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-133] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-292] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-330] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [49-64] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [68-69] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-123] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-329] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-123] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-54] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-53] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-264] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-287] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-353] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-249] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-63] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-69] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 103, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [103-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-359] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-77] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-100] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-145] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-121] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-130] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-150] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-230] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-189] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-277] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-240] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-279] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-320] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-357] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-149] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-139] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-172] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-188] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-305] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-320] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-343] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-240] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-276] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-292] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-179] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-284] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-197] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-207] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-226] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-308] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-322] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-327] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-348] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-355] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-193] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-351] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-359] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-198] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-220] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-237] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-255] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-285] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-294] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-301] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-332] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-348] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-357] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-230] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-217] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-229] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-238] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-237] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-301] for track '58' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-320] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-327] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-350] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-356] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-238] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-247] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-283] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-292] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-327] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-265] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-302] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-309] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-329] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-269] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-265] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-319] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-340] for track '63' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-297] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-312] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-327] for track '64' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-286] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-328] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-359] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-310] for track '68' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-334] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-307] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-315] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-359] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-310] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-359] for track '73' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-332] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-339] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-338] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-359] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-352] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-359] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-353] for track '79' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.

</details>