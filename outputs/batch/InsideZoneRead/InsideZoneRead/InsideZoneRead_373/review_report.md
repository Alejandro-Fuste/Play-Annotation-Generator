# Play-Annotation-Generator Annotation Review — InsideZoneRead_373

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_373`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RB | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `11` | `10` |
| ✅ EXACT | `Action_ReadDefender` | DE2 | defense | `11` | `10` |
| ✅ EXACT | `Action_Keep` | DE2 | defense | `11` | `10` |
| ✅ EXACT | `Action_BlockSecondLevel` | CB1 | defense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | DE2 | defense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `21` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_BallSnap` | RB | `14` | `13` | 5 | START | 5 | 19 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `16` | 8 | START | 8 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 8 | START | 8 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 8 | START | 8 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 8 | START | 8 | 29 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 8 | START | 8 | 81 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `11` | `10` | 19 | END | 5 | 19 |
| ✅ EXACT | `Action_ReadDefender` | DE2 | `11` | `10` | 24 | START | 24 | 30 |
| ✅ EXACT | `Action_Keep` | DE2 | `11` | `10` | 31 | START | 31 | 57 |
| ✅ EXACT | `Action_BlockSecondLevel` | CB1 | `5` | `4` | 32 | START | 32 | 81 |
| ✅ EXACT | `Action_BallCarry` | DE2 | `11` | `10` | 58 | START | 58 | 74 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 81 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 123 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 5 | 19 | 15 | inferred_complete_timeline |
| `Action_None` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 90 | 329 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 329 | 325 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 93 | 89 | inferred_complete_timeline |
| `Action_None` | 95 | 329 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 222 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 47 | 43 | inferred_complete_timeline |
| `Action_None` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_None` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_None` | 76 | 90 | 15 | inferred_complete_timeline |
| `Action_None` | 115 | 124 | 10 | inferred_complete_timeline |
| `Action_None` | 128 | 137 | 10 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 145 | 238 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 81 | 74 | inferred_complete_timeline |
| `Action_None` | 82 | 329 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 29 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 81 | 27 | inferred_complete_timeline |
| `Action_None` | 82 | 132 | 51 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 151 | 15 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_None` | 163 | 195 | 33 | inferred_complete_timeline |
| `Action_None` | 210 | 226 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 62 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 81 | 15 | inferred_complete_timeline |
| `Action_None` | 82 | 103 | 22 | inferred_complete_timeline |
| `Action_None` | 108 | 220 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 53 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 25 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 81 | 7 | inferred_complete_timeline |
| `Action_None` | 82 | 113 | 32 | inferred_complete_timeline |
| `Action_None` | 121 | 166 | 46 | inferred_complete_timeline |
| `Action_None` | 168 | 176 | 9 | inferred_complete_timeline |
| `Action_None` | 178 | 186 | 9 | inferred_complete_timeline |
| `Action_None` | 191 | 220 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 329 | 325 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 19 | 15 | inferred_complete_timeline |
| `Action_None` | 20 | 23 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 24 | 30 | 7 | inferred_complete_timeline |
| `Action_Keep` | 31 | 57 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 58 | 74 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 44 | 40 | inferred_complete_timeline |
| `Action_None` | 52 | 100 | 49 | inferred_complete_timeline |
| `Action_None` | 115 | 247 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 54 | 50 | inferred_complete_timeline |
| `Action_None` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_None` | 61 | 173 | 113 | inferred_complete_timeline |
| `Action_None` | 175 | 181 | 7 | inferred_complete_timeline |
| `Action_None` | 185 | 329 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 80 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 238 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 32 | 81 | 50 | inferred_complete_timeline |
| `Action_None` | 82 | 329 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 273 | 269 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_None` | 282 | 284 | 3 | inferred_complete_timeline |
| `Action_None` | 286 | 305 | 20 | inferred_complete_timeline |
| `Action_None` | 316 | 329 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 329 | 325 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 329 | 325 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 120 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 303 | 179 | inferred_complete_timeline |
| `Action_None` | 305 | 307 | 3 | inferred_complete_timeline |
| `Action_None` | 310 | 329 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 20–21 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 89–128 | 35 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 122–298 | 177 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 133–329 | 197 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 134–329 | 196 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 151–154 | 4 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 181–219 | 4 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 188–193 | 6 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 200–329 | 128 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 213–329 | 112 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 240–329 | 90 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 250–252 | 3 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 273–276 | 4 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 298–326 | 29 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 301–310 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 69 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [5-222] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-93] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-54] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-173] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-181] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-273] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-305] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-44] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-100] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-247] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [31-57] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [58-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-238] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-88] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-53] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-303] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-113] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-166] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-220] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-62] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-103] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-220] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-47] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-90] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-238] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-29] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-81] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-132] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-195] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-226] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-21] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-115] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-128] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-298] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-226] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-326] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-310] for track '37' has 2 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_373'; source metadata written as null.

</details>