# Play-Annotation-Generator Annotation Review — SplitZone_290

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_290`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 131
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | defense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 43 | START | 43 | 55 |
| ✅ EXACT | `Action_SplitBlock` | TE | `10` | `10` | 52 | START | 52 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `13` | 54 | START | 54 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `16` | 54 | START | 54 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 54 | START | 56 | 106 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | `20` | `20` | 54 | START | 55 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `21` | 54 | START | 54 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 55 | END | 43 | 55 |
| ✅ EXACT | `Action_PressEdge` | RB | `12` | `12` | 61 | START | 61 | 85 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 79 | START | 79 | 85 |
| ✅ EXACT | `Action_BallCarry` | RB | `12` | `12` | 86 | START | 86 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | `18` | `18` | 94 | START | 94 | 99 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 55 | 13 | inferred_complete_timeline |
| `Action_None` | 56 | 78 | 23 | inferred_complete_timeline |
| `Action_Handoff` | 79 | 85 | 7 | inferred_complete_timeline |
| `Action_None` | 86 | 163 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PressEdge` | 61 | 85 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 86 | 128 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 359 | 317 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 135 | 93 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 143 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_SplitBlock` | 52 | 103 | 52 | inferred_complete_timeline |
| `Action_None` | 104 | 182 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 88 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 112 | 12 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 188 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 63 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_BallSnap` | 43 | 55 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 106 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 112 | 5 | inferred_complete_timeline |
| `Action_None` | 113 | 139 | 27 | inferred_complete_timeline |
| `Action_None` | 147 | 156 | 10 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 171 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 80 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 112 | 31 | inferred_complete_timeline |
| `Action_None` | 113 | 113 | 1 | inferred_complete_timeline |
| `Action_None` | 136 | 177 | 42 | inferred_complete_timeline |
| `Action_None` | 179 | 200 | 22 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 217 | 12 | inferred_complete_timeline |
| `Action_None` | 219 | 253 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 74 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 86 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 112 | 17 | inferred_complete_timeline |
| `Action_None` | 113 | 120 | 8 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 125 | 127 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 189 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 82 | 40 | inferred_complete_timeline |
| `Action_None` | 86 | 90 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 94 | 99 | 6 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 101 | 117 | 17 | inferred_complete_timeline |
| `Action_None` | 118 | 204 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 91 | 49 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 196 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 198 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 309 | 267 | inferred_complete_timeline |
| `Action_None` | 315 | 330 | 16 | inferred_complete_timeline |
| `Action_None` | 334 | 359 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 359 | 317 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 189 | 147 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 149 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 206 | 164 | inferred_complete_timeline |
| `Action_None` | 210 | 299 | 90 | inferred_complete_timeline |
| `Action_None` | 301 | 302 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 359 | 317 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 57–215 | 27 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 82–96 | 12 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 87–177 | 4 | 2 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 98–196 | 95 | 4 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 129–133 | 5 | 1 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 137–359 | 220 | 2 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 138–163 | 25 | 2 | Undefined position; Undefined team |
| `29` | `29` | Position_Unknown | Team_Unknown | 151–225 | 66 | 3 | Undefined position; Undefined team |
| `30` | `30` | Position_Unknown | Team_Unknown | 160–194 | 33 | 2 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 165–187 | 18 | 4 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 166–168 | 3 | 1 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 183–192 | 8 | 2 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 266–267 | 2 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 279–281 | 3 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 280–359 | 80 | 1 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 324–359 | 36 | 1 | Undefined position; Undefined team |
| `40` | `62` | Position_Unknown | Team_Unknown | 324–359 | 36 | 1 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 325–359 | 35 | 1 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 332–359 | 28 | 1 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 356–359 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `20` (LG): Annotated start 54 != Inferred start 55
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [43–55], lower_priority='Action_ZoneBlock' annotated_start=54, effective_Action_ZoneBlock_start=56.
- ⚠️ Action 'Action_None' range [43-143] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-198] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-82] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-309] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-330] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-359] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-135] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [79-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-189] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [52-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [86-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-86] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-93] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-189] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 113, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [113-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-177] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-217] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-91] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [94-99] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-139] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-156] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-88] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-215] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-153] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-167] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-196] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-334] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-359] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-183] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-211] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-225] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-190] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-187] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-359] for track '38' has 2 frames without a visible bounding box.
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

</details>