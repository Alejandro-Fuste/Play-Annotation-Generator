# Play-Annotation-Generator Annotation Review — Hitch_34

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_34`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 145
- **Validation Warnings:** 154
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 123
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_RunHitchRoute` | WR4 | offense | `3` | `3` |
| ⚠️ START CHANGED | `Action_ThrowPass` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_BallCarry` | WR4 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `14` | `14` | 22 | START | 22 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `10` | `10` | 30 | START | 30 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `12` | `12` | 30 | START | 30 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 30 | START | 38 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 30 | START | 30 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 30 | START | 30 | 63 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 37 | END | 22 | 37 |
| ✅ EXACT | `Action_RunHitchRoute` | WR4 | `3` | `3` | 39 | START | 39 | 136 |
| ⚠️ START CHANGED | `Action_ThrowPass` | QB | `18` | `18` | 93 | START | 96 | 103 |
| ✅ EXACT | `Action_BallCarry` | WR4 | `3` | `3` | 137 | START | 137 | 239 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 37 | 16 | inferred_complete_timeline |
| `Action_None` | 38 | 51 | 14 | inferred_complete_timeline |
| `Action_None` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_None` | 81 | 92 | 12 | inferred_complete_timeline |
| `Action_ThrowPass` | 96 | 103 | 8 | inferred_complete_timeline |
| `Action_None` | 104 | 182 | 79 | inferred_complete_timeline |
| `Action_None` | 184 | 239 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 40 | 19 | inferred_complete_timeline |
| `Action_None` | 54 | 57 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 54 | 33 | inferred_complete_timeline |
| `Action_None` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_None` | 61 | 239 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 39 | 136 | 98 | inferred_complete_timeline |
| `Action_BallCarry` | 137 | 239 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 42 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 196 | 152 | inferred_complete_timeline |
| `Action_PassBlock` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 215 | 216 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 36 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 47 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 86 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 33 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 125 | 88 | inferred_complete_timeline |
| `Action_PassBlock` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 239 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 63 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 89 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 110 | 81 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 226 | 113 | inferred_complete_timeline |
| `Action_PassBlock` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 57 | 36 | inferred_complete_timeline |
| `Action_None` | 59 | 124 | 66 | inferred_complete_timeline |
| `Action_None` | 128 | 133 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 48 | 27 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 98 | 77 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 177 | 31 | inferred_complete_timeline |
| `Action_None` | 181 | 239 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 48 | 27 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 74 | 4 | inferred_complete_timeline |
| `Action_None` | 79 | 90 | 12 | inferred_complete_timeline |
| `Action_None` | 92 | 226 | 135 | inferred_complete_timeline |
| `Action_None` | 228 | 238 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 162 | 141 | inferred_complete_timeline |
| `Action_None` | 170 | 176 | 7 | inferred_complete_timeline |
| `Action_None` | 181 | 202 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 48 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 48 | 27 | inferred_complete_timeline |
| `Action_None` | 51 | 55 | 5 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_None` | 82 | 88 | 7 | inferred_complete_timeline |
| `Action_None` | 90 | 96 | 7 | inferred_complete_timeline |
| `Action_None` | 101 | 114 | 14 | inferred_complete_timeline |
| `Action_None` | 118 | 133 | 16 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 73 | 52 | inferred_complete_timeline |
| `Action_None` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_None` | 103 | 109 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 176 | 155 | inferred_complete_timeline |
| `Action_None` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_None` | 186 | 192 | 7 | inferred_complete_timeline |
| `Action_None` | 196 | 204 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 30–73 | 22 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 55–238 | 173 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 78–112 | 29 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 83–239 | 145 | 7 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 118–239 | 122 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 119–239 | 106 | 7 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 127–239 | 110 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 131–133 | 3 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 138–159 | 22 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 147–239 | 63 | 8 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 149–239 | 72 | 3 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 151–159 | 9 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 192–193 | 2 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 198–239 | 31 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 218–224 | 7 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 222–223 | 2 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 223–227 | 5 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ `Action_ThrowPass` for actor_track_id `18` (QB): Annotated start 93 != Inferred start 96

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 108 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [22–37], lower_priority='Action_PassBlock' annotated_start=30, effective_Action_PassBlock_start=38.
- ⚠️ Action 'Action_None' range [22-54] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-109] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-57] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-48] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-162] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-55] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-88] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-114] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-133] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-42] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [204-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [215-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-36] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-47] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-177] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [22-33] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [127-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-40] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-90] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-238] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-51] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-92] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-182] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-226] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-63] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-89] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-39] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-73] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-220] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-104] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-92] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-110] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-175] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-209] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-239] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-134] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-183] for track '27' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-201] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-138] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-159] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-179] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-234] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-172] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-225] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-224] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '41' has 1 frames without a visible bounding box.
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