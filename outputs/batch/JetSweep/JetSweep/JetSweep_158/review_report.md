# Play-Annotation-Generator Annotation Review — JetSweep_158

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_158`
- **Frame Range:** 0 to 3869 (3870 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 3869
- **Player Tracks:** 410
- **Ball Tracks:** 0
- **Action Segments:** 872
- **Validation Warnings:** 1636
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 8
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 851
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `14` | `13` |
| ✅ EXACT | `Action_BallSnap` | DT | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `14` | `13` | 24 | START | 24 | 44 |
| ✅ EXACT | `Action_BallSnap` | DT | `9` | `8` | 31 | START | 31 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `10` | `9` | 36 | START | 36 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `10` | 36 | START | 36 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 36 | START | 38 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `3` | `2` | 36 | START | 36 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `4` | 36 | START | 36 | 62 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `7` | 36 | START | 36 | 48 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 44 | END | 31 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | `12` | `11` | 49 | START | 49 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `14` | `13` | 57 | START | 59 | 93 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 115 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 44 | 14 | inferred_complete_timeline |
| `Action_None` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_Toss` | 49 | 53 | 5 | inferred_complete_timeline |
| `Action_Toss` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_None` | 57 | 57 | 1 | inferred_complete_timeline |
| `Action_None` | 59 | 75 | 17 | inferred_complete_timeline |
| `Action_None` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_None` | 87 | 91 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_LeadBlock` | 36 | 42 | 7 | inferred_complete_timeline |
| `Action_LeadBlock` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_LeadBlock` | 49 | 53 | 5 | inferred_complete_timeline |
| `Action_LeadBlock` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_LeadBlock` | 61 | 65 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 43 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 60 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 62 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 111 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 116 | 190 | 75 | inferred_complete_timeline |
| `Action_None` | 194 | 274 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 38–190
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 38 | 73 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 115 | 25 | inferred_complete_timeline |
| `Action_None` | 116 | 177 | 62 | inferred_complete_timeline |
| `Action_None` | 183 | 190 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 48 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 65 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 101 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_None` | 116 | 119 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 55 | 25 | inferred_complete_timeline |
| `Action_None` | 59 | 88 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 78 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 44 | 14 | inferred_complete_timeline |
| `Action_None` | 45 | 178 | 134 | inferred_complete_timeline |
| `Action_None` | 183 | 275 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 85 | 55 | inferred_complete_timeline |
| `Action_None` | 90 | 152 | 63 | inferred_complete_timeline |
| `Action_None` | 192 | 235 | 44 | inferred_complete_timeline |
| `Action_None` | 241 | 274 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 174 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 77 | 47 | inferred_complete_timeline |
| `Action_None` | 79 | 274 | 196 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–183 | 136 | 5 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 24–274 | 170 | 8 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 56–128 | 44 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 62–174 | 99 | 6 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 66–125 | 57 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 77–213 | 124 | 5 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 93–121 | 26 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 108–112 | 5 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 127–275 | 132 | 5 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 129–274 | 138 | 5 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 130–274 | 106 | 6 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 175–275 | 101 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 186–274 | 82 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 195–229 | 24 | 3 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 207–230 | 24 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 207–274 | 68 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 210–274 | 56 | 3 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 210–274 | 65 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 222–256 | 15 | 2 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 239–273 | 6 | 2 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 251–274 | 18 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 259–274 | 16 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 275–284 | 10 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 275–284 | 10 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 275–284 | 10 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 275–284 | 10 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 275–284 | 10 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 275–284 | 10 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 276–284 | 9 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 276–284 | 9 | 1 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 276–284 | 9 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 276–284 | 9 | 1 | Undefined position; Undefined team |
| `45` | `85` | Position_Unknown | Team_Unknown | 407–766 | 358 | 2 | Undefined position; Undefined team |
| `46` | `86` | Position_Unknown | Team_Unknown | 407–723 | 317 | 1 | Undefined position; Undefined team |
| `47` | `87` | Position_Unknown | Team_Unknown | 407–801 | 395 | 1 | Undefined position; Undefined team |
| `48` | `88` | Position_Unknown | Team_Unknown | 407–667 | 261 | 1 | Undefined position; Undefined team |
| `49` | `89` | Position_Unknown | Team_Unknown | 407–801 | 372 | 7 | Undefined position; Undefined team |
| `50` | `90` | Position_Unknown | Team_Unknown | 407–801 | 371 | 4 | Undefined position; Undefined team |
| `51` | `91` | Position_Unknown | Team_Unknown | 407–801 | 370 | 4 | Undefined position; Undefined team |
| `52` | `92` | Position_Unknown | Team_Unknown | 407–801 | 395 | 1 | Undefined position; Undefined team |
| `53` | `93` | Position_Unknown | Team_Unknown | 407–801 | 395 | 1 | Undefined position; Undefined team |
| `54` | `94` | Position_Unknown | Team_Unknown | 407–694 | 288 | 1 | Undefined position; Undefined team |
| `55` | `95` | Position_Unknown | Team_Unknown | 407–725 | 311 | 5 | Undefined position; Undefined team |
| `56` | `96` | Position_Unknown | Team_Unknown | 407–801 | 395 | 1 | Undefined position; Undefined team |
| `57` | `97` | Position_Unknown | Team_Unknown | 407–801 | 395 | 1 | Undefined position; Undefined team |
| `58` | `98` | Position_Unknown | Team_Unknown | 407–801 | 382 | 2 | Undefined position; Undefined team |
| `59` | `99` | Position_Unknown | Team_Unknown | 407–801 | 368 | 2 | Undefined position; Undefined team |
| `60` | `100` | Position_Unknown | Team_Unknown | 407–595 | 189 | 1 | Undefined position; Undefined team |
| `61` | `101` | Position_Unknown | Team_Unknown | 407–631 | 205 | 3 | Undefined position; Undefined team |
| `62` | `102` | Position_Unknown | Team_Unknown | 407–801 | 395 | 1 | Undefined position; Undefined team |
| `63` | `103` | Position_Unknown | Team_Unknown | 407–801 | 391 | 3 | Undefined position; Undefined team |
| `64` | `104` | Position_Unknown | Team_Unknown | 407–801 | 395 | 1 | Undefined position; Undefined team |
| `65` | `105` | Position_Unknown | Team_Unknown | 413–800 | 385 | 4 | Undefined position; Undefined team |
| `66` | `106` | Position_Unknown | Team_Unknown | 414–418 | 5 | 1 | Undefined position; Undefined team |
| `67` | `108` | Position_Unknown | Team_Unknown | 418–723 | 300 | 3 | Undefined position; Undefined team |
| `68` | `110` | Position_Unknown | Team_Unknown | 608–777 | 140 | 5 | Undefined position; Undefined team |
| `69` | `111` | Position_Unknown | Team_Unknown | 626–801 | 110 | 5 | Undefined position; Undefined team |
| `70` | `113` | Position_Unknown | Team_Unknown | 630–631 | 2 | 1 | Undefined position; Undefined team |
| `71` | `114` | Position_Unknown | Team_Unknown | 635–801 | 167 | 1 | Undefined position; Undefined team |
| `72` | `117` | Position_Unknown | Team_Unknown | 670–686 | 17 | 1 | Undefined position; Undefined team |
| `73` | `118` | Position_Unknown | Team_Unknown | 690–694 | 5 | 1 | Undefined position; Undefined team |
| `74` | `119` | Position_Unknown | Team_Unknown | 695–801 | 91 | 5 | Undefined position; Undefined team |
| `75` | `121` | Position_Unknown | Team_Unknown | 696–697 | 2 | 1 | Undefined position; Undefined team |
| `76` | `122` | Position_Unknown | Team_Unknown | 724–726 | 3 | 1 | Undefined position; Undefined team |
| `77` | `123` | Position_Unknown | Team_Unknown | 739–774 | 9 | 3 | Undefined position; Undefined team |
| `78` | `124` | Position_Unknown | Team_Unknown | 741–801 | 39 | 3 | Undefined position; Undefined team |
| `79` | `125` | Position_Unknown | Team_Unknown | 750–801 | 32 | 4 | Undefined position; Undefined team |
| `80` | `126` | Position_Unknown | Team_Unknown | 750–801 | 49 | 2 | Undefined position; Undefined team |
| `81` | `127` | Position_Unknown | Team_Unknown | 750–751 | 2 | 1 | Undefined position; Undefined team |
| `82` | `128` | Position_Unknown | Team_Unknown | 755–758 | 4 | 1 | Undefined position; Undefined team |
| `83` | `129` | Position_Unknown | Team_Unknown | 762–776 | 11 | 2 | Undefined position; Undefined team |
| `84` | `131` | Position_Unknown | Team_Unknown | 771–798 | 27 | 2 | Undefined position; Undefined team |
| `85` | `132` | Position_Unknown | Team_Unknown | 794–1058 | 192 | 2 | Undefined position; Undefined team |
| `86` | `133` | Position_Unknown | Team_Unknown | 800–801 | 2 | 1 | Undefined position; Undefined team |
| `87` | `134` | Position_Unknown | Team_Unknown | 802–1060 | 209 | 3 | Undefined position; Undefined team |
| `88` | `135` | Position_Unknown | Team_Unknown | 802–1041 | 202 | 2 | Undefined position; Undefined team |
| `89` | `136` | Position_Unknown | Team_Unknown | 802–1033 | 179 | 3 | Undefined position; Undefined team |
| `90` | `137` | Position_Unknown | Team_Unknown | 802–804 | 3 | 1 | Undefined position; Undefined team |
| `91` | `138` | Position_Unknown | Team_Unknown | 802–804 | 3 | 1 | Undefined position; Undefined team |
| `92` | `139` | Position_Unknown | Team_Unknown | 802–1025 | 186 | 2 | Undefined position; Undefined team |
| `93` | `140` | Position_Unknown | Team_Unknown | 802–804 | 3 | 1 | Undefined position; Undefined team |
| `94` | `141` | Position_Unknown | Team_Unknown | 802–1048 | 209 | 2 | Undefined position; Undefined team |
| `95` | `142` | Position_Unknown | Team_Unknown | 802–804 | 3 | 1 | Undefined position; Undefined team |
| `96` | `143` | Position_Unknown | Team_Unknown | 802–804 | 3 | 1 | Undefined position; Undefined team |
| `97` | `144` | Position_Unknown | Team_Unknown | 802–1060 | 216 | 6 | Undefined position; Undefined team |
| `98` | `145` | Position_Unknown | Team_Unknown | 802–804 | 3 | 1 | Undefined position; Undefined team |
| `99` | `146` | Position_Unknown | Team_Unknown | 802–804 | 3 | 1 | Undefined position; Undefined team |
| `100` | `147` | Position_Unknown | Team_Unknown | 802–804 | 3 | 1 | Undefined position; Undefined team |
| `101` | `148` | Position_Unknown | Team_Unknown | 844–1021 | 178 | 1 | Undefined position; Undefined team |
| `102` | `149` | Position_Unknown | Team_Unknown | 844–1041 | 192 | 2 | Undefined position; Undefined team |
| `103` | `150` | Position_Unknown | Team_Unknown | 844–1219 | 369 | 4 | Undefined position; Undefined team |
| `104` | `151` | Position_Unknown | Team_Unknown | 844–858 | 15 | 1 | Undefined position; Undefined team |
| `105` | `152` | Position_Unknown | Team_Unknown | 844–1035 | 192 | 1 | Undefined position; Undefined team |
| `106` | `153` | Position_Unknown | Team_Unknown | 844–1072 | 229 | 1 | Undefined position; Undefined team |
| `107` | `154` | Position_Unknown | Team_Unknown | 844–1060 | 217 | 1 | Undefined position; Undefined team |
| `108` | `155` | Position_Unknown | Team_Unknown | 850–1060 | 127 | 8 | Undefined position; Undefined team |
| `109` | `157` | Position_Unknown | Team_Unknown | 904–918 | 15 | 1 | Undefined position; Undefined team |
| `110` | `158` | Position_Unknown | Team_Unknown | 1016–1062 | 47 | 1 | Undefined position; Undefined team |
| `111` | `159` | Position_Unknown | Team_Unknown | 1028–1063 | 6 | 2 | Undefined position; Undefined team |
| `112` | `160` | Position_Unknown | Team_Unknown | 1029–1046 | 7 | 2 | Undefined position; Undefined team |
| `113` | `164` | Position_Unknown | Team_Unknown | 1035–1062 | 25 | 2 | Undefined position; Undefined team |
| `114` | `165` | Position_Unknown | Team_Unknown | 1038–1180 | 123 | 4 | Undefined position; Undefined team |
| `115` | `166` | Position_Unknown | Team_Unknown | 1040–1117 | 63 | 2 | Undefined position; Undefined team |
| `116` | `167` | Position_Unknown | Team_Unknown | 1040–1053 | 14 | 1 | Undefined position; Undefined team |
| `117` | `168` | Position_Unknown | Team_Unknown | 1047–1048 | 2 | 1 | Undefined position; Undefined team |
| `118` | `169` | Position_Unknown | Team_Unknown | 1047–1048 | 2 | 1 | Undefined position; Undefined team |
| `119` | `170` | Position_Unknown | Team_Unknown | 1049–1157 | 100 | 2 | Undefined position; Undefined team |
| `120` | `173` | Position_Unknown | Team_Unknown | 1061–1169 | 105 | 2 | Undefined position; Undefined team |
| `121` | `175` | Position_Unknown | Team_Unknown | 1061–1086 | 26 | 1 | Undefined position; Undefined team |
| `122` | `176` | Position_Unknown | Team_Unknown | 1061–1063 | 3 | 1 | Undefined position; Undefined team |
| `123` | `179` | Position_Unknown | Team_Unknown | 1066–1166 | 101 | 1 | Undefined position; Undefined team |
| `124` | `182` | Position_Unknown | Team_Unknown | 1068–1219 | 126 | 5 | Undefined position; Undefined team |
| `125` | `185` | Position_Unknown | Team_Unknown | 1078–1219 | 137 | 3 | Undefined position; Undefined team |
| `126` | `187` | Position_Unknown | Team_Unknown | 1083–1084 | 2 | 1 | Undefined position; Undefined team |
| `127` | `188` | Position_Unknown | Team_Unknown | 1083–1219 | 137 | 1 | Undefined position; Undefined team |
| `128` | `189` | Position_Unknown | Team_Unknown | 1098–1159 | 46 | 3 | Undefined position; Undefined team |
| `129` | `190` | Position_Unknown | Team_Unknown | 1101–1194 | 91 | 2 | Undefined position; Undefined team |
| `130` | `191` | Position_Unknown | Team_Unknown | 1142–1219 | 74 | 2 | Undefined position; Undefined team |
| `131` | `193` | Position_Unknown | Team_Unknown | 1144–1219 | 73 | 2 | Undefined position; Undefined team |
| `132` | `194` | Position_Unknown | Team_Unknown | 1164–1168 | 5 | 1 | Undefined position; Undefined team |
| `133` | `196` | Position_Unknown | Team_Unknown | 1176–1219 | 37 | 2 | Undefined position; Undefined team |
| `134` | `198` | Position_Unknown | Team_Unknown | 1194–1219 | 23 | 2 | Undefined position; Undefined team |
| `135` | `199` | Position_Unknown | Team_Unknown | 1196–1199 | 4 | 1 | Undefined position; Undefined team |
| `136` | `200` | Position_Unknown | Team_Unknown | 1208–1210 | 3 | 1 | Undefined position; Undefined team |
| `137` | `201` | Position_Unknown | Team_Unknown | 1217–1218 | 2 | 1 | Undefined position; Undefined team |
| `138` | `202` | Position_Unknown | Team_Unknown | 1220–1229 | 10 | 1 | Undefined position; Undefined team |
| `139` | `203` | Position_Unknown | Team_Unknown | 1220–1261 | 12 | 2 | Undefined position; Undefined team |
| `140` | `204` | Position_Unknown | Team_Unknown | 1220–1743 | 408 | 3 | Undefined position; Undefined team |
| `141` | `205` | Position_Unknown | Team_Unknown | 1220–1229 | 10 | 1 | Undefined position; Undefined team |
| `142` | `206` | Position_Unknown | Team_Unknown | 1220–1229 | 10 | 1 | Undefined position; Undefined team |
| `143` | `207` | Position_Unknown | Team_Unknown | 1220–1229 | 10 | 1 | Undefined position; Undefined team |
| `144` | `208` | Position_Unknown | Team_Unknown | 1220–1302 | 12 | 2 | Undefined position; Undefined team |
| `145` | `209` | Position_Unknown | Team_Unknown | 1220–1229 | 10 | 1 | Undefined position; Undefined team |
| `146` | `210` | Position_Unknown | Team_Unknown | 1220–1229 | 10 | 1 | Undefined position; Undefined team |
| `147` | `211` | Position_Unknown | Team_Unknown | 1220–1743 | 403 | 6 | Undefined position; Undefined team |
| `148` | `212` | Position_Unknown | Team_Unknown | 1220–1229 | 10 | 1 | Undefined position; Undefined team |
| `149` | `213` | Position_Unknown | Team_Unknown | 1220–1229 | 10 | 1 | Undefined position; Undefined team |
| `150` | `214` | Position_Unknown | Team_Unknown | 1220–1229 | 10 | 1 | Undefined position; Undefined team |
| `151` | `215` | Position_Unknown | Team_Unknown | 1220–1229 | 10 | 1 | Undefined position; Undefined team |
| `152` | `216` | Position_Unknown | Team_Unknown | 1220–1229 | 10 | 1 | Undefined position; Undefined team |
| `153` | `217` | Position_Unknown | Team_Unknown | 1220–1745 | 410 | 3 | Undefined position; Undefined team |
| `154` | `218` | Position_Unknown | Team_Unknown | 1220–1745 | 410 | 3 | Undefined position; Undefined team |
| `155` | `219` | Position_Unknown | Team_Unknown | 1220–1229 | 10 | 1 | Undefined position; Undefined team |
| `156` | `220` | Position_Unknown | Team_Unknown | 1220–1474 | 139 | 3 | Undefined position; Undefined team |
| `157` | `221` | Position_Unknown | Team_Unknown | 1220–1229 | 10 | 1 | Undefined position; Undefined team |
| `158` | `222` | Position_Unknown | Team_Unknown | 1265–1302 | 31 | 2 | Undefined position; Undefined team |
| `159` | `223` | Position_Unknown | Team_Unknown | 1314–1954 | 576 | 5 | Undefined position; Undefined team |
| `160` | `224` | Position_Unknown | Team_Unknown | 1314–1474 | 128 | 2 | Undefined position; Undefined team |
| `161` | `225` | Position_Unknown | Team_Unknown | 1314–1479 | 133 | 2 | Undefined position; Undefined team |
| `162` | `226` | Position_Unknown | Team_Unknown | 1314–1743 | 383 | 6 | Undefined position; Undefined team |
| `163` | `227` | Position_Unknown | Team_Unknown | 1314–1463 | 115 | 3 | Undefined position; Undefined team |
| `164` | `228` | Position_Unknown | Team_Unknown | 1314–1720 | 353 | 10 | Undefined position; Undefined team |
| `165` | `229` | Position_Unknown | Team_Unknown | 1314–1474 | 128 | 2 | Undefined position; Undefined team |
| `166` | `230` | Position_Unknown | Team_Unknown | 1314–1743 | 392 | 3 | Undefined position; Undefined team |
| `167` | `231` | Position_Unknown | Team_Unknown | 1314–1465 | 119 | 2 | Undefined position; Undefined team |
| `168` | `232` | Position_Unknown | Team_Unknown | 1314–1743 | 397 | 2 | Undefined position; Undefined team |
| `169` | `233` | Position_Unknown | Team_Unknown | 1314–1742 | 384 | 5 | Undefined position; Undefined team |
| `170` | `234` | Position_Unknown | Team_Unknown | 1314–1485 | 98 | 4 | Undefined position; Undefined team |
| `171` | `235` | Position_Unknown | Team_Unknown | 1314–1627 | 259 | 7 | Undefined position; Undefined team |
| `172` | `236` | Position_Unknown | Team_Unknown | 1314–1481 | 135 | 2 | Undefined position; Undefined team |
| `173` | `237` | Position_Unknown | Team_Unknown | 1314–1743 | 389 | 4 | Undefined position; Undefined team |
| `174` | `238` | Position_Unknown | Team_Unknown | 1314–1659 | 304 | 7 | Undefined position; Undefined team |
| `175` | `239` | Position_Unknown | Team_Unknown | 1314–1409 | 63 | 2 | Undefined position; Undefined team |
| `176` | `240` | Position_Unknown | Team_Unknown | 1350–1743 | 346 | 4 | Undefined position; Undefined team |
| `177` | `242` | Position_Unknown | Team_Unknown | 1450–1745 | 253 | 4 | Undefined position; Undefined team |
| `178` | `245` | Position_Unknown | Team_Unknown | 1458–1460 | 3 | 1 | Undefined position; Undefined team |
| `179` | `246` | Position_Unknown | Team_Unknown | 1466–1467 | 2 | 1 | Undefined position; Undefined team |
| `180` | `247` | Position_Unknown | Team_Unknown | 1472–1743 | 248 | 6 | Undefined position; Undefined team |
| `181` | `250` | Position_Unknown | Team_Unknown | 1475–1743 | 257 | 3 | Undefined position; Undefined team |
| `182` | `251` | Position_Unknown | Team_Unknown | 1475–1640 | 166 | 1 | Undefined position; Undefined team |
| `183` | `252` | Position_Unknown | Team_Unknown | 1477–1485 | 9 | 1 | Undefined position; Undefined team |
| `184` | `253` | Position_Unknown | Team_Unknown | 1480–1644 | 165 | 1 | Undefined position; Undefined team |
| `185` | `254` | Position_Unknown | Team_Unknown | 1480–1481 | 2 | 1 | Undefined position; Undefined team |
| `186` | `255` | Position_Unknown | Team_Unknown | 1480–1481 | 2 | 1 | Undefined position; Undefined team |
| `187` | `256` | Position_Unknown | Team_Unknown | 1482–1743 | 262 | 1 | Undefined position; Undefined team |
| `188` | `257` | Position_Unknown | Team_Unknown | 1482–1483 | 2 | 1 | Undefined position; Undefined team |
| `189` | `258` | Position_Unknown | Team_Unknown | 1486–1738 | 241 | 3 | Undefined position; Undefined team |
| `190` | `260` | Position_Unknown | Team_Unknown | 1489–1743 | 252 | 2 | Undefined position; Undefined team |
| `191` | `262` | Position_Unknown | Team_Unknown | 1506–1517 | 12 | 1 | Undefined position; Undefined team |
| `192` | `265` | Position_Unknown | Team_Unknown | 1609–1612 | 4 | 1 | Undefined position; Undefined team |
| `193` | `268` | Position_Unknown | Team_Unknown | 1623–1657 | 33 | 2 | Undefined position; Undefined team |
| `194` | `269` | Position_Unknown | Team_Unknown | 1642–1712 | 67 | 2 | Undefined position; Undefined team |
| `195` | `270` | Position_Unknown | Team_Unknown | 1662–1685 | 13 | 3 | Undefined position; Undefined team |
| `196` | `271` | Position_Unknown | Team_Unknown | 1666–1745 | 80 | 1 | Undefined position; Undefined team |
| `197` | `272` | Position_Unknown | Team_Unknown | 1670–1743 | 72 | 2 | Undefined position; Undefined team |
| `198` | `273` | Position_Unknown | Team_Unknown | 1690–1955 | 239 | 2 | Undefined position; Undefined team |
| `199` | `274` | Position_Unknown | Team_Unknown | 1731–1743 | 7 | 2 | Undefined position; Undefined team |
| `200` | `275` | Position_Unknown | Team_Unknown | 1744–1954 | 184 | 2 | Undefined position; Undefined team |
| `201` | `276` | Position_Unknown | Team_Unknown | 1744–1960 | 190 | 2 | Undefined position; Undefined team |
| `202` | `277` | Position_Unknown | Team_Unknown | 1744–1943 | 173 | 2 | Undefined position; Undefined team |
| `203` | `278` | Position_Unknown | Team_Unknown | 1744–1935 | 165 | 2 | Undefined position; Undefined team |
| `204` | `279` | Position_Unknown | Team_Unknown | 1744–1954 | 184 | 2 | Undefined position; Undefined team |
| `205` | `280` | Position_Unknown | Team_Unknown | 1744–1954 | 184 | 2 | Undefined position; Undefined team |
| `206` | `281` | Position_Unknown | Team_Unknown | 1744–1954 | 184 | 2 | Undefined position; Undefined team |
| `207` | `282` | Position_Unknown | Team_Unknown | 1744–1954 | 184 | 2 | Undefined position; Undefined team |
| `208` | `283` | Position_Unknown | Team_Unknown | 1744–1954 | 184 | 2 | Undefined position; Undefined team |
| `209` | `284` | Position_Unknown | Team_Unknown | 1744–1973 | 203 | 2 | Undefined position; Undefined team |
| `210` | `285` | Position_Unknown | Team_Unknown | 1744–1920 | 150 | 2 | Undefined position; Undefined team |
| `211` | `286` | Position_Unknown | Team_Unknown | 1744–1946 | 176 | 2 | Undefined position; Undefined team |
| `212` | `287` | Position_Unknown | Team_Unknown | 1744–1958 | 188 | 2 | Undefined position; Undefined team |
| `213` | `288` | Position_Unknown | Team_Unknown | 1774–1960 | 187 | 1 | Undefined position; Undefined team |
| `214` | `289` | Position_Unknown | Team_Unknown | 1774–1954 | 181 | 1 | Undefined position; Undefined team |
| `215` | `290` | Position_Unknown | Team_Unknown | 1774–1954 | 181 | 1 | Undefined position; Undefined team |
| `216` | `291` | Position_Unknown | Team_Unknown | 1856–2114 | 245 | 4 | Undefined position; Undefined team |
| `217` | `292` | Position_Unknown | Team_Unknown | 1888–1960 | 10 | 2 | Undefined position; Undefined team |
| `218` | `295` | Position_Unknown | Team_Unknown | 1913–1915 | 3 | 1 | Undefined position; Undefined team |
| `219` | `296` | Position_Unknown | Team_Unknown | 1938–1941 | 4 | 1 | Undefined position; Undefined team |
| `220` | `298` | Position_Unknown | Team_Unknown | 1955–1971 | 17 | 1 | Undefined position; Undefined team |
| `221` | `299` | Position_Unknown | Team_Unknown | 1955–1962 | 8 | 1 | Undefined position; Undefined team |
| `222` | `300` | Position_Unknown | Team_Unknown | 1955–2114 | 159 | 2 | Undefined position; Undefined team |
| `223` | `301` | Position_Unknown | Team_Unknown | 1955–1957 | 3 | 1 | Undefined position; Undefined team |
| `224` | `302` | Position_Unknown | Team_Unknown | 1955–1993 | 39 | 1 | Undefined position; Undefined team |
| `225` | `304` | Position_Unknown | Team_Unknown | 1958–1975 | 18 | 1 | Undefined position; Undefined team |
| `226` | `306` | Position_Unknown | Team_Unknown | 1962–2114 | 137 | 4 | Undefined position; Undefined team |
| `227` | `308` | Position_Unknown | Team_Unknown | 1966–2114 | 149 | 1 | Undefined position; Undefined team |
| `228` | `309` | Position_Unknown | Team_Unknown | 1969–2114 | 145 | 2 | Undefined position; Undefined team |
| `229` | `310` | Position_Unknown | Team_Unknown | 1985–2020 | 34 | 2 | Undefined position; Undefined team |
| `230` | `312` | Position_Unknown | Team_Unknown | 1995–1996 | 2 | 1 | Undefined position; Undefined team |
| `231` | `314` | Position_Unknown | Team_Unknown | 2005–2007 | 3 | 1 | Undefined position; Undefined team |
| `232` | `315` | Position_Unknown | Team_Unknown | 2009–2012 | 4 | 1 | Undefined position; Undefined team |
| `233` | `317` | Position_Unknown | Team_Unknown | 2020–2071 | 8 | 2 | Undefined position; Undefined team |
| `234` | `318` | Position_Unknown | Team_Unknown | 2027–2114 | 88 | 1 | Undefined position; Undefined team |
| `235` | `320` | Position_Unknown | Team_Unknown | 2033–2034 | 2 | 1 | Undefined position; Undefined team |
| `236` | `321` | Position_Unknown | Team_Unknown | 2060–2061 | 2 | 1 | Undefined position; Undefined team |
| `237` | `322` | Position_Unknown | Team_Unknown | 2063–2105 | 5 | 2 | Undefined position; Undefined team |
| `238` | `323` | Position_Unknown | Team_Unknown | 2067–2114 | 48 | 1 | Undefined position; Undefined team |
| `239` | `324` | Position_Unknown | Team_Unknown | 2076–2114 | 39 | 1 | Undefined position; Undefined team |
| `240` | `325` | Position_Unknown | Team_Unknown | 2087–2114 | 28 | 1 | Undefined position; Undefined team |
| `241` | `326` | Position_Unknown | Team_Unknown | 2094–2114 | 21 | 1 | Undefined position; Undefined team |
| `242` | `328` | Position_Unknown | Team_Unknown | 2098–2106 | 8 | 2 | Undefined position; Undefined team |
| `243` | `329` | Position_Unknown | Team_Unknown | 2101–2114 | 14 | 1 | Undefined position; Undefined team |
| `244` | `330` | Position_Unknown | Team_Unknown | 2105–2114 | 10 | 1 | Undefined position; Undefined team |
| `245` | `331` | Position_Unknown | Team_Unknown | 2105–2114 | 10 | 1 | Undefined position; Undefined team |
| `246` | `332` | Position_Unknown | Team_Unknown | 2106–2114 | 9 | 1 | Undefined position; Undefined team |
| `247` | `333` | Position_Unknown | Team_Unknown | 2138–2174 | 36 | 2 | Undefined position; Undefined team |
| `248` | `334` | Position_Unknown | Team_Unknown | 2138–2176 | 34 | 4 | Undefined position; Undefined team |
| `249` | `335` | Position_Unknown | Team_Unknown | 2138–2175 | 32 | 4 | Undefined position; Undefined team |
| `250` | `336` | Position_Unknown | Team_Unknown | 2138–2174 | 37 | 1 | Undefined position; Undefined team |
| `251` | `337` | Position_Unknown | Team_Unknown | 2138–2174 | 12 | 3 | Undefined position; Undefined team |
| `252` | `338` | Position_Unknown | Team_Unknown | 2138–2176 | 38 | 2 | Undefined position; Undefined team |
| `253` | `339` | Position_Unknown | Team_Unknown | 2141–2176 | 6 | 2 | Undefined position; Undefined team |
| `254` | `340` | Position_Unknown | Team_Unknown | 2142–2173 | 17 | 3 | Undefined position; Undefined team |
| `255` | `345` | Position_Unknown | Team_Unknown | 2155–2177 | 13 | 4 | Undefined position; Undefined team |
| `256` | `348` | Position_Unknown | Team_Unknown | 2172–2173 | 2 | 1 | Undefined position; Undefined team |
| `257` | `349` | Position_Unknown | Team_Unknown | 2174–2176 | 3 | 1 | Undefined position; Undefined team |
| `258` | `350` | Position_Unknown | Team_Unknown | 2180–2183 | 4 | 1 | Undefined position; Undefined team |
| `259` | `351` | Position_Unknown | Team_Unknown | 2225–2422 | 198 | 1 | Undefined position; Undefined team |
| `260` | `352` | Position_Unknown | Team_Unknown | 2225–2421 | 193 | 3 | Undefined position; Undefined team |
| `261` | `353` | Position_Unknown | Team_Unknown | 2225–2462 | 237 | 2 | Undefined position; Undefined team |
| `262` | `354` | Position_Unknown | Team_Unknown | 2225–2447 | 210 | 2 | Undefined position; Undefined team |
| `263` | `355` | Position_Unknown | Team_Unknown | 2225–2444 | 214 | 3 | Undefined position; Undefined team |
| `264` | `356` | Position_Unknown | Team_Unknown | 2225–2533 | 300 | 5 | Undefined position; Undefined team |
| `265` | `357` | Position_Unknown | Team_Unknown | 2225–2423 | 199 | 1 | Undefined position; Undefined team |
| `266` | `358` | Position_Unknown | Team_Unknown | 2225–2373 | 149 | 1 | Undefined position; Undefined team |
| `267` | `359` | Position_Unknown | Team_Unknown | 2225–2425 | 201 | 1 | Undefined position; Undefined team |
| `268` | `360` | Position_Unknown | Team_Unknown | 2225–2451 | 227 | 1 | Undefined position; Undefined team |
| `269` | `361` | Position_Unknown | Team_Unknown | 2225–2539 | 315 | 1 | Undefined position; Undefined team |
| `270` | `362` | Position_Unknown | Team_Unknown | 2225–2649 | 420 | 2 | Undefined position; Undefined team |
| `271` | `363` | Position_Unknown | Team_Unknown | 2225–2569 | 331 | 4 | Undefined position; Undefined team |
| `272` | `364` | Position_Unknown | Team_Unknown | 2225–2535 | 309 | 2 | Undefined position; Undefined team |
| `273` | `365` | Position_Unknown | Team_Unknown | 2225–2449 | 225 | 1 | Undefined position; Undefined team |
| `274` | `366` | Position_Unknown | Team_Unknown | 2225–2407 | 183 | 1 | Undefined position; Undefined team |
| `275` | `367` | Position_Unknown | Team_Unknown | 2225–2449 | 214 | 4 | Undefined position; Undefined team |
| `276` | `368` | Position_Unknown | Team_Unknown | 2225–2414 | 190 | 1 | Undefined position; Undefined team |
| `277` | `369` | Position_Unknown | Team_Unknown | 2225–2565 | 332 | 3 | Undefined position; Undefined team |
| `278` | `370` | Position_Unknown | Team_Unknown | 2225–2372 | 140 | 2 | Undefined position; Undefined team |
| `279` | `371` | Position_Unknown | Team_Unknown | 2225–2430 | 206 | 1 | Undefined position; Undefined team |
| `280` | `372` | Position_Unknown | Team_Unknown | 2225–2421 | 197 | 1 | Undefined position; Undefined team |
| `281` | `373` | Position_Unknown | Team_Unknown | 2375–2402 | 14 | 2 | Undefined position; Undefined team |
| `282` | `374` | Position_Unknown | Team_Unknown | 2378–2443 | 66 | 1 | Undefined position; Undefined team |
| `283` | `375` | Position_Unknown | Team_Unknown | 2378–2381 | 4 | 1 | Undefined position; Undefined team |
| `284` | `376` | Position_Unknown | Team_Unknown | 2418–2554 | 137 | 1 | Undefined position; Undefined team |
| `285` | `377` | Position_Unknown | Team_Unknown | 2422–2449 | 28 | 1 | Undefined position; Undefined team |
| `286` | `378` | Position_Unknown | Team_Unknown | 2463–2542 | 77 | 2 | Undefined position; Undefined team |
| `287` | `380` | Position_Unknown | Team_Unknown | 2473–2566 | 87 | 2 | Undefined position; Undefined team |
| `288` | `382` | Position_Unknown | Team_Unknown | 2481–2961 | 413 | 2 | Undefined position; Undefined team |
| `289` | `383` | Position_Unknown | Team_Unknown | 2494–2643 | 103 | 5 | Undefined position; Undefined team |
| `290` | `384` | Position_Unknown | Team_Unknown | 2509–2584 | 76 | 1 | Undefined position; Undefined team |
| `291` | `387` | Position_Unknown | Team_Unknown | 2536–2646 | 104 | 2 | Undefined position; Undefined team |
| `292` | `389` | Position_Unknown | Team_Unknown | 2564–2649 | 76 | 3 | Undefined position; Undefined team |
| `293` | `390` | Position_Unknown | Team_Unknown | 2564–2649 | 86 | 1 | Undefined position; Undefined team |
| `294` | `395` | Position_Unknown | Team_Unknown | 2608–2804 | 164 | 3 | Undefined position; Undefined team |
| `295` | `398` | Position_Unknown | Team_Unknown | 2611–2644 | 34 | 1 | Undefined position; Undefined team |
| `296` | `399` | Position_Unknown | Team_Unknown | 2613–2639 | 27 | 1 | Undefined position; Undefined team |
| `297` | `401` | Position_Unknown | Team_Unknown | 2625–2641 | 17 | 1 | Undefined position; Undefined team |
| `298` | `402` | Position_Unknown | Team_Unknown | 2630–2634 | 5 | 1 | Undefined position; Undefined team |
| `299` | `403` | Position_Unknown | Team_Unknown | 2630–2631 | 2 | 1 | Undefined position; Undefined team |
| `300` | `404` | Position_Unknown | Team_Unknown | 2632–2633 | 2 | 1 | Undefined position; Undefined team |
| `301` | `405` | Position_Unknown | Team_Unknown | 2633–2649 | 17 | 1 | Undefined position; Undefined team |
| `302` | `406` | Position_Unknown | Team_Unknown | 2633–2638 | 6 | 1 | Undefined position; Undefined team |
| `303` | `407` | Position_Unknown | Team_Unknown | 2681–2798 | 117 | 2 | Undefined position; Undefined team |
| `304` | `408` | Position_Unknown | Team_Unknown | 2681–2984 | 265 | 3 | Undefined position; Undefined team |
| `305` | `409` | Position_Unknown | Team_Unknown | 2681–2798 | 115 | 2 | Undefined position; Undefined team |
| `306` | `410` | Position_Unknown | Team_Unknown | 2681–2935 | 251 | 3 | Undefined position; Undefined team |
| `307` | `411` | Position_Unknown | Team_Unknown | 2681–2795 | 110 | 2 | Undefined position; Undefined team |
| `308` | `412` | Position_Unknown | Team_Unknown | 2681–2750 | 69 | 2 | Undefined position; Undefined team |
| `309` | `413` | Position_Unknown | Team_Unknown | 2681–2840 | 157 | 2 | Undefined position; Undefined team |
| `310` | `414` | Position_Unknown | Team_Unknown | 2681–2822 | 138 | 2 | Undefined position; Undefined team |
| `311` | `415` | Position_Unknown | Team_Unknown | 2681–3078 | 363 | 5 | Undefined position; Undefined team |
| `312` | `416` | Position_Unknown | Team_Unknown | 2681–2748 | 68 | 1 | Undefined position; Undefined team |
| `313` | `417` | Position_Unknown | Team_Unknown | 2681–2803 | 121 | 2 | Undefined position; Undefined team |
| `314` | `418` | Position_Unknown | Team_Unknown | 2681–3049 | 368 | 2 | Undefined position; Undefined team |
| `315` | `419` | Position_Unknown | Team_Unknown | 2681–2836 | 148 | 3 | Undefined position; Undefined team |
| `316` | `420` | Position_Unknown | Team_Unknown | 2681–2800 | 115 | 3 | Undefined position; Undefined team |
| `317` | `421` | Position_Unknown | Team_Unknown | 2681–2752 | 72 | 1 | Undefined position; Undefined team |
| `318` | `424` | Position_Unknown | Team_Unknown | 2751–2913 | 147 | 5 | Undefined position; Undefined team |
| `319` | `425` | Position_Unknown | Team_Unknown | 2761–2788 | 28 | 1 | Undefined position; Undefined team |
| `320` | `428` | Position_Unknown | Team_Unknown | 2780–2814 | 30 | 2 | Undefined position; Undefined team |
| `321` | `429` | Position_Unknown | Team_Unknown | 2788–2817 | 29 | 2 | Undefined position; Undefined team |
| `322` | `430` | Position_Unknown | Team_Unknown | 2790–2802 | 13 | 1 | Undefined position; Undefined team |
| `323` | `433` | Position_Unknown | Team_Unknown | 2808–2898 | 86 | 2 | Undefined position; Undefined team |
| `324` | `435` | Position_Unknown | Team_Unknown | 2826–2828 | 3 | 1 | Undefined position; Undefined team |
| `325` | `436` | Position_Unknown | Team_Unknown | 2863–3078 | 210 | 3 | Undefined position; Undefined team |
| `326` | `437` | Position_Unknown | Team_Unknown | 2863–2864 | 2 | 1 | Undefined position; Undefined team |
| `327` | `438` | Position_Unknown | Team_Unknown | 2875–3078 | 188 | 3 | Undefined position; Undefined team |
| `328` | `439` | Position_Unknown | Team_Unknown | 2881–3078 | 157 | 6 | Undefined position; Undefined team |
| `329` | `440` | Position_Unknown | Team_Unknown | 2886–2995 | 81 | 2 | Undefined position; Undefined team |
| `330` | `442` | Position_Unknown | Team_Unknown | 2889–3078 | 190 | 1 | Undefined position; Undefined team |
| `331` | `444` | Position_Unknown | Team_Unknown | 2907–3078 | 169 | 2 | Undefined position; Undefined team |
| `332` | `446` | Position_Unknown | Team_Unknown | 2919–3078 | 154 | 3 | Undefined position; Undefined team |
| `333` | `447` | Position_Unknown | Team_Unknown | 2928–2929 | 2 | 1 | Undefined position; Undefined team |
| `334` | `448` | Position_Unknown | Team_Unknown | 2930–2990 | 61 | 1 | Undefined position; Undefined team |
| `335` | `449` | Position_Unknown | Team_Unknown | 2941–2962 | 22 | 1 | Undefined position; Undefined team |
| `336` | `450` | Position_Unknown | Team_Unknown | 2945–3078 | 93 | 7 | Undefined position; Undefined team |
| `337` | `452` | Position_Unknown | Team_Unknown | 2948–2957 | 10 | 1 | Undefined position; Undefined team |
| `338` | `453` | Position_Unknown | Team_Unknown | 2965–3078 | 110 | 3 | Undefined position; Undefined team |
| `339` | `454` | Position_Unknown | Team_Unknown | 2989–3011 | 23 | 1 | Undefined position; Undefined team |
| `340` | `455` | Position_Unknown | Team_Unknown | 2995–3078 | 84 | 1 | Undefined position; Undefined team |
| `341` | `456` | Position_Unknown | Team_Unknown | 3006–3078 | 73 | 1 | Undefined position; Undefined team |
| `342` | `457` | Position_Unknown | Team_Unknown | 3014–3078 | 58 | 2 | Undefined position; Undefined team |
| `343` | `459` | Position_Unknown | Team_Unknown | 3042–3068 | 19 | 2 | Undefined position; Undefined team |
| `344` | `461` | Position_Unknown | Team_Unknown | 3096–3155 | 60 | 1 | Undefined position; Undefined team |
| `345` | `462` | Position_Unknown | Team_Unknown | 3096–3155 | 60 | 1 | Undefined position; Undefined team |
| `346` | `463` | Position_Unknown | Team_Unknown | 3096–3155 | 60 | 1 | Undefined position; Undefined team |
| `347` | `464` | Position_Unknown | Team_Unknown | 3098–3100 | 3 | 1 | Undefined position; Undefined team |
| `348` | `465` | Position_Unknown | Team_Unknown | 3102–3146 | 27 | 4 | Undefined position; Undefined team |
| `349` | `467` | Position_Unknown | Team_Unknown | 3130–3131 | 2 | 1 | Undefined position; Undefined team |
| `350` | `469` | Position_Unknown | Team_Unknown | 3199–3668 | 470 | 1 | Undefined position; Undefined team |
| `351` | `470` | Position_Unknown | Team_Unknown | 3199–3668 | 450 | 3 | Undefined position; Undefined team |
| `352` | `471` | Position_Unknown | Team_Unknown | 3199–3502 | 304 | 1 | Undefined position; Undefined team |
| `353` | `472` | Position_Unknown | Team_Unknown | 3199–3628 | 427 | 4 | Undefined position; Undefined team |
| `354` | `473` | Position_Unknown | Team_Unknown | 3199–3668 | 470 | 1 | Undefined position; Undefined team |
| `355` | `474` | Position_Unknown | Team_Unknown | 3199–3668 | 470 | 1 | Undefined position; Undefined team |
| `356` | `475` | Position_Unknown | Team_Unknown | 3199–3618 | 404 | 4 | Undefined position; Undefined team |
| `357` | `476` | Position_Unknown | Team_Unknown | 3199–3668 | 470 | 1 | Undefined position; Undefined team |
| `358` | `477` | Position_Unknown | Team_Unknown | 3199–3869 | 629 | 2 | Undefined position; Undefined team |
| `359` | `478` | Position_Unknown | Team_Unknown | 3199–3869 | 618 | 3 | Undefined position; Undefined team |
| `360` | `479` | Position_Unknown | Team_Unknown | 3199–3668 | 468 | 3 | Undefined position; Undefined team |
| `361` | `480` | Position_Unknown | Team_Unknown | 3199–3668 | 470 | 1 | Undefined position; Undefined team |
| `362` | `481` | Position_Unknown | Team_Unknown | 3199–3668 | 459 | 2 | Undefined position; Undefined team |
| `363` | `482` | Position_Unknown | Team_Unknown | 3199–3668 | 449 | 4 | Undefined position; Undefined team |
| `364` | `483` | Position_Unknown | Team_Unknown | 3199–3668 | 459 | 3 | Undefined position; Undefined team |
| `365` | `484` | Position_Unknown | Team_Unknown | 3199–3668 | 468 | 2 | Undefined position; Undefined team |
| `366` | `485` | Position_Unknown | Team_Unknown | 3199–3668 | 470 | 1 | Undefined position; Undefined team |
| `367` | `486` | Position_Unknown | Team_Unknown | 3199–3427 | 221 | 2 | Undefined position; Undefined team |
| `368` | `487` | Position_Unknown | Team_Unknown | 3199–3461 | 263 | 1 | Undefined position; Undefined team |
| `369` | `488` | Position_Unknown | Team_Unknown | 3199–3668 | 467 | 3 | Undefined position; Undefined team |
| `370` | `489` | Position_Unknown | Team_Unknown | 3199–3668 | 436 | 2 | Undefined position; Undefined team |
| `371` | `490` | Position_Unknown | Team_Unknown | 3199–3668 | 464 | 4 | Undefined position; Undefined team |
| `372` | `492` | Position_Unknown | Team_Unknown | 3287–3305 | 6 | 2 | Undefined position; Undefined team |
| `373` | `493` | Position_Unknown | Team_Unknown | 3424–3437 | 12 | 2 | Undefined position; Undefined team |
| `374` | `495` | Position_Unknown | Team_Unknown | 3437–3668 | 232 | 1 | Undefined position; Undefined team |
| `375` | `496` | Position_Unknown | Team_Unknown | 3453–3454 | 2 | 1 | Undefined position; Undefined team |
| `376` | `500` | Position_Unknown | Team_Unknown | 3473–3668 | 196 | 1 | Undefined position; Undefined team |
| `377` | `502` | Position_Unknown | Team_Unknown | 3499–3668 | 165 | 2 | Undefined position; Undefined team |
| `378` | `503` | Position_Unknown | Team_Unknown | 3515–3571 | 32 | 6 | Undefined position; Undefined team |
| `379` | `508` | Position_Unknown | Team_Unknown | 3544–3545 | 2 | 1 | Undefined position; Undefined team |
| `380` | `509` | Position_Unknown | Team_Unknown | 3545–3604 | 41 | 4 | Undefined position; Undefined team |
| `381` | `511` | Position_Unknown | Team_Unknown | 3571–3633 | 27 | 4 | Undefined position; Undefined team |
| `382` | `514` | Position_Unknown | Team_Unknown | 3587–3601 | 13 | 3 | Undefined position; Undefined team |
| `383` | `517` | Position_Unknown | Team_Unknown | 3620–3668 | 33 | 6 | Undefined position; Undefined team |
| `384` | `519` | Position_Unknown | Team_Unknown | 3633–3663 | 28 | 4 | Undefined position; Undefined team |
| `385` | `521` | Position_Unknown | Team_Unknown | 3651–3659 | 9 | 1 | Undefined position; Undefined team |
| `386` | `522` | Position_Unknown | Team_Unknown | 3656–3664 | 7 | 2 | Undefined position; Undefined team |
| `387` | `523` | Position_Unknown | Team_Unknown | 3660–3668 | 7 | 2 | Undefined position; Undefined team |
| `388` | `524` | Position_Unknown | Team_Unknown | 3662–3663 | 2 | 1 | Undefined position; Undefined team |
| `389` | `525` | Position_Unknown | Team_Unknown | 3712–3869 | 158 | 1 | Undefined position; Undefined team |
| `390` | `526` | Position_Unknown | Team_Unknown | 3712–3869 | 158 | 1 | Undefined position; Undefined team |
| `391` | `527` | Position_Unknown | Team_Unknown | 3712–3869 | 158 | 1 | Undefined position; Undefined team |
| `392` | `528` | Position_Unknown | Team_Unknown | 3712–3869 | 154 | 2 | Undefined position; Undefined team |
| `393` | `529` | Position_Unknown | Team_Unknown | 3712–3869 | 157 | 2 | Undefined position; Undefined team |
| `394` | `530` | Position_Unknown | Team_Unknown | 3712–3869 | 158 | 1 | Undefined position; Undefined team |
| `395` | `531` | Position_Unknown | Team_Unknown | 3712–3869 | 158 | 1 | Undefined position; Undefined team |
| `396` | `532` | Position_Unknown | Team_Unknown | 3712–3869 | 158 | 1 | Undefined position; Undefined team |
| `397` | `533` | Position_Unknown | Team_Unknown | 3712–3869 | 158 | 1 | Undefined position; Undefined team |
| `398` | `534` | Position_Unknown | Team_Unknown | 3712–3869 | 158 | 1 | Undefined position; Undefined team |
| `399` | `535` | Position_Unknown | Team_Unknown | 3712–3869 | 158 | 1 | Undefined position; Undefined team |
| `400` | `536` | Position_Unknown | Team_Unknown | 3712–3869 | 158 | 1 | Undefined position; Undefined team |
| `401` | `537` | Position_Unknown | Team_Unknown | 3717–3813 | 97 | 1 | Undefined position; Undefined team |
| `402` | `538` | Position_Unknown | Team_Unknown | 3729–3739 | 11 | 1 | Undefined position; Undefined team |
| `403` | `539` | Position_Unknown | Team_Unknown | 3750–3869 | 44 | 4 | Undefined position; Undefined team |
| `404` | `540` | Position_Unknown | Team_Unknown | 3755–3757 | 3 | 1 | Undefined position; Undefined team |
| `405` | `541` | Position_Unknown | Team_Unknown | 3768–3835 | 67 | 2 | Undefined position; Undefined team |
| `406` | `542` | Position_Unknown | Team_Unknown | 3790–3793 | 4 | 1 | Undefined position; Undefined team |
| `407` | `543` | Position_Unknown | Team_Unknown | 3822–3837 | 16 | 1 | Undefined position; Undefined team |
| `408` | `544` | Position_Unknown | Team_Unknown | 3823–3826 | 4 | 1 | Undefined position; Undefined team |
| `409` | `545` | Position_Unknown | Team_Unknown | 3836–3838 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `10` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Toss` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 397 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 397 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 794 |
| Missing visible bounding boxes during action | 841 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 3869 as fallback play end.
- ⚠️ Action 'Action_None' range [31-77] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-274] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-78] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-65] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-174] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-62] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-190] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-274] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-85] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-152] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-235] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-274] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-55] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-88] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-48] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-275] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [36-42] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [46-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [49-53] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [55-56] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [61-65] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-43] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [49-53] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 57, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [57-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-75] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-183] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [24-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [46-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [59-93] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [95-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [139-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [157-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [181-248] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [267-274] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-190] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-100] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-140] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-174] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-108] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-192] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-205] for track '21' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-250] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-191] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-262] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-274] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-167] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-201] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-274] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-275] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-248] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-274] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-207] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-229] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-230] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-274] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-245] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-274] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-232] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-259] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-274] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-274] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-284] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-284] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-284] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-284] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-284] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-284] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-284] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-284] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-284] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-284] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-734] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [737-766] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-723] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-801] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-667] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-723] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [725-726] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [728-732] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [737-739] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [749-757] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [761-790] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [796-801] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-715] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [720-721] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [741-780] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [782-801] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-615] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-722] for track '51' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [728-730] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [749-801] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-801] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-801] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-694] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-549] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-562] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-642] for track '55' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [645-651] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-725] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-801] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-801] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-451] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-801] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-617] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [645-801] for track '59' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-595] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-584] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-608] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-631] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-801] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-623] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-632] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-801] for track '63' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-801] for track '64' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-736] for track '65' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [738-741] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [743-779] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [781-800] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-418] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-471] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-723] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-724] for track '68' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [749-757] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [761-764] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [766-767] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [770-777] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-627] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-630] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [694-756] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [758-764] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [766-801] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-631] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-801] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [670-686] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-694] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [695-726] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [735-736] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [742-757] for track '74' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [759-766] for track '74' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [769-801] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [696-697] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [724-726] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [739-743] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [770-771] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [773-774] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [741-758] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [761-766] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [787-801] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [750-756] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [763-764] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [770-781] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [791-801] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [750-757] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [761-801] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [750-751] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [755-758] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [762-766] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [771-776] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [771-794] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [796-798] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [794-800] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [874-1058] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [800-801] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [843-1026] for track '87' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1039-1060] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [843-1041] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [857-1029] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1031-1033] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [843-1025] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [843-1048] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '96' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '97' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [843-941] for track '97' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [943-944] for track '97' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [946-1015] for track '97' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1017-1018] for track '97' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1021-1060] for track '97' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '98' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [802-804] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [844-1021] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [844-866] for track '102' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [873-1041] for track '102' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [844-1131] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1133-1145] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1150-1156] for track '103' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1159-1219] for track '103' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [844-858] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [844-1035] for track '105' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [844-1072] for track '106' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [844-1060] for track '107' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [850-876] for track '108' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [882-885] for track '108' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [888-909] for track '108' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [911-919] for track '108' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [924-925] for track '108' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [927-928] for track '108' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [934-949] for track '108' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1016-1060] for track '108' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [904-918] for track '109' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1016-1062] for track '110' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1028-1029] for track '111' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1060-1063] for track '111' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1029-1033] for track '112' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1045-1046] for track '112' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1035-1046] for track '113' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1050-1062] for track '113' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1038-1060] for track '114' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1069-1077] for track '114' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1086-1138] for track '114' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1143-1180] for track '114' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1040-1045] for track '115' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1061-1117] for track '115' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1040-1053] for track '116' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1047-1048] for track '117' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1047-1048] for track '118' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1049-1068] for track '119' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1078-1157] for track '119' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1061-1148] for track '120' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1153-1169] for track '120' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1061-1086] for track '121' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1061-1063] for track '122' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1066-1166] for track '123' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1068-1073] for track '124' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1091-1142] for track '124' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1147-1164] for track '124' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1169-1214] for track '124' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1216-1219] for track '124' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1078-1186] for track '125' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1190-1211] for track '125' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1214-1219] for track '125' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1083-1084] for track '126' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1083-1219] for track '127' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1098-1124] for track '128' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1127-1138] for track '128' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1153-1159] for track '128' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1101-1170] for track '129' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1174-1194] for track '129' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1142-1206] for track '130' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1211-1219] for track '130' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1144-1163] for track '131' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1167-1219] for track '131' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1164-1168] for track '132' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1176-1178] for track '133' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1186-1219] for track '133' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1194-1214] for track '134' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1218-1219] for track '134' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1196-1199] for track '135' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1208-1210] for track '136' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1217-1218] for track '137' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '138' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '139' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1260-1261] for track '139' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '140' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1313-1315] for track '140' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1743] for track '140' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '141' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '142' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '143' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '144' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1301-1302] for track '144' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '145' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '146' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '147' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1313-1315] for track '147' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1696] for track '147' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1699-1705] for track '147' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1708-1737] for track '147' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1739-1743] for track '147' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '148' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '149' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '150' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '151' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '152' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '153' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1313-1315] for track '153' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1745] for track '153' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '154' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1313-1315] for track '154' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1745] for track '154' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '155' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '156' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1313-1315] for track '156' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1474] for track '156' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1220-1229] for track '157' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1265-1266] for track '158' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1274-1302] for track '158' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '159' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1613] for track '159' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1616-1743] for track '159' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1890] for track '159' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1892-1954] for track '159' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '160' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1474] for track '160' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '161' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1479] for track '161' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '162' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1523] for track '162' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1529-1530] for track '162' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1532-1598] for track '162' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1601-1633] for track '162' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1640-1743] for track '162' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '163' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1459] for track '163' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1462-1463] for track '163' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '164' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1481] for track '164' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1486-1623] for track '164' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1625-1646] for track '164' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1648-1667] for track '164' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1670-1680] for track '164' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1684-1688] for track '164' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1691-1696] for track '164' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1698-1711] for track '164' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1719-1720] for track '164' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '165' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1474] for track '165' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '166' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1505] for track '166' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1511-1743] for track '166' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '167' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1465] for track '167' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '168' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1743] for track '168' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '169' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1643] for track '169' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1645-1665] for track '169' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1668-1678] for track '169' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1688-1742] for track '169' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '170' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1437] for track '170' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1439-1440] for track '170' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1481-1485] for track '170' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '171' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1540] for track '171' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1542-1570] for track '171' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1572-1590] for track '171' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1605-1616] for track '171' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1621-1622] for track '171' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1625-1627] for track '171' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '172' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1481] for track '172' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '173' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1642] for track '173' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1648-1649] for track '173' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1653-1743] for track '173' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '174' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1380] for track '174' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1382-1383] for track '174' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1385-1587] for track '174' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1593-1594] for track '174' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1596-1642] for track '174' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1644-1659] for track '174' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1314-1315] for track '175' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1349-1409] for track '175' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1350-1353] for track '176' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1380-1389] for track '176' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1407-1705] for track '176' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1711-1743] for track '176' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1450-1622] for track '177' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1626-1641] for track '177' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1668-1674] for track '177' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1689-1745] for track '177' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1458-1460] for track '178' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1466-1467] for track '179' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1472-1532] for track '180' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1534-1542] for track '180' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1550-1578] for track '180' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1588-1593] for track '180' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1599-1602] for track '180' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1605-1743] for track '180' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1475-1546] for track '181' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1548-1552] for track '181' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1564-1743] for track '181' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1475-1640] for track '182' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1477-1485] for track '183' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1480-1644] for track '184' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1480-1481] for track '185' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1480-1481] for track '186' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1482-1743] for track '187' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1482-1483] for track '188' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1486-1610] for track '189' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1613-1632] for track '189' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1643-1738] for track '189' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1489-1513] for track '190' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1517-1743] for track '190' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1506-1517] for track '191' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1609-1612] for track '192' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1623-1647] for track '193' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1650-1657] for track '193' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1642-1674] for track '194' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1679-1712] for track '194' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1662-1664] for track '195' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1670-1671] for track '195' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1678-1685] for track '195' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1666-1745] for track '196' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1670-1712] for track '197' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1715-1743] for track '197' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1690-1745] for track '198' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1955] for track '198' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1731-1735] for track '199' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1742-1743] for track '199' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1744-1745] for track '200' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1954] for track '200' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1744-1745] for track '201' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1960] for track '201' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1744-1745] for track '202' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1943] for track '202' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1744-1745] for track '203' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1935] for track '203' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1744-1745] for track '204' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1954] for track '204' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1744-1745] for track '205' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1954] for track '205' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1744-1745] for track '206' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1954] for track '206' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1744-1745] for track '207' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1954] for track '207' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1744-1745] for track '208' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1954] for track '208' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1744-1745] for track '209' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1973] for track '209' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1744-1745] for track '210' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1920] for track '210' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1744-1745] for track '211' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1946] for track '211' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1744-1745] for track '212' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1773-1958] for track '212' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1774-1960] for track '213' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1774-1954] for track '214' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1774-1954] for track '215' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1856-1944] for track '216' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1956-2032] for track '216' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2034-2039] for track '216' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2042-2114] for track '216' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1888-1890] for track '217' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1954-1960] for track '217' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1913-1915] for track '218' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1938-1941] for track '219' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1955-1971] for track '220' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1955-1962] for track '221' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1955-2043] for track '222' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2045-2114] for track '222' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1955-1957] for track '223' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1955-1993] for track '224' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1958-1975] for track '225' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1962-2017] for track '226' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2020-2074] for track '226' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2084-2087] for track '226' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2093-2114] for track '226' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1966-2114] for track '227' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1969-2029] for track '228' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2031-2114] for track '228' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1985-2016] for track '229' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2019-2020] for track '229' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1995-1996] for track '230' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2005-2007] for track '231' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2009-2012] for track '232' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2020-2021] for track '233' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2066-2071] for track '233' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2027-2114] for track '234' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2033-2034] for track '235' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2060-2061] for track '236' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2063-2065] for track '237' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2104-2105] for track '237' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2067-2114] for track '238' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2076-2114] for track '239' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2087-2114] for track '240' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2094-2114] for track '241' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2098-2102] for track '242' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2104-2106] for track '242' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2101-2114] for track '243' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2105-2114] for track '244' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2105-2114] for track '245' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2106-2114] for track '246' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2138-2145] for track '247' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2147-2174] for track '247' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2138-2159] for track '248' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2161-2164] for track '248' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2168-2171] for track '248' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2173-2176] for track '248' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2138-2144] for track '249' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2147-2166] for track '249' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2169-2171] for track '249' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2174-2175] for track '249' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2138-2174] for track '250' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2138-2145] for track '251' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2168-2169] for track '251' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2173-2174] for track '251' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2138-2168] for track '252' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2170-2176] for track '252' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2141-2144] for track '253' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2175-2176] for track '253' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2142-2145] for track '254' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2159-2169] for track '254' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2172-2173] for track '254' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2155-2156] for track '255' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2161-2166] for track '255' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2171-2172] for track '255' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2175-2177] for track '255' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2172-2173] for track '256' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2174-2176] for track '257' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2180-2183] for track '258' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2422] for track '259' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2413] for track '260' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2416-2417] for track '260' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2420-2421] for track '260' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2458] for track '261' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2460-2462] for track '261' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2357] for track '262' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2371-2447] for track '262' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2423] for track '263' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2425-2433] for track '263' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2439-2444] for track '263' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2405] for track '264' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2407-2423] for track '264' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2425-2431] for track '264' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2435-2437] for track '264' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2442-2533] for track '264' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2423] for track '265' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2373] for track '266' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2425] for track '267' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2451] for track '268' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2539] for track '269' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2351] for track '270' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2357-2649] for track '270' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2491] for track '271' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2496-2499] for track '271' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2506-2562] for track '271' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2567-2569] for track '271' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2498] for track '272' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2501-2535] for track '272' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2449] for track '273' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2407] for track '274' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2410] for track '275' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2413-2414] for track '275' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2421-2425] for track '275' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2429-2449] for track '275' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2414] for track '276' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2379] for track '277' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2384-2396] for track '277' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2402-2565] for track '277' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2349] for track '278' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2358-2372] for track '278' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2430] for track '279' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2225-2421] for track '280' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2375-2380] for track '281' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2395-2402] for track '281' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2378-2443] for track '282' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2378-2381] for track '283' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2418-2554] for track '284' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2422-2449] for track '285' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2463-2485] for track '286' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2489-2542] for track '286' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2473-2547] for track '287' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2555-2566] for track '287' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2481-2611] for track '288' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2680-2961] for track '288' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2494-2557] for track '289' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2563-2566] for track '289' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2572-2573] for track '289' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2607-2608] for track '289' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2613-2643] for track '289' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2509-2584] for track '290' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2536-2637] for track '291' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2645-2646] for track '291' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2564-2576] for track '292' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2586-2609] for track '292' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2611-2649] for track '292' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2564-2649] for track '293' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2608-2649] for track '294' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2680-2762] for track '294' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2766-2804] for track '294' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2611-2644] for track '295' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2613-2639] for track '296' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2625-2641] for track '297' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2630-2634] for track '298' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2630-2631] for track '299' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2632-2633] for track '300' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2633-2649] for track '301' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2633-2638] for track '302' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2786] for track '303' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2788-2798] for track '303' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2933] for track '304' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2960-2965] for track '304' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2979-2984] for track '304' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2771] for track '305' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2775-2798] for track '305' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2807] for track '306' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2811-2813] for track '306' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2815-2935] for track '306' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2743] for track '307' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2749-2795] for track '307' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2746] for track '308' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2748-2750] for track '308' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2785] for track '309' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2789-2840] for track '309' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2775] for track '310' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2780-2822] for track '310' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2867] for track '311' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2891-2917] for track '311' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2925-2958] for track '311' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2962-2991] for track '311' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2994-3078] for track '311' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2748] for track '312' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2763] for track '313' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2766-2803] for track '313' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2933] for track '314' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2935-3049] for track '314' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2764] for track '315' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2771-2782] for track '315' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2785-2836] for track '315' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2706] for track '316' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2709-2721] for track '316' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2725-2800] for track '316' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2681-2752] for track '317' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2751-2811] for track '318' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2814-2847] for track '318' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2851-2852] for track '318' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2863-2864] for track '318' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2866-2913] for track '318' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2761-2788] for track '319' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2780-2801] for track '320' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2807-2814] for track '320' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2788-2812] for track '321' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2814-2817] for track '321' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2790-2802] for track '322' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2808-2890] for track '323' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2896-2898] for track '323' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2826-2828] for track '324' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2863-2966] for track '325' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2971-3054] for track '325' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3057-3078] for track '325' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2863-2864] for track '326' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2875-2899] for track '327' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2904-3041] for track '327' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3054-3078] for track '327' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2881-2892] for track '328' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2894-2898] for track '328' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2901-2902] for track '328' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2909-2931] for track '328' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2942-3005] for track '328' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3028-3078] for track '328' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2886-2958] for track '329' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2988-2995] for track '329' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2889-3078] for track '330' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2907-3041] for track '331' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3045-3078] for track '331' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2919-2975] for track '332' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2978-3039] for track '332' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3044-3078] for track '332' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2928-2929] for track '333' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2930-2990] for track '334' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2941-2962] for track '335' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2945-2946] for track '336' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2963-2978] for track '336' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2980-2984] for track '336' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2986-2993] for track '336' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2996-3013] for track '336' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3025-3044] for track '336' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3055-3078] for track '336' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2948-2957] for track '337' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2965-2978] for track '338' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2982-2984] for track '338' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2986-3078] for track '338' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2989-3011] for track '339' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2995-3078] for track '340' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3006-3078] for track '341' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3014-3029] for track '342' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3037-3078] for track '342' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3042-3051] for track '343' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3060-3068] for track '343' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3096-3155] for track '344' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3096-3155] for track '345' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3096-3155] for track '346' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3098-3100] for track '347' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3102-3115] for track '348' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3118-3120] for track '348' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3127-3131] for track '348' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3142-3146] for track '348' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3130-3131] for track '349' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3668] for track '350' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3484] for track '351' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3489-3490] for track '351' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3507-3668] for track '351' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3502] for track '352' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3604] for track '353' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3606-3612] for track '353' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3614-3622] for track '353' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3624-3628] for track '353' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3668] for track '354' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3668] for track '355' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3546] for track '356' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3557-3558] for track '356' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3563-3604] for track '356' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3607-3618] for track '356' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3668] for track '357' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3668] for track '358' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3668] for track '359' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3711-3725] for track '359' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3737-3869] for track '359' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3598] for track '360' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3600-3604] for track '360' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3606-3668] for track '360' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3668] for track '361' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3533] for track '362' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3545-3668] for track '362' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3429] for track '363' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3431-3441] for track '363' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3445-3614] for track '363' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3632-3668] for track '363' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3466] for track '364' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3471-3498] for track '364' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3506-3668] for track '364' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3613] for track '365' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3616-3668] for track '365' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3668] for track '366' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3417] for track '367' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3426-3427] for track '367' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3461] for track '368' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3467] for track '369' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3469-3535] for track '369' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3538-3668] for track '369' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3409] for track '370' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3444-3668] for track '370' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3199-3411] for track '371' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3413-3466] for track '371' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3469-3471] for track '371' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3475-3668] for track '371' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3287-3290] for track '372' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3304-3305] for track '372' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3424-3431] for track '373' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3434-3437] for track '373' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3437-3668] for track '374' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3453-3454] for track '375' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3473-3668] for track '376' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3499-3503] for track '377' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3509-3668] for track '377' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3515-3518] for track '378' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3521-3526] for track '378' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3528-3530] for track '378' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3532-3537] for track '378' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3542-3552] for track '378' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3570-3571] for track '378' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3544-3545] for track '379' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3545-3563] for track '380' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3569-3582] for track '380' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3584-3585] for track '380' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3599-3604] for track '380' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3571-3588] for track '381' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3601-3603] for track '381' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3608-3610] for track '381' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3631-3633] for track '381' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3587-3590] for track '382' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3592-3593] for track '382' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3595-3601] for track '382' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3620-3626] for track '383' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3628-3631] for track '383' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3633-3634] for track '383' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3646-3647] for track '383' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3650-3662] for track '383' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3664-3668] for track '383' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3633-3637] for track '384' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3639-3647] for track '384' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3649-3653] for track '384' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3655-3663] for track '384' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3651-3659] for track '385' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3656-3660] for track '386' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3663-3664] for track '386' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3660-3662] for track '387' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3665-3668] for track '387' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3662-3663] for track '388' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3712-3869] for track '391' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3712-3822] for track '392' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3712-3843] for track '393' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3712-3869] for track '400' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3717-3813] for track '401' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3729-3739] for track '402' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3750-3753] for track '403' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3810-3814] for track '403' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3831-3862] for track '403' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3755-3757] for track '404' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3768-3787] for track '405' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3789-3835] for track '405' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3790-3793] for track '406' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3822-3837] for track '407' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3823-3826] for track '408' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3836-3838] for track '409' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '81' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '81' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '82' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '82' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '83' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '83' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '84' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '84' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '85' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '85' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '86' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '86' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '87' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '87' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '88' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '88' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '89' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '89' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '90' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '90' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '91' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '91' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '92' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '92' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '93' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '93' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '94' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '94' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '95' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '95' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '96' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '96' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '97' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '97' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '98' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '98' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '99' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '99' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '100' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '100' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '101' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '101' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '102' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '102' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '103' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '103' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '104' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '104' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '105' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '105' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '106' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '106' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '107' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '107' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '108' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '108' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '109' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '109' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '110' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '110' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '111' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '111' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '112' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '112' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '113' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '113' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '114' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '114' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '115' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '115' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '116' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '116' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '117' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '117' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '118' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '118' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '119' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '119' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '120' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '120' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '121' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '121' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '122' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '122' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '123' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '123' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '124' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '124' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '125' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '125' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '126' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '126' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '127' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '127' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '128' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '128' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '129' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '129' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '130' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '130' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '131' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '131' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '132' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '132' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '133' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '133' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '134' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '134' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '135' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '135' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '136' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '136' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '137' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '137' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '138' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '138' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '139' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '139' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '140' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '140' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '141' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '141' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '142' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '142' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '143' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '143' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '144' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '144' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '145' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '145' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '146' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '146' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '147' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '147' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '148' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '148' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '149' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '149' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '150' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '150' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '151' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '151' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '152' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '152' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '153' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '153' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '154' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '154' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '155' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '155' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '156' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '156' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '157' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '157' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '158' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '158' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '159' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '159' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '160' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '160' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '161' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '161' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '162' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '162' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '163' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '163' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '164' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '164' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '165' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '165' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '166' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '166' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '167' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '167' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '168' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '168' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '169' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '169' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '170' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '170' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '171' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '171' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '172' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '172' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '173' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '173' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '174' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '174' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '175' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '175' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '176' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '176' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '177' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '177' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '178' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '178' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '179' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '179' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '180' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '180' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '181' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '181' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '182' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '182' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '183' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '183' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '184' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '184' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '185' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '185' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '186' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '186' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '187' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '187' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '188' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '188' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '189' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '189' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '190' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '190' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '191' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '191' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '192' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '192' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '193' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '193' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '194' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '194' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '195' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '195' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '196' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '196' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '197' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '197' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '198' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '198' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '199' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '199' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '200' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '200' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '201' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '201' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '202' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '202' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '203' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '203' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '204' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '204' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '205' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '205' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '206' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '206' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '207' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '207' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '208' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '208' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '209' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '209' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '210' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '210' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '211' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '211' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '212' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '212' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '213' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '213' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '214' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '214' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '215' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '215' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '216' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '216' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '217' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '217' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '218' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '218' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '219' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '219' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '220' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '220' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '221' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '221' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '222' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '222' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '223' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '223' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '224' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '224' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '225' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '225' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '226' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '226' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '227' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '227' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '228' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '228' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '229' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '229' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '230' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '230' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '231' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '231' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '232' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '232' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '233' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '233' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '234' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '234' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '235' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '235' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '236' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '236' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '237' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '237' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '238' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '238' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '239' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '239' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '240' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '240' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '241' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '241' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '242' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '242' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '243' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '243' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '244' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '244' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '245' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '245' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '246' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '246' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '247' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '247' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '248' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '248' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '249' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '249' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '250' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '250' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '251' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '251' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '252' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '252' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '253' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '253' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '254' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '254' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '255' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '255' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '256' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '256' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '257' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '257' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '258' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '258' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '259' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '259' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '260' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '260' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '261' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '261' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '262' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '262' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '263' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '263' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '264' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '264' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '265' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '265' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '266' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '266' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '267' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '267' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '268' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '268' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '269' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '269' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '270' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '270' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '271' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '271' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '272' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '272' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '273' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '273' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '274' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '274' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '275' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '275' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '276' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '276' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '277' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '277' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '278' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '278' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '279' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '279' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '280' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '280' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '281' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '281' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '282' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '282' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '283' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '283' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '284' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '284' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '285' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '285' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '286' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '286' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '287' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '287' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '288' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '288' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '289' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '289' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '290' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '290' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '291' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '291' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '292' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '292' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '293' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '293' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '294' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '294' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '295' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '295' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '296' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '296' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '297' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '297' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '298' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '298' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '299' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '299' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '300' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '300' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '301' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '301' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '302' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '302' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '303' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '303' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '304' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '304' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '305' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '305' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '306' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '306' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '307' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '307' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '308' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '308' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '309' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '309' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '310' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '310' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '311' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '311' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '312' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '312' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '313' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '313' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '314' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '314' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '315' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '315' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '316' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '316' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '317' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '317' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '318' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '318' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '319' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '319' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '320' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '320' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '321' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '321' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '322' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '322' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '323' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '323' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '324' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '324' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '325' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '325' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '326' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '326' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '327' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '327' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '328' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '328' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '329' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '329' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '330' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '330' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '331' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '331' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '332' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '332' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '333' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '333' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '334' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '334' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '335' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '335' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '336' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '336' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '337' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '337' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '338' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '338' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '339' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '339' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '340' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '340' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '341' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '341' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '342' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '342' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '343' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '343' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '344' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '344' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '345' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '345' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '346' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '346' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '347' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '347' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '348' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '348' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '349' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '349' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '350' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '350' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '351' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '351' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '352' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '352' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '353' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '353' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '354' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '354' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '355' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '355' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '356' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '356' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '357' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '357' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '358' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '358' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '359' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '359' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '360' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '360' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '361' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '361' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '362' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '362' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '363' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '363' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '364' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '364' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '365' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '365' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '366' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '366' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '367' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '367' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '368' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '368' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '369' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '369' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '370' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '370' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '371' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '371' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '372' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '372' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '373' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '373' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '374' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '374' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '375' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '375' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '376' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '376' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '377' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '377' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '378' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '378' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '379' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '379' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '380' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '380' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '381' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '381' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '382' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '382' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '383' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '383' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '384' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '384' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '385' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '385' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '386' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '386' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '387' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '387' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '388' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '388' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '389' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '389' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '390' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '390' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '391' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '391' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '392' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '392' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '393' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '393' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '394' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '394' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '395' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '395' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '396' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '396' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '397' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '397' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '398' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '398' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '399' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '399' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '400' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '400' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '401' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '401' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '402' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '402' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '403' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '403' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '404' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '404' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '405' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '405' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '406' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '406' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '407' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '407' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '408' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '408' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '409' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '409' has undefined team_side. Will map to Team_Unknown.

</details>