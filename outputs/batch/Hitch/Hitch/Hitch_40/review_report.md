# Play-Annotation-Generator Annotation Review — Hitch_40

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_40`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 62
- **Ball Tracks:** 0
- **Action Segments:** 203
- **Validation Warnings:** 247
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 182
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_RunHitchRoute` | WR2 | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `18` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 16 | START | 16 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 19 | START | 19 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `17` | 19 | START | 19 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 19 | START | 29 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 19 | START | 19 | 40 |
| ✅ EXACT | `Action_PassBlock` | RT | `6` | `6` | 19 | START | 19 | 66 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 28 | END | 16 | 28 |
| ✅ EXACT | `Action_RunHitchRoute` | WR2 | `18` | `18` | 36 | START | 36 | 155 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 145 | START | 145 | 147 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `18` | `18` | 194 | START | 194 | 256 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 28 | 13 | inferred_complete_timeline |
| `Action_None` | 29 | 112 | 84 | inferred_complete_timeline |
| `Action_None` | 118 | 144 | 27 | inferred_complete_timeline |
| `Action_ThrowPass` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 208 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 46 | 31 | inferred_complete_timeline |
| `Action_None` | 48 | 60 | 13 | inferred_complete_timeline |
| `Action_None` | 62 | 111 | 50 | inferred_complete_timeline |
| `Action_None` | 116 | 136 | 21 | inferred_complete_timeline |
| `Action_None` | 150 | 175 | 26 | inferred_complete_timeline |
| `Action_None` | 179 | 329 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 36 | 155 | 120 | inferred_complete_timeline |
| `Action_None` | 156 | 193 | 38 | inferred_complete_timeline |
| `Action_BallCarry` | 194 | 256 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 81 | 66 | inferred_complete_timeline |
| `Action_None` | 86 | 204 | 119 | inferred_complete_timeline |
| `Action_None` | 211 | 269 | 59 | inferred_complete_timeline |
| `Action_None` | 277 | 320 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 82 | 67 | inferred_complete_timeline |
| `Action_None` | 90 | 122 | 33 | inferred_complete_timeline |
| `Action_None` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 175 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 42 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 111 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 132 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 140 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 167 | 175 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 177 | 179 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 52 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 62 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 152 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 230 | 233 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 28 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 42 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 78 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 40 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 61 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 87 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 94 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 113 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 136 | 138 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 66 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 108 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 107 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_None` | 44 | 46 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 102 | 87 | inferred_complete_timeline |
| `Action_None` | 115 | 121 | 7 | inferred_complete_timeline |
| `Action_None` | 126 | 133 | 8 | inferred_complete_timeline |
| `Action_None` | 135 | 141 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 109 | 94 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_None` | 119 | 318 | 200 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 329 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 70 | 55 | inferred_complete_timeline |
| `Action_None` | 84 | 151 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 329 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 329 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 179 | 164 | inferred_complete_timeline |
| `Action_None` | 185 | 194 | 10 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 329 | 314 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 70–71 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 73–329 | 184 | 16 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 97–224 | 70 | 6 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 127–142 | 14 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 135–136 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 153–329 | 176 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 154–297 | 58 | 4 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 157–329 | 162 | 6 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 158–159 | 2 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 158–194 | 25 | 3 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 159–329 | 128 | 9 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 180–299 | 105 | 3 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 202–325 | 105 | 5 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 214–308 | 5 | 2 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 218–308 | 54 | 6 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 221–329 | 105 | 2 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 228–290 | 13 | 3 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 229–231 | 3 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 247–297 | 10 | 2 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 253–286 | 15 | 3 | Undefined position; Undefined team |
| `42` | `50` | Position_Unknown | Team_Unknown | 255–280 | 25 | 2 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 260–329 | 28 | 3 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 261–285 | 12 | 3 | Undefined position; Undefined team |
| `45` | `56` | Position_Unknown | Team_Unknown | 269–329 | 42 | 4 | Undefined position; Undefined team |
| `46` | `57` | Position_Unknown | Team_Unknown | 269–282 | 12 | 2 | Undefined position; Undefined team |
| `47` | `58` | Position_Unknown | Team_Unknown | 272–277 | 6 | 1 | Undefined position; Undefined team |
| `48` | `60` | Position_Unknown | Team_Unknown | 280–295 | 16 | 1 | Undefined position; Undefined team |
| `49` | `61` | Position_Unknown | Team_Unknown | 280–281 | 2 | 1 | Undefined position; Undefined team |
| `50` | `63` | Position_Unknown | Team_Unknown | 285–290 | 6 | 1 | Undefined position; Undefined team |
| `51` | `64` | Position_Unknown | Team_Unknown | 286–290 | 5 | 1 | Undefined position; Undefined team |
| `52` | `65` | Position_Unknown | Team_Unknown | 286–288 | 3 | 1 | Undefined position; Undefined team |
| `53` | `69` | Position_Unknown | Team_Unknown | 289–329 | 24 | 2 | Undefined position; Undefined team |
| `54` | `70` | Position_Unknown | Team_Unknown | 291–303 | 13 | 1 | Undefined position; Undefined team |
| `55` | `73` | Position_Unknown | Team_Unknown | 293–329 | 28 | 3 | Undefined position; Undefined team |
| `56` | `75` | Position_Unknown | Team_Unknown | 296–313 | 16 | 2 | Undefined position; Undefined team |
| `57` | `76` | Position_Unknown | Team_Unknown | 298–308 | 11 | 1 | Undefined position; Undefined team |
| `58` | `77` | Position_Unknown | Team_Unknown | 298–329 | 30 | 2 | Undefined position; Undefined team |
| `59` | `80` | Position_Unknown | Team_Unknown | 304–308 | 5 | 1 | Undefined position; Undefined team |
| `60` | `82` | Position_Unknown | Team_Unknown | 307–308 | 2 | 1 | Undefined position; Undefined team |
| `61` | `83` | Position_Unknown | Team_Unknown | 312–329 | 14 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 165 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [16–28], lower_priority='Action_PassBlock' annotated_start=19, effective_Action_PassBlock_start=29.
- ⚠️ Action 'Action_None' range [16-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-82] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-81] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-269] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-320] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-107] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-66] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [145-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-208] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-70] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-151] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-179] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-102] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-318] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-60] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-111] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-136] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-175] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-52] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-62] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [131-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [163-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [230-233] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-42] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-46] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-132] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-140] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [167-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [177-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' range [36-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [194-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-78] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-40] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-61] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [136-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-108] for track '21' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-111] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-174] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-229] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-105] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-140] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-198] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-224] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-138] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-325] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-178] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-233] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-297] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-198] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-268] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-183] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-194] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-243] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-264] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-265] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-284] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-299] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-318] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-237] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-274] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-284] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-308] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-228] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-297] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-262] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-280] for track '42' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-271] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-294] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-274] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-295] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-290] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-303] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-303] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-329] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-302] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-313] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-308] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-308] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-329] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-308] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '61' has 1 frames without a visible bounding box.
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

</details>