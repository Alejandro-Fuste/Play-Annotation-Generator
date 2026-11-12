# Play-Annotation-Generator Annotation Review — SplitZone_243

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_243`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 115
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
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 66 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 64 | START | 64 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `10` | 67 | START | 67 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `16` | 67 | START | 67 | 86 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `21` | `21` | 67 | START | 79 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `8` | 67 | START | 67 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 67 | START | 67 | 169 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `11` | `11` | 74 | START | 74 | 169 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 78 | END | 64 | 78 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 84 | START | 84 | 96 |
| ✅ EXACT | `Action_BallCarry` | RB | `17` | `17` | 97 | START | 97 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `10` | `10` | 98 | START | 98 | 149 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 169 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–224
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 64 | 78 | 15 | inferred_complete_timeline |
| `Action_None` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 84 | 96 | 13 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 212 | 113 | inferred_complete_timeline |
| `Action_None` | 215 | 224 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 100 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 244 | 181 | inferred_complete_timeline |
| `Action_None` | 251 | 269 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 249 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SplitBlock` | 74 | 169 | 96 | inferred_complete_timeline |
| `Action_None` | 170 | 226 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 93 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 169 | 103 | inferred_complete_timeline |
| `Action_None` | 170 | 212 | 43 | inferred_complete_timeline |
| `Action_None` | 216 | 220 | 5 | inferred_complete_timeline |
| `Action_None` | 223 | 226 | 4 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 86 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 166 | 15 | inferred_complete_timeline |
| `Action_None` | 171 | 206 | 36 | inferred_complete_timeline |
| `Action_None` | 208 | 212 | 5 | inferred_complete_timeline |
| `Action_None` | 215 | 220 | 6 | inferred_complete_timeline |
| `Action_None` | 224 | 235 | 12 | inferred_complete_timeline |
| `Action_None` | 244 | 245 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 249 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_BallSnap` | 64 | 78 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 169 | 91 | inferred_complete_timeline |
| `Action_None` | 170 | 269 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 90 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 97 | 6 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 98 | 149 | 52 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 157 | 164 | 8 | inferred_complete_timeline |
| `Action_None` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_None` | 177 | 186 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 121 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 169 | 38 | inferred_complete_timeline |
| `Action_None` | 170 | 208 | 39 | inferred_complete_timeline |
| `Action_None` | 216 | 223 | 8 | inferred_complete_timeline |
| `Action_None` | 225 | 269 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 151 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 167 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 152 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 117 | 54 | inferred_complete_timeline |
| `Action_None` | 124 | 167 | 44 | inferred_complete_timeline |
| `Action_None` | 169 | 269 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 125 | 62 | inferred_complete_timeline |
| `Action_None` | 127 | 143 | 17 | inferred_complete_timeline |
| `Action_None` | 228 | 245 | 18 | inferred_complete_timeline |
| `Action_None` | 247 | 256 | 10 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 74 | 11 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_None` | 91 | 212 | 122 | inferred_complete_timeline |
| `Action_None` | 214 | 259 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 249 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 168 | 105 | inferred_complete_timeline |
| `Action_None` | 172 | 269 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 211 | 148 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 222 | 3 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 119 | 56 | inferred_complete_timeline |
| `Action_None` | 124 | 190 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 220 | 157 | inferred_complete_timeline |
| `Action_None` | 223 | 230 | 8 | inferred_complete_timeline |
| `Action_None` | 232 | 256 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 105–142 | 38 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 112–123 | 12 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 116–118 | 3 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 127–269 | 143 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 139–221 | 82 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 156–196 | 39 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 173–229 | 30 | 3 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 188–269 | 64 | 6 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 207–269 | 57 | 5 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 238–269 | 29 | 2 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 238–269 | 25 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `21` (C): Annotated start 67 != Inferred start 79
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 103 frames exceeds threshold 90 frames [start=67, end=169].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 103 frames exceeds threshold 90 frames [start=67, end=169].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (LG) duration 103 frames exceeds threshold 90 frames [start=67, end=169].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 103 frames exceeds threshold 90 frames [start=67, end=169].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [64–78], lower_priority='Action_ZoneBlock' annotated_start=67, effective_Action_ZoneBlock_start=79.
- ⚠️ Action 'Action_None' range [64-151] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-244] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-93] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-249] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-249] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-167] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-208] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-212] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [98-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [151-152] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [157-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-186] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-190] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-245] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-256] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-212] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-224] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-211] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [152-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-235] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [97-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-74] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-212] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-259] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-220] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-123] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-221] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-167] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-196] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-219] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-231] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-256] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-249] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-265] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-252] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '33' has 1 frames without a visible bounding box.
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

</details>