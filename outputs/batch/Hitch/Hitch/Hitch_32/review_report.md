# Play-Annotation-Generator Annotation Review — Hitch_32

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_32`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 122
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunHitchRoute` | WR4 | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR4 | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `16` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 1 | START | 1 | 11 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `10` | `10` | 4 | START | 4 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 4 | START | 12 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 4 | START | 4 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `3` | `3` | 4 | START | 4 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `7` | `7` | 4 | START | 4 | 22 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 11 | END | 1 | 11 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunHitchRoute` | WR4 | `11` | `11` | 20 | START | 20 | 49 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 81 | START | 81 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR4 | `11` | `11` | 114 | START | 114 | 158 |

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
- **Visible Frames:** 0–160
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 11 | 11 | inferred_complete_timeline |
| `Action_None` | 12 | 73 | 62 | inferred_complete_timeline |
| `Action_None` | 75 | 80 | 6 | inferred_complete_timeline |
| `Action_ThrowPass` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_None` | 90 | 90 | 1 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 50 | 50 | inferred_complete_timeline |
| `Action_None` | 53 | 210 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 72 | 72 | inferred_complete_timeline |
| `Action_None` | 76 | 210 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 101 | 101 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 120 | 9 | inferred_complete_timeline |
| `Action_None` | 124 | 188 | 65 | inferred_complete_timeline |
| `Action_None` | 190 | 196 | 7 | inferred_complete_timeline |
| `Action_None` | 198 | 209 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 92 | 92 | inferred_complete_timeline |
| `Action_None` | 98 | 172 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 20 | 49 | 30 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 52 | 104 | 53 | inferred_complete_timeline |
| `Action_None` | 105 | 113 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 114 | 158 | 45 | inferred_complete_timeline |
| `Action_BallCarry` | 173 | 187 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 189 | 192 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 22 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 38 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 49 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 68 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 95 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 142 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 20 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 58 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 72 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 95 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 108 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 132 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 174 | 175 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 11 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 22 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 102 | 78 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 115 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 127 | 130 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 167 | 172 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 174 | 209 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 22 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 84 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 22 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 120 | 96 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 95 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 39 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 197 | 157 | inferred_complete_timeline |
| `Action_None` | 200 | 210 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 22 | 22 | inferred_complete_timeline |
| `Action_None` | 25 | 98 | 74 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 115 | 11 | inferred_complete_timeline |
| `Action_None` | 117 | 145 | 29 | inferred_complete_timeline |
| `Action_None` | 149 | 154 | 6 | inferred_complete_timeline |
| `Action_None` | 157 | 184 | 28 | inferred_complete_timeline |
| `Action_None` | 186 | 210 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 22 | 22 | inferred_complete_timeline |
| `Action_None` | 25 | 114 | 90 | inferred_complete_timeline |
| `Action_None` | 118 | 145 | 28 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_None` | 207 | 209 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 161 | 161 | inferred_complete_timeline |
| `Action_None` | 189 | 197 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 189 | 189 | inferred_complete_timeline |
| `Action_None` | 197 | 210 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 152 | 152 | inferred_complete_timeline |
| `Action_None` | 154 | 170 | 17 | inferred_complete_timeline |
| `Action_None` | 173 | 210 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 195 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 59–60 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 112–159 | 37 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 119–208 | 88 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 153–207 | 40 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 189–196 | 8 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 193–196 | 4 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 195–196 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 204–205 | 2 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 206–208 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (9 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (9 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (9 segments found)
- ⚠️ Ambiguous match for action `Action_RunHitchRoute` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [1–11], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=12.
- ⚠️ Action 'Action_None' range [1-72] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-39] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-197] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-22] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-84] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-22] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-114] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-145] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-50] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-22] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-98] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-145] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-184] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-22] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-38] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-49] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-53] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-68] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-73] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-95] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [107-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-142] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-152] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-197] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-22] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-120] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' range [20-49] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [114-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [173-187] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [189-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-172] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-73] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 90, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [90-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-189] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-188] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-209] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-95] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-195] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-22] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-102] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [121-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [127-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [167-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [174-209] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-20] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-58] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-95] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [138-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [174-175] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-139] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-128] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-208] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-207] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-196] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '32' has 1 frames without a visible bounding box.
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

</details>