# Play-Annotation-Generator Annotation Review — StopAndGo_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_3`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 138
- **Validation Warnings:** 150
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 119
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ START CHANGED | `Action_PassBlock` | RG | offense | `24` | `23` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_PumpFake` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_VerticalStem` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_SellStop` | WR3 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `24` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 4 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `20` | `20` | 5 | START | 5 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `16` | `16` | 8 | START | 8 | 42 |
| ✅ EXACT | `Action_PassBlock` | LT | `18` | `18` | 8 | START | 8 | 239 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | `20` | `20` | 8 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_PassBlock` | RG | `24` | `23` | 8 | START | 68 | 69 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 25 | END | 5 | 25 |
| ✅ EXACT | `Action_PumpFake` | QB | `14` | `14` | 60 | START | 60 | 95 |
| ✅ EXACT | `Action_VerticalStem` | WR3 | `0` | `0` | 65 | START | 65 | 70 |
| ✅ EXACT | `Action_SellStop` | WR3 | `0` | `0` | 71 | START | 71 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | `0` | `0` | 95 | START | 95 | 99 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 96 | START | 96 | 108 |

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
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 25 | 21 | inferred_complete_timeline |
| `Action_None` | 26 | 59 | 34 | inferred_complete_timeline |
| `Action_PumpFake` | 60 | 95 | 36 | inferred_complete_timeline |
| `Action_ThrowPass` | 96 | 108 | 13 | inferred_complete_timeline |
| `Action_None` | 109 | 111 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 188 | 184 | inferred_complete_timeline |
| `Action_None` | 191 | 217 | 27 | inferred_complete_timeline |
| `Action_None` | 219 | 239 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 239 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 63 | 59 | inferred_complete_timeline |
| `Action_None` | 69 | 126 | 58 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 165 | 8 | inferred_complete_timeline |
| `Action_None` | 170 | 239 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_VerticalStem` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_SellStop` | 71 | 94 | 24 | inferred_complete_timeline |
| `Action_RunGoRoute` | 95 | 99 | 5 | inferred_complete_timeline |
| `Action_RunGoRoute` | 101 | 183 | 83 | inferred_complete_timeline |
| `Action_RunGoRoute` | 189 | 192 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 39 | 35 | inferred_complete_timeline |
| `Action_None` | 56 | 61 | 6 | inferred_complete_timeline |
| `Action_None` | 64 | 188 | 125 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 235 | 8 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 239 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 5 | 18 | 14 | inferred_complete_timeline |
| `Action_BallSnap` | 23 | 24 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 68–69
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PassBlock` | 68 | 69 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 42 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 191 | 147 | inferred_complete_timeline |
| `Action_PassBlock` | 216 | 239 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 53 | 49 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 46 | 42 | inferred_complete_timeline |
| `Action_None` | 48 | 101 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 138 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 93 | 89 | inferred_complete_timeline |
| `Action_None` | 96 | 152 | 57 | inferred_complete_timeline |
| `Action_None` | 155 | 159 | 5 | inferred_complete_timeline |
| `Action_None` | 162 | 166 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 197 | 193 | inferred_complete_timeline |
| `Action_None` | 205 | 223 | 19 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 126 | 122 | inferred_complete_timeline |
| `Action_None` | 130 | 167 | 38 | inferred_complete_timeline |
| `Action_None` | 170 | 176 | 7 | inferred_complete_timeline |
| `Action_None` | 178 | 184 | 7 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 239 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 239 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 88 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 239 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 125 | 121 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_None` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_None` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 149 | 145 | inferred_complete_timeline |
| `Action_None` | 152 | 156 | 5 | inferred_complete_timeline |
| `Action_None` | 162 | 175 | 14 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 198 | 204 | 7 | inferred_complete_timeline |
| `Action_None` | 208 | 239 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–141 | 142 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–118 | 114 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 52–63 | 10 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 81–230 | 138 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 87–97 | 5 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 87–182 | 86 | 6 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 96–194 | 83 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 108–238 | 115 | 5 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 109–110 | 2 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 124–166 | 26 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 130–151 | 22 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 161–226 | 58 | 6 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 194–204 | 11 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 207–209 | 3 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 212–226 | 15 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 220–239 | 14 | 3 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 229–239 | 7 | 2 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 230–232 | 3 | 1 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 230–239 | 6 | 2 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (3 segments found)
- ❌ Missing segment for action `Action_PassBlock` on target `20` (C)
- ⚠️ `Action_PassBlock` for actor_track_id `24` (RG): Annotated start 8 != Inferred start 68
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `0` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 104 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 7: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [5–24], lower_priority='Action_PassBlock' annotated_start=8, effective_Action_PassBlock_start=25.
- ⚠️ Action 'Action_SellStop' range [71-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [95-99] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [101-183] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [189-192] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-46] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-138] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-167] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-88] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-149] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-175] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-63] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-165] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-239] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-197] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-223] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-239] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-152] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-188] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-217] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [216-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-39] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-188] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-141] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [5-18] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [23-24] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-103] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-63] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-69] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-130] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-208] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-230] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-129] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-168] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-176] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-175] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-139] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-191] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-238] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-140] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-166] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-151] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-166] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-192] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-209] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-226] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-204] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-226] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>