# Play-Annotation-Generator Annotation Review — InsideZoneRead_317

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_317`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 145
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 119
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Keep` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 18 | START | 18 | 33 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `13` | 21 | START | 21 | 102 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `16` | `15` | 21 | START | 21 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `17` | 21 | START | 21 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 21 | START | 34 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 21 | START | 21 | 37 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 33 | END | 18 | 33 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `5` | 38 | START | 38 | 46 |
| ✅ EXACT | `Action_Keep` | QB | `6` | `5` | 47 | START | 47 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `6` | `5` | 67 | START | 67 | 161 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 102 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 33 | 16 | inferred_complete_timeline |
| `Action_None` | 34 | 37 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 38 | 46 | 9 | inferred_complete_timeline |
| `Action_Keep` | 47 | 66 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 67 | 161 | 95 | inferred_complete_timeline |
| `Action_BallCarry` | 164 | 175 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 50 | 33 | inferred_complete_timeline |
| `Action_None` | 56 | 178 | 123 | inferred_complete_timeline |
| `Action_None` | 180 | 190 | 11 | inferred_complete_timeline |
| `Action_None` | 194 | 210 | 17 | inferred_complete_timeline |
| `Action_None` | 212 | 215 | 4 | inferred_complete_timeline |
| `Action_None` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_None` | 223 | 227 | 5 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 226 | 209 | inferred_complete_timeline |
| `Action_None` | 229 | 239 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 97 | 80 | inferred_complete_timeline |
| `Action_None` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_None` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 140 | 123 | inferred_complete_timeline |
| `Action_None` | 142 | 200 | 59 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 239 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 102 | 82 | inferred_complete_timeline |
| `Action_None` | 103 | 117 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 37 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 102 | 56 | inferred_complete_timeline |
| `Action_None` | 103 | 132 | 30 | inferred_complete_timeline |
| `Action_None` | 137 | 174 | 38 | inferred_complete_timeline |
| `Action_None` | 178 | 182 | 5 | inferred_complete_timeline |
| `Action_None` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 239 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_BallSnap` | 18 | 33 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 102 | 69 | inferred_complete_timeline |
| `Action_None` | 103 | 172 | 70 | inferred_complete_timeline |
| `Action_None` | 174 | 239 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 102 | 82 | inferred_complete_timeline |
| `Action_None` | 103 | 119 | 17 | inferred_complete_timeline |
| `Action_None` | 126 | 133 | 8 | inferred_complete_timeline |
| `Action_None` | 137 | 174 | 38 | inferred_complete_timeline |
| `Action_None` | 178 | 199 | 22 | inferred_complete_timeline |
| `Action_None` | 202 | 239 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 52 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 102 | 49 | inferred_complete_timeline |
| `Action_None` | 103 | 117 | 15 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 165 | 43 | inferred_complete_timeline |
| `Action_None` | 168 | 172 | 5 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 189 | 11 | inferred_complete_timeline |
| `Action_None` | 192 | 239 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 131 | 114 | inferred_complete_timeline |
| `Action_None` | 137 | 171 | 35 | inferred_complete_timeline |
| `Action_None` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_None` | 183 | 189 | 7 | inferred_complete_timeline |
| `Action_None` | 195 | 203 | 9 | inferred_complete_timeline |
| `Action_None` | 205 | 239 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 87 | 70 | inferred_complete_timeline |
| `Action_None` | 95 | 100 | 6 | inferred_complete_timeline |
| `Action_None` | 111 | 118 | 8 | inferred_complete_timeline |
| `Action_None` | 120 | 126 | 7 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 164 | 8 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 239 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 96 | 79 | inferred_complete_timeline |
| `Action_None` | 108 | 115 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 178 | 161 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 131 | 114 | inferred_complete_timeline |
| `Action_None` | 136 | 171 | 36 | inferred_complete_timeline |
| `Action_None` | 173 | 239 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 133 | 116 | inferred_complete_timeline |
| `Action_None` | 137 | 239 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |
| `Action_None` | 215 | 218 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 239 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 151 | 134 | inferred_complete_timeline |
| `Action_None` | 155 | 158 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 183 | 166 | inferred_complete_timeline |
| `Action_None` | 191 | 220 | 30 | inferred_complete_timeline |
| `Action_None` | 229 | 233 | 5 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–239 | 209 | 5 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–239 | 215 | 11 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 95–239 | 123 | 9 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 121–238 | 110 | 4 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 124–125 | 2 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 191–239 | 48 | 2 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 203–239 | 37 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 234–238 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 103 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 634: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 634: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [18–33], lower_priority='Action_ZoneBlock' annotated_start=21, effective_Action_ZoneBlock_start=34.
- ⚠️ Action 'Action_None' range [18-97] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-133] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-166] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-226] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [67-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [164-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-200] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-50] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-178] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-190] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-76] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-129] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-149] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-158] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-169] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-190] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-203] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-239] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-131] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-171] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-203] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-239] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-115] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-87] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-151] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-133] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-174] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-199] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-189] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-183] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-220] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-131] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-239] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-172] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-239] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-37] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-132] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-174] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-133] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-227] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-234] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>