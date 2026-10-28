# Play-Annotation-Generator Annotation Review — Draw_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_55`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 137
- **Validation Warnings:** 142
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 110
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `6` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 37 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 35 | START | 35 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `11` | `10` | 38 | START | 52 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `16` | `15` | 38 | START | 38 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `18` | 38 | START | 38 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `22` | `21` | 38 | START | 38 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `8` | `7` | 38 | START | 38 | 82 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 51 | END | 35 | 51 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `14` | `13` | 54 | START | 54 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `14` | `13` | 98 | START | 98 | 164 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 133 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_SnapReceive` | 35 | 51 | 17 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 54 | 97 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 98 | 164 | 67 | inferred_complete_timeline |
| `Action_BallCarry` | 168 | 240 | 73 | inferred_complete_timeline |
| `Action_BallCarry` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 248 | 253 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 259 | 267 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 103 | 69 | inferred_complete_timeline |
| `Action_None` | 106 | 158 | 53 | inferred_complete_timeline |
| `Action_None` | 160 | 198 | 39 | inferred_complete_timeline |
| `Action_None` | 200 | 216 | 17 | inferred_complete_timeline |
| `Action_None` | 218 | 222 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 269 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 202 | 168 | inferred_complete_timeline |
| `Action_None` | 206 | 269 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 269 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 82 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 133 | 50 | inferred_complete_timeline |
| `Action_None` | 134 | 195 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 96 | 59 | inferred_complete_timeline |
| `Action_PassBlock` | 98 | 106 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 133 | 26 | inferred_complete_timeline |
| `Action_None` | 134 | 154 | 21 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 265 | 99 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_BallSnap` | 35 | 51 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 52 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 79 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 99 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 133 | 31 | inferred_complete_timeline |
| `Action_None` | 134 | 207 | 74 | inferred_complete_timeline |
| `Action_None` | 210 | 213 | 4 | inferred_complete_timeline |
| `Action_None` | 215 | 269 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 59 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 133 | 65 | inferred_complete_timeline |
| `Action_None` | 134 | 202 | 69 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |
| `Action_None` | 212 | 269 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 72 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 133 | 60 | inferred_complete_timeline |
| `Action_None` | 134 | 269 | 136 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 132 | 98 | inferred_complete_timeline |
| `Action_None` | 134 | 269 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 86 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 269 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 74 | 40 | inferred_complete_timeline |
| `Action_None` | 76 | 81 | 6 | inferred_complete_timeline |
| `Action_None` | 83 | 96 | 14 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 149 | 115 | inferred_complete_timeline |
| `Action_None` | 154 | 180 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 155 | 121 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 191 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 225 | 191 | inferred_complete_timeline |
| `Action_None` | 229 | 238 | 10 | inferred_complete_timeline |
| `Action_None` | 245 | 247 | 3 | inferred_complete_timeline |
| `Action_None` | 253 | 269 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 125 | 91 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 147 | 150 | 4 | inferred_complete_timeline |
| `Action_None` | 154 | 180 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 191 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 269 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 195 | 161 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–269 | 252 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 7–212 | 170 | 9 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 99–217 | 117 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 110–269 | 160 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 148–151 | 4 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 181–242 | 42 | 6 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 183–209 | 25 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 191–229 | 32 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 192–258 | 66 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 196–269 | 67 | 3 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 200–213 | 14 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 209–269 | 61 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 223–269 | 47 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 225–269 | 45 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 229–230 | 2 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 242–269 | 28 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 252–268 | 16 | 2 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 255–267 | 9 | 2 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 97 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 109: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [35–51], lower_priority='Action_PassBlock' annotated_start=38, effective_Action_PassBlock_start=52.
- ⚠️ Action 'Action_None' range [35-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-269] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-202] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-195] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-149] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-191] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '10' starts at frame 52, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [52-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-79] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-198] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-216] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-155] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-191] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [98-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [168-240] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [243-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-253] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [259-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-269] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-133] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-195] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [98-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-265] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-9] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-34] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-78] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-182] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-209] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-112] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-217] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-213] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-231] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-240] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-218] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-213] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-269] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-269] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-265] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>