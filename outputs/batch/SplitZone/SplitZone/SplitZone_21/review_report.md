# Play-Annotation-Generator Annotation Review — SplitZone_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_21`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `15` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 5 | START | 5 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `1` | `Group` | 5 | START | 5 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 5 | START | 5 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 5 | START | 5 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 5 | START | 5 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 5 | START | 5 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 5 | START | 5 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 5 | START | 5 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 5 | START | 5 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 5 | START | 5 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 5 | START | 5 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `16` | `16` | 79 | START | 79 | 85 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `16` | 82 | START | 120 | 160 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LT | `18` | `18` | 82 | START | 103 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 82 | START | 110 | 112 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RT | `20` | `20` | 82 | START | 95 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 82 | START | 103 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `1` | `1` | 84 | START | 84 | 85 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `4` | 95 | END | 79 | 95 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `4` | 104 | START | 104 | 119 |
| ✅ EXACT | `Action_BallCarry` | RB | `15` | `15` | 120 | START | 120 | 137 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 160 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 5–226
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 78 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 79 | 95 | 17 | inferred_complete_timeline |
| `Action_None` | 96 | 103 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 104 | 119 | 16 | inferred_complete_timeline |
| `Action_None` | 120 | 226 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 5–137
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 119 | 115 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 137 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 5–167
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 83 | 79 | inferred_complete_timeline |
| `Action_SplitBlock` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 89 | 113 | 25 | inferred_complete_timeline |
| `Action_SplitBlock` | 121 | 157 | 37 | inferred_complete_timeline |
| `Action_SplitBlock` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 167 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 5–449
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 78 | 74 | inferred_complete_timeline |
| `Action_None` | 79 | 449 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 5–449
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 78 | 74 | inferred_complete_timeline |
| `Action_None` | 79 | 258 | 180 | inferred_complete_timeline |
| `Action_None` | 264 | 300 | 37 | inferred_complete_timeline |
| `Action_None` | 304 | 449 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 5–80
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 78 | 10 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 5–258
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 63 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 160 | 58 | inferred_complete_timeline |
| `Action_None` | 161 | 193 | 33 | inferred_complete_timeline |
| `Action_None` | 196 | 258 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 5–261
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 29 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 50 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 58 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 114 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 160 | 45 | inferred_complete_timeline |
| `Action_None` | 161 | 198 | 38 | inferred_complete_timeline |
| `Action_None` | 203 | 215 | 13 | inferred_complete_timeline |
| `Action_None` | 226 | 261 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 5–291
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 78 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 79 | 85 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 160 | 41 | inferred_complete_timeline |
| `Action_None` | 161 | 291 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 5–289
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 63 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 156 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 225 | 65 | inferred_complete_timeline |
| `Action_None` | 231 | 289 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 5–96
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 28 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 41 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 48 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 96 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 5–294
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 32 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 58 | 23 | inferred_complete_timeline |
| `Action_None` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_None` | 123 | 294 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–111
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 58 | 54 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_None` | 95 | 111 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 5–336
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 51 | 47 | inferred_complete_timeline |
| `Action_None` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_None` | 100 | 113 | 14 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 138 | 18 | inferred_complete_timeline |
| `Action_None` | 144 | 156 | 13 | inferred_complete_timeline |
| `Action_None` | 159 | 336 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 5–298
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 78 | 74 | inferred_complete_timeline |
| `Action_None` | 79 | 294 | 216 | inferred_complete_timeline |
| `Action_None` | 296 | 298 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 5–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 78 | 74 | inferred_complete_timeline |
| `Action_None` | 79 | 114 | 36 | inferred_complete_timeline |
| `Action_None` | 121 | 449 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 5–309
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 78 | 74 | inferred_complete_timeline |
| `Action_None` | 79 | 309 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 5–419
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 59 | 55 | inferred_complete_timeline |
| `Action_None` | 95 | 114 | 20 | inferred_complete_timeline |
| `Action_None` | 116 | 120 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 354 | 232 | inferred_complete_timeline |
| `Action_None` | 356 | 419 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 78 | 74 | inferred_complete_timeline |
| `Action_None` | 79 | 329 | 251 | inferred_complete_timeline |
| `Action_None` | 331 | 449 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 5–258
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 78 | 74 | inferred_complete_timeline |
| `Action_None` | 79 | 118 | 40 | inferred_complete_timeline |
| `Action_None` | 135 | 156 | 22 | inferred_complete_timeline |
| `Action_None` | 159 | 174 | 16 | inferred_complete_timeline |
| `Action_None` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_None` | 199 | 258 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 5–449
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 78 | 74 | inferred_complete_timeline |
| `Action_None` | 79 | 449 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 5–203
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 78 | 74 | inferred_complete_timeline |
| `Action_None` | 79 | 203 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 109–449 | 333 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 124–281 | 144 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 132–242 | 66 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 138–140 | 3 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 147–285 | 131 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 149–173 | 21 | 4 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 196–332 | 137 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 207–449 | 243 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 246–270 | 25 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 316–345 | 24 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 336–339 | 4 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 336–337 | 2 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 365–366 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `16` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 82 != Inferred start 120
- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (LT): Annotated start 82 != Inferred start 103
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `20` (RT): Annotated start 82 != Inferred start 95
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `1` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [79–95], lower_priority='Action_ZoneBlock' annotated_start=82, effective_Action_ZoneBlock_start=96.
- ⚠️ Action 'Action_None' range [79-258] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-300] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-449] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [84-85] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [89-113] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [121-157] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-226] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-114] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-449] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-174] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-294] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-354] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-419] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-58] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-294] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-58] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-111] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-51] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-138] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-336] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-119] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [120-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [79-85] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [88-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-291] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-309] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-160] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-193] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-258] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-63] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-156] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-225] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-289] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-28] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-48] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-29] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-58] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-114] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-198] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-215] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-261] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-115] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-298] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-449] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-202] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-281] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-242] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-285] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-173] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-332] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-270] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-345] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-339] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '35' has 1 frames without a visible bounding box.
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

</details>