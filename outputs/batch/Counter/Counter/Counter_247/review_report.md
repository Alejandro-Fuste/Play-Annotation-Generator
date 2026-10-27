# Play-Annotation-Generator Annotation Review — Counter_247

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_247`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 176
- **Validation Warnings:** 191
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 150
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE1 | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `21` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 90 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 91 | START | 91 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `20` | `19` | 93 | START | 93 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE1 | `21` | `20` | 93 | START | 93 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `22` | `21` | 93 | START | 93 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `18` | `17` | 93 | START | 93 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `2` | `1` | 93 | START | 93 | 153 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 104 | END | 91 | 104 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 117 | START | 117 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 134 | START | 134 | 307 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 191 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_SnapReceive` | 91 | 104 | 14 | inferred_complete_timeline |
| `Action_None` | 105 | 116 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 117 | 133 | 17 | inferred_complete_timeline |
| `Action_None` | 134 | 329 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–312
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_BallCarry` | 134 | 307 | 174 | inferred_complete_timeline |
| `Action_BallCarry` | 311 | 312 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 329 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 123 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 263 | 64 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 107 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 173 | 191 | 19 | inferred_complete_timeline |
| `Action_None` | 192 | 325 | 134 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 114 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 156 | 163 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 191 | 18 | inferred_complete_timeline |
| `Action_None` | 192 | 200 | 9 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 211 | 216 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_BallSnap` | 91 | 104 | 14 | inferred_complete_timeline |
| `Action_None` | 105 | 110 | 6 | inferred_complete_timeline |
| `Action_None` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_None` | 127 | 131 | 5 | inferred_complete_timeline |
| `Action_None` | 134 | 139 | 6 | inferred_complete_timeline |
| `Action_None` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 157 | 6 | inferred_complete_timeline |
| `Action_None` | 161 | 212 | 52 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PullBlock` | 93 | 138 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 142 | 191 | 50 | inferred_complete_timeline |
| `Action_None` | 192 | 329 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 263 | 173 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_None` | 271 | 274 | 4 | inferred_complete_timeline |
| `Action_None` | 277 | 329 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 173 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 287 | 197 | inferred_complete_timeline |
| `Action_None` | 315 | 320 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 166 | 76 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 141 | 51 | inferred_complete_timeline |
| `Action_None` | 150 | 214 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 155 | 65 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 139 | 49 | inferred_complete_timeline |
| `Action_None` | 141 | 176 | 36 | inferred_complete_timeline |
| `Action_None` | 212 | 223 | 12 | inferred_complete_timeline |
| `Action_None` | 227 | 247 | 21 | inferred_complete_timeline |
| `Action_None` | 249 | 263 | 15 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_None` | 271 | 274 | 4 | inferred_complete_timeline |
| `Action_None` | 277 | 280 | 4 | inferred_complete_timeline |
| `Action_None` | 285 | 288 | 4 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |
| `Action_None` | 302 | 315 | 14 | inferred_complete_timeline |
| `Action_None` | 324 | 325 | 2 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 141 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 329 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 329 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 266 | 176 | inferred_complete_timeline |
| `Action_None` | 268 | 280 | 13 | inferred_complete_timeline |
| `Action_None` | 282 | 292 | 11 | inferred_complete_timeline |
| `Action_None` | 294 | 305 | 12 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 324 | 326 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 220 | 130 | inferred_complete_timeline |
| `Action_None` | 222 | 329 | 108 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–329 | 325 | 6 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–329 | 314 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 5–107 | 70 | 7 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 15–16 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 104–106 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 126–288 | 67 | 7 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 136–141 | 5 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 141–162 | 22 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 148–315 | 123 | 9 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 155–160 | 4 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 179–185 | 7 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 181–329 | 140 | 5 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 187–312 | 49 | 13 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 195–329 | 133 | 3 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 204–314 | 110 | 2 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 230–329 | 100 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 262–329 | 16 | 5 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 274–275 | 2 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 290–329 | 40 | 1 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 291–293 | 3 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 292–316 | 9 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `2` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 138 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 496: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 496: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '17' (RG) duration 99 frames exceeds threshold 90 frames [start=93, end=191].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 99 frames exceeds threshold 90 frames [start=93, end=191].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (TE1) duration 99 frames exceeds threshold 90 frames [start=93, end=191].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (LT) duration 99 frames exceeds threshold 90 frames [start=93, end=191].
- ⚠️ Action 'Action_PullLeadBlock' range [93-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [155-160] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [163-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [134-307] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [311-312] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-212] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-220] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-223] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-247] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-263] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-315] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-162] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-187] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-243] for track '10' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-214] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-266] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-280] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-292] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-305] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-287] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-320] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-155] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-166] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-263] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-329] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [93-138] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [93-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [156-163] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [170-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-191] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-200] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [93-123] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [125-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-263] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [93-107] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [173-191] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-325] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-13] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-34] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-81] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-242] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-263] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-162] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-187] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-266] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-288] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-307] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-315] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-187] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-226] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-266] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-329] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-196] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-322] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-308] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-329] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>