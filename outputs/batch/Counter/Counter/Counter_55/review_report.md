# Play-Annotation-Generator Annotation Review — Counter_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_55`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 116 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 116 | START | 116 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `12` | `11` | 117 | START | 117 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `13` | `12` | 117 | START | 117 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `21` | `20` | 117 | START | 117 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `8` | `7` | 117 | START | 117 | 158 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 130 | END | 116 | 130 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 139 | START | 139 | 153 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `2` | 154 | START | 154 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 198 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_SnapReceive` | 116 | 130 | 15 | inferred_complete_timeline |
| `Action_None` | 131 | 138 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 139 | 153 | 15 | inferred_complete_timeline |
| `Action_None` | 154 | 304 | 151 | inferred_complete_timeline |
| `Action_None` | 306 | 311 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 153 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 154 | 329 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 168 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 117 | 158 | 42 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_None` | 235 | 329 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_DownBlock` | 117 | 127 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 164 | 171 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 184 | 185 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_DownBlock` | 117 | 126 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 184 | 189 | 6 | inferred_complete_timeline |
| `Action_None` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_None` | 233 | 329 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_BallSnap` | 116 | 124 | 9 | inferred_complete_timeline |
| `Action_None` | 149 | 158 | 10 | inferred_complete_timeline |
| `Action_None` | 163 | 170 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_PullBlock` | 117 | 127 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 164 | 171 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 178 | 182 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 329 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 132 | 17 | inferred_complete_timeline |
| `Action_None` | 148 | 153 | 6 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 171 | 11 | inferred_complete_timeline |
| `Action_None` | 175 | 187 | 13 | inferred_complete_timeline |
| `Action_None` | 189 | 194 | 6 | inferred_complete_timeline |
| `Action_None` | 198 | 204 | 7 | inferred_complete_timeline |
| `Action_None` | 206 | 208 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 128 | 13 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 329 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 132 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 128 | 13 | inferred_complete_timeline |
| `Action_None` | 165 | 171 | 7 | inferred_complete_timeline |
| `Action_None` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 329 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 129 | 14 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 171 | 8 | inferred_complete_timeline |
| `Action_None` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_None` | 184 | 187 | 4 | inferred_complete_timeline |
| `Action_None` | 230 | 329 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 140 | 25 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 168 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 189 | 74 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 329 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 202 | 87 | inferred_complete_timeline |
| `Action_None` | 233 | 329 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 175–329 | 155 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 208–329 | 121 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 214–235 | 22 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 231–329 | 99 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 234–329 | 96 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 240–329 | 90 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 240–329 | 90 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 283–284 | 2 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 298–317 | 5 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (8 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 68 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [116-168] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-144] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-202] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [117-158] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [165-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-127] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [164-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [178-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [184-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [165-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [170-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [184-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-304] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-311] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-140] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [117-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [151-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [164-171] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [178-182] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [184-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [116-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-300] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '32' has 1 frames without a visible bounding box.
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

</details>