# Play-Annotation-Generator Annotation Review — JetSweep_228

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_228`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 64
- **Ball Tracks:** 0
- **Action Segments:** 156
- **Validation Warnings:** 219
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 131
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_LeadBlock` | TE1 | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 24 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `20` | `19` | 21 | START | 22 | 52 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 25 | START | 25 | 34 |
| ✅ EXACT | `Action_LeadBlock` | TE1 | `16` | `15` | 27 | START | 27 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `0` | 27 | START | 27 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 27 | START | 43 | 47 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 27 | START | 27 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 27 | START | 27 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `7` | 27 | START | 27 | 49 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 38 | END | 25 | 38 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 48 | START | 48 | 56 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `20` | `19` | 57 | START | 57 | 58 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 144 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 38 | 14 | inferred_complete_timeline |
| `Action_None` | 39 | 47 | 9 | inferred_complete_timeline |
| `Action_Toss` | 48 | 56 | 9 | inferred_complete_timeline |
| `Action_None` | 57 | 95 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 64 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_LeadBlock` | 27 | 144 | 118 | inferred_complete_timeline |
| `Action_None` | 145 | 152 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 60 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 52 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 67 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 94 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 49 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 91 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 34 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 47 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 105 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 46 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 65 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 55 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 63 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 31 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 40 | 16 | inferred_complete_timeline |
| `Action_None` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_None` | 55 | 104 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 31 | 7 | inferred_complete_timeline |
| `Action_None` | 46 | 65 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 55 | 31 | inferred_complete_timeline |
| `Action_None` | 65 | 72 | 8 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_None` | 80 | 102 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 92 | 68 | inferred_complete_timeline |
| `Action_None` | 95 | 145 | 51 | inferred_complete_timeline |
| `Action_None` | 152 | 156 | 5 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 172 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 45 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 249 | 225 | inferred_complete_timeline |
| `Action_None` | 251 | 255 | 5 | inferred_complete_timeline |
| `Action_None` | 262 | 283 | 22 | inferred_complete_timeline |
| `Action_None` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_None` | 290 | 297 | 8 | inferred_complete_timeline |
| `Action_None` | 300 | 379 | 80 | inferred_complete_timeline |
| `Action_None` | 385 | 388 | 4 | inferred_complete_timeline |
| `Action_None` | 401 | 404 | 4 | inferred_complete_timeline |
| `Action_None` | 406 | 418 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 52 | 28 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 97 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 22–58 | 33 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 27–72 | 44 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 38–72 | 31 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 56–97 | 34 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 64–125 | 62 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 68–106 | 39 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 73–332 | 250 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 75–419 | 320 | 8 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 84–93 | 10 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 91–92 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 91–173 | 83 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 95–154 | 60 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 99–149 | 51 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 108–245 | 127 | 2 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 138–175 | 36 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 140–249 | 110 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 143–419 | 260 | 2 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 146–266 | 121 | 1 | Undefined position; Undefined team |
| `37` | `40` | Position_Unknown | Team_Unknown | 151–249 | 94 | 3 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 156–158 | 3 | 1 | Undefined position; Undefined team |
| `39` | `43` | Position_Unknown | Team_Unknown | 160–284 | 119 | 3 | Undefined position; Undefined team |
| `40` | `44` | Position_Unknown | Team_Unknown | 164–419 | 249 | 3 | Undefined position; Undefined team |
| `41` | `45` | Position_Unknown | Team_Unknown | 169–200 | 32 | 1 | Undefined position; Undefined team |
| `42` | `46` | Position_Unknown | Team_Unknown | 176–305 | 114 | 4 | Undefined position; Undefined team |
| `43` | `47` | Position_Unknown | Team_Unknown | 179–419 | 241 | 1 | Undefined position; Undefined team |
| `44` | `48` | Position_Unknown | Team_Unknown | 181–240 | 60 | 1 | Undefined position; Undefined team |
| `45` | `50` | Position_Unknown | Team_Unknown | 211–252 | 38 | 2 | Undefined position; Undefined team |
| `46` | `52` | Position_Unknown | Team_Unknown | 218–243 | 26 | 1 | Undefined position; Undefined team |
| `47` | `53` | Position_Unknown | Team_Unknown | 221–419 | 187 | 3 | Undefined position; Undefined team |
| `48` | `54` | Position_Unknown | Team_Unknown | 223–419 | 184 | 3 | Undefined position; Undefined team |
| `49` | `55` | Position_Unknown | Team_Unknown | 230–292 | 62 | 2 | Undefined position; Undefined team |
| `50` | `58` | Position_Unknown | Team_Unknown | 260–298 | 29 | 3 | Undefined position; Undefined team |
| `51` | `59` | Position_Unknown | Team_Unknown | 271–305 | 34 | 2 | Undefined position; Undefined team |
| `52` | `64` | Position_Unknown | Team_Unknown | 306–354 | 46 | 2 | Undefined position; Undefined team |
| `53` | `72` | Position_Unknown | Team_Unknown | 325–326 | 2 | 1 | Undefined position; Undefined team |
| `54` | `73` | Position_Unknown | Team_Unknown | 327–417 | 7 | 2 | Undefined position; Undefined team |
| `55` | `74` | Position_Unknown | Team_Unknown | 330–419 | 90 | 1 | Undefined position; Undefined team |
| `56` | `79` | Position_Unknown | Team_Unknown | 349–380 | 32 | 1 | Undefined position; Undefined team |
| `57` | `80` | Position_Unknown | Team_Unknown | 359–360 | 2 | 1 | Undefined position; Undefined team |
| `58` | `81` | Position_Unknown | Team_Unknown | 359–368 | 6 | 2 | Undefined position; Undefined team |
| `59` | `82` | Position_Unknown | Team_Unknown | 361–416 | 53 | 2 | Undefined position; Undefined team |
| `60` | `83` | Position_Unknown | Team_Unknown | 379–419 | 41 | 1 | Undefined position; Undefined team |
| `61` | `84` | Position_Unknown | Team_Unknown | 391–393 | 3 | 1 | Undefined position; Undefined team |
| `62` | `85` | Position_Unknown | Team_Unknown | 396–419 | 24 | 1 | Undefined position; Undefined team |
| `63` | `87` | Position_Unknown | Team_Unknown | 398–399 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `20` (Position_Unknown): Annotated start 21 != Inferred start 22
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 45 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 45 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 90 |
| Missing visible bounding boxes during action | 126 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '15' (TE1) duration 118 frames exceeds threshold 90 frames [start=27, end=144].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [25–38], lower_priority='Action_ZoneBlock' annotated_start=27, effective_Action_ZoneBlock_start=39.
- ⚠️ Action 'Action_ZoneBlock' range [27-52] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-67] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [27-55] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-45] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [27-46] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-65] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-52] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-55] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-72] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [27-49] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-64] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-145] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-63] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-249] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-283] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-297] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-379] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-388] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-404] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-418] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-31] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-60] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [25-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [22-52] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [57-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-60] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-71] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-125] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-253] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-261] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-293] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-332] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-198] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-224] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-337] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-348] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-93] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-173] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-154] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-149] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-140] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-245] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-171] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-249] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-283] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-266] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-216] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-235] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-249] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-220] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-253] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-284] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-181] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-207] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-419] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-200] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-204] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-247] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-305] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-240] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-242] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-252] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-243] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-304] for track '47' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-388] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-338] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-347] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-251] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-292] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-298] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-290] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-305] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-344] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-354] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-417] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-380] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-368] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-399] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-416] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-419] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-393] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '63' has 1 frames without a visible bounding box.
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

</details>