# Play-Annotation-Generator Annotation Review — Hitch_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_56`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 151
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunHitchRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `11` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 1 | START | 1 | 17 |
| ✅ EXACT | `Action_PassBlock` | LT | `10` | `10` | 4 | START | 4 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `13` | 4 | START | 4 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 4 | START | 4 | 174 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `20` | `20` | 4 | START | 18 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 4 | START | 4 | 29 |
| ✅ EXACT | `Action_RunHitchRoute` | WR1 | `0` | `0` | 17 | START | 17 | 89 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 17 | END | 1 | 17 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 67 | START | 67 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `0` | `0` | 119 | START | 119 | 121 |

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
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 17 | 17 | inferred_complete_timeline |
| `Action_None` | 18 | 66 | 49 | inferred_complete_timeline |
| `Action_ThrowPass` | 67 | 71 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 153 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 17 | 89 | 73 | inferred_complete_timeline |
| `Action_None` | 90 | 118 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 123 | 127 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 131 | 133 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 280 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 53 | 53 | inferred_complete_timeline |
| `Action_None` | 60 | 174 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 174 | 174 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 57 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 29 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 34 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 17 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 169 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 174 | 171 | inferred_complete_timeline |
| `Action_PassBlock` | 176 | 181 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 131 | 128 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 140 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 152 | 152 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 43 | 43 | inferred_complete_timeline |
| `Action_None` | 45 | 51 | 7 | inferred_complete_timeline |
| `Action_None` | 53 | 54 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 145 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 174 | 174 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 292 | 292 | inferred_complete_timeline |
| `Action_None` | 298 | 312 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 174 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 144 | 144 | inferred_complete_timeline |
| `Action_None` | 146 | 163 | 18 | inferred_complete_timeline |
| `Action_None` | 166 | 359 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 255 | 255 | inferred_complete_timeline |
| `Action_None` | 257 | 359 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 273 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 82 | 82 | inferred_complete_timeline |
| `Action_None` | 85 | 87 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 166 | 166 | inferred_complete_timeline |
| `Action_None` | 169 | 193 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 21–23 | 3 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 34–38 | 5 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 46–51 | 6 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 54–173 | 120 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 68–144 | 77 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 68–165 | 51 | 9 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 71–161 | 91 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 72–90 | 19 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 83–127 | 36 | 2 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 101–174 | 74 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 105–106 | 2 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 175–266 | 92 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 175–182 | 4 | 2 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 175–220 | 46 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 177–180 | 4 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 178–181 | 4 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 178–181 | 4 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 182–200 | 8 | 2 | Undefined position; Undefined team |
| `41` | `68` | Position_Unknown | Team_Unknown | 188–205 | 18 | 1 | Undefined position; Undefined team |
| `42` | `72` | Position_Unknown | Team_Unknown | 191–193 | 3 | 1 | Undefined position; Undefined team |
| `43` | `73` | Position_Unknown | Team_Unknown | 192–222 | 22 | 2 | Undefined position; Undefined team |
| `44` | `74` | Position_Unknown | Team_Unknown | 195–196 | 2 | 1 | Undefined position; Undefined team |
| `45` | `76` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `46` | `77` | Position_Unknown | Team_Unknown | 226–359 | 134 | 1 | Undefined position; Undefined team |
| `47` | `78` | Position_Unknown | Team_Unknown | 229–231 | 3 | 1 | Undefined position; Undefined team |
| `48` | `79` | Position_Unknown | Team_Unknown | 250–359 | 110 | 1 | Undefined position; Undefined team |
| `49` | `81` | Position_Unknown | Team_Unknown | 273–359 | 87 | 1 | Undefined position; Undefined team |
| `50` | `84` | Position_Unknown | Team_Unknown | 284–359 | 68 | 2 | Undefined position; Undefined team |
| `51` | `85` | Position_Unknown | Team_Unknown | 291–359 | 68 | 2 | Undefined position; Undefined team |
| `52` | `86` | Position_Unknown | Team_Unknown | 300–301 | 2 | 1 | Undefined position; Undefined team |
| `53` | `87` | Position_Unknown | Team_Unknown | 307–359 | 52 | 2 | Undefined position; Undefined team |
| `54` | `90` | Position_Unknown | Team_Unknown | 338–354 | 17 | 1 | Undefined position; Undefined team |
| `55` | `91` | Position_Unknown | Team_Unknown | 344–359 | 16 | 1 | Undefined position; Undefined team |
| `56` | `93` | Position_Unknown | Team_Unknown | 359–359 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `20` (C): Annotated start 4 != Inferred start 18
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 35 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 35 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 70 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [1–17], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=18.
- ⚠️ Action 'Action_BallCarry' range [119-121] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [131-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-280] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-53] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-144] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-255] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-43] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-51] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-292] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-312] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-145] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-57] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-174] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-166] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-193] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [67-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-82] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [176-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-29] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-34] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-23] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-38] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-51] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-75] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-102] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-161] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-90] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-127] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-174] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-266] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-220] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-205] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-222] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-345] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-308] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-354] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-354] for track '54' has 2 frames without a visible bounding box.
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

</details>