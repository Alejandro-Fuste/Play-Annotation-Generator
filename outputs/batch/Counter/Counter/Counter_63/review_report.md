# Play-Annotation-Generator Annotation Review — Counter_63

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_63`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 132
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `16` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 127 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 128 | START | 128 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `19` | `18` | 132 | START | 132 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `20` | `19` | 132 | START | 132 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `22` | `21` | 132 | START | 142 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `21` | `20` | 132 | START | 132 | 143 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `14` | `13` | 132 | START | 132 | 224 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 141 | END | 128 | 141 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `16` | 152 | START | 152 | 168 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `18` | `17` | 169 | START | 195 | 199 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 224 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_SnapReceive` | 128 | 141 | 14 | inferred_complete_timeline |
| `Action_None` | 142 | 151 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 152 | 168 | 17 | inferred_complete_timeline |
| `Action_None` | 169 | 229 | 61 | inferred_complete_timeline |
| `Action_None` | 232 | 283 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_BallCarry` | 195 | 199 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 127 | 18 | inferred_complete_timeline |
| `Action_None` | 128 | 352 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–304
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 159 | 32 | inferred_complete_timeline |
| `Action_None` | 163 | 304 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–313
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 313 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 151 | 24 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 178 | 15 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 238 | 37 | inferred_complete_timeline |
| `Action_None` | 240 | 254 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–322
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 158 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 185 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 195 | 224 | 30 | inferred_complete_timeline |
| `Action_None` | 225 | 322 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 135 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 177 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 225 | 229 | 5 | inferred_complete_timeline |
| `Action_None` | 234 | 289 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_BallSnap` | 128 | 141 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 142 | 142 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 146 | 153 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 164 | 171 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 211 | 224 | 14 | inferred_complete_timeline |
| `Action_None` | 225 | 280 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 131 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 132 | 143 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 147 | 152 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 155 | 178 | 24 | inferred_complete_timeline |
| `Action_PullBlock` | 183 | 190 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 200 | 218 | 19 | inferred_complete_timeline |
| `Action_PullBlock` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 225 | 231 | 7 | inferred_complete_timeline |
| `Action_None` | 234 | 266 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 132 | 224 | 93 | inferred_complete_timeline |
| `Action_None` | 225 | 243 | 19 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 257 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 174 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 156 | 29 | inferred_complete_timeline |
| `Action_None` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_None` | 175 | 291 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 152 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 158 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 158 | 31 | inferred_complete_timeline |
| `Action_None` | 180 | 195 | 16 | inferred_complete_timeline |
| `Action_None` | 201 | 295 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 269 | 142 | inferred_complete_timeline |
| `Action_None` | 272 | 309 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 158 | 31 | inferred_complete_timeline |
| `Action_None` | 163 | 182 | 20 | inferred_complete_timeline |
| `Action_None` | 184 | 319 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 283 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 221 | 94 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 238 | 7 | inferred_complete_timeline |
| `Action_None` | 240 | 291 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–389 | 390 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–389 | 382 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–213 | 155 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 133–142 | 10 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 165–169 | 5 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 167–389 | 219 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 179–327 | 146 | 4 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 194–316 | 123 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 237–301 | 41 | 4 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 248–330 | 79 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 252–274 | 23 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 265–270 | 6 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 282–286 | 5 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 284–290 | 7 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 289–290 | 2 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 311–313 | 3 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 348–355 | 6 | 2 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 380–389 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (9 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (8 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `18` (RB): Annotated start 169 != Inferred start 195

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 103 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 128: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (LG) duration 93 frames exceeds threshold 90 frames [start=132, end=224].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (LT) duration 93 frames exceeds threshold 90 frames [start=132, end=224].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '20' (RG) duration 93 frames exceeds threshold 90 frames [start=132, end=224].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (C) duration 93 frames exceeds threshold 90 frames [start=132, end=224].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [128–141], lower_priority='Action_DownBlock' annotated_start=132, effective_Action_DownBlock_start=142.
- ⚠️ Action 'Action_None' range [128-174] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-352] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-195] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-295] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-178] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-238] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-254] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-304] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-313] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-238] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-291] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-319] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-291] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-283] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [132-224] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-243] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-269] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-309] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-193] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-370] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-389] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-229] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-283] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [195-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [132-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-177] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [202-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [206-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-289] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [132-158] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [192-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-322] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-93] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [132-143] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [147-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [155-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [183-190] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [195-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [200-218] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [220-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [223-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-231] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-266] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '21' starts at frame 142, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [142-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [146-153] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [164-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-280] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-137] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-143] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-174] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-142] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-190] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-389] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-196] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-327] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-316] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-244] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-297] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-330] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-270] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-286] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>