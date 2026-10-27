# Play-Annotation-Generator Annotation Review — Counter_170

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_170`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 152
- **Validation Warnings:** 182
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 128
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB1 | defense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | LB1 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB2 | defense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_PullLeadBlock` | DE1 | defense | `16` | `15` |
| ✅ EXACT | `Action_PlaySideFakeStep` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | SAF1 | defense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | SAF1 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_BallSnap` | LB1 | `13` | `12` | 2 | START | 2 | 2 |
| ✅ EXACT | `Action_DownBlock` | LB1 | `13` | `12` | 3 | START | 3 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB2 | `15` | `14` | 3 | START | 3 | 20 |
| ✅ EXACT | `Action_DownBlock` | RT | `18` | `17` | 3 | START | 3 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `20` | `19` | 3 | START | 3 | 25 |
| ✅ EXACT | `Action_PullLeadBlock` | DE1 | `16` | `15` | 3 | START | 3 | 52 |
| ✅ EXACT | `Action_PlaySideFakeStep` | QB | `11` | `10` | 12 | START | 12 | 47 |
| ✅ EXACT | `Action_SnapReceive` | SAF1 | `9` | `8` | 15 | END | 2 | 15 |
| ✅ EXACT | `Action_Handoff` | SAF1 | `9` | `8` | 22 | START | 22 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `11` | `10` | 48 | START | 48 | 306 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 102 | BOUNDARY | N/A | N/A |

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
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 12 | 47 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 48 | 306 | 259 | inferred_complete_timeline |
| `Action_BallCarry` | 313 | 317 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 320 | 359 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–351
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 94 | 93 | inferred_complete_timeline |
| `Action_None` | 117 | 255 | 139 | inferred_complete_timeline |
| `Action_None` | 258 | 336 | 79 | inferred_complete_timeline |
| `Action_None` | 338 | 351 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 107 | 106 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 70 | 69 | inferred_complete_timeline |
| `Action_None` | 72 | 101 | 30 | inferred_complete_timeline |
| `Action_None` | 104 | 126 | 23 | inferred_complete_timeline |
| `Action_None` | 129 | 359 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 57 | 56 | inferred_complete_timeline |
| `Action_None` | 99 | 101 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_None` | 100 | 123 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 27 | 26 | inferred_complete_timeline |
| `Action_None` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_None` | 34 | 55 | 22 | inferred_complete_timeline |
| `Action_None` | 60 | 68 | 9 | inferred_complete_timeline |
| `Action_None` | 71 | 140 | 70 | inferred_complete_timeline |
| `Action_None` | 145 | 359 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_PullBlock` | 27 | 77 | 51 | inferred_complete_timeline |
| `Action_PullBlock` | 91 | 102 | 12 | inferred_complete_timeline |
| `Action_None` | 103 | 359 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 49 | 48 | inferred_complete_timeline |
| `Action_None` | 53 | 129 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 3 | 102 | 100 | inferred_complete_timeline |
| `Action_None` | 103 | 185 | 83 | inferred_complete_timeline |
| `Action_None` | 188 | 206 | 19 | inferred_complete_timeline |
| `Action_None` | 210 | 260 | 51 | inferred_complete_timeline |
| `Action_None` | 262 | 359 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 3 | 52 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–351
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 37 | 36 | inferred_complete_timeline |
| `Action_None` | 56 | 89 | 34 | inferred_complete_timeline |
| `Action_None` | 100 | 176 | 77 | inferred_complete_timeline |
| `Action_None` | 180 | 185 | 6 | inferred_complete_timeline |
| `Action_None` | 188 | 207 | 20 | inferred_complete_timeline |
| `Action_None` | 210 | 341 | 132 | inferred_complete_timeline |
| `Action_None` | 345 | 351 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–351
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 160 | 159 | inferred_complete_timeline |
| `Action_None` | 162 | 345 | 184 | inferred_complete_timeline |
| `Action_None` | 349 | 351 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–337
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 173 | 172 | inferred_complete_timeline |
| `Action_None` | 175 | 181 | 7 | inferred_complete_timeline |
| `Action_None` | 190 | 337 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 2 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 3 | 62 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 3 | 20 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 24 | 38 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 67 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 50 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 135 | 83 | inferred_complete_timeline |
| `Action_None` | 139 | 359 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 109 | 108 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 296 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 15 | 14 | inferred_complete_timeline |
| `Action_None` | 16 | 21 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 22 | 47 | 26 | inferred_complete_timeline |
| `Action_None` | 48 | 100 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–354
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 74 | 73 | inferred_complete_timeline |
| `Action_None` | 77 | 96 | 20 | inferred_complete_timeline |
| `Action_None` | 102 | 305 | 204 | inferred_complete_timeline |
| `Action_None` | 307 | 354 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 8–56 | 36 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 26–40 | 15 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 56–359 | 303 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 58–331 | 272 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 66–121 | 52 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 68–311 | 195 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 68–359 | 230 | 5 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 92–311 | 201 | 8 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 108–359 | 232 | 3 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 149–359 | 209 | 3 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 150–359 | 207 | 3 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 157–158 | 2 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 159–217 | 59 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 161–173 | 13 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 186–200 | 10 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 270–272 | 3 | 1 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 276–278 | 3 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 276–324 | 47 | 2 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 277–332 | 56 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 280–300 | 9 | 3 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 290–291 | 2 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 295–359 | 62 | 2 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 332–359 | 28 | 1 | Undefined position; Undefined team |
| `47` | `67` | Position_Unknown | Team_Unknown | 332–355 | 24 | 1 | Undefined position; Undefined team |
| `48` | `68` | Position_Unknown | Team_Unknown | 332–359 | 28 | 1 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 333–359 | 27 | 1 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 335–359 | 16 | 2 | Undefined position; Undefined team |
| `51` | `71` | Position_Unknown | Team_Unknown | 349–359 | 11 | 1 | Undefined position; Undefined team |
| `52` | `72` | Position_Unknown | Team_Unknown | 350–359 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 114 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '22' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (RT) duration 100 frames exceeds threshold 90 frames [start=3, end=102].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '19' (C) duration 100 frames exceeds threshold 90 frames [start=3, end=102].
- ⚠️ Action 'Action_None' range [2-57] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-296] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-70] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-126] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-123] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-94] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-255] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-336] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-351] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-74] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-305] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-354] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-109] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-173] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-181] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-337] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-100] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-50] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [48-306] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [313-317] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-160] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-345] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [3-62] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-107] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [3-20] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [24-38] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [40-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-67] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [3-52] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-207] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-341] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-351] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [3-102] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-185] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-206] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-260] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-49] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-129] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [3-25] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [27-77] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-32] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-140] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-19] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-40] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-139] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-331] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-102] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-121] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-73] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-160] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-311] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-305] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-315] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-107] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-123] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-225] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-251] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-311] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-245] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-359] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-327] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-359] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-155] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-171] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-217] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-320] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-332] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-355] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-359] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-341] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-356] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>