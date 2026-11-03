# Play-Annotation-Generator Annotation Review — OutRoutes_123

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_123`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 152
- **Validation Warnings:** 175
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `22` | `22` |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 36 | START | 36 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 36 | START | 36 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 36 | START | 36 | 47 |
| ✅ EXACT | `Action_PassBlock` | LT | `21` | `21` | 36 | START | 36 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `22` | `22` | 36 | START | 36 | 47 |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | `0` | `0` | 40 | START | 40 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 40 | END | 40 | 40 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 87 | START | 87 | 94 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `0` | `0` | 128 | START | 128 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `0` | `0` | 137 | START | 137 | 228 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_None` | 41 | 86 | 46 | inferred_complete_timeline |
| `Action_ThrowPass` | 87 | 94 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 56 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 109 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 150 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 247 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 257 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_RunOutRoute` | 40 | 127 | 88 | inferred_complete_timeline |
| `Action_SecureCatch` | 128 | 136 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 137 | 228 | 92 | inferred_complete_timeline |
| `Action_BallCarry` | 250 | 269 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 67 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 90 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 47 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 47 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 115 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 139 | 147 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 167 | 231 | 65 | inferred_complete_timeline |
| `Action_PassBlock` | 234 | 237 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 243 | 269 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 47 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 102 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 269 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 47 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 95 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 47 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 101 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 269 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 96 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 101 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 145 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 236 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 269 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 56 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 145 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 269 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 218 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 240 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 269 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 203 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 235 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 256 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 266 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 235 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–96 | 66 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–58 | 36 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 87–99 | 12 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 90–269 | 168 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 91–203 | 113 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 100–101 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 111–121 | 8 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 116–269 | 128 | 7 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 116–222 | 73 | 8 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 117–269 | 153 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 124–269 | 146 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 128–132 | 4 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 132–269 | 103 | 7 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 132–269 | 125 | 5 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 135–269 | 133 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 144–269 | 98 | 8 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 171–269 | 93 | 3 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 236–238 | 3 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 247–269 | 23 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 252–255 | 4 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 255–256 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (8 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 128 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 130: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_BallCarry' range [137-228] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [250-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-101] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-145] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-156] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-236] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-67] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-90] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-145] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-235] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-77] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-186] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-203] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-256] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-262] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-47] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-84] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-240] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-89] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-109] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-247] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-257] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-262] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [87-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-115] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [139-147] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [167-231] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [234-237] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [239-240] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [243-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-102] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-125] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-241] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-203] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-101] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-116] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-121] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-224] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-240] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-118] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-122] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-131] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-158] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-175] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-181] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-196] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-222] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-182] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-187] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-200] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-231] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-237] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-151] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-220] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-141] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-269] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-152] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-182] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-232] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-236] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-267] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-174] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-226] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-238] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-255] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-256] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>