# Play-Annotation-Generator Annotation Review — JetSweep_213

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_213`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE1 | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `19` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 92 |
| ✅ EXACT | `Action_JetMotion` | WR | `1` | `0` | 46 | START | 46 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `17` | `16` | 93 | START | 93 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE1 | `14` | `13` | 95 | START | 95 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 95 | START | 95 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `11` | 95 | START | 95 | 187 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `17` | `16` | 95 | START | 109 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 95 | START | 95 | 119 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 108 | END | 93 | 108 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 113 | START | 113 | 124 |
| ✅ EXACT | `Action_BallCarry` | WR | `1` | `0` | 125 | START | 125 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 213 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_SnapReceive` | 93 | 108 | 16 | inferred_complete_timeline |
| `Action_None` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_Toss` | 113 | 124 | 12 | inferred_complete_timeline |
| `Action_None` | 125 | 227 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 194 | 102 | inferred_complete_timeline |
| `Action_None` | 197 | 208 | 12 | inferred_complete_timeline |
| `Action_None` | 211 | 269 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_JetMotion` | 46 | 124 | 79 | inferred_complete_timeline |
| `Action_BallCarry` | 125 | 269 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_LeadBlock` | 95 | 198 | 104 | inferred_complete_timeline |
| `Action_LeadBlock` | 201 | 213 | 13 | inferred_complete_timeline |
| `Action_None` | 214 | 269 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 101 | 9 | inferred_complete_timeline |
| `Action_None` | 103 | 161 | 59 | inferred_complete_timeline |
| `Action_None` | 165 | 243 | 79 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 269 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 112 | 20 | inferred_complete_timeline |
| `Action_None` | 140 | 144 | 5 | inferred_complete_timeline |
| `Action_None` | 147 | 155 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 119 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 140 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_BallSnap` | 93 | 104 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 113 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 133 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 213 | 61 | inferred_complete_timeline |
| `Action_None` | 214 | 258 | 45 | inferred_complete_timeline |
| `Action_None` | 260 | 265 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 187 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 213 | 24 | inferred_complete_timeline |
| `Action_None` | 214 | 233 | 20 | inferred_complete_timeline |
| `Action_None` | 239 | 269 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 149 | 57 | inferred_complete_timeline |
| `Action_None` | 151 | 258 | 108 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 123 | 31 | inferred_complete_timeline |
| `Action_None` | 125 | 129 | 5 | inferred_complete_timeline |
| `Action_None` | 131 | 224 | 94 | inferred_complete_timeline |
| `Action_None` | 228 | 231 | 4 | inferred_complete_timeline |
| `Action_None` | 244 | 269 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 5–125
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 38 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 92 | 49 | inferred_complete_timeline |
| `Action_None` | 93 | 101 | 9 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 101 | 9 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 108 | 269 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 127 | 35 | inferred_complete_timeline |
| `Action_None` | 150 | 153 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 207 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 245 | 153 | inferred_complete_timeline |
| `Action_None` | 247 | 263 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 134 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 134 | 42 | inferred_complete_timeline |
| `Action_None` | 139 | 172 | 34 | inferred_complete_timeline |
| `Action_None` | 189 | 200 | 12 | inferred_complete_timeline |
| `Action_None` | 213 | 246 | 34 | inferred_complete_timeline |
| `Action_None` | 259 | 269 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 186 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 222 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 113 | 21 | inferred_complete_timeline |
| `Action_None` | 118 | 190 | 73 | inferred_complete_timeline |
| `Action_None` | 201 | 235 | 35 | inferred_complete_timeline |
| `Action_None` | 241 | 244 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 132–159 | 28 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 153–269 | 95 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 158–269 | 107 | 5 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 163–269 | 92 | 4 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 164–269 | 95 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 189–269 | 81 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 189–258 | 70 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 218–269 | 52 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 223–260 | 23 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 224–261 | 38 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 242–247 | 4 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 250–251 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 250–260 | 11 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `17` (C): Annotated start 95 != Inferred start 109
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 119 frames exceeds threshold 90 frames [start=95, end=213].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (RT) duration 119 frames exceeds threshold 90 frames [start=95, end=213].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '13' (TE1) duration 119 frames exceeds threshold 90 frames [start=95, end=213].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [93–108], lower_priority='Action_ZoneBlock' annotated_start=95, effective_Action_ZoneBlock_start=109.
- ⚠️ Action 'Action_BallCarry' range [125-269] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-245] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-222] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-194] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-208] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-200] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-246] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-227] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-190] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-235] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-258] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-258] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [95-198] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-269] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-224] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-101] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-161] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-243] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [93-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-101] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-119] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-140] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-38] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-159] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-221] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-191] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-246] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-265] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-249] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-232] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-245] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-261] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-260] for track '33' has 1 frames without a visible bounding box.
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

</details>